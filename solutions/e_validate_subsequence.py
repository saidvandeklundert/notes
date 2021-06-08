array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

def isValidSubsequence(array, sequence):
    alt_sequence = []
    for i in array:
        if len(alt_sequence) == len(sequence):
            break
        if i in sequence:
            alt_sequence.append(i)

    result = alt_sequence == sequence

    return result





if __name__ == "__main__":
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array, sequence))
    array = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [6, 1, -1, 10]
    print(isValidSubsequence(array, sequence))    
    array = [ 1,1,1,1,1]
    sequence = [1,1,1]
    print(isValidSubsequence(array, sequence))     