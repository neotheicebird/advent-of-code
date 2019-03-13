# we need a functions that can read the input

def parse_input(input_file):
    with open(input_file, 'rt') as fp:
        for change in fp.readlines():
            yield int(change)

if __name__ == "__main__":
    inp = "input.txt"
    current_frequency = 0
    for change in parse_input(inp):
        current_frequency += change

    print("Solution #1a")
    print(current_frequency)

    current_frequency = 0
    out = set()
    out.add(current_frequency)
    
    found_repetition = False

    while not found_repetition:
    # repeat the file reads many times if required
        for change in parse_input(inp):
            current_frequency += change
            if current_frequency not in out:
                out.add(current_frequency)
            else:
                found_repetition = True
                break

    print("Solution #1b")
    print(current_frequency)