from manim import *
from manim.utils.color.XKCD import BLUSHPINK


class Tangent(Scene):
    def construct(self):
        text = Text("The tangent line", font_size=50)
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.move_to(UP*3))
        axes = (
            Axes(x_range=[0, 10, 1], x_length=12, y_range=[0, 20, 5], y_length=6)
            .add_coordinates()
            .to_edge(DL, buff=0.25)
        )

        func = axes.plot(
            lambda x: 0.1 * (x - 2) * (x - 5) * (x - 7) + 7,
            x_range=[0, 10],
            color=BLUSHPINK,
        )

        x = ValueTracker(7)
        dx = ValueTracker(2)

        secant = always_redraw(
            lambda: axes.get_secant_slope_group(
                x=x.get_value(),
                graph=func,
                dx=dx.get_value(),
                dx_line_color=YELLOW,
                dy_line_color=ORANGE,
                dx_label="\mathrm{d}x",
                dy_label="\mathrm{d}y",
                secant_line_color=GREEN,
                secant_line_length=8,
            )
        )

        dot1 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(axes.c2p(x.get_value(), func.underlying_function(x.get_value())))
        )
        dot2 = always_redraw(
            lambda: Dot()
            .scale(0.7)
            .move_to(
                axes.c2p(
                    x.get_value() + dx.get_value(),
                    func.underlying_function(x.get_value() + dx.get_value()),
                )
            )
        )

        self.add(axes, func)
        self.play(Create(VGroup(dot1, dot2, secant)))
        self.play(dx.animate.set_value(0.001), run_time=8)
        self.wait(2)
        self.play(x.animate.set_value(1), run_time=5)
        self.wait()
        self.play(x.animate.set_value(7), run_time=5)
        self.wait()
        self.play(dx.animate.set_value(2), run_time=5)
        self.wait()
