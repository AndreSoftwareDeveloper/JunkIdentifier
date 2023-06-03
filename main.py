import kivy
from kivy.uix.label import Label
import time
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy import platform
from PIL import Image as PILImage
from kivy.uix.image import Image

kivy.require('2.2.0')
Builder.load_file('CameraLayOut.kv')

api_response = {}

class MainScreen(Screen):
    pass


class MyApp(App):

    def on_start(self, **kwargs):
        if platform == "android":
            from android.permissions import request_permissions, Permission
            request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])


    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name='main'))
        screen_manager.add_widget(CameraScreen(name='camera'))
        screen_manager.add_widget(ResultScreen(name='result'))
        return screen_manager


class CameraScreen(Screen):
    def capture(self):
        camera = self.ids['camera']
        image = camera.__self__
        texture = image.texture
        pixels = texture.pixels
        pil_image = PILImage.frombytes(mode='RGBA', size=texture.size, data=pixels)
        pil_image.save('output.png')

        time.sleep(4)
        res = {}
        text = ''
        if res.get('object') == 'bulky_waste':
            text = 'Twój odpad musi byc zutylizowany przez PSZOK. W przyszlosci nasza aplikacja bedzie wyswietlać hormonogram odbioru odpadów w twojej okolicy, ale niestety nie dzisiaj:('
        if res.get('object') == 'green':
            text = 'Wyrzuc do zielonego.'
        if res.get('object') == 'blue':
            text = 'Wyrzuc do niebieskiego.'
        if res.get('object') == 'brown':
            text = 'To jest oczywiste. Wyrzucaj do brazowego'
        if res.get('object') == 'yellow':
            text = 'To jest oczywiste. Wyrzucaj do zółtego'

        if text == '':
            text = 'Niestety ja nie wiem do ktorej kategorii moze nalezec twój obiekt. Powodzenia.'
        text = str(type(camera))
        self.add_widget(Label(text=text, font_size='20sp'))


class ResultScreen(Screen):
    def build(self):
        print(api_response)



if __name__ == '__main__':

    MyApp().run()
