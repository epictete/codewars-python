def cakes(recipe, available):
    mins = []
    for key, value in recipe.items():
        x = available.get(key, 0)
        qty = x//value
        mins.append(qty)
    return min(mins)


# recipe = {"flour": 500, "sugar": 200, "eggs": 1}
# available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))