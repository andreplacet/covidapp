from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen


class Gerenciador(ScreenManager):
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


CovidApp().run()
