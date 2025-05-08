from manim import *


class EquationExercise(Scene):
    def construct(self):
        eq1 = MathTex(
            r"\begin{cases} \sqrt{(x_N - 4)^2 + (y_N - 4)^2} = \sqrt{10} \\ 3x_N - y_N + 2 = 0 \end{cases}"
        )

        self.play(Write(eq1))
        self.wait(1)
