# HW_Assignment2 (Spell Correction using LM)
This project is the submission for the HW Assignment 2 of the course COMP 8730 - Natural Language Processing and Understanding.

The system is divided into multiple files and some files need to be run before executing the main file to get the required data. 
It is highly suggested that you run the program on google colab platform, otherwise you may face issue of package installation. 
In case of any such problem, install the package explicitly using 'pip'. 
*E.g. 'pip install nltk'*

The file structure is given below. 
- main.ipynb: Main Python notebook
- brown_corpus_to_file.py: Takes the raw brown corpus as an input and returns a single text file 'text_str.txt' containing string statements
- model_creation.py: Using the file 'text_str.txt' it trains an n-gram language model
- modeloutput.py: Returns the minimum distance of a word from all the words provided in the specified list.
- successatk.py: Returns a boolean value if the correct word is found or not in the first k items

While executing, make sure that you have 'text_str.txt' file ready with the use of brown_corpus_to_file.py and all your models ready. 
The model file names should follow the naming convention for system to detect it. 
Due to the time limit, we could not implement multiprocessing or multithreading to the system so the system takes a large amount of time to generate the result.

The data used for the implementation includes...
- n-gram langauge modeling : https://www.kaggle.com/code/alvations/n-gram-language-model-with-nltk/notebook
- birkbeck corpus : https://ota.bodleian.ox.ac.uk/repository/xmlui/handle/20.500.12024/0643
- brown corpus via nltk : http://www.nltk.org/nltk_data/

