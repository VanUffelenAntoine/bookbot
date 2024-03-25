def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(f"Word count: {word_count}")

def generate_dic_letters(text):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    chars_dic = {}
    for char in chars:
        chars_dic[char] = 0
    print(chars_dic)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

main()