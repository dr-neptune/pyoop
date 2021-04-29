from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests


# communicate with frontend.kv
Builder.load_file("wiki_frontend.kv")

class FirstScreen(Screen):
    def get_image_link(self):
        # get user query from text input
        query = self.manager.current_screen.ids.txt.text
        print(f"Now searching: {query}\n")

        # get wikipedia page and the first image link
        return wikipedia.page(query).images[0]
        
    def download_image(self):
        # download the image
        image_path = "files/image.png"
        with open(image_path, "wb") as file:
            file.write(requests.get(self.get_image_link()).content)
        return image_path

    def clear_image(self):
        self.manager.current_screen.ids.img.source = ""
        self.manager.current_screen.ids.img.reload()
        
    def set_image(self):
        self.clear_image()
        # place new image in the image bucket
        self.manager.current_screen.ids.img.source = self.download_image()
        self.manager.current_screen.ids.img.reload()

class RootWidget(ScreenManager):
    pass
    
class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()
