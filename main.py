import pyperclip
import os


def color(word: str) -> str:
    color1 = "&f&l"
    alternate_color = ["&a&l","&2&l"]
    new_word = ""
    j: bool = False

    for i, char in enumerate(word):
        if i % 2 == 0:
            new_word += alternate_color[j] + char
            j = not j
        else:
            new_word += color1 + char

    return new_word
`

def main() -> int:
    word = str((input("What is the Phrase? ")))

    os.system("cls")

    new_word = color(word)
    word_length = len(word)
    new_format_length = len(new_word)

    pyperclip.copy(new_word)

    print(f"Phrase is '{word}'")
    print(f"Character length: {word_length}")
    print(f"Length with formatting: {new_format_length}\n")
    print(f"Formatted Phrase '{new_word}', has been copied to clipboard ")

    return 0


if __name__ == "__main__":
    main()
