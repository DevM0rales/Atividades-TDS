import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.app import App

class Adicionar(BoxLayout):
    pass

class MeuApp(App):
    def build(self):
        return Adicionar()
    
    
MeuApp().run()