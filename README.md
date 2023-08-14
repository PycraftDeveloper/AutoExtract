# AutoExtract
A small project designed to automatically extract archives from the downloads folder.

## Overview
This project is designed to run in the background of your computer and every 10 seconds it will scan your downloads folder for archives, if it finds an archive then it will automatically extract the file to the downloads folder and remove the original file. Unfortunately, this has only be tested on Windows (10 and 11), but Linux compatibility will be added in a future revision.

## Features
AutoExtract is fast, outpacing Windows' default extraction utility and at times even 7-zip!
AutoExtract is small, it uses approximately 9.9 mb of memory and only checks for new files every 10 seconds to reduce CPU-usage.
AutoExtract is super easy to uninstall and uninstall, not requiring any changes to registry or environment variables and does not rely on having other apps installed.*

(*Compiled editions only here, running the python file from source WILL require an install of Python 3)

## Additional Information
### Setting AutoExtract to run on system-start-up
This small tutorial will only work for compiled editions of the project.
1. Download the compiled version from the releases section.
2. Accept any Windows security pop-ups, this happens when downloading all exe files from GitHub and this project is tested to be safe.
3. Move the file to a folder of your choosing.
4. Right-click on the file and click "Create Shortcut".
5. Cut (or copy) that shortcut to the compiled version of AutoExtract
6. Navigate to the start menu and under the 'apps' menu, right-click on an app. We are looking for an 'Open file location' option, not all apps have this, we do this to open the folder where start menu shortcuts are located.
7. Then locate the folder named 'start-up' and open it#.
8. Paste the file shortcut here, then when you restart your computer, the project will run in the background automatically helping you to extract any downloaded archives.

## Supported Files
Currently the project only supports '.zip' archives, other file types may be added in future revisions, apologies if this is inconvenient. Also, ALWAYS make sure your downloading files you trust, this project will not touch other files in the download folder, including other executables, but extracting archives can be dangerous if you do not trust the creator, so be careful and I hope this project has been helpful!

## Performance Comparison
![image](https://user-images.githubusercontent.com/81379254/167310217-54c977a6-0aa7-4fa6-9e82-a44704497388.png)
