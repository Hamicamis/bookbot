def wordcounter(a):
    count = len(a.split())
    return count

def characters(a):
    letter_counts={}
    with open(a) as f:
        d=f.read()
        j=d.lower()
        b=[ch for ch in j]
        for letter in b:
            letter_counts[letter] = letter_counts.get(letter,0) + 1
            letter_counts[letter]

    return letter_counts

def man(items):
    return items["num"]

def Filter(a):
    keys = list(a.keys())
    values = a.values()
    
    b=[]
    c={}
    n=0
    for i in values:
        l=keys[n]
        if l.isalpha()==True:
            c["char"]=l+":"
            c["num"]=i
            b.append(c)
            c={}
        n+=1
    b.sort(reverse=True, key=man)
    for k in b:
        print (*k.values())
        