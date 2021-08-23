# pip install pafy
# pip install youtube_dl
import pafy


def youtubeDownloader(userInput):
    # Opening the file that contains the links in read mode
    file = open(userInput, 'r')
    # Irriterate through the file
    for link in file:
        # Assign link to the "url" variable
        url = link
        try:
            video = pafy.new(url)
            # Extracting the best available audio
            best_quality = video.getbestaudio()
            print(video.title)
            # Downloading the extracted file
            best_quality.download()
        except:
            pass
    file.close()


userInput = input("Please enter .txt file which contains the youtube links to download: ")
extention = ".txt"

# Check if the file contains the .txt extention
if extention in userInput:
    youtubeDownloader(userInput)
else:
    userInput += extention
    youtubeDownloader(userInput)
