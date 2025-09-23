#Manutenção Preventiva

from kivy.app import App
from kivy.uix.button import Button

def salvar_log(erro):
    with open("log_erros.txt", "a") as f:
        f.write(f"Erro detectado: {erro}\n")

class PreventivoApp(App):
    def build(self):
        return Button(text="Simular erro", on_press=self.gera_erro)

    def gera_erro(self, instance):
        try:
            x = 1 / 0  # Erro proposital
        except Exception as e:
            salvar_log(e)
            print("Erro registrado no log, para futura correção!")

PreventivoApp().run()
