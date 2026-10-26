import os
import shutil

def organize_files(target_directory):
    if not os.path.exists(target_directory):
        print(f"Directory '{target_directory}' does not exist.")
        return

    # Define categories and extensions
    extensions_map = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audio": [".mp3", ".wav", ".aac"],
        "Archives": [".zip", ".rar", ".tar", ".gz"],
        "Code": [".py", ".js", ".html", ".css", ".cpp", ".java"]
    }

    print(f"Organizing files in: {target_directory}\n")

    for filename in os.listdir(target_directory):
        file_path = os.path.join(target_directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        file_ext = os.path.splitext(filename)[1].lower()
        moved = False

        for category, extensions in extensions_map.items():
            if file_ext in extensions:
                category_dir = os.path.join(target_directory, category)
                os.makedirs(category_dir, exist_ok=True)
                
                shutil.move(file_path, os.path.join(category_dir, filename))
                print(f"Moved: {filename} -> {category}/")
                moved = True
                break
        
        if not moved:
            other_dir = os.path.join(target_directory, "Others")
            os.makedirs(other_dir, exist_ok=True)
            shutil.move(file_path, os.path.join(other_dir, filename))
            print(f"Moved: {filename} -> Others/")

    print("\n✅ File organization completed successfully!")

if __name__ == "__main__":
    target_dir = input("Enter the path of the directory to organize (press Enter for current folder): ").strip()
    if not target_dir:
        target_dir = "."
    organize_files(target_dir)