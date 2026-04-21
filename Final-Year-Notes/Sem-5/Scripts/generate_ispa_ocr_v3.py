import os
import subprocess
import sys

try:
    from AppKit import NSPDFImageRep, NSImage, NSBitmapImageRep, NSPNGFileType
    from Foundation import NSData
    APPKIT_AVAILABLE = True
except ImportError:
    APPKIT_AVAILABLE = False

def convert_pdf_to_images_appkit(pdf_path, output_dir):
    if not APPKIT_AVAILABLE:
        print("AppKit not available.")
        return []
        
    images = []
    try:
        with open(pdf_path, "rb") as f:
            pdf_data = f.read()
        
        ns_data = NSData.dataWithBytes_length_(pdf_data, len(pdf_data))
        pdf_rep = NSPDFImageRep.imageRepWithData_(ns_data)
        
        if not pdf_rep:
            print("Failed to load PDF representation.")
            return []
            
        page_count = pdf_rep.pageCount()
        print(f"PDF has {page_count} pages.")
        
        for i in range(page_count):
            pdf_rep.setCurrentPage_(i)
            image = NSImage.alloc().init()
            image.addRepresentation_(pdf_rep)
            
            # Create bitmap representation
            bitmap = NSBitmapImageRep.imageRepWithData_(image.TIFFRepresentation())
            png_data = bitmap.representationUsingType_properties_(NSPNGFileType, None)
            
            output_file = os.path.join(output_dir, f"page_{i+1}.png")
            png_data.writeToFile_atomically_(output_file, True)
            images.append(output_file)
            print(f"Saved {output_file}")
            
    except Exception as e:
        print(f"Error converting PDF with AppKit: {e}")
        
    return images

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
        temp_dir = os.path.join(os.path.dirname(pdf_path), f"temp_images_{pdf_name}")
        os.makedirs(temp_dir, exist_ok=True)
        
        if APPKIT_AVAILABLE:
            images = convert_pdf_to_images_appkit(pdf_path, temp_dir)
            if images:
                ocr_images(images, md_path)
                print(f"Created {md_path}")
            else:
                print(f"Failed to convert {pdf_name}")
        else:
            # Fallback to sips (single page)
            print("Using sips fallback (first page only)...")
            cmd = ["sips", "-s", "format", "png", pdf_path, "--out", os.path.join(temp_dir, "page_1.png")]
            subprocess.run(cmd)
            ocr_images([os.path.join(temp_dir, "page_1.png")], md_path)
            
    else:
        print(f"File not found: {pdf_path}")

print("Done.")
