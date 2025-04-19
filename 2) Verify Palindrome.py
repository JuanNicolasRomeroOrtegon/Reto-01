
def verify_palindrome(word: str) -> bool:
    word = word.lower()
    for x in range(len(word) // 2):
        if word[x] != word[-x-1]:
            return False
    return True

def test():
    assert verify_palindrome("radar") == True
    assert verify_palindrome("level") == True
    assert verify_palindrome("civic") == True

    assert verify_palindrome("hello") == False
    assert verify_palindrome("python") == False

    assert verify_palindrome("noon") == True
    assert verify_palindrome("abba") == True
    assert verify_palindrome("a") == True
    assert verify_palindrome("") == True
    assert verify_palindrome("Madam") == True  
    assert verify_palindrome("nolemonnomelon") == True

    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Explicación del código:
Se convierte la palabra en minúsculas para que no de problemas (Ej: M != m)
Se verifica hasta la mitad de la longitud de la palabra, pues estamos revisando
las letras de dos en dos. 
Verifica si las letras son iguales para ver si es palíndromo o no.
"""
