import wikipedia

while True:
    input = input("Question: ")
   # wikipedia.set_lang("es")
    print(wikipedia.summary(input, sentences=2))

    