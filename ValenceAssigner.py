"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import csv
from StringIO import StringIO

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

        # default neutral psychological valence of 4.5 in a scale of 1-9
        self._text_valence = float(4.5)

        # list with words to be added to anew from this
        self._unrated = []

    def _handle_valences(self):
        up = float(0.0)
        down = float(0.0)
        for key, value in self.anew_valences.items():
            freq = self.input_words.count(key)
            up += value * freq
            down += freq

        try:
           self._text_valence = up / down
        except ZeroDivisionError:
            # leave to default value
            pass

    def _handle_unrated(self):
        self._unrated = filter(lambda k: k not in self.anew_valences.keys(),
                               self.input_words)
        self._unrated = list(set(self._unrated))

    @property
    def text_valence(self):
        self._handle_valences()
        return self._text_valence

    @property
    def unrated(self):
        self._handle_unrated()
        return self._unrated

def generate_csv(header, rows):
    output = StringIO()
    csv_writer = csv.writer(output)
    csv_writer.writerow(header)
    for item in rows:
        csv_writer.writerow([value.encode('utf-8') for value in item])

    return output.getvalue()

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
    # gather all unrated words from all texts
    all_unrated = []

    for story in stories:
        v = ValenceAssigner("stories/%s" % story)
        #print v.text_valence
        all_unrated.extend(v.unrated)

    all_unrated = list(set(all_unrated))
    columns = []
    for word in all_unrated:
        columns.append([word, '4.5', '4.5', '4.5', '1'])

    header = ['Description', 'Valence Mean', 'Arousal Mean',
              'Dominance Mean', 'People Counter']
    answer = generate_csv(header, columns)
    with open("unrated.csv", "w") as fo:
        fo.write(answer)

