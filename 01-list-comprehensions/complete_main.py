def power_shelf_potency(potion_potencies):
    new_potency = [ 
        potency * 5 for potency in potion_potencies 
        if potency <= 100
    ]

    return new_potency
