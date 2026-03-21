# made in collabortion with Artificial Intelligence (AI).
# My first AI collaboration project, I hope you like it!

import os
import pytube 
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

url = input("Enter Youtube URL: ")

# let user choose where to save the video
folder = filedialog.askdirectory(title="Choose Download Location")

if not folder:
    print("No folder selected. Exiting.")
    exit()
else:
    try:
        yt = YouTube(url)
        print(f"Title: {yt.title}")
        print(f"Author: {yt.author}")
        print(f"Views: {yt.views}")
        print(f"Length: {yt.length} seconds")

        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=folder)
        
        print(f"Video downloaded successfully to {folder}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

