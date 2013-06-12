"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
from Parser import Parser
from stopwords import stopwords

class ValenceTextHandler:
    """
    """

    def __init__(self, file_input):
        self.parser = Parser(file_input)
        # get initial parser list of words
        self.input_words = self.parser.words

    def get_statistics(self):
        words = self.input_words
        print 'The text you submitted was %s words in length.' % len(words)

        bigwords = len([word for word in words if len(word) > 6])
        print 'Big words (> 6 letters) in your file: %s' % bigwords

        articles = ['a', 'an', 'the']
        articles_count = sum([words.count(x) for x in articles])
        print 'Articles (a, an, the) in your file: %s' % articles_count

        self_references = ['I', 'me', 'my']
        ref_count = sum([words.count(x) for x in self_references])
        print 'Self-references (I, me, my) in your file: %s' % ref_count

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
        v.get_statistics()
        print
