# List Comprehensions

A programmer will frequently want to create a list from another list. Python list comprehensions are a concise way to create lists without having to write looping code. 

For example, let's create a list of numbers and a second list that contains doubled values from the first list. We can use a list comphension for the `doubled` list.

```py
numbers = [ 1, 2, 3, 4 ]
doubled = [ num * 2 for num in numbers ]
print(doubled)
# [2, 4, 6, 8]
```

A list comprehension is easiest read from right to left. In English, the code says:

1. Use all the of the items in the `numbers` list. This similar to the *"for loop"* syntax. (`for num in numbers`)
1. Double each number. (`num * 2`)
1. Create a list. (Wrap everything with square brackets `[ ]`)

The result is a new list containing the doubled numbers assigned to `doubled`.

This could all be done with a *for loop* and an *if* statement. So, why would I use a list comprehension? 

List comprehensions make your code cleaner, and shorter. Instead of writing every step of a for loop you are writing code that is more ["declarative"](https://en.wikipedia.org/wiki/Declarative_programming) (programmer speak for describing the desired outcome, not ever step in the process).

## Adding a Filter

A list comprehension can add an `if` condition to include only items that match the condition. For example, let's only double the numbers if they are greater than 2:

```py
numbers = [1, 2, 3, 4]
filtered_and_doubled = [num * 2 for num in numbers if num > 2]
print(filtered_and_doubled)
# [6, 8]
```

## Assignment

Fantasy Quest has added a new feature: the *potion power shelf*. Moving a potion to the power shelf will increase it's potency by 500%. That's a geat deal! There's a catch. You cannot move potions with potency over 100 points to the power shelf.

Complete the `power_shelf_potency` function. It takes as input a list of potency values, and returns a list of the new increased values. If a potion cannot be moved to the power shelf do not include it in the result.
