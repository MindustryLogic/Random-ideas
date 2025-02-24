import manim as manim
from manim import *
class helloSEKAI(Scene):
    def construct (self):
        oHi = (Text("hello SEKAI"))
        self.play(Create(oHi))
        self.wait

class intro(Scene):
    def construct (self):
        SoonToBeTree = (Text("Tree"))
        FirstText = (Text("Bad apple\nremix"))
        self.play(Create(FirstText))
        self.wait
        self.play(Rotate(SoonToBeTree),angle=0.5*PI)
        
class UsingRotate(Scene):
    def construct(self):
        self.play(
            Rotate(
                Square(side_length=0.5).shift(UP * 2),
                angle=2*PI,
                about_point=ORIGIN,
                rate_func=linear,
                color=BLUE,
            ),
            Rotate(Square(side_length=0.5), angle=2*PI, rate_func=linear),
            )