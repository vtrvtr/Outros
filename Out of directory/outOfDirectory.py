import shutil
import os
from unipath import Path


def main(folder, extension=[]):

    for file_or_subfolder in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, file_or_subfolder)):
            for file in os.listdir(os.path.join(folder, file_or_subfolder)):
                path = Path(os.path.join(folder, file_or_subfolder, file))
                if path.ext in extension or len(extension) == 0:
                    dest = path.parent.parent
                    print 'Moving {0} to {1}'.format(file, dest)
                    path.move(dest)

                    
if __name__ == "__main__":
    src = raw_input("Origin folder\n")
    extension = list(raw_input(
        "extensions separated by a space (if empty all files will be copied)\n").split())
    main(src, extension)
