quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
          "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

# show random quote
user_answer = "B"

if user_answer is "B":
    # leave the program
    pass
elif user_answer == "C":
    print("c'est la bonne réponse ! Et G pas d'humour, je C...")
else:
    pass


# Show another quote

def get_random_quote(my_list):
    # get a random number
    quote = my_list[0]
    print(quote)

    return "the program is over"


print(get_random_quote(quotes))
