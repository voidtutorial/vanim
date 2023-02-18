from manim import *

from vanim.components import Buffer

class DifferentWeight(Scene):
    def construct(self):
        code = '''
        void vuln()
        {
            char buf[8];
            gets(buf);
        }
        '''

        rendered_code = Code(
            code=code,
            corner_radius=0,
            background_stroke_width=0,
            tab_width=4,
            language="C",
            insert_line_no=False,
            font="Monospace"
        )

        text = Text("char buf[8]")

        foobar = Text("foobar")

        data = [["-"]*8]
        buf_table = Table(
            table=data,
            include_outer_lines=True
        )

        overflow = Table(
            [["-"]*2],
            include_outer_lines=True,
        )

        c1 = overflow.get_cell((1,1), color=RED)
        c2 = overflow.get_cell((1,2), color=RED)

        overflow.add(c1, c2)

        gg1 = Group(buf_table, overflow).arrange(RIGHT, buff=0)

        g1 = Group(text, gg1).scale(0.5).arrange(DOWN, buff=0.5).to_edge(DOWN, buff=1)
        g2 = Group(rendered_code).arrange(buff=1)

        self.add(g2)
        self.wait()
        self.play(g2.animate.shift(UP).to_edge(UP, buff=1))
        self.wait()
        self.play(GrowFromCenter(g1))
        self.wait()

        data[0][1] = "B"
        g1.add(foobar)
        self.wait(5)
        

