### Reto #1 Programación Orientada a Objetos

Se presentan ejercicios realizados con *programación estructurada*, se aplican  
los conceptos revisados en clase.

**Comentarios de cada ejercicio:**

---

#### Ejercicio 1  
Se efectúan las *operaciones básicas* con un **`match case`** y si hay una  
*división por 0*, salta un **error**.

---

#### Ejercicio 2  
Se convierte la palabra en *minúsculas* para evitar problemas (Ej: **`M != m`**).  
Se verifica hasta la *mitad de la longitud* de la palabra, pues estamos  
revisando las letras de *dos en dos*.  
Verifica si las letras son *iguales* para determinar si es un **palíndromo**.

---

#### Ejercicio 3  
En la *primera función* se verifica si un número es **primo**, y esto se hace  
verificando solo *números impares* de dos en dos para *optimizar* el proceso.  
En la *segunda función* se pasa cada *elemento de la lista* en la primera  
función y se retorna una lista con todos los números que verifiquen ser *primos*.

---

#### Ejercicio 4  
Se comparan las *sumas consecutivas* con el **`>`**. Si es mayor, entonces se  
vuelve a asignar la variable **`greater`** y se hace con **`len(num_list) - 1`**  
para evitar un *error de índice*.

---

#### Ejercicio 5  
La *primera función* (**`sort_characters`**) ordena *alfabéticamente* los  
caracteres de cada palabra de la *lista original* y retorna una nueva lista  
con estas palabras ordenadas *carácter por carácter*.

La *segunda función* (**`words_with_the_same_characters`**) compara todas las  
*combinaciones posibles* de palabras ordenadas. Si encuentra dos o más  
palabras con los *mismos caracteres*, agrega esa lista de caracteres ordenada  
**solo una vez** al resultado (para evitar *repeticiones* en la tercera función).

La *tercera función* (**`return_words`**) utiliza la lista de *caracteres en  
común* para recuperar las *palabras originales* que tienen esos mismos  
caracteres, y las retorna.

