# Enumerate

It is very common for a programmer to create an incrementing count when looping over a list.

```py
items = ["Bread", "Potion"]
i = 0
for item in items:
    print(f"{i}: {item}")
    i += 1
```

Normally, when you loop through a list, Python only gives you the items. If you wrap your list in `enumerate()`, Python provides you two things at every step: the count and the item itself.

```py
for i, item in enumerate(items):
    print(f"{i}: {item}")

# 0: Bread
# 1: Potion
```

Let's see an example of `enumerate()` used within a list comprehension.

```py
count_items = [f"{i}: {item}" for i, item in enumerate(items)]
print(count_items)

# ['0: Bread', '1: Potion']
```

## Where to Start Counting?

By default, `enumerate()` starts counting at `0`.  We can optionally pass a start argument to tell `enumerate()` where to begin:

```py
for i, item in enumerate(items, start=1):
    print(f"{i}: {item}")

# 1: Bread
# 2: Potion
```

## Assignment

Fantasy Quest needs an inventory menu so players can see what they are carrying and pick an item by number. Each line should show a 1-based index followed by the item name, like `(1) Bread`.

Complete the `create_inventory_menu` function. It takes a list of item names and returns a new list of formatted menu strings. Numbering starts at 1, not 0. Use `enumerate()` with a list comprehension.

For example, given `["Bread", "Potion"]`, the function should return `["(1) Bread", "(2) Potion"]`.
