quotes = ["Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !",
          "On doit pouvoir choisir entre s'écouter parler et se faire entendre."]

characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]

# show random quote
user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme.")


# Show another quote

def get_random_quote(my_list):
    # get a random number
    quote = my_list[0]
    print(quote)

    return "the program is over"


while user_answer != "B":
    print(get_random_quote(quotes))
    user_answer = input("Tapez entree pour connaitre une autre citation ou B pour quitter le programme.")


for character in characters:
    a_character = character.capitalize()
    print(a_character)

print(get_random_quote(quotes))
