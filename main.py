from pytube import YouTube

link = input("Enter youtube video URL: ")

# select_resolution= str(input("Options:\n1. 144p\n2. 240p\n3. 360p\n4. 480p\n5. 720p\n6. 1080p\nEnter preferred resolution: "))

# conditional to select resolution

# if select_resolution == "1" or select_resolution == "144p":
#     resolution = "144p"
# elif select_resolution == "2" or select_resolution == "240p":
#     resolution =  "240p" 
# elif select_resolution == "3" or select_resolution == "360p":
#     resolution = "360p"
# elif select_resolution == "4" or select_resolution == "480p":
#     resolution = "480p"
# elif select_resolution == "5" or select_resolution == "720p":
#     resolution = "720p"
# elif select_resolution == "6" or select_resolution == "1080p":
#     resolution = "1080p"          


def Download(link):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        youtubeObject.download() # add path to download folder
    except:
        print("An Error occured")  
    print("Download successful, check your download folder")  


Download(link)

