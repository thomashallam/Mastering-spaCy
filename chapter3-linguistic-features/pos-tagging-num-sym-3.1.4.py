#!/usr/bin/env python3

import spacy
nlp = spacy.load("en")

doc = nlp("He earned $5.5 million in 2020 and paid %35 tax.")
for token in doc:
    print(token.text, otken.pos_, token.tag), spacy.explain(token.pos_), spacy.explain(token.tag_))

