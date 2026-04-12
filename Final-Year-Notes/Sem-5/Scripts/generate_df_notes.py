import os
import zipfile
import re
import subprocess
import sys

def extract_text_from_pptx(pptx_path):
    text = []
    try:
        with zipfile.ZipFile(pptx_path, 'r') as z:
            slides = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            slides.sort(key=lambda x: int(re.search(r'slide(\d+)\.xml', x).group(1)))
            
            for file in slides:
                content = z.read(file).decode('utf-8')
                clean = re.sub('<[^>]+>', ' ', content)
                clean = re.sub(r'\s+', ' ', clean).strip()
                text.append(clean)
    except Exception as e:
        print(f"Error reading {pptx_path}: {e}")
        return ""
    return "\n\n".join(text)

def extract_text_from_pdf_ocr(pdf_path):
    # This is a fallback if we can't use pypdf
    # We will use sips to convert to png and then tesseract
    text = []
    try:
        # Create a temp directory for images
        temp_dir = os.path.join(os.path.dirname(pdf_path), "temp_ocr_images")
        os.makedirs(temp_dir, exist_ok=True)
        
        # Convert PDF to images using sips (one image per page is tricky with sips for multi-page pdfs)
        # sips might only handle the first page or require specific handling.
        # Actually, python's os.system might be better to call tesseract directly if it supports pdf.
        # Tesseract 5+ supports PDF input if linked with leptonica that supports it.
        # Let's try tesseract directly first.
        
        output_base = os.path.join(temp_dir, "output")
        cmd = ["tesseract", pdf_path, output_base, "-l", "eng"]
        subprocess.run(cmd, check=True, capture_output=True)
        
        # Tesseract output might be output.txt
        with open(output_base + ".txt", "r") as f:
            text.append(f.read())
            
        # Cleanup
        # shutil.rmtree(temp_dir) 
        
    except Exception as e:
        print(f"OCR Error on {pdf_path}: {e}")
        return f"[OCR Failed for {os.path.basename(pdf_path)}]"
    return "\n".join(text)

source_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Digital Forensics/Theory"
output_file = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Notes/Digital Forensics/DF_Notes.md"

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as out:
    out.write("# Digital Forensics Notes\n\n")
    for filename in sorted(os.listdir(source_dir)):
        path = os.path.join(source_dir, filename)
        if filename.endswith(".pptx"):
            out.write(f"## {filename}\n\n")
            text = extract_text_from_pptx(path)
            out.write(text + "\n\n")
            print(f"Processed PPTX: {filename}")
        elif filename.endswith(".pdf"):
            out.write(f"## {filename}\n\n")
            # Try OCR directly
            text = extract_text_from_pdf_ocr(path)
            out.write(text + "\n\n")
            print(f"Processed PDF: {filename}")

print("Done.")
