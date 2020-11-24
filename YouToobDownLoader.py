#!/usr/bin/env python3
from pytube import YouTube
import os

print ("YouLoader : Youtube Downloader By Sarthak Roy (' https://sarthakroyblog.netlify.app/ ')")
yt_link = input('Enter the  YouTube Video Link : ')
download_loc = os.path.expanduser("~/Downloads/")
try:
    title = YouTube(yt_link).title
except:
    print ("Invalid YouTube Link or Internet connection unabalable.")
    quit()
print ("Your Video has been fetched, Title is : ",title)
print ("Its is Downloading Now...Wait for some time")
try:
    YouTube(yt_link).streams.filter(progressive=True).order_by('resolution')[-1].download(download_loc)
    print ("Successfully Downloaded inside Downloads folder.")
except:
    print ("Something Went Wrong. Please Try Again or Feedback me at my email.")
    quit ()
