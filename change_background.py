
from datetime import datetime
import os
import random
import subprocess

# from appscript import app, mactypes



# https://www.reddit.com/r/mac/comments/ncujqi/an_applescript_to_change_all_of_your_desktops/


def set_current_time():

    image_path = "/Users/jasperchong/PycharmProjects/lit clock/personal_custom/images"


    SCRIPT = """/usr/bin/osascript<<END
    tell application "Finder"
    set desktop picture to POSIX file "{}"
    end tell
    END"""

    def set_desktop_background(filename):
        subprocess.Popen(SCRIPT.format(path), shell=True)

    current_datetime = datetime.now()
    ctime = datetime.strftime(current_datetime, "%H%M")

    # image_path = '/Users/jasperchong/PycharmProjects/lit clock/personal/image_dump'
    names = os.listdir(image_path)
    names.sort()
    
    options = []
    idx = None
    while idx == None:
        try:
            idx = names.index("quote_"+ctime+"_0.jpg") #! make sure correct image type
        except:
            # increase the time by one minute (better to be early than late imo)
            ctime = str(int(ctime)+1)

    while ctime in names[idx]:
        options.append(names[idx])
        idx += 1

    img = random.choice(options)

    path = image_path +'/' + img

    set_desktop_background(path)
    #return path
    


# if __name__ == '__main__':
#     print(set_current_time())