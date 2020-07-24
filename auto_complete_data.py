from color import *
import sys

class AutoCompleteData:
    def __init__(self,completed_sentence,source_text,offset,score):
        self.completed_sentence = completed_sentence.strip()
        self.source_text = source_text
        self.offset = offset
        self.score = score

    def print_(self, text):
        first_index = (self.completed_sentence.lower()).find(text)
        end_index = first_index + len(text)
        if (first_index == -1):
            print(self.completed_sentence + " ( the source from " + str(self.source_text) + " in line " + str(
                self.offset) + " score : " + str(self.score) + " )")
        else:
            print(self.completed_sentence[:first_index], end=" ")
            sys.stdout.write(BLUE)
            print(text, end="")
            sys.stdout.write(RESET)
            print(self.completed_sentence[end_index:] + " ( the source from " + str(self.source_text) + " in line " + str(
                self.offset) + " score : " + str(self.score) + " )")




