from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder


class Tela_Principal(Screen):
    pass

class Tela1(Screen):
    pass


class Tela2(Screen):
    pass


class Tela3(Screen):
    pass


class Tela4(Screen):
    pass


class Tela5(Screen):
    pass


    

class Meu_App(App):
    def build(self):
        Builder.load_file('telas.kv')
        sm = ScreenManager()
        sm.add_widget(Tela_Principal(name='principal'))
        sm.add_widget(Tela2(name='tela1'))
        sm.add_widget(Tela3(name='tela2'))
        sm.add_widget(Tela4(name='tela3'))
        sm.add_widget(Tela5(name='tela4'))
        sm.add_widget(Tela5(name='tela5'))         
        return sm
    
Meu_App().run()
