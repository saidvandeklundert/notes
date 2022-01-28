list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

for nr_1, nr_2 in zip(list_1, list_2):
    print(f"{nr_1} - {nr_2}")

x = zip(list_1, list_2)
print(type(x))
