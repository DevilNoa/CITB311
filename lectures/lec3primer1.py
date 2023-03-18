price_with = 10
item_with = 30
header = "%-*s%s"
item = "%-*s%.2f"
print("=" * 40)
print(header % (item_with + len(str(price_with)), "артикул", "цена"))
print("-" * 40)
print(item % (item_with, "coffee", 1.5))
print(item % (item_with, "muffin", 1.5))
print(item % (item_with, "ice coffee", 1.5))
print(item % (item_with, "fresh coffee", 1.5))
print("=" * 40)
