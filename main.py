
def count_letters(s: str):
    letters = {}
    for char in s:
        if char.lower() not in letters :
            letters[char.lower()] = 0
        letters[char.lower()] += 1
    return letters

def print_char_count(chars: dict[str, int]) -> None :
    for k, v in sorted(chars.items(), key=lambda item: item[1], reverse=True) :
        if k.isalpha() :
            print(f"The '{k}' character was found {v} times")

def print_word_count(s: str) -> None :
    print(f"{len(s.split())} words found in the document")

def print_full_report(s: str, file: str) -> None:
    print(f"--- Begin report of {file} ---")
    print_word_count(s)
    print("")
    print_char_count(count_letters(s))
    print("--- End report ---")


def main():

    file: str = "books/frankenstein.txt"

    with open(file) as f:
        file_content = f.read()

    print_full_report(file_content, file)

main()
