
def count_letters(s: str):
    letters = {}
    for char in s:
        if char.lower() not in letters :
            letters[char.lower()] = 0
        letters[char.lower()] += 1
    return letters


def main():

    file: str = "books/frankenstein.txt"

    with open(file) as f:
        file_content = f.read()
    #print(len(file_content.split()))
    print(count_letters(file_content))

main()
