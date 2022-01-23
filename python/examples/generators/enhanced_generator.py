def took_a_hit():
    print("ready to take a hit!")
    while True:
        n = yield
        print(f"I took a hit! Oucht because of {n}")


receiver = took_a_hit()

print(receiver.send(None))
print(receiver.send("bullet"))
print(receiver.send("spear"))
print(receiver.send("prayers"))
receiver.close()  # generator is garbage collected.
