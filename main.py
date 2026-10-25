
import requests
import random

pokemon = {
    "bulbasaur": "https://pokeapi.co/api/v2/pokemon/bulbasaur",
    "ivysaur": "https://pokeapi.co/api/v2/pokemon/ivysaur",
    "venusaur": "https://pokeapi.co/api/v2/pokemon/venusaur",
    "charmander": "https://pokeapi.co/api/v2/pokemon/charmander",
    "charmeleon": "https://pokeapi.co/api/v2/pokemon/charmeleon"
}

# five pokemons to choose
print("CHOICES: ")
print("bulbasaur")
print("ivysaur")
print("venusaur")
print("charmander")
print("charmeleon")
print("")

#random choice to random the five pokemons from dictionary, and keys to convert the names into list name
answer = random.choice(list(pokemon.keys())) 

#try for errors to try to execute the API
try:
    response = requests.get(pokemon[answer])

    if response.status_code == 200:
        data = response.json()

        print("guess the pokemon")
        print("Height:", data["height"])
        print("Weight:", data["weight"])
        print("Abilities:")

        for ability in data["abilities"]:
            print("-", ability["ability"]["name"]) #ability is from the API and name from API 

        guess = input("Guess the Pokemon: ")


        if guess == answer:
            print("Correct! You win!")
        else:
            guess = input("Wrong! Try again: ")

        if guess == answer:
            print("Correct! You win!")
        else:
            guess = input("Last attempt: ")

        if guess == answer:
            print("Correct! You win!")
        else:
            print("The Pokemon was", answer)

    else:
        print("Failed to get Pokemon data.")

except requests.exceptions.RequestException:
    print("Network error! Check your internet connection.")
