import time

character_dict = {}

if __name__ == "__main__":
    start_time = time.time()
    with open("/var/tmp/random.txt", "r") as file:
        for line in file:
            for char in line:
                if char in character_dict:
                    character_dict[char] += 1
                else:
                    character_dict[char] = 1

    print(character_dict)
    print("--- %s seconds ---" % (time.time() - start_time))
