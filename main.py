#!/usr/bin/env python

import os
import exifread
import re

folder_list = ["/Users/daniel/Pictures/DCIM/100ANDRO"]

def main():
    for folder in folder_list:
        for file in os.listdir(folder):
            if file.endswith(".jpg") or file.endswith(".JPG"):
                f = open(folder + "/" + file, 'rb')
                tags = exifread.process_file(f)
                date = re.sub(":", "-", tags["EXIF DateTimeOriginal"].printable)
                date = re.sub(" ", "--", date)
                print "mv {} {}.jpg".format(folder + "/" + file, folder + "/" + date)

if __name__ == '__main__':
    main()