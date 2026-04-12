import os
import subprocess
import sys

def ocr_pdf(pdf_path, output_path):
    try:
        # Create a temp directory for images/output
        temp_dir = os.path.join(os.path.dirname(pdf_path), "temp_ocr_ispa")
        os.makedirs(temp_dir, exist_ok=True)
        
        output_base = os.path.join(temp_dir, "output")
        
        # Tesseract command
        # We use the list format for subprocess to handle spaces in filenames correctly
        cmd = ["tesseract", pdf_path, output_base, "-l", "eng"]
        
        print(f"Running OCR on {pdf_path}...")
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Tesseract appends .txt
        txt_file = output_base + ".txt"
        
        if os.path.exists(txt_file):
            with open(txt_file, "r") as f:
                content = f.read()
            
            with open(output_path, "w") as out:
                out.write(f"# Extracted Text from {os.path.basename(pdf_path)}\n\n")
                out.write(content)
            print(f"Successfully created {output_path}")
        else:
            print(f"Error: Output file {txt_file} not found.")
            
    except subprocess.CalledProcessError as e:
        print(f"OCR Failed for {pdf_path}: {e.stderr.decode()}")
    except Exception as e:
        print(f"An error occurred: {e}")

base_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Information Security Policy and Audit/Theory"
output_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Notes/Information Security Policy and Audit"

files_to_process = [
    ("ISPA_UNIT1.pdf", "ISPA_Unit_1.md"),
    ("Unit 2 (1).pdf", "ISPA_Unit_2.md")
]

os.makedirs(output_dir, exist_ok=True)

for pdf_name, md_name in files_to_process:
    pdf_path = os.path.join(base_dir, pdf_name)
    md_path = os.path.join(output_dir, md_name)
    
    if os.path.exists(pdf_path):
        ocr_pdf(pdf_path, md_path)
    else:
        print(f"File not found: {pdf_path}")

print("Done.")
