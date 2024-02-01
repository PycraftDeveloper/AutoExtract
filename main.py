from os.path import expanduser
from os import path, listdir, sep
from time import sleep
from platform import system
from shutil import unpack_archive

from send2trash import send2trash
from py7zr import SevenZipFile
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

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

def extractor(file):
    if ".crdownload" in file or ".tmp" in file:
        return
    formatted_file = file.split(sep)[-1].split(".")[0]
    destination_name = f"Extracted {formatted_file}"
    destination = downloads_path+sep+destination_name
    try:
        unpack_archive(
            file,
            destination)

        sleep(0.5)

        send2trash(file)

    except:
        try:
            with SevenZipFile(file, mode='r') as archive:
                archive.extractall(path=destination)

            sleep(0.5)

            send2trash(file)
        except:
            pass

class EventHandler(FileSystemEventHandler):
    def __init__(self):
        self.whitelist = []

    def on_modified(self, event):
        if event.is_directory is False:
            file = event.src_path
            if file not in self.whitelist:
                self.whitelist.append(file)

                extractor(file)

                self.whitelist.remove(file)

if __name__ == "__main__":
    files = listdir(downloads_path)
    for file in files:
        extractor(downloads_path+sep+file)

    event_handler = EventHandler()
    observer = Observer()
    observer.schedule(event_handler, downloads_path, recursive=False)
    observer.start()
    observer.join()