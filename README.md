He hecho un programa que resuelve un laberinto y me dice los pasos que hay que hacer para resolverlo.

Primero, he defindo una funcion "find_path" y dentro de esa funcion he definido otra "dfs" que es "depth first search" para hacer la busqueda del camino.
Luego he marcado la posicion inicial como "visited" para que cuando busque nuevas posiciones las reconozca y luego haga una lista ("path"). 
He indicado las posibles direciones (arriba, abajo, derecha, izquierda) para la busqueda. He hecho condiciones con el "if" para que se verifique que todavia no estan "visited".

Fuera de dfs he definido las variables rows y columns y los espacios para crear el laberinto. 
He definido las coordenadas del laberinto y para terminar he definido que el path (la lista) sea lo que devuelva la funcion find_path y que me haga un print para obtener el resultado del camino que hay que seguir para salir de el laberinto. 
