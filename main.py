from manim import *

class Anim(Scene):
    def construct(self):
        circle = Circle(color=PINK).set_fill(opacity=0.8)

        self.play(Create(circle))
        self.wait()
