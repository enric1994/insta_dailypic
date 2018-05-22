import datetime
import os
import subprocess
import time
import sys

import pynstagram.photo

print('pynstagram started!')
while(True):
    if(datetime.datetime.now().hour == 15):
        print ('clean old photos')
        os.system("rm *.jpg")

        print ('make picture, crop')
        os.system("ffmpeg -f video4linux2 -i /dev/video0 -vframes 1 photo.jpg")
        os.system("convert photo.jpg -crop 480x480 photo.jpg")

        print ('upload photo')
        pynstagram.photo.upload('photo-0.jpg',time.strftime("%c"))
        print ('done! now sleeping 5h')
        time.sleep(2*60*60)
    print("waiting 60s...")
    time.sleep(60);
