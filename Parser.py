"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013

Parser class:
    [input] - file of ASCII text
    [output] - list containing words (initial text stripped of punctuation)
"""
import string

class Parser:
    def __init__(self, file_input):
        self.file_input = file_input
        self.words = []

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
                    self.words.extend(line_words)

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
        p.parse_file()
        print p.words.__len__()

