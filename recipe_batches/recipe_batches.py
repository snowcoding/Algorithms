#!/usr/bin/python

import math

#Iterative Solution
def recipe_batches(rec, ing):

    #Initialize a list that will hold the batches for each ingredient
    batches = []

    #For loop through the reciple items
    for item,val in rec.items():

        #If the item isn't in ing or we don't have enough return 0
        if not item in ing or ing[item] < val:
            return 0

        #Otherwise, divide the proportions and append to the list
        else:
            batches.append(ing[item]/val)
    
    #return the min floor of all values > 1
    return min( [math.floor(b) for b in batches if b >= 1] )

if __name__ == '__main__':
    # Change the entries of these dictionaries to test 
    # your implementation with different inputs
    recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
    ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))