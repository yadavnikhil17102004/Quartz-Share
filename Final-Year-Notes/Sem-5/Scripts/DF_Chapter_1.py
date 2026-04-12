import os
import subprocess
import sys
import tempfile
from pdf2image import convert_from_path

def ocr_pdf(pdf_path, output_path):
    try:
        print(f"Converting {pdf_path} to images...")
        images = convert_from_path(pdf_path)
        
        full_text = []
        print(f"OCR processing {len(images)} pages...")
        
        with tempfile.TemporaryDirectory() as temp_dir:
            for i, image in enumerate(images):
                temp_img_path = os.path.join(temp_dir, f"temp_page_{i}.png")
                image.save(temp_img_path, "PNG")
                
                cmd = ["tesseract", temp_img_path, "stdout", "-l", "eng"]
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode == 0:
                    full_text.append(f"--- Page {i+1} ---\n{result.stdout}\n")
                else:
                    print(f"Error OCRing page {i+1}: {result.stderr}")
            
        with open(output_path, "w") as out:
            out.write(f"# Extracted Syllabus\n\n")
            out.write("\n".join(full_text))
            
        print(f"Successfully created {output_path}")

    except Exception as e:
        print(f"Error processing {pdf_path}: {e}")

ocr_pdf("syllabus.pdf", "syllabus_ocr.md")
