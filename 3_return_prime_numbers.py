
def is_it_prime(num: int) -> bool:
    if num == 2:
        return True
    
    if num <= 1 or num % 2 == 0:
        return False
    
    # We start from 3 and add up 2 each time (we're only checking odd numbers)
    for x in range(3, int(num**0.5) + 1, 2):
        if num % x == 0:
            return False
    return True

def list_that_returns_primes(full_list: list[int]) -> list[int]:
    returned_list = []
    for element in full_list:
        if is_it_prime(element):
            returned_list.append(element)
    return returned_list

def test():
    assert list_that_returns_primes([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [2, 3, 5, 7]
    assert list_that_returns_primes([11, 13, 17]) == [11, 13, 17]
    assert list_that_returns_primes([0, 1, 4, 6, 8, 9, 10]) == []
    assert list_that_returns_primes([]) == []
    assert list_that_returns_primes([-3, -2, -1, 0, 1]) == []
    assert list_that_returns_primes([97, 98, 99]) == [97]

    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Explicación del código:
En la primera función se verifica si un número es primo, y esto se hace 
verificando solo numeros impares de dos en dos para optimizar el proceso. 
Se revisa hasta la raíz cuadrada del número porque los divisores se presentan en pares. 
Si un número n tiene un divisor a, entonces también tiene un divisor b tal que a×b=n.
En cada pareja de divisores, al menos uno de ellos debe ser menor o igual que la raíz cuadrada 
de n, de lo contrario, el producto a×b sería mayor que n, lo cual es un absurdo. Por eso, 
basta con verificar los posibles divisores hasta n para determinar si un número es primo.
En la segunda función se pasa cada elemento de la lista en la primera función y 
se retorna una lista con todos los números que verifique ser primos.
"""
