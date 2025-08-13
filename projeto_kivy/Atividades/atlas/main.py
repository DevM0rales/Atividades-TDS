from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, BooleanProperty
from kivy.clock import Clock

class PainelIA(BoxLayout):
    status = StringProperty("IA Desligada")
    nivel_ameaca = NumericProperty(0)
    ia_ligada = BooleanProperty(False)

    def alternar_ia(self, estado):
        """Liga ou desliga a IA"""
        self.ia_ligada = estado
        if self.ia_ligada:
            self.status = "IA Ligada"
            self.nivel_ameaca = 10
            # Inicia aumento de ameaça se ligado
            Clock.schedule_interval(self.aumentar_ameaca, 1)
        else:
            self.status = "IA Desligada"
            self.nivel_ameaca = 0
            Clock.unschedule(self.aumentar_ameaca)

    def aumentar_ameaca(self, dt):
        """Simula aumento do nível de ameaça"""
        if self.nivel_ameaca < 100:
            self.nivel_ameaca += 5

    def enviar_comando(self):
        """Processa o comando digitado"""
        comando = self.ids.campo_comando.text.strip().lower()
        if not comando:
            return

        if not self.ia_ligada:
            self.status = "IA desligada. Ligue para receber comandos."
        else:
            if comando == "alerta":
                self.status = "⚠️ ALERTA ATIVADO"
                self.nivel_ameaca = min(self.nivel_ameaca + 20, 100)
            elif comando == "reduzir":
                self.status = "🔽 Ameaça Reduzida"
                self.nivel_ameaca = max(self.nivel_ameaca - 20, 0)
            else:
                self.status = f"Comando recebido: {comando}"

        self.ids.campo_comando.text = ""  # Limpa campo

class PainelIAApp(App):
    def build(self):
        return PainelIA()

if __name__ == "__main__":
    PainelIAApp().run()
