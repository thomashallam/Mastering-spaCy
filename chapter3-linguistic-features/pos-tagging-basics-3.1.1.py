#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")

doc = nlp("Alicia and me went to the school by bus")
for token in doc:
    print(token.text, otken.pos_, token.tag), spacy.explain(token.pos_), spacy.explain(token.tag_))

