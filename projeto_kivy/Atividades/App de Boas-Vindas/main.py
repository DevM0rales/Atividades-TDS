from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle

class MeuLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        # Fundo branco
        with self.canvas.before:
            Color(1, 1, 1, 1)  # branco
            self.bg = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_bg, pos=self._update_bg)

        # Texto de bem-vindo
        self.label = Label(
            text="Bem-vindo!",
            font_size=32,
            color=(0, 0, 0, 1)  # preto
        )

        # Caixa de texto
        self.text_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.3),
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=[10, 10]
        )

        # Botão
        botao = Button(
            text="Confirmar",
            size_hint=(1, 0.3),
            background_normal='',  # remove estilo padrão
            background_color=(0.2, 0.6, 1, 1),  # azul
            color=(1, 1, 1, 1),  # texto branco
            font_size=20
        )
        botao.bind(on_press=self.atualizar_texto)

        # Adiciona widgets no layout
        self.add_widget(self.label)
        self.add_widget(self.text_input)
        self.add_widget(botao)

    def atualizar_texto(self, instance):
        nome = self.text_input.text.strip()
        if nome:
            self.label.text = f"Bem-vindo, {nome}!"
        else:
            self.label.text = "Bem-vindo!"

    def _update_bg(self, *args):
        self.bg.size = self.size
        self.bg.pos = self.pos


class MeuApp(App):
    def build(self):
        return MeuLayout()


MeuApp().run()
