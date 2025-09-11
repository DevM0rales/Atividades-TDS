from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.core.window import Window
import random

# Fundo do aplicativo
Window.clearcolor = (0.15, 0.15, 0.2, 1)

class FilmeApp(App):
    def build(self):
        # 🎬 Listas de filmes por gênero (com ano)
        self.filmes_acao = [
            ("Matrix", 1999),
            ("Vingadores: Ultimato", 2019),
            ("John Wick", 2014),
            ("Homem Aranha", 2002)
        ]

        self.filmes_comedia = [
            ("Se Beber, Não Case!", 2009),
            ("As Branquelas", 2004),
            ("Gente Grande", 2010),
            ("Meu Malvado Favorito", 2010)
        ]

        self.filmes_animacao = [
            ("Toy Story", 1995),
            ("Shrek", 2001),
            ("Divertida Mente", 2015),
            ("Procurando Nemo", 2003)
        ]

        self.genero_escolhido = None  # Para armazenar o gênero selecionado

        # Layout principal
        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        self.label_titulo = Label(
            text="Bem-vindo!\nDigite seu nome e escolha um gênero:",
            font_size=22,
            color=(1, 1, 1, 1),
            halign="center"
        )

        # Campo para digitar o nome
        self.input_nome = TextInput(
            hint_text="Digite seu nome aqui",
            multiline=False,
            font_size=18,
            size_hint=(1, 0.2),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1)
        )

        # Botões de seleção de gênero
        box_generos = BoxLayout(size_hint=(1, 0.3), spacing=10)

        self.btn_acao = ToggleButton(text="Ação", group="genero")
        self.btn_acao.bind(on_press=self.selecionar_genero)

        self.btn_comedia = ToggleButton(text="Comédia", group="genero")
        self.btn_comedia.bind(on_press=self.selecionar_genero)

        self.btn_animacao = ToggleButton(text="Animação", group="genero")
        self.btn_animacao.bind(on_press=self.selecionar_genero)

        box_generos.add_widget(self.btn_acao)
        box_generos.add_widget(self.btn_comedia)
        box_generos.add_widget(self.btn_animacao)

        # Botões de ação
        box_botoes = BoxLayout(size_hint=(1, 0.3), spacing=10)

        self.botao_sugerir = Button(
            text="Sugerir Filme",
            background_color=(0.2, 0.6, 1, 1),
            font_size=20
        )
        self.botao_sugerir.bind(on_press=self.sugerir_filme)

        self.botao_limpar = Button(
            text="Limpar",
            background_color=(1, 0.3, 0.3, 1),
            font_size=20
        )
        self.botao_limpar.bind(on_press=self.limpar)

        box_botoes.add_widget(self.botao_sugerir)
        box_botoes.add_widget(self.botao_limpar)

        # Label para exibir o resultado
        self.label_resultado = Label(
            text="",
            font_size=20,
            color=(1, 1, 1, 1),
            halign="center"
        )

        # Adicionando widgets ao layout principal
        layout.add_widget(self.label_titulo)
        layout.add_widget(self.input_nome)
        layout.add_widget(box_generos)
        layout.add_widget(box_botoes)
        layout.add_widget(self.label_resultado)

        return layout

    def selecionar_genero(self, instance):
        self.genero_escolhido = instance.text

    def sugerir_filme(self, instance):
        nome = self.input_nome.text.strip()

        if not nome:
            self.label_resultado.text = "Por favor, digite seu nome."
            return

        if not self.genero_escolhido:
            self.label_resultado.text = "Por favor, selecione um gênero."
            return

        # Seleciona a lista correta de filmes com base no gênero
        if self.genero_escolhido == "Ação":
            filme, ano = random.choice(self.filmes_acao)
        elif self.genero_escolhido == "Comédia":
            filme, ano = random.choice(self.filmes_comedia)
        elif self.genero_escolhido == "Animação":
            filme, ano = random.choice(self.filmes_animacao)
        else:
            self.label_resultado.text = "Gênero inválido."
            return

        self.label_resultado.text = f"Olá, {nome}!\nSua sugestão de filme de {self.genero_escolhido} é:\n[b]{filme} ({ano})[/b]"
        self.label_resultado.markup = True

    def limpar(self, instance):
        self.input_nome.text = ""
        self.genero_escolhido = None
        self.btn_acao.state = "normal"
        self.btn_comedia.state = "normal"
        self.btn_animacao.state = "normal"
        self.label_resultado.text = ""

if __name__ == "__main__":
    FilmeApp().run()
