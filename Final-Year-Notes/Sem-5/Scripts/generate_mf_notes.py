import os
import zipfile
import re

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

source_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Mobile Forensics/Theory"
output_file = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe/Notes/Mobile Forensics/MF_Notes.md"

os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(output_file, "w") as out:
    out.write("# Mobile Forensics Notes\n\n")
    for filename in sorted(os.listdir(source_dir)):
        if filename.endswith(".pptx"):
            out.write(f"## {filename}\n\n")
            path = os.path.join(source_dir, filename)
            text = extract_text_from_pptx(path)
            out.write(text + "\n\n")
            print(f"Processed {filename}")

print("Done.")
