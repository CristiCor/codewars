


My solution:

def cakes(recipe, available):
    # TODO: insert code
    nr_cakes = []
    
    for item in recipe.keys():
        #print(item)
        if item not in available.keys():
            return 0
        nr_cakes.append(available[item]/recipe[item])
    
    #print(nr_cakes)
    return int(min(nr_cakes))

Best practice solution:

def cakes(recipe, available):
  return min(available.get(k, 0)/recipe[k] for k in recipe)

super clever :)))