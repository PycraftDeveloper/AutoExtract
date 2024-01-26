from os.path import expanduser
from os import path, listdir
from time import sleep
from platform import system
from shutil import unpack_archive

from send2trash import send2trash
from py7zr import SevenZipFile

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

basic_archive_types = [".zip", ".tar", ".gztar", ".bztar", ".xztar"]

while True:
    try:
        files = listdir(downloads_path)
        for file in files:
            if any(x in file for x in basic_archive_types):
                unpack_archive(
                    rf"{downloads_path}\{file}",
                    rf"{downloads_path}")

                send2trash(rf"{downloads_path}\{file}")

            elif ".7z" in file:
                with SevenZipFile(rf"{downloads_path}\{file}", mode='r') as archive:
                    archive.extractall(path=rf"{downloads_path}")

                send2trash(rf"{downloads_path}\{file}")
    except Exception as error:
        print(error)

    sleep(10)
