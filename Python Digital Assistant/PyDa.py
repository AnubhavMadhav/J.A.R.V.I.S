import wikipedia
import wolframalpha

while  True:
    input = input("Question:")

    try:
        app_id = "HH23Y3-5645968TGY"
        client = wolframalpha.Client(app_id)
        res = client.query(input)
        answer = next(res.results).text
        print(answer)
    except:
        # wikipedia.set_lang("es")
        print(wikipedia.summary(input, sentences=2))
        