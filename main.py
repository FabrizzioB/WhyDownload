import logging
import PySimpleGUI as sg

from pytube import YouTube


class YouTubeDownloaderApp:

    def __init__(self, link: str):
        self.link = link

    
    def download_video(self):
        yt_object = YouTube(self.link)
        yt_object = yt_object.streams.get_highest_resolution()
    
        try:
            yt_object.download()
        except NameError:
            logging.error("There has been an error when downloading your YouTube video...")
        
        print("Download completed!\n")


    def download_audio(self):
        yt_object = YouTube(self.link)
        yt_object = yt_object.streams.get_audio_only("mp4")
    
        try:
            yt_object.download()
        except NameError:
            logging.error("There has been an error when downloading your YouTube audio...")
        
        print("Download completed!\n")

if __name__ == "__main__":
    # Create the window for the app
    sg.theme('DarkAmber')
    # Layout
    layout = [[sg.Text("This app allows you to download files within YouTube")],
              [sg.Text("Choose one of the following: ")],
              [sg.Radio('Video (HQ)', 1, enable_events=True, key='R1'), sg.Radio('Audio (.mp4)', 1, enable_events=True, key='R2')],
              [sg.Text("Enter the link from which you want to download: "), sg.InputText()],
              [sg.Button("Download"), sg.Button("Exit")]]
    
    # Window is opening here
    window = sg.Window(title="YouTube Downloader v1.0", layout=layout, margins=(90, 60))

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the Exit button
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "Download":
            """The link for the source you want to download"""
            vid_link = values[0]
            yt_downloader = YouTubeDownloaderApp(vid_link)

            """Choose if you want audio or video"""
            if values['R1']:
                yt_downloader.download_video()
            elif values['R2']:
                yt_downloader.download_audio()

    window.close()
