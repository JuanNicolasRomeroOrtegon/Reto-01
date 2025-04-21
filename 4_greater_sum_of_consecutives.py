
def find_max_consecutive_sum(num_list: list) -> int:
    if len(num_list) < 2:
        raise ValueError("The list must contain at least two elements.")
    
    greater = num_list[0]
    for x in range(len(num_list) - 1):
        if num_list[x] + num_list[x+1] > greater:
            greater = num_list[x] + num_list[x+1]
    return greater

def test():
    assert find_max_consecutive_sum([1, 2, 3, 4, 5]) == 9  # 4 + 5
    assert find_max_consecutive_sum([-10, -20, -3, -4]) == -7  # -3 + -4
    assert find_max_consecutive_sum([-5, 100, -1, 50]) == 99  # -1 + 50
    assert find_max_consecutive_sum([7, 8]) == 15
    assert find_max_consecutive_sum([5, 5, 5, 5]) == 10
    assert find_max_consecutive_sum([0, 0, 0]) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Explicación del código:
Se comparan las sumas consecutivas con el '>', si es mayor entonces se vuelve a
asignar la variable greater y se hace con len(num_list) - 1 para evitar un error 
de índice.
"""
