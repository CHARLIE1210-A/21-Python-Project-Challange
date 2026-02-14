import shutil
import os
import logging

# ================= LOGGING =================
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
} 

def organize_folder(folder_path):
    if not os.path.exists(folder_path):
        logger.info("Folder does not exist")
        return
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isdir(file_path):
            continue # skip folder
        
        ext = os.path.splitext(filename)[1].lower()
        
        moved = False
        for folder, extensions in FILE_TYPES.items():
            if ext in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                
                shutil.move(file_path, os.path.join(folder_path, folder))
                logger.info(f"Moved: {filename} -> {folder}")
                
                moved = True
                break
            
        if not moved:
            other = os.path.join(folder, "Others")
            os.makedirs(other, exist_ok=True)
            shutil.move(file_path, os.path.join(other, filename))
            logger.info(f"Moved: {filename} -> Others")
      
            
            
def main():
    logger.info("Folder organizer Application: ")
    folder = input("Enter folder path: ").strip()
    if organize_folder(folder):
        logger.info("Organization complete")
    else:
        logger.info("No Organization happened.")
    
    
if __name__ == "__main__":
    main()