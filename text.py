import time
import sys

class Text():
    def __init__(self):
        self.name = "text"

    def text_speed(self, texte, delai=0.01):
        for i in texte:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(delai)
        print()