
def sort_characters(original_list: list[str]) -> list[list[str]]:
    return [sorted(word) for word in original_list]

def words_with_the_same_characters(sorted_letters: list[list[str]]) -> list[str]:
    same_characters: list[list[str]]

    same_characters = []
    for x in range(len(sorted_letters) - 1):
        #We compare each word
        for y in range(x + 1, len(sorted_letters)):
            # We do this to avoid repetitions:
            if sorted_letters[x] == sorted_letters[y] and (
            sorted_letters[x] not in same_characters):
                same_characters.append(sorted_letters[x])
                
    return same_characters

def return_words(original_list: list[str]) -> list[str]:
    same_words: list

    sorted_letters = sort_characters(original_list)
    same_characters = words_with_the_same_characters(sorted_letters)

    same_words = []
    for x in range(len(same_characters)):
        for w in range(len(sorted_letters)):
            if same_characters[x] == sorted_letters[w]:
                same_words.append(original_list[w])
        
    return same_words

def test():
    assert return_words(["amor", "roma", "perro"]) == ["amor", "roma"]
    assert return_words(["abc", "bca", "cab", "xyz", "zyx", "xzy"]) == ["abc", 
    "bca", "cab", "xyz", "zyx", "xzy"]
    assert return_words(["arbol", "al", "amor", "roma", "la", "omar", 
    "ramo"]) == ["al", "la", "amor", "roma", "omar", "ramo"]
    assert return_words(["a", "b", "c"]) == []
    assert return_words(["aaa", "aaa", "aaa"]) == ["aaa", "aaa", "aaa"]
    assert return_words([]) == []
    print("All tests passed!")

if __name__ == "__main__":
    test()

"""
Explicación del código:
La primera función (`sort_characters`) ordena alfabéticamente los caracteres 
de cada palabra de la lista original y retorna una nueva lista con estas 
palabras ordenadas carácter por carácter.

La segunda función (`words_with_the_same_characters`) compara todas las 
combinaciones posibles de palabras ordenadas. Si encuentra dos o más palabras 
con los mismos caracteres, agrega esa lista de caracteres ordenada SOLO UNA VEZ 
al resultado.(Solo se agrega una vez esta lista de caracteres ordenada para 
evitar repeticiones en la tercera función)

La tercera función (`return_words`) utiliza la lista de caracteres en común 
para recuperar las palabras originales que tienen esos mismos caracteres, y 
las retorna.
"""

