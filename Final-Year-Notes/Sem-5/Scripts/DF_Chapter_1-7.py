import os
import subprocess
import glob

def find_docx_files(root_dir):
    docx_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".docx") and not file.startswith("~$"):
                docx_files.append(os.path.join(root, file))
    return docx_files

def convert_to_pdf(docx_path):
    output_dir = os.path.dirname(docx_path)
    # soffice path on macOS
    soffice_path = "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    
    cmd = [
        soffice_path,
        "--headless",
        "--convert-to", "pdf",
        "--outdir", output_dir,
        docx_path
    ]
    
    try:
        print(f"Converting: {docx_path}")
        subprocess.run(cmd, check=True, capture_output=True)
        print(f"Successfully converted: {docx_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {docx_path}: {e}")
        print(f"Stderr: {e.stderr.decode()}")

def main():
    root_dir = "/Users/nikhilyadav/Desktop/Obsi/obsi_vault_hehe/Exams_hehe"
    docx_files = find_docx_files(root_dir)
    
    print(f"Found {len(docx_files)} DOCX files.")
    
    for docx in docx_files:
        convert_to_pdf(docx)

if __name__ == "__main__":
    main()
