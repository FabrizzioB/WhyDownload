# Developed by Fabrizzio Brandão
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pathlib import Path
import logging

kivy.require('2.3.0')


class YouTubeDownloader:
    downloads_path = str(Path.home() / "Downloads")

    def __init__(self, link):
        self.link = link

    def download_video(self):
        """Download video with maximum resolution to local folder."""
        youtube_object = YouTube(url=self.link, on_progress_callback=on_progress)
        video_stream = youtube_object.streams.get_highest_resolution()

        try:
            video_stream.download(output_path=self.downloads_path)
            return "Video download completed!\nCheck your Downloads folder."
        except Exception as e:
            logging.error(f"Error downloading video: {str(e)}")
            return "An error occurred during video download."

    def download_audio(self):
        """Download audio (.mp3) from a specific link."""
        youtube_object = YouTube(url=self.link, on_progress_callback=on_progress)
        audio_stream = youtube_object.streams.get_audio_only()

        try:
            audio_stream.download(output_path=self.downloads_path, mp3=True)
            return "Audio download completed!\nCheck your Downloads folder."
        except Exception as e:
            logging.error(f"Error downloading audio: {str(e)}")
            return "An error occurred during audio download."


class YouTubeDownloadApp(App):
    def build(self):
        self.title = "YouTube Downloader"
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.info_label = Label(text="This app allows you to download video or audio.")
        self.layout.add_widget(self.info_label)

        self.radio_video = ToggleButton(text='Video', group='media_type')
        self.radio_audio = ToggleButton(text='Audio', group='media_type')
        self.layout.add_widget(self.radio_video)
        self.layout.add_widget(self.radio_audio)

        self.url_input = TextInput(hint_text='Enter the link', multiline=False)
        self.layout.add_widget(self.url_input)

        download_button = Button(text='Download')
        download_button.bind(on_press=self.download_content)
        self.layout.add_widget(download_button)

        return self.layout

    def download_content(self, instance):
        vid_link = self.url_input.text.strip()

        if not vid_link:
            message = "Please enter a valid link."
            self.show_popup(message)
            return

        ytdown = YouTubeDownloader(vid_link)

        if self.radio_video.state == 'down':
            message = ytdown.download_video()
        elif self.radio_audio.state == 'down':
            message = ytdown.download_audio()
        else:
            message = "Please select either Video or Audio."

        self.show_popup(message)

    def show_popup(self, message):
        """Display a popup message."""
        popup = Popup(title='YouTube Downloader', content=Label(text=message), size_hint=(0.7, 0.5))
        popup.open()


if __name__ == "__main__":
    YouTubeDownloadApp().run()