sentence = "Wir fahren auf dem Riesenrad mit dem Auto!"

def speek_chinese(text):
    text = text.replace("r", "l")
    text = text.replace("R", "L")

    return text

def remove_vocals(text):
    vocals = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
    new_text = ""
    for letter in text:
        if letter not in vocals:   
            new_text += letter
    
    return new_text



print(speek_chinese(sentence))
print(remove_vocals(sentence))

