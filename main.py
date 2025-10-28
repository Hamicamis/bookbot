def main():
    import sys
    if len(sys.argv)==1:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
            
    text_frombook = get_book_text(sys.argv[1])  

    from stats import wordcounter
    num_words= wordcounter(text_frombook)
    print ("Found",num_words,"total words")

    from stats import characters
    karakterszamok=characters(sys.argv[1])
    from stats import Filter
    Filter(karakterszamok)





def get_book_text(a):
    with open(a) as f:
        return f.read()
    

main()
