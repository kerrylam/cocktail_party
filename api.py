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


def drink_by_id(cocktail_id):
    # url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php'
    # response = requests.get(url, params= {'i': cocktail_id})
    # data = response.json()
    # result = data['drinks']
    
    # for cocktail in result:
    #     name = cocktail['strDrink']
    #     instructions = cocktail['strInstructions']
    #     url = cocktail['strDrinkThumb']
    #     ingredients_list = []
    #     measurements_list = []
    #     ingredient_pics = []
    #     img_url = "https://www.thecocktaildb.com/images/ingredients/"
    #     x = 1
    #     while (True):
    #         strIngredient = "strIngredient" + str(x)
    #         strMeasure = "strMeasure" + str(x)
    #         ingredient = cocktail[strIngredient]
    #         measurement = cocktail[strMeasure]
    #         if (ingredient is None):
    #             break
    #         else:
    #             ingredients_list.append(ingredient)
    #             measurements_list.append(measurement)
    #             ingredient_pics.append(img_url + ingredient + "-small.png")
    #         x += 1


    url = 'https://www.thecocktaildb.com/api/json/v1/1/lookup.php'
    response = requests.get(url, params= {'i': cocktail_id})
    data = response.json()
    result = data['drinks']
    
    for cocktail in result:
        name = cocktail['strDrink']
        instructions = cocktail['strInstructions']
        url = cocktail['strDrinkThumb']
        ingredients = {}
        img_url = "https://www.thecocktaildb.com/images/ingredients/"
        x = 1
        while (True):
            strIngredient = "strIngredient" + str(x)
            strMeasure = "strMeasure" + str(x)
            ingredient = cocktail[strIngredient]
            measurement = cocktail[strMeasure]
            if (ingredient is None):
                break
            else:
                ingredients['ingredient'] = ingredient
                ingredients['ingredient']['measurement'] = measurement
                ingredients['ingredient']['img_url'] = img_url + ingredient + "-small.png"
            x += 1
    return ingredients

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
