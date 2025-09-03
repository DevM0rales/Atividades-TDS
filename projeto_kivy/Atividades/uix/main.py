from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from api import autenticar_usuario  # Importa a API fake

# Cores de fundo
Window.clearcolor = (0.95, 0.95, 0.95, 1)


class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation="vertical", padding=20, spacing=15)

        layout.add_widget(Label(
            text="Login",
            font_size=32,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2)
        ))

        self.username = TextInput(
            hint_text="Usuário",
            multiline=False,
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10)
        )
        layout.add_widget(self.username)

        self.password = TextInput(
            hint_text="Senha",
            password=True,
            multiline=False,
            size_hint=(1, 0.15),
            background_normal='',
            background_color=(1, 1, 1, 1),
            foreground_color=(0, 0, 0, 1),
            padding=(10, 10)
        )
        layout.add_widget(self.password)

        login_btn = Button(
            text="Entrar",
            size_hint=(1, 0.15),
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        login_btn.bind(on_press=self.validar_login)
        layout.add_widget(login_btn)

        self.feedback = Label(
            text="",
            color=(1, 0, 0, 1),
            font_size=14,
            size_hint=(1, 0.1)
        )
        layout.add_widget(self.feedback)

        layout.add_widget(Button(
            text="Cadastrar-se",
            size_hint=(1, 0.15),
            background_color=(0.1, 0.8, 0.3, 1),
            color=(1, 1, 1, 1)
        ))

        self.add_widget(layout)

    def validar_login(self, instance):
        usuario = self.username.text
        senha = self.password.text

        if autenticar_usuario(usuario, senha):
            self.feedback.text = "Login bem-sucedido!"
            self.feedback.color = (0, 0.6, 0, 1)
        else:
            self.feedback.text = "Usuário ou senha incorretos."
            self.feedback.color = (1, 0, 0, 1)


class LoginApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name="login"))
        return sm



LoginApp().run()
