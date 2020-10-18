import nltk
import pandas as pd
import matplotlib.pyplot as plt

"""
Helper functions for data mining lab session 2018 Fall Semester
Author: Elvis Saravia
Email: ellfae@gmail.com
"""

def format_rows(docs):
    """ format the text field and strip special characters """
    D = []
    for d in docs.data:
        temp_d = " ".join(d.split("\n")).strip('\n\t')
        D.append([temp_d])
    return D

def format_labels(target, docs):
    """ format the labels """
    return docs.target_names[target]

def check_missing_values(row):
    """ functions that check and verifies if there are missing values in dataframe """
    counter = 0
    for element in row:
        if element == True:
            counter+=1
    return ("The amoung of missing records is: ", counter)

def tokenize_text(text, remove_stopwords=False):
    """
    Tokenize text using the nltk library
    """
    tokens = []
    for d in nltk.sent_tokenize(text, language='english'):
        for word in nltk.word_tokenize(d, language='english'):
            # filters here
            tokens.append(word)
    return tokens

def plot_term_matrix(matrix, precision):
    plt.subplots(figsize=(20, 25))
    plt.spy(matrix, precision=precision, markersize=1)

def convert_file_to_dataframe(file):
    with open(file, 'r', encoding='utf8') as reader:
        lines = reader.readlines()
        sentence = list()
        label = list()
        for l in lines:
            split = l.split('\t')
            sentence.append(split[0])
            label.append(split[1].rstrip())
        df = pd.DataFrame({'sentence': sentence, 'label': label})

    return df