
def main():

    file: str = "books/frankenstein.txt"

    with open(file) as f:
        file_content = f.read()
    print(file_content)

main()
