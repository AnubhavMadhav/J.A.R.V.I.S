import wikipedia

while True:
    input = input("Question: ")
    print(wikipedia.summary(input))