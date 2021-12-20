import os
import youtube_dl
PATH = '/'.join(os.getcwd().split('/')[:3]) + "/Downloads/Music" #The Directory where the downloaded files will be saved.
def download(video_info,PATH):
    """
    Will download a .wav audio file of a youtube video to the given path.
    """
    
    filename = f"/{video_info['title']}.wav" #Format of the downloaded files
    options={
        'format':'bestaudio/best',
        'keepvideo':False,
        'outtmpl':PATH + filename,
    }
    
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print(f"Download complete... {filename}")

def main():
    #Creates a Folder for storing all the files downloaded using this script if not one already exisitng.
    if not os.path.isdir(PATH):
        os.mkdir(PATH )
    url = input("Enter a Youtube Video or Playlist link:")
    videos_info = youtube_dl.YoutubeDL().extract_info(url = url,download=False)
    
    #Checking if it is a Playlist or a video.
    try:
        for video_info in videos_info['entries']:
            download(video_info,PATH)
    except KeyError:
        download(videos_info,PATH)

if __name__=='__main__':
    main()