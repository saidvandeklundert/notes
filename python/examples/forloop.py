def for_loop(n: int):
    for i in range(n):
        print(i)
        if i > 5:
            break
    else:
        print("Ran the else statement")


# hitting the else statement
for_loop(4)

# not hitting the else statement
for_loop(10)
