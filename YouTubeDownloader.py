import logging
import PySimpleGUI as PySimple
from pathlib import Path
from pytube import YouTube


class YouTubeDownloader:

    """
    Developed by Fabrizzio Brandão

    This is a YouTube Downloader Application
    Just insert the link and choose the type of download and click download
    File will appear in the "Downloads" folder
    """

    downloads_path = str(Path.home() / "Downloads")

    def __init__(self, link):
        self.link = link

    def download_video(self):
        """This method allows you to download videos (.mp4) with maximum resolution to your local folder."""
        youtube_object = YouTube(self.link)
        youtube_object = youtube_object.streams.get_highest_resolution()
        try:
            youtube_object.download(output_path=self.downloads_path)
        except NameError:
            logging.error("There has been an error when downloading your YouTube Video...")

        print("This download has completed!\nCheck your folder where file is located.")

    def download_audio(self):
        """This method allows you to download audios (.mp4) from a specific link to your local folder."""
        youtube_object = YouTube(self.link)
        youtube_object = youtube_object.streams.get_audio_only("mp4")
        try:
            youtube_object.download(output_path=self.downloads_path)
        except NameError:
            logging.error("There has been an error when downloading your YouTube Video...")

        print("Download is complete!\nCheck your \"Downloads\" folder.")


if __name__ == "__main__":
    # Create the window
    PySimple.theme('DarkAmber')

    # Layout is established here
    layout = [[PySimple.Text("This app allows you to download YouTube video or audio.")],
              [PySimple.Text("Choose one of the following: ")],
              [PySimple.Radio('Video', 1, enable_events=True, key='R1'),
               PySimple.Radio('Audio', 1, enable_events=True, key='R2')],
              [PySimple.Text("Enter the link from which you want to download: "), PySimple.InputText()],
              [PySimple.Button("Download"), PySimple.Button("Exit")]]

    # Window is opening here
    window = PySimple.Window(title="YouTube Downloader", layout=layout, margins=(90, 60))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the Exit button
        if event == "Exit" or event == PySimple.WIN_CLOSED:
            break
        elif event == "Download":
            """The link for the source you want to download"""
            vid_link = values[0]
            ytdown = YouTubeDownloader(vid_link)
            """Choose if you want audio or video"""
            if values['R1']:
                ytdown.download_video()
            elif values['R2']:
                ytdown.download_audio()

    # Finally close the window
    window.close()
