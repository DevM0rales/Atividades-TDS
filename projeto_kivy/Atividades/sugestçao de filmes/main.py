from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random

# Personalização de cores e fundo
Window.clearcolor = (0.15, 0.15, 0.2, 1)  # Fundo escuro

class FilmeApp(App):
    def build(self):
        self.filmes = [
            ("Matrix", 1999),
            ("Toy Story", 1995),
            ("Avatar", 2009),
            ("O Rei Leão", 1994),
            ("Homem-Aranha", 2002),
            ("Vingadores: Ultimato", 2019),
            ("Interestelar", 2014),
            ("Shrek", 2001),
            ("Duna", 2021),
            ("Brilho eterna de uma mente sem lembranças", 2000)
        ]

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.label_titulo = Label(
            text="Bem-vindo!\nDigite seu nome para receber uma sugestão de filme:",
            font_size=22,
            color=(1, 1, 1, 1),
            halign="center"
        )

        self.input_nome = TextInput(
            hint_text="Digite seu nome aqui",
            multiline=False,
            font_size=18,
            size_hint=(1, 0.2),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )

        self.botao_sugerir = Button(
            text="Sugerir Filme",
            size_hint=(1, 0.3),
            background_color=(0.2, 0.6, 1, 1),
            font_size=20
        )
        self.botao_sugerir.bind(on_press=self.sugerir_filme)

        self.label_resultado = Label(
            text="",
            font_size=20,
            color=(1, 1, 1, 1),
            halign="center"
        )

        layout.add_widget(self.label_titulo)
        layout.add_widget(self.input_nome)
        layout.add_widget(self.botao_sugerir)
        layout.add_widget(self.label_resultado)

        return layout

    def sugerir_filme(self, instance):
        nome = self.input_nome.text.strip()

        if not nome:
            self.label_resultado.text = "Por favor, digite seu nome."
            return

        filme, ano = random.choice(self.filmes)
        self.label_resultado.text = f" Olá, [b]{nome}[/b]! Sua sugestão é:\n[b]{filme} ({ano})[/b]"
        self.label_resultado.markup = True  # Habilita negrito


if __name__ == "__main__":
    FilmeApp().run()
