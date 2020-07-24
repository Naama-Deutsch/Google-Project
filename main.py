
from init import init_dict
import string
from get_completions import get_best_k_completions
from user_api import get_input
from user_api import print_data
from const_value import STOP_INPUT

def clear_str(str):
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    str = " ".join(str.lower().split())
    return str


def run():
    while True:
        user_input = ""
        new_input = get_input("Enter your text: ")
        while new_input != STOP_INPUT:
            user_input = clear_str(user_input + new_input)

            res = get_best_k_completions(user_input) #TODO get...

            print_data(res,user_input)

            new_input = get_input(user_input)





def main():
    init_dict()
    run()



if __name__ == "__main__":
    main()

