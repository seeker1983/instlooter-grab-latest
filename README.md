# Description
Python3 script to load latest images from instagram and upload zipped archive into google drive folder.
## How it works.
1. You specify a list of users on instagram you want to load latest images from.
2. Setup the script to run in schedule(e.g. cron)
3. Script loads images for each user, zips them, uploads the archive to google drive folder and appends the link into google sheet.
## Perfomance
Currently, due to instagram Graph Query API restrictions, script allows downloading **12 users per hour**, provided you ask for **latest 100 pictures**.

## Installation
1. Create service account key for google cloud platform project. Download **.json** file and set *key_file_location* the path in config.py
2. Make a copy of test sheet.
https://docs.google.com/spreadsheets/d/1Xp7n1Gl3lPyoKskMZhAO8yVUmH6g6XWuxQi1vQrbbAU/copy
3. Take **client_email** from credentials json file in step 1 and give edit access to this email to sheet from step 2
http://prntscr.com/oiue7v
4. Create a google drive folder, and, similar to step 3 add *client_email* edit access to the folder.
5. Install python3 dependencies.
```
    pip3 install -r requirements.txt
```
6. Test instalooter is working
```
    instalooter user instagram test -n 20
```
Make user folder test is created and images are downloaded inside.
**Note**: If you're not running from desktop(VPS, no browser available), you need to install user-agent manually:
```
    cp user-agent.txt ~/.cache/instalooter/2.4.0/
```
7. Test script
```
    python3 main.py
```
If everything is setup correctly, the appropriate row in google sheet will have google drive link for newly uploaded file added, and the appropriate file will appread in google drive folder configured in step 4.

## Credits
- [Instlooter](https://github.com/althonos/InstaLooter), for quick and nice image downloads.