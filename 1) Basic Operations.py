
def basic_operations(num1: int, num2: int, election: str) -> int: 
    match election: 
        case "+": 
            return num1 + num2 
        case "-": 
            return num1 - num2 
        case "*": 
            return num1 * num2
        case "/":   
            if num2 == 0: 
                raise ValueError("Division by zero isn't allowed")
            return num1 / num2
        case _: 
            return 0

def test():
    assert basic_operations(5, 3, "+") == 8
    assert basic_operations(-2, 7, "+") == 5

    assert basic_operations(10, 4, "-") == 6
    assert basic_operations(0, 5, "-") == -5

    assert basic_operations(6, 7, "*") == 42
    assert basic_operations(-3, 3, "*") == -9

    assert basic_operations(8, 2, "/") == 4.0
    assert basic_operations(7, 2, "/") == 3.5

    # Division by zero
    try:
        basic_operations(10, 0, "/")
    except ValueError as e:
        assert str(e) == "Division by zero isn't allowed"

    # No valid
    assert basic_operations(5, 5, "%") == 0
    assert basic_operations(2, 3, "**") == 0

    print("All test cases passed!")

if __name__ == "__main__":   
    test()

"""
Explicación del código:
Se efectuan las operaciones básicas con un match case y si hay una división por
0 salta un error.
"""