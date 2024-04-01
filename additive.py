from manim import *
import numpy as np


class AdditiveFunction(Scene):
    def construct(self):
        axes = (
            Axes(x_range=[0, 2.1, 1], x_length=12, y_range=[0, 7, 2], y_length=6)
            .add_coordinates()
            .to_edge(DL, buff=0.25)
        )

        func1 = axes.plot(lambda x: x**2, x_range=[0, 2], color=YELLOW)
        func1_lab = (
            MathTex("y={x}^2").scale(0.8).next_to(func1, UR, buff=0.2).set_color(YELLOW)
        )

        func2 = axes.plot(lambda x: x, x_range=[0, 2], color=GREEN)
        func2_lab = (
            MathTex("y=x").scale(0.8).next_to(func2, UR, buff=0.2).set_color(GREEN)
        )

        func3 = axes.plot(lambda x: x**2 + x, x_range=[0, 2], color=PURPLE_D)
        func3_lab = (
            MathTex("y=x^2 + x")
            .scale(0.8)
            .next_to(func3, UR, buff=0.2)
            .set_color(PURPLE_D)
        )

        self.add(axes, func1, func2, func3, func1_lab, func2_lab, func3_lab)
        self.wait()

        for k in np.arange(0.2, 2.1, 0.2):
            line1 = DashedLine(
                start=axes.c2p(k, 0),
                end=axes.c2p(k, func1.underlying_function(k)),
                stroke_color=YELLOW,
                stroke_width=5,
            )

            line2 = DashedLine(
                start=axes.c2p(k, 0),
                end=axes.c2p(k, func2.underlying_function(k)),
                stroke_color=GREEN,
                stroke_width=7,
            )

            line3 = Line(
                start=axes.c2p(k, 0),
                end=axes.c2p(k, func3.underlying_function(k)),
                stroke_color=PURPLE,
                stroke_width=10,
            )

            self.play(Create(line1))
            self.play(Create(line2))

            if len(line1) > len(line2):
                self.play(line2.animate.shift(UP * line1.get_length()))
            else:
                self.play(line1.animate.shift(UP * line2.get_length()))

            self.play(Create(line3))
        self.wait()

        area1 = axes.get_riemann_rectangles(
            graph=func1, x_range=[0, 2], dx=0.1, color=[BLUE, GREEN]
        )
        area2 = axes.get_riemann_rectangles(
            graph=func2, x_range=[0, 2], dx=0.1, color=[YELLOW, PURPLE]
        )

        self.play(Create(area1))
        self.play(area1.animate.set_opacity(0.5))
        self.play(Create(area2))
        self.wait()
        for k in range(20):
            self.play(area2[k].animate.shift(UP * area1[k].get_height()))
        self.wait()
