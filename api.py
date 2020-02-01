from flask import request
import requests

class Ingredient:
  def __init__(self, name, measurement):
    self.name = name
    self.measurement = measurement
  def __str__(self):
    if (self.measurement is None):
        return self.name
    return self.name + ", " + self.measurement
    

def drink_by_letter():
    url = 'https://www.thecocktaildb.com/api/json/v1/1/search.php?f=a'
    response = requests.get(url)
    data = response.json()
    cocktails = data['drinks']

    for cocktail in cocktails:
        name = cocktail['strDrink']
        url = cocktail['strDrinkThumb']
        instructions = cocktail['strInstructions']
        # print(f'{name}, url:{url}, instructions:{instructions}')
        ingredients = []
        x = 1
        while (True):
            strIngredient = "strIngredient" + str(x)
            strMeasure = "strMeasure" + str(x)
            ingredient = cocktail[strIngredient]
            measurement = cocktail[strMeasure]
            if (ingredient is None):
                break
            else:
                ingredients.append(Ingredient(ingredient, measurement))
            x += 1
        print(f'{name}, instructions:{instructions}')
        print('ingredients:'' '.join(map(str, ingredients)))
        print("\n")
