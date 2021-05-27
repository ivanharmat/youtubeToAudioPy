import sys
import os
import wget
import moviepy.editor as mp

def main():

	if len(sys.argv) > 1 :

		downloadedFile = wget.download(str(sys.argv[1]))
		movedDownloadedFile = "files/"+downloadedFile
		# move and rename file
		if len(sys.argv) > 2 :
			movedDownloadedFile = "files/"+str(sys.argv[2])+".mp4"
		os.rename(downloadedFile, movedDownloadedFile)
		print("Download Done" + movedDownloadedFile)

		print("Now converting to mp3 ...")

		clip = mp.VideoFileClip(movedDownloadedFile)
		clip.audio.write_audiofile(movedDownloadedFile+".mp3")

		# delete the video file - not needed anymore
		os.remove(movedDownloadedFile)

		print("Converting to mp3 done!")
	else :
		print("Error - enter video url.")

if __name__ == "__main__":
    main()