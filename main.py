def main():
    text_frombook = get_book_text("books/frankenstein.txt")

    from stats import wordcounter
    num_words= wordcounter(text_frombook)
    print ("Found",num_words,"total words")

    from stats import characters
    karakterszamok=characters("books/frankenstein.txt")
    from stats import Filter
    Filter(karakterszamok)
    #print(karakterszamok)
    






def get_book_text(a):
    with open(a) as f:
        return f.read()
    

main()
