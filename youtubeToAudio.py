import sys
import os
from pytube import YouTube
import moviepy.editor as mp


def main():

	if len(sys.argv) > 1 :
		youtube_file = "https://www.youtube.com/watch?v="+str(sys.argv[1])
		youtube_video = YouTube(youtube_file)

		print("Downloading "+youtube_video.title)

		downloadable_streams = youtube_video.streams

		downloadable_streams.first().download("files/")

		os.rename("files/"+downloadable_streams.first().default_filename, "files/"+youtube_video.title+".mp4")

		print("Video downloaded!")
		print("Now converting to mp3 ...")

		clip = mp.VideoFileClip("files/"+youtube_video.title+".mp4")
		clip.audio.write_audiofile("files/"+youtube_video.title+".mp3")

		# delete the video file - not needed anymore
		os.remove("files/"+youtube_video.title+".mp4")

		print("Converting to mp3 done!")


	else :
		print("Error - enter youtube video url.")


if __name__ == "__main__":
	main()