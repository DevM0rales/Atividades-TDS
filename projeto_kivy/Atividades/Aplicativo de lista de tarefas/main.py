from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle


class ListaTarefasApp(App):
    def build(self):
        # Layout principal
        main_layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        # Fundo branco
        with main_layout.canvas.before:
            Color(1, 1, 1, 1)  # branco
            self.bg = Rectangle(size=main_layout.size, pos=main_layout.pos)
        main_layout.bind(size=self._update_bg, pos=self._update_bg)

        # Título fixo
        titulo = Label(
            text=" Minha Lista de Tarefas",
            font_size=28,
            size_hint=(1, 0.2),
            color=(0, 0, 0, 1)  # texto preto
        )
        main_layout.add_widget(titulo)

        # Entrada de texto + botão "Adicionar"
        entrada_layout = BoxLayout(size_hint=(1, 0.2), spacing=10)
        self.entrada = TextInput(
            hint_text="Digite uma tarefa...",
            multiline=False,
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[10, 10]
        )
        botao_add = Button(
            text="Adicionar",
            background_normal='',
            background_color=(0.2, 0.6, 1, 1),  # azul
            color=(1, 1, 1, 1),
            font_size=18
        )
        botao_add.bind(on_press=self.adicionar_tarefa)
        entrada_layout.add_widget(self.entrada)
        entrada_layout.add_widget(botao_add)

        main_layout.add_widget(entrada_layout)

        # Área da lista de tarefas com ScrollView
        self.scroll = ScrollView(size_hint=(1, 0.6))
        self.lista_layout = GridLayout(cols=1, spacing=5, size_hint_y=None)
        self.lista_layout.bind(minimum_height=self.lista_layout.setter('height'))
        self.scroll.add_widget(self.lista_layout)

        main_layout.add_widget(self.scroll)

        # Botão limpar lista
        botao_limpar = Button(
            text="Limpar Lista",
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(1, 0.2, 0.2, 1),  # vermelho
            color=(1, 1, 1, 1),
            font_size=18
        )
        botao_limpar.bind(on_press=self.limpar_lista)
        main_layout.add_widget(botao_limpar)

        return main_layout

    def adicionar_tarefa(self, instance):
        tarefa = self.entrada.text.strip()
        if tarefa:
            nova_tarefa = Label(
                text=f"• {tarefa}",
                font_size=20,
                size_hint_y=None,
                height=40,
                color=(0, 0, 0, 1)
            )
            self.lista_layout.add_widget(nova_tarefa)
            self.entrada.text = ""  # limpa o campo
        else:
            aviso = Label(
                text="Insira uma tarefa válida",
                font_size=16,
                size_hint_y=None,
                height=30,
                color=(1, 0, 0, 1)
            )
            self.lista_layout.add_widget(aviso)

    def limpar_lista(self, instance):
        self.lista_layout.clear_widgets()

    def _update_bg(self, *args):
        self.bg.size = args[0].size
        self.bg.pos = args[0].pos


ListaTarefasApp().run()
