from kivy.uix.textinput import TextInput
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner



class MeuApp(App):
    def build(self):
        
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        self.caixa_texto = TextInput(
            text='Informe seu nome',
            size_hint=(1, 0.2)
            )
        
        
        self.genero = Spinner(
            text='Gêneros',
            values=("Comédia", "Terror", "Romance", "Ação"),
            size_hint=(1, 0.2)   
        )
        
        self.botao = Button(
            text='Sugerir Filme', 
            size_hint=(1, 0.2))
        
        
        self.texto = Label(
            text='Sugestão de Filmes', 
            size_hint=(1, 0.2))
        
        
        layout.add_widget(self.texto)
        layout.add_widget(self.caixa_texto)
        layout.add_widget(self.genero)
        layout.add_widget(self.botao)
    
        return layout
    
    def sugerir(self, instace):
        filmes = {
            "Ação" : [],
            "Terror": [],
            "Romance": [],
            "Comédia": []
        }
    
MeuApp().run()

