import os
import shutil

def delete_files_in_directory(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Loop through all files and directories in the folder
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            # Check if it's a file or a symbolic link, and delete it
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                print(f"Deleted file: {file_path}")
            # Check if it's a directory and delete its contents recursively
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
                print(f"Deleted directory and its contents: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == "__main__":
    # Use /tmp as the directory since it's the target of the bind mount
    folder_path = "/tmp"
    delete_files_in_directory(folder_path)
