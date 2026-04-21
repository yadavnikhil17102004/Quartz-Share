import os
import subprocess
import sys
import glob

def convert_pdf_to_images_sips(pdf_path, output_dir):
    # sips converts PDF to one image. If multi-page, it might only do the first or all?
    # sips usually handles single page. 
    # But we can try to use a python script to iterate if sips doesn't support it.
    # Actually, let's try to just run sips and see what happens.
    # If sips produces one file, we might be missing pages.
    # A better way on mac without poppler is using NSImage/Quartz via python, but that requires pyobjc.
    # Let's assume sips might not be enough for multi-page.
    
    # Alternative: 'shortcuts' or 'automator' command line?
    # Or maybe 'python' has a library installed?
    # We checked pypdf and pdfminer, they are missing.
    
    # Let's try to run sips.
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    output_prefix = os.path.join(output_dir, base_name)
    
    # sips command to convert all pages? sips doesn't support extracting all pages easily.
    # It seems we are stuck without poppler for multi-page PDF to image conversion easily via CLI tools standardly available.
    # EXCEPT: 'python3' might have 'pdf2image' if the user installed it? No, we checked.
    
    # Wait, the user said "try ocr".
    # I will try to use 'sips' to convert. If it only does first page, I will note that.
    # However, I can try to use 'mutool' if installed? No.
    
    # Let's try to use a python script that uses 'CoreGraphics' if available (standard on mac python?)
    # Usually not available in standard venv.
    
    # Let's just try sips and see if it generates multiple files or one.
    # If it generates one, we will use that.
    
    cmd = ["sips", "-s", "format", "png", pdf_path, "--out", output_dir]
    # sips --out directory might convert all pages?
    # Let's try.
    subprocess.run(cmd, check=False)
    
    return glob.glob(os.path.join(output_dir, "*.png"))

def ocr_images(image_paths, output_path):
    full_text = []
    for img in sorted(image_paths):
        try:
            cmd = ["tesseract", img, "stdout", "-l", "eng"]
            result = subprocess.run(cmd, capture_output=True, text=True)
            full_text.append(result.stdout)
        except Exception as e:
            print(f"Error OCRing {img}: {e}")
            
    with open(output_path, "w") as f:
        f.write("\n\n".join(full_text))

# ... (rest of the script)
