import pyo3_examples


if __name__ == "__main__":
    x = pyo3_examples.sum_as_string(5, 20)
    print(x)
    x = pyo3_examples.multiply(5, 20)
    print(x)
    print(pyo3_examples.list_sum([10, 10, 10, 10, 10, 5]))
