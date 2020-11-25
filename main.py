from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy_garden.mapview import MapView


def update_window_size(width, heigth):
    Window.size = (width, heigth)


class Gerenciador(ScreenManager):
    pass


class MapaSuzano(Screen):
    pass


class MenuPrincipal(Screen):
    pass


class Confirmacao(Screen):
    pass


class Cadastro(Screen):
    pass


class CovidApp(App):
    def build(self):
        return Gerenciador()


update_window_size(500, 600)
CovidApp().run()
