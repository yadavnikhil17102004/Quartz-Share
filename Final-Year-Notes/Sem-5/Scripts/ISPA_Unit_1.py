import os
import subprocess
import sys
from pdf2image import convert_from_path

def ocr_pdf_full(pdf_path, output_path):
    try:
        print(f"Converting {pdf_path} to images...")
        # Convert all pages to images
        images = convert_from_path(pdf_path)
        
        full_text = []
        print(f"OCR processing {len(images)} pages...")
        
        for i, image in enumerate(images):
            # Save temp image for tesseract (or pass directly if using pytesseract, but we use subprocess for tesseract CLI)
            temp_img_path = f"temp_page_{i}.png"
            image.save(temp_img_path, "PNG")
            
            cmd = ["tesseract", temp_img_path, "stdout", "-l", "eng"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode == 0:
                full_text.append(f"--- Page {i+1} ---\n{result.stdout}\n")
            else:
                print(f"Error OCRing page {i+1}: {result.stderr}")
            
            os.remove(temp_img_path)
            
        with open(output_path, "w") as out:
            out.write(f"# Extracted Text from {os.path.basename(pdf_path)}\n\n")
            out.write("\n".join(full_text))
            
            # Re-append enrichment
            out.write("\n\n## Enrichment: Fact Checks & Extra Info (2025 Trends)\n\n")
            out.write("> [!IMPORTANT] ISPA Updates (ISO 27001:2022)\n")
            out.write("> *   **Policy Consolidation**: Merged policies into \"Information Security Policies\" (Annex A 5.1).\n")
            out.write("> *   **Topic-Specific Policies**: Requirement for specific policies (e.g., Cloud, Secure Development).\n")
            out.write("> *   **Lifecycle Management**: Emphasis on regular review, approval, and communication.\n")
            out.write("> *   **Integration**: Policies must be part of training and awareness programs.\n")
            
        print(f"Successfully created {output_path}")

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

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
        ocr_pdf_full(pdf_path, md_path)
    else:
        print(f"File not found: {pdf_path}")

print("Done.")
