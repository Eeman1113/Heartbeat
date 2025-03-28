import os
import shutil
from PIL import Image
import sys

def rename_and_convert_images(folder_path):
    """
    Rename image files in the specified folder sequentially and convert them to WebP format.
    
    Args:
    folder_path (str): Path to the folder containing image files
    
    Supported input file extensions: .png, .jpeg, .jpg, .heic
    Output format: .webp
    """
    # Supported image extensions
    supported_extensions = ['.png', '.jpeg', '.jpg', '.heic']
    
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in supported_extensions]
    
    # Sort files to ensure consistent ordering
    image_files.sort()
    
    # Track how many files were successfully processed
    converted_count = 0
    
    # Convert and rename files
    for index, filename in enumerate(image_files, 1):
        # New filename with webp extension
        new_filename = f"{index}.webp"
        
        # Full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        # Skip if the target file already exists
        if os.path.exists(new_path):
            print(f"Skipping: {filename} -> {new_filename} (target file already exists)")
            continue
            
        try:
            # Open and convert the image to WebP
            try:
                with Image.open(old_path) as img:
                    # HEIC files might need special handling
                    if filename.lower().endswith('.heic'):
                        # For HEIC files, we need to convert to RGB mode first
                        img = img.convert('RGB')
                    
                    # Save as WebP with high quality
                    img.save(new_path, 'WEBP', quality=90) 
                    # Delete original file after successful conversion
                    os.remove(old_path)
                    print(f"Converted and renamed: {filename} -> {new_filename} (original deleted)")
                    converted_count += 1
            except Exception as e:
                print(f"Error converting {filename}: {e}")
                continue
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")
    
    print(f"Converted and renamed {converted_count} out of {len(image_files)} image files to WebP format. Original files have been deleted.")

def main():
    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        print("Error: The Pillow library is required but not installed.")
        print("Please install it using: pip install Pillow")
        sys.exit(1)
        
    # Get folder path from user input
    folder_path = input("Enter the full path to the folder containing images: ").strip()
    
    # Validate folder path
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return
    
    # Confirm with user before processing
    confirm = input(f"Are you sure you want to convert all image files in {folder_path} to WebP format and DELETE originals? (yes/no): ").lower()
    
    if confirm == 'yes':
        rename_and_convert_images(folder_path)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()