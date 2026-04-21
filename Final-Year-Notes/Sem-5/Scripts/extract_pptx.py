import zipfile
import re
import sys
import os

def extract_text(pptx_path):
    text = []
    try:
        with zipfile.ZipFile(pptx_path, 'r') as z:
            # Sort slides to maintain order (slide1, slide2, etc.)
            slides = [f for f in z.namelist() if f.startswith('ppt/slides/slide') and f.endswith('.xml')]
            # Simple numeric sort
            slides.sort(key=lambda x: int(re.search(r'slide(\d+)\.xml', x).group(1)))
            
            for file in slides:
                content = z.read(file).decode('utf-8')
                # Remove XML tags
                clean = re.sub('<[^>]+>', ' ', content)
                # Collapse multiple spaces
                clean = re.sub(r'\s+', ' ', clean).strip()
                text.append(f"--- Slide {file} ---\n{clean}\n")
    except Exception as e:
        print(f"Error reading {pptx_path}: {e}")
        return ""
    return "\n".join(text)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(extract_text(sys.argv[1]))
