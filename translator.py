def translator(phrase):
    translation=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation+="g"
        else :
            translation+=letter

    return translation

print(translator(input("enter a phrase:")))