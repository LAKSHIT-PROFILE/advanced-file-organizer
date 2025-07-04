import os
import shutil

# ✅ Customize your target source folder here
source_folder = r'C:\Users\laksh\Downloads'

# ✅ Define extension groups
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', '.odt'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi', '.flv', '.wmv', '.webm'],
    'Audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac'],
    'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2'],
    'Executables': ['.exe', '.msi', '.bat', '.sh'],
    'Installers': ['.apk', '.deb', '.rpm'],
    'Scripts': ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.rb', '.ps1'],
    'Designs': ['.psd', '.ai', '.xd', '.fig', '.sketch'],
    'Fonts': ['.ttf', '.otf', '.woff'],
    'Others': []  # default catch-all
}

def organize_files(folder):
    moved_count = 0
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            destination_folder = 'Others'  # Default if no match

            # Find matching category
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    destination_folder = folder_name
                    break

            target_path = os.path.join(folder, destination_folder)
            os.makedirs(target_path, exist_ok=True)

            # Avoid moving if already inside target folder
            if os.path.abspath(file_path).startswith(os.path.abspath(target_path)):
                continue

            try:
                shutil.move(file_path, os.path.join(target_path, filename))
                print(f"✅ Moved: {filename} → {destination_folder}")
                moved_count += 1
            except Exception as e:
                print(f"❌ Error moving {filename}: {e}")

    print(f"\n🎯 Total files moved: {moved_count}")

# 🔁 Run it
organize_files(source_folder)
