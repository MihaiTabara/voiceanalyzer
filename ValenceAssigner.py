"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import csv

from ValenceTextHandler import ValenceTextHandler

class AnewValences:
    def __init__(self, file_input):
        self._valences = {}
        self.file_input = file_input

    def handle(self):
        with open(self.file_input,'rb') as fin:
            dr = csv.DictReader(fin)
            for i in dr:
                self._valences[i['Description']] = float(i['Valence Mean'])

    @property
    def valences(self):
        self.handle()
        return self._valences

class ValenceAssigner:
    """
    ValenceAssigner class is the class to assign a general valence to a text.
        * [input] - list containing valuable words
        * [output] - total valuance of text
    """
    def __init__(self, file_input):
        self.helper = ValenceTextHandler(file_input)
        self.input_words = self.helper.words

        self.anew = AnewValences("scripts/male.csv")
        self.anew_valences = self.anew.valences

        self._text_valence = float(4.5)

    def _handle(self):
        up = float(0.0)
        down = float(0.0)
        for key, value in self.anew_valences.items():
            freq = self.input_words.count(key)
            up += value * freq
            down += freq
        try:
           self._text_valence = up / down
        except ZeroDivisionError:
            # default neutral psychological valence of 4.5 in a scale of 1-9
            pass

    @property
    def text_valence(self):
        self._handle()
        return self._text_valence

if __name__=="__main__":
    stories = ["aladdin_and_the_wonder_lamp",
               "beauty_and_the_beast",
               "cinderlla",
               "hansel_and_gretel",
               "history_of_jack_and_giant_killer",
               "rapunzel",
               "red_riding_hood",
               "sleeping_beauty",
               "snow_white",
               "the_frog_prince",
               "tom_thumb"]
    for story in stories:
        v = ValenceAssigner("stories/%s" % story)
        print v.text_valence
