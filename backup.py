import os
import shutil
import sys
from datetime import datetime


def backup_files(source_dir, destination_dir):
    if not os.path.exists(source_dir):
        print("ERROR: Source directory not avilabe")
        return

    if not os.path.exists(destination_dir):
        print("ERROR: Destination directory not avilabe")
        return

    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)

        if os.path.isfile(source_file):
            dest_file = os.path.join(destination_dir, file_name)

            if os.path.exists(dest_file):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(file_name)
                dest_file = os.path.join(
                    destination_dir, f"{name}_{timestamp}{ext}"
                )

            shutil.copy2(source_file, dest_file)

    print("Backup completed successfully")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_dir> <destination_dir>")
        sys.exit(1)

    backup_files(sys.argv[1], sys.argv[2])
