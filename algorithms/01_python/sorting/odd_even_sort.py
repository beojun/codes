"""Odd-even (brick) sort."""
def odd_even_sort(values: list[int]) -> list[int]:
    result = values[:]
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for start in (1, 0):
            for i in range(start, len(result) - 1, 2):
                if result[i] > result[i + 1]:
                    result[i], result[i + 1] = result[i + 1], result[i]
                    sorted_flag = False
    return result


if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    assert odd_even_sort(data) == sorted(data)
    print("odd-even sort ok")
