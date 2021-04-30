from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard

from filesharer import FileSharer
import webbrowser
import time

# communicate with frontend.kv
Builder.load_file("frontend.kv")


class CameraScreen(Screen):
    def start(self):
        """Starts the camera and changes the button text"""
        self.ids.camera.Index = -1
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture
        self.ids.camera.opacity = 1


    def stop(self):
        """stops the camera and changes button text"""
        self.ids.camera.play = False
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None
        self.ids.camera.opacity = 0

    def capture(self):
        """
        Creates a filename with current time.
        Captures an image and saves it with the given filename
        """
        self.filename = "files/" + time.strftime("%Y%m%d-%H%M%S") + ".png"
        self.ids.camera.export_to_png(self.filename)
        self.manager.current = "image_screen"
        self.manager.current_screen.ids.img.source = self.filename


class ImageScreen(Screen):
    link_message = "Create a link first!"

    def create_link(self):
        """
        Accesses the photo filepath, uploads it to the web
        and inserts the link in the label widget
        """
        file_path = App.get_running_app().root.ids.camera_screen.filename
        file_sharer = FileSharer(file_path)
        self.url = file_sharer.share()
        self.ids.link.text = self.url

    def copy_link(self):
        """
        copy link to the clipboard
        """
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text = self.link_message

    def open_link(self):
        """
        Open link with the default browser
        """
        try:
            webbrowser.open(self.url)
        except:
            self.ids.link.text = self.link_message


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
