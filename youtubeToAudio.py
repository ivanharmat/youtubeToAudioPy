import sys
import os
from pytube import YouTube
import moviepy.editor as mp


def main():

	if len(sys.argv) > 1 :
		youtubeFile = "https://www.youtube.com/watch?v="+str(sys.argv[1])
		youtubeVideo = YouTube(youtubeFile)

		print("Downloading "+youtubeVideo.title)

		downloadableStreams = youtubeVideo.streams

		downloadableStreams.first().download("files/")

		os.rename("files/"+downloadableStreams.first().default_filename, "files/"+youtubeVideo.title+".mp4")

		print("Video downloaded!")
		print("Now converting to mp3 ...")

		clip = mp.VideoFileClip("files/"+youtubeVideo.title+".mp4")
		clip.audio.write_audiofile("files/"+youtubeVideo.title+".mp3")

		# delete the video file - not needed anymore
		os.remove("files/"+youtubeVideo.title+".mp4")

		print("Converting to mp3 done!")


	else :
		print("Error - enter youtube video url.")


if __name__ == "__main__":
    main()