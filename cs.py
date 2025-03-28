import os
import shutil

def rename_image_files(folder_path):
    """
    Rename image files in the specified folder sequentially.
    
    Args:
    folder_path (str): Path to the folder containing image files
    
    Supported file extensions: .png, .jpeg, .jpg, .heic
    """
    # Supported image extensions
    supported_extensions = ['.png', '.jpeg', '.jpg', '.heic']
    
    # Get all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if os.path.splitext(f)[1].lower() in supported_extensions]
    
    # Sort files to ensure consistent ordering
    image_files.sort()
    
    # Track how many files were successfully renamed
    renamed_count = 0
    
    # Rename files
    for index, filename in enumerate(image_files, 1):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1]
        
        # Create new filename
        new_filename = f"{index}{file_ext}"
        
        # Full paths
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        
        # Skip if the filenames are the same
        if filename == new_filename:
            print(f"Skipping: {filename} (already has the correct name)")
            continue
        
        try:
            # Check if the target file already exists
            if os.path.exists(new_path):
                print(f"Skipping: {filename} -> {new_filename} (target file already exists)")
                continue
                
            # Rename the file using os.rename instead of shutil.copy2
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")
            renamed_count += 1
        except Exception as e:
            print(f"Error renaming {filename}: {e}")
    
    print(f"Renamed {renamed_count} out of {len(image_files)} image files.")

def main():
    # Get folder path from user input
    folder_path = input("Enter the full path to the folder containing images: ").strip()
    
    # Validate folder path
    if not os.path.isdir(folder_path):
        print("Error: Invalid folder path.")
        return
    
    # Confirm with user before renaming
    confirm = input(f"Are you sure you want to rename all image files in {folder_path}? (yes/no): ").lower()
    
    if confirm == 'yes':
        rename_image_files(folder_path)
    else:
        print("Operation cancelled.")

if __name__ == "__main__":
    main()