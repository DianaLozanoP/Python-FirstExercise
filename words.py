def print_upper_words (words):
    ''' Takes words, returns them in Uppercase'''
    for x in words:
        print (x.upper())

def print_upper_wordse (words):
    '''Print each word uppercase, if it starts with e or E'''
    for x in words:
        if x.startswith("e") or x.startswith("E"):
            print(x.upper())

def print_upper_wordsm (words, must_start_with):
    '''Print each word, uppercase, if the word starts with the letters indicated'''
    for x in words:
        for y in must_start_with:
            if x.startswith(y):
                print (x.upper())

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"])
print_upper_wordsm(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})