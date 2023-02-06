# -*- coding: utf-8 -*-
"""brown_corpus_to_file.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/194f7684iSN8X_WA7-S6FUadKDsCLP0aL
"""

import nltk
nltk.download("brown")

from nltk.corpus import brown
len(brown.words())

text = brown.sents()
text

double_list = text
print(double_list)
text_str = ""
for para in double_list:
  for word in para:
    text_str = text_str + " " + str(word)
  text_str += "\n"

text_str

f = open("text_str.txt", "w")
f.write(text_str)
f.close()