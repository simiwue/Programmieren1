def word_wrap(poem, max_length):
    word_list = poem.split(" ")
    new_line = ""
    new_poem = ""

    for word in word_list:
        if len(new_line) <= max_length:
            new_line += (word + " ")
        
        else:
            new_poem += new_line + "\n"
            new_line = word + " "

    return(new_poem)




s = "Der Sehnsucht entgegen, sie erleben. "
s = s + "Wer kann das schon. Den Traeumen entgegen, "
s = s + "sie erleben. Wer macht das schon. Den Gefuehlen"
s = s + " entgegen, sie erleben. Wer wagt das schon. "
s = s + "Der Liebe entgegen, sie erleben. Wer darf das schon."
# print(s)



print (word_wrap(s,30))
