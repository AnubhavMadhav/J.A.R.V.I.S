import wolframalpha

input = input("Question :")
app_id = "HH23Y3-5645968TGY"
client = wolframalpha.Client(app_id)

res = client.query(input)
answer = next(res.results).text
print(answer)
