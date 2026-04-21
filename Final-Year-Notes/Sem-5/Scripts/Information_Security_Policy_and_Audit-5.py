import os
import subprocess
import sys
import tempfile
from pdf2image import convert_from_path

def ocr_pdf_full(pdf_path, output_path):
    try:
        print(f"Converting {pdf_path} to images...")
        # Convert all pages to images
        images = convert_from_path(pdf_path)
        
        full_text = []
        print(f"OCR processing {len(images)} pages...")
        
        # Use temp directory
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, image in enumerate(images):
                temp_img_path = os.path.join(temp_dir, f"temp_page_{i}.png")
                image.save(temp_img_path, "PNG")
                
                if not os.path.exists(temp_img_path):
                    print(f"Error: Failed to save {temp_img_path}")
                    continue
                    
                cmd = ["tesseract", temp_img_path, "stdout", "-l", "eng"]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    full_text.append(f"--- Page {i+1} ---\n{result.stdout}\n")
                else:
                    print(f"Error OCRing page {i+1}: {result.stderr}")
            
        with open(output_path, "w") as out:
            out.write(f"# Extracted Text from {os.path.basename(pdf_path)}\n\n")
            out.write("\n".join(full_text))
            
        print(f"Successfully created {output_path}")

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

base_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Digital Forensics/Theory"
output_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Notes/Digital Forensics"

files_to_process = [
    ("1.pdf", "DF_Chapter_1_Raw.md"),
    ("The Basics of Digital Forensics.pdf", "DF_Chapter_2_Raw.md"),
    ("Understanding Decimal, Binary, Hexadecimal, and Encoding (1).pdf", "DF_Chapter_4_Raw.md")
]

os.makedirs(output_dir, exist_ok=True)

for pdf_name, md_name in files_to_process:
    pdf_path = os.path.join(base_dir, pdf_name)
    md_path = os.path.join(output_dir, md_name)
    
    if os.path.exists(pdf_path):
        ocr_pdf_full(pdf_path, md_path)
    else:
        print(f"File not found: {pdf_path}")

print("Done.")
