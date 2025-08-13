import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.lang import Builder

Builder.load_file("pong.kv")  # Certifique-se de que esse arquivo existe

# Definindo a classe da Bola
class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)
    
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos
        
    def bounce_paddle(self, paddle):
        if self.collide_widget(paddle):
            self.velocity_x *= -1

# Definindo a classe da Raquete (Player)
class PongPaddle(Widget):  # Corrigido: Nome com maiúscula
    pass

# Definindo a classe principal do jogo
class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)
    
    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = Vector(*vel).rotate(45)  # Corrigido: velocity, não veloxity
        
    def update(self, dt):
        self.ball.move()
        
        if self.ball.y < 0 or self.ball.top > self.height:
            self.ball.velocity_y *= -1
            
        self.ball.bounce_paddle(self.player1)
        self.ball.bounce_paddle(self.player2)
        
        if self.ball.x < 0 or self.ball.x > self.width:
            self.serve_ball()
            
class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)  # Corrigido: schedule_interval
        return game

if __name__ == "__main__":
    PongApp().run()
