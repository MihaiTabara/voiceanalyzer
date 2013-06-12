"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import string

class Parser:
    """
    Parser class is used to process text from ASCII files to get word list
        * [input] - file of ASCII text
        * [output] - list containing words (initial text stripped of punctuation)
    """

    def __init__(self, file_input):
        self.file_input = file_input
        self._words = []

    def parse_line(self, string_line):
        exclude = set(string.punctuation)

        line = string_line.rstrip()
        parsed_line = ''.join(ch for ch in line if ch not in exclude)

        return parsed_line.split()

    def parse_file(self):
        with open(self.file_input, "r") as f:
            raw_content = f.readlines()
            for line in raw_content:
                line_words = self.parse_line(line)
                if line_words:
                    self._words.extend(line_words)

    @property
    def words(self):
        self.parse_file()
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
        p = Parser("stories/%s" % story)
        print p.words.__len__()

