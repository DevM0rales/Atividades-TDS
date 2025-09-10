# ia_simulacao.py
import json
import threading
import time
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.progressbar import ProgressBar
from kivy.animation import Animation
from kivy.core.audio import SoundLoader


class IASimulacao(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", **kwargs)

        # Estado inicial
        self.nivel_ameaca = 20
        self.status = "Online"
        self.carregar_estado()

        # Cabeçalho fixo
        cabecalho = BoxLayout(size_hint_y=0.1, spacing=5, padding=5)
        for cmd in ["injetar_virus", "desligar_sistemas", "acessar_dados"]:
            btn = Button(text=cmd, on_press=lambda inst, c=cmd: self.send_command(c))
            cabecalho.add_widget(btn)
        self.add_widget(cabecalho)

        # Barra de ameaça
        self.progress_bar = ProgressBar(max=100, value=self.nivel_ameaca, size_hint_y=0.05)
        self.add_widget(self.progress_bar)

        # Área de log
        self.scroll = ScrollView(size_hint=(1, 0.85))
        self.log_label = Label(size_hint_y=None, text="", valign="top")
        self.log_label.bind(texture_size=self.update_log_height)
        self.scroll.add_widget(self.log_label)
        self.add_widget(self.scroll)

        # Thread de monitoramento da IA
        threading.Thread(target=self.monitor_ia, daemon=True).start()

    def update_log_height(self, instance, value):
        self.log_label.height = value[1]
        self.log_label.text_size = (self.log_label.width, None)

    def add_log(self, mensagem):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.log_label.text += f"{timestamp} {mensagem}\n"
        self.scroll.scroll_y = 0  # Mantém a rolagem no fim

    def send_command(self, comando):
        respostas = {
            "injetar_virus": "IA: Vírus implantado nos sistemas externos!",
            "desligar_sistemas": "IA: Sistemas principais foram desligados!",
            "acessar_dados": "IA: Banco de dados invadido com sucesso!",
        }

        if comando in respostas:
            self.add_log(respostas[comando])
            self.nivel_ameaca += 15
            self.progress_bar.value = self.nivel_ameaca
            if self.nivel_ameaca >= 80:
                self.piscar_barra()
                self.alerta_sonoro()
        else:
            self.add_log("IA: Comando não reconhecido.")

        self.salvar_estado()

    def piscar_barra(self):
        anim = (Animation(value=self.nivel_ameaca, duration=0.3) +
                Animation(value=self.nivel_ameaca - 5, duration=0.3))
        anim.repeat = True
        anim.start(self.progress_bar)

    def alerta_sonoro(self):
        alerta = SoundLoader.load("alerta.wav")
        if alerta:
            alerta.play()

    def salvar_estado(self):
        with open("estado.json", "w") as f:
            json.dump({
                "nivel_ameaca": self.nivel_ameaca,
                "status": self.status
            }, f)

    def carregar_estado(self):
        try:
            with open("estado.json", "r") as f:
                dados = json.load(f)
                self.nivel_ameaca = dados.get("nivel_ameaca", 20)
                self.status = dados.get("status", "Online")
        except FileNotFoundError:
            pass

    def monitor_ia(self):
        while True:
            time.sleep(5)
            self.add_log("IA: Processos internos concluídos.")
            self.salvar_estado()


class IASimulacaoApp(App):
    def build(self):
        return IASimulacao()


if __name__ == "__main__":
    IASimulacaoApp().run()
