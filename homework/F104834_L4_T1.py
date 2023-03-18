text = input()
h = {}

# for letter in text:
#     if letter in h:
#         h[letter] += 1
#     else:
#         h[letter] = 1

for letter in text:
    h[letter] = h.get(letter, 0) + 1
print(h)