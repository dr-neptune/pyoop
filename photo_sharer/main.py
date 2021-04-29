from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests


# communicate with frontend.kv
Builder.load_file("frontend.kv")

class FirstScreen(Screen):
    def search_image(self):
        # remove image in the image bucket
        self.manager.current_screen.ids.img.source = "files/hot_dog.png"
        # search image
        # get user query from text input
        query = self.manager.current_screen.ids.txt.text
        print(f"Now searching: {query}\n")
        
        # get wikipedia page and the first image link
        image_link = wikipedia.page(query).images[0]
        
        # download the image
        image_path = "files/image.png"
        with open(image_path, "wb") as file:
            file.write(requests.get(image_link).content)
        
        # place new image in the image bucket
        self.manager.current_screen.ids.img.source = image_path

class RootWidget(ScreenManager):
    pass
    
class MainApp(App):
    def build(self):
        return RootWidget()

MainApp().run()
