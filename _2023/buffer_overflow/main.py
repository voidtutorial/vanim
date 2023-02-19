from manim import *
from vanim.components import *

class BufferOverflow(Scene):
    def construct(self):
        code = '''
        void vuln()
        {
            char buf[8];
            gets(buf);
        }
        '''

        buf = Buffer("hello", PURPLE)

        self.play(Write(buf.scale(0.5)))


        self.wait()
