from os.path import expanduser
from os import path, listdir
from time import sleep
from zipfile import ZipFile
from platform import system

from send2trash import send2trash

def get_download_path():
    """Returns the default downloads path for linux or windows"""
    if system() == "Windows":
        from winreg import OpenKey, QueryValueEx, HKEY_CURRENT_USER
        sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
        downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
        with OpenKey(HKEY_CURRENT_USER, sub_key) as key:
            location = QueryValueEx(key, downloads_guid)[0]
        del OpenKey, QueryValueEx, HKEY_CURRENT_USER
        return location
    else:
        return path.join(expanduser('~'), 'downloads')

downloads_path = get_download_path()

print("Ready!")

while True:
    try:
        files = listdir(downloads_path)
        for file in files:
            if ".zip" in file:
                    print(f"Attempting to extract: {file}")
                    with ZipFile(rf"{downloads_path}\{file}", 'r') as zip_file:
                        zip_file.extractall(path=rf"{downloads_path}\{file[:-4]}")

                    send2trash(rf"{downloads_path}\{file}")
                    print("Done")
    except Exception as error:
        print(error)

    sleep(10)
