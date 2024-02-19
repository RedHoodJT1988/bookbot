def word_count(book):
    words = book.split()
    return len(words)

def count_letters(book):
    cleaned_text = ''.join(char.lower() for char in book if char.isalpha())
    letter_count = {}
    for char in cleaned_text:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count

def print_report(words_count, letters_count):
    print(f"--- Begin report of books/frankenstein.txt ---")
    print(f"{words_count} words found in the document\n")
    sorted_letters = sorted(letters_count.items(), key=lambda x: x[1], reverse=True)
    for char, count in sorted_letters:
        print(f"The '{char}' character was found {count} times")
        print(f"--- End report ---")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        total_words = word_count(file_contents)
        letters_count = count_letters(file_contents)
        print_report(total_words, letters_count)
        print(f"Number of words in the book: {total_words}")
        print("letter count:")
        print(letters_count)
        

main()