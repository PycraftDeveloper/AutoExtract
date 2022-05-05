import os, time
from zipfile import ZipFile

from os.path import expanduser
home = expanduser("~")
downloads_path = home + os.sep + "Downloads"

while True:
    files = os.listdir(downloads_path)
    for i in range(len(files)):
        if ".zip" in files[i]:
            try:
                print(f"Attempting to extract: {files[i]}")
                with ZipFile(rf"{downloads_path}\{files[i]}", 'r') as zip:
                    zip.extractall(path=rf"{downloads_path}\{files[i][:-4]}")

                os.remove(rf"{downloads_path}\{files[i]}")
                print("Done")
            except Exception as Message:
                print(Message)
                
    time.sleep(10)
