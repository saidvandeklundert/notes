from io import StringIO
STRING_1 = str([ x for x in range(10000)])
STRING_2 = str([ x for x in range(10000)])
LIST_OF_STRINGS = [STRING_1, STRING_2]
def test_1():
    """Using +="""
    ret = ""

    for string in LIST_OF_STRINGS:
        ret += string
    return ret

def test_2():
    return "".join(LIST_OF_STRINGS)


def test_3():
    buffer = StringIO()

    for string in LIST_OF_STRINGS:
        buffer.write(string)
  
    return buffer.getvalue()

def test_4():

    return f"{LIST_OF_STRINGS[0]}{LIST_OF_STRINGS[1]}" 

if __name__ == '__main__':
    import timeit
    print(timeit.timeit(
        "test_1()",
        setup="from __main__ import test_1")
        )
    print(timeit.timeit(
        "test_2()",
        setup="from __main__ import test_2")
        )
    print(timeit.timeit(
        "test_3()",
        setup="from __main__ import test_3")
        )        
    print(timeit.timeit(
        "test_4()",
        setup="from __main__ import test_4")
        )                
          

    