from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

Window.clearcolor = (0.8, 0.8, 0.8, 1)


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = 20
        self.spacing = 15


        self.nome_input = TextInput(
            hint_text="Digite seu nome",
            multiline=False,
            size_hint=(1, 0.2)
        )
        self.add_widget(self.nome_input)

    
        self.idade_input = TextInput(
            hint_text="Digite sua idade",
            multiline=False,
            input_filter="int",  # permite apenas números
            size_hint=(1, 0.2)
        )
        self.add_widget(self.idade_input)


        btn = Button(
            text="Enviar",
            size_hint=(1, 0.2),
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1)
        )
        btn.bind(on_press=self.verificar_idade)
        self.add_widget(btn)

        
        self.mensagem = Label(
            text="",
            size_hint=(1, 0.2),
            color=(0, 0, 0, 1),
            font_size=18
        )
        self.add_widget(self.mensagem)

    def verificar_idade(self, instance):
        nome = self.nome_input.text.strip()
        idade_texto = self.idade_input.text.strip()

        if not nome or not idade_texto:
            self.mensagem.text = "Preencha todos os campos!"
            self.mensagem.color = (1, 0, 0, 1)  # vermelho
            return

        try:
            idade = int(idade_texto)
        except ValueError:
            self.mensagem.text = "Digite uma idade válida!"
            self.mensagem.color = (1, 0, 0, 1)
            return

        if idade < 18:
            self.mensagem.text = f"Olá, {nome}! Você é menor de idade."
            self.mensagem.color = (0, 0.5, 1, 1)  # azul
            
        else:
            self.mensagem.text = f"Olá, {nome}! Você é maior de idade."
            self.mensagem.color = (0, 0.6, 0, 1)  # verde


class IdadeApp(App):
    def build(self):
        return MainLayout()


if __name__ == "__main__":
    IdadeApp().run()
