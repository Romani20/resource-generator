import spacy
from spacy_wordnet.wordnet_annotator import WordnetAnnotator
from wonderwords import RandomWord
import csv

#spacy.cli.download("en_core_web_md")
nlp = spacy.load("en_core_web_md")

with open("edited_synonyms.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    total_sim, avg = 0, 0
    for row in csv_reader:
        w1, w2 = row[0], row[1]
        print(w1, w2)

        w1 = nlp.vocab[w1]
        w2 = nlp.vocab[w2]
        total_sim += w2.similarity(w1)
        avg = round(total_sim/399, 3)
    print(avg)

with open("edited_antonyms.csv", 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)

    total_sim, avg = 0, 0
    for row in csv_reader:

        w1, w2 = row[0], row[1]
        print(w1, w2)

        w1 = nlp.vocab[w1]
        w2 = nlp.vocab[w2]
        total_sim += w2.similarity(w1)
        avg = round(total_sim/399, 3)
    print(avg)
