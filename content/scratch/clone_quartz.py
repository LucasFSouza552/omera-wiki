import os
import urllib.request
import zipfile
import shutil

# Use relative paths to avoid Windows absolute path formatting issues in python
zip_path = "quartz.zip"
extract_dir = "quartz_temp"
target_dir = "quartz_wiki"

try:
    # 1. Download zip
    print("Downloading Quartz v4 zip...")
    urllib.request.urlretrieve("https://github.com/jackyzha0/quartz/archive/refs/heads/v4.zip", zip_path)
    print("Download complete!")
    
    # 2. Extract zip
    print("Extracting zip...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print("Extraction complete!")
    
    # 3. Move contents to target_dir
    # The zip contains a folder like "quartz-v4"
    extracted_folder = os.listdir(extract_dir)[0]
    src_path = os.path.join(extract_dir, extracted_folder)
    
    if os.path.exists(target_dir):
        shutil.rmtree(target_dir)
        
    shutil.move(src_path, target_dir)
    print(f"Quartz cloned and moved to: {target_dir}")
    
    # 4. Clean up temp files
    os.remove(zip_path)
    shutil.rmtree(extract_dir)
    print("Clean up completed successfully!")

except Exception as e:
    print(f"Error occurred: {e}")
