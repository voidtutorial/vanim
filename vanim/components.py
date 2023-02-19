from manim import *

class Cell(VGroup):
    def __init__(self, data, width, height, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        self.box = Rectangle(
                width=width,
                height=height,
                fill_color=color,
                fill_opacity=0.5,
                stroke_color=color
        )
        self.text = Text(data).move_to(self.box.get_center())

        self.add(self.box, self.text)

    def update_data(self, data):
        self.text.text = data

class Buffer(VGroup):
    def __init__(self, data, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        for byte in data:
            cell = Cell(byte, 2, 2, color=color)
            self.add(cell)
        self.arrange(RIGHT, buff=0)

    def replace(self, data, color):
        self.__init__(data, color)

class Proc(VGroup):
    def __init__(self, code, lang, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        code = Code(
            code=code,
            corner_radius=0,
            background_stroke_width=0,
            tab_width=4,
            language=lang,
            insert_line_no=False,
            font="Monospace",
        )
        self.add(code)

class Debugger(VGroup):
    def __init__(self, code, lang, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        code = Code(
            code=code,
            corner_radius=0,
            background_stroke_width=0,
            tab_width=4,
            language=lang,
            font="Monospace",
        )
        arrow = Arrow(
            max_tip_length_to_length_ratio=0.1,
            color=color,
        )
        self.add(code, arrow)
        self.arrange(LEFT)

class Heap(VGroup):
    def __init__(self, data, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        for line in data:
            cell = Cell(line, 4, 2, color=color)
            self.add(cell)
        self.arrange(UP, buff=0)

class Stack(VGroup):
    def __init__(self, data, color=PURPLE, **kwargs):
        super().__init__(**kwargs)
        for line in data:
            cell = Cell(line, 4, 2, color=color)
            self.add(cell)
        self.arrange(DOWN, buff=0)

