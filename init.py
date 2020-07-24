from file_data import FileData
import string
import linecache

import os

from const_value import K

#=========Auxliliary Functions=========#

def get_files_name_list():

    path = "‏‏python-data"

    files_name_list = []

    for root, dirs, files in os.walk(path):
        for file in files:
            files_name_list.append(os.path.join(root, file))
    return files_name_list

def update_subsentences_dict(match_sentences, index, sentence):
        if not match_sentences:
            match_sentences.append(index)
            return

        for i,ind in enumerate(match_sentences):
            tmp_senrence = " ".join(linecache.getline(file_data_dict[ind].name, file_data_dict[ind].line).split("\n")).strip()

            if sentence.lower().strip() < (tmp_senrence.lower()):
                match_sentences.insert(i, index)

                if len(match_sentences) > K:
                    match_sentences.pop()
                return

        if len(match_sentences) < K:
            match_sentences.append(index)
            return




def clear_str(str):
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    return str.lower()

def get_subqueries(sentence):
    return set([sentence[i: j] for i in range(len(sentence)) for j in range(i + 1, len(sentence) + 1)])

#======================================#

def init_dict():
    print("Loading the files and prepering the system...")
    files_name_list = get_files_name_list()
    file_data_dict_index = 0
    for file in files_name_list:
        with open(file, encoding='utf-8') as my_file:
            sentences = my_file.read().split("\n")
        line_number = 1
        for sentence in sentences:

            file_data_dict[file_data_dict_index] = (FileData(file, line_number))
            sentence = clear_str(sentence)
            subsentences = get_subqueries(sentence)
            for subsentence in subsentences:
                subsentences_dict[subsentence] = [] if subsentence not in subsentences_dict.keys() else subsentences_dict[subsentence]
                update_subsentences_dict(subsentences_dict[subsentence], file_data_dict_index , sentence)
            line_number += 1
            file_data_dict_index += 1
    print("The system is ready.")



subsentences_dict = {}
file_data_dict = {}
