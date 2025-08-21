from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label 
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen



class Tela_Gerenciamento(ScreenManager):
    pass


class Tela1(Screen):
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


class MeuApp(App):
    def build(self):
        tela = Tela_Gerenciamento()
        tela.add_widget()
        Tela1.add_widget()
        Tela2.add_widget()
        Tela3.a1d_widget()
        Tela4.add_widget()
        Tela5.add_widget()      
    
MeuApp().run()
