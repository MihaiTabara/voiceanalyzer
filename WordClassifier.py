"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import sys
import csv
import random

from ValenceAssigner import generate_csv

class WordClassifer:
    """
    Class instance to simulate classification as it is in ANEW
    """
    def __init__(self, file_input):
        self.file_input = file_input
        self._words = {}

    def _handle(self):
        with open(self.file_input,'rb') as fin:
            dr = csv.DictReader(fin)

            for i in dr:
                d = {}
                d['Valence Mean'] = float(i['Valence Mean'])
                d['Arousal Mean'] = float(i['Arousal Mean'])
                d['Dominance Mean'] = float(i['Dominance Mean'])
                d['People Counter'] = int(i['People Counter'])
                self._words[i['Description']] = d

    @property
    def words(self):
        self._handle()
        return self._words

    def update(self, words):
        columns = []
        for key, value in words.items():
            columns.append([key,
                            str(value['Valence Mean']),
                            str(value['Arousal Mean']),
                            str(value['Dominance Mean']),
                            str(value['People Counter'])])

        header = ['Description', 'Valence Mean', 'Arousal Mean',
                  'Dominance Mean', 'People Counter']
        answer = generate_csv(header, columns)
        with open("unrated.csv", "w") as fo:
            fo.write(answer)

    def classify(self):
        marks = ['1', '1.5', '2', '2.5', '3', '3.5', '4',
                 '4.5', '5', '5.5', '6', '6.5', '7', '7.5',
                 '8', '8.5', '9']
        words = self.words
        to_rate_word = random.choice(words.keys())

        while(1):
            sys.stdout.write("> With a scale ranging from 1 to 9 "
                             "(0.5 resolution)\n")
            sys.stdout.write("> Please rate the following word \"%s\"\n" % to_rate_word)
            sys.stdout.write("> Where 1 - bad, 9 - good\n")
            line = sys.stdin.readline()
            mark1 = float(line)

            sys.stdout.write("> With a scale ranging from 1 to 9 "
                             "(0.5 resolution)\n")
            sys.stdout.write("> Please rate the following word \"%s\"\n" % to_rate_word)
            sys.stdout.write("> Where 1 - passive, 9 - active\n")
            line = sys.stdin.readline()
            mark2 = float(line)

            sys.stdout.write("> With a scale ranging from 1 to 9 "
                             "(0.5 resolution)\n")
            sys.stdout.write("> Please rate the following word \"%s\"\n" % to_rate_word)
            sys.stdout.write("> Where 1 - weak, 9 - strong\n")
            line = sys.stdin.readline()
            mark3 = float(line)

            if mark1 and mark2 and mark3:
                words[to_rate_word]['People Counter'] += 1
                current_counter = words[to_rate_word]['People Counter']
                words[to_rate_word]['Valence Mean'] += mark1
                words[to_rate_word]['Valence Mean'] /= current_counter
                words[to_rate_word]['Arousal Mean'] += mark2
                words[to_rate_word]['Arousal Mean'] /= current_counter
                words[to_rate_word]['Dominance Mean'] += mark3
                words[to_rate_word]['Dominance Mean'] /= current_counter

                self.update(words)
                sys.stdout.write("> Thank you for your ratings!")
                sys.exit(0)

            if line == "bye\n":
                sys.exit(0)

            if line == '\n':
                continue

if __name__=="__main__":
    w = WordClassifer("unrated.csv")
    w.classify()
