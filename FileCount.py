import os

file_path = "FileCount.txt"
fileduplicate_path = "FileDuplicate.txt"
def count_files(folder_path):
    try:
        # Initialize counter for files
        num_files = 0
        
        # Walk through all directories and subdirectories
        for root, dirs, files in os.walk(folder_path):
            # For each file found, increment the counter
            num_files += len(files)
            # if num_files > 50:
            #     with open(file_path, 'a') as file:
            #         file.write(f"\n Number of files in {folder_path}: {num_files}")
            #     continue
            # For each directory found, count files within
            for directory in dirs:
                subdir_path = os.path.join(root, directory)
                num_files += count_files(subdir_path)
                # if num_files > 50:
                #     with open(file_path, 'a') as file:
                #         file.write(f"\n Number of files in {folder_path}: {num_files}")
                #     continue

                
        if num_files != -1:
            with open(file_path, 'a') as file:
                file.write(f"\n Number of files in {folder_path}: {num_files}")
        return num_files
    except Exception as e:
        print("An error occurred:", e)
        return -1

def find_duplicate_filenames(folder_path):
    # Dictionary to store file names and their corresponding paths
    filenames_dict = {}

    # List to store duplicate file names
    duplicate_filenames = []

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            # Get just the file name without the path
            filename = os.path.basename(file)
            # If the file name already exists in the dictionary, it's a duplicate
            if filename in filenames_dict:
                duplicate_filenames.append(filename)
                # Add both file paths to the duplicate list
                duplicate_filenames.append(filenames_dict[filename])
                duplicate_filenames.append(file_path)
            else:
                filenames_dict[filename] = file_path

    return duplicate_filenames

# Example usage:
# Example usage:
folder_path = "C:\\Rakesh\\DummyProject\\Personal_UOW"  # Change this to your folder path
num_files = count_files(folder_path)

if num_files != -1:
    print(f"Number of files in {folder_path}: {num_files}")

duplicates = find_duplicate_filenames(folder_path)
print(duplicates)
if duplicates:
    for i in range(0, len(duplicates), 2):
        with open(fileduplicate_path, 'a') as file:
            file.write(f"File name: {duplicates[i]}")
            file.write(f"File path 1: {duplicates[i+1]}")
            file.write(f"File path 2: {duplicates[i+2]}")
else:
    print("No duplicate file names found.")