"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import csv

from jellyfish import levenshtein_distance, jaro_distance
from stemming.porter2 import stem

from Parser import Parser
from stopwords import stopwords

class AnewWords:
    def __init__(self, file_input):
        self._words = []
        self.file_input = file_input

    def handle(self):
        with open(self.file_input,'rb') as fin:
            dr = csv.DictReader(fin)
            self._words = [i['Description'] for i in dr]

    @property
    def words(self):
        self.handle()
        return self._words

class ValenceTextHandler:
    """
    ValenceTextHandler class is a helper class for ValenceAssigner.
    It further processes input text by:
        * eliminating blacklist words
        * eliminating articles, useless words, noise-producer words

        * [input] - list containing words (initial text stripped of punctuation)
        * [output] - list containing valuable words
    """

    def __init__(self, file_input):
        self.parser = Parser(file_input)
        # get initial parser list of words
        self.input_words = self.parser.words
        self._words = []

        # get ANEW words
        self.anew = AnewWords("scripts/male.csv")
        self.anew_words = self.anew.words

    def handle(self):
        # remove stopwords
        self._words = filter(lambda k: k not in stopwords, self.input_words)
        # lower each word
        self._words = [word.lower() for word in self._words]
        # stem words if not in ANEW database
        self._words = [stem(word) if word not in self.anew_words
                                  else word for word in self._words]

        # Jaro-winkler and Levensteinh distance empiracally proved to be a bad
        # idea
        """
        tmp = []
        for word in self._words:
            for anew_word in self.anew_words:
                ld = levenshtein_distance(word, anew_word)
                jd = jaro_distance(word, anew_word)
                if ld <= 1 and jd >= 0.90:
                    pass
        """

    @property
    def words(self):
        self.handle()
        return self._words

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
