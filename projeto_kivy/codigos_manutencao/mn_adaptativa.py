#Manutenção Adaptativa

from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window


#Faz uma adaptação para suportar um tema escuro no software
class AdaptativoApp(App):
    def build(self):
        # Simula o modo escuro
        Window.clearcolor = (0, 0, 0, 1)  # Fundo preto
        return Label(text="Agora o app suporta tema escuro!", color=(1, 1, 1, 1))

AdaptativoApp().run()
