def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    report_count(text)

def report_count(text) : 
    sorted_chars = sorted(count_chars(text).items(),key=lambda d: d[1],reverse=True)
    print("--------Begin Report--------")
    print(f"Word count: {count_words(text)}")
    for key,value in sorted_chars:
        if not key.isalpha():
            continue
        print(f"The '{key}' character was found {value} times")
    print("--------End Report--------")
    

def count_chars(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

main()