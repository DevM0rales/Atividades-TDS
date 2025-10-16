from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
import random
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

#                    R  G  B  A
Window.clearcolor = (1, 1, 1, 1)

# ---------- Tela de Boas-Vindas ----------
class TelaBoasVindas(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.input_nome = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )

        btn_continuar = Button(
            text="Continuar",
            size_hint=(1, 0.2)
        )
        btn_continuar.bind(on_press=self.ir_para_sugestoes)

        layout.add_widget(Label(text="Bem-vindo! Digite seu nome:", color=(0.5, 0.5, 0.5, 1), font_size=18))
        layout.add_widget(self.input_nome)
        layout.add_widget(btn_continuar)

        self.add_widget(layout)

    def ir_para_sugestoes(self, instance):
        nome = self.input_nome.text.strip()
        if nome:
            self.manager.get_screen("sugestoes").set_nome(nome)
            self.manager.current = "sugestoes"


# ---------- Tela de Sugestões ----------
class TelaSugestoes(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical', spacing=10, padding=20)

        self.label_boasvindas = Label(text="", font_size=24, color=(0.5, 0.5, 0.5, 1))
        self.spinner_genero = Spinner(
            text="Escolha um gênero",
            values=("Ação", "Comédia", "Animação"),
            size_hint=(1, 0.2),
            
        )

        btn_sugerir = Button(
            text="Sugerir Filme",
            size_hint=(1, 0.2)
        )
        btn_sugerir.bind(on_press=self.sugerir_filme)

        self.label_filme = Label(text="", color=(0, 0, 0, 1))

        self.layout.add_widget(self.label_boasvindas)
        self.layout.add_widget(self.spinner_genero)
        self.layout.add_widget(btn_sugerir)
        self.layout.add_widget(self.label_filme)

        self.add_widget(self.layout)

        # Dicionário de filmes
        self.filmes = {
            "Ação": ["John Wick", "Mad Max: Estrada da Fúria", "Gladiador"],
            "Comédia": ["As Branquelas", "Todo Mundo em Pânico", "O Máskara"],
            "Animação": ["Toy Story", "Shrek", "Procurando Nemo", "Gato de botas"],
            "Terror": ["Invocação do mal", ]
        }

    def set_nome(self, nome):
        self.label_boasvindas.text = f"Olá, {nome}! Escolha um gênero de filme:"

    def sugerir_filme(self, instance):
        genero = self.spinner_genero.text
        if genero in self.filmes:
            filme = random.choice(self.filmes[genero])
            self.label_filme.text = f"Sugestão: {filme}"
        else:
            self.label_filme.text = "Por favor, escolha um gênero válido!"


# ---------- Gerenciador de Telas ----------
class Gerenciador(ScreenManager):
    pass


# ---------- Aplicativo ----------
class MeuApp(App):
    def build(self):
        sm = Gerenciador()
        sm.add_widget(TelaBoasVindas(name="boasvindas"))
        sm.add_widget(TelaSugestoes(name="sugestoes"))
        return sm


if __name__ == "__main__":
    MeuApp().run()
