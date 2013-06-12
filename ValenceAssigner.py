"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import csv

from Parser import Parser
from stopwords import stopwords

class ValenceTextHandler:
    """
    ValenceTextHandler class is used to further process input text such as:
        * eliminate blacklist words
        * eliminate articles, useless words, noise-producer words

        * [input] - list containing words (initial text stripped of punctuation)
        * [output] - list containing valuable words
    """

    def __init__(self, file_input):
        self.parser = Parser(file_input)
        # get initial parser list of words
        self.input_words = self.parser.words
        self._words = []

    def handle(self):
        self._words = filter(lambda k: k not in stopwords, self.input_words)

    @property
    def words(self):
        self.handle()
        return self._words

class ValenceAssigner:
    pass

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
        v = ValenceTextHandler("stories/%s" % story)
        print len(v.words)
