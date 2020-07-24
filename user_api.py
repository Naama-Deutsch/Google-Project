def get_input(msg):
    return input(msg)

def print_data(res,input):
    print(f"Here are {len(res)} suggestions:") if len(res) > 0 else print(
        "no ssuggestions")
    for i in range(len(res)):
        print(f"{i + 1}.", end = " ")
        res[i].print_(input)
