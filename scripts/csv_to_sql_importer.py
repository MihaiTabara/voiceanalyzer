"""
Mihai Tabara @ 2013
Emilia Ciobanu @ 2013
"""
import csv, sqlite3

tables = ['male', 'female', 'egged']

for t in tables:
    con = sqlite3.connect("%s.sl3" % t)
    cur = con.cursor()
    cur.execute("CREATE TABLE %s (id INTEGER PRIMARY KEY, "
                                    "description TEXT, "
                                    "word_no INTEGER, "
                                    "valence TEXT, "
                                    "valence_sd TEXT, "
                                    "arousal TEXT, "
                                    "arousal_sd TEXT, "
                                    "dominance TEXT, "
                                    "dominance_sd TEXT, "
                                    "word_fr INTEGER);" % t)

    with open('%s.csv' % t,'rb') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Description'], i['Word No.'],
                  i['Valence Mean'], i['Valence SD'],
                  i['Arousal Mean'], i['Arousal SD'],
                  i['Dominance Mean'], i['Dominance SD'],
                  i['Word Frequency']) for i in dr]

    cur.executemany("INSERT INTO %s (description, word_no, valence,"
                                    "valence_sd, arousal, arousal_sd,"
                                    "dominance, dominance_sd, word_fr"
                                    ") VALUES (?,?,?,?,?,?,?,?,?);" % t, to_db)
    con.commit()
