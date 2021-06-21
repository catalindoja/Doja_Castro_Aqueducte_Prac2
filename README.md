# Doja_Castro_Aqueducte_Prac2
Practica 2 d'algorisme de programacio sobre el calcul del cost d'un aqueducte

# Algorisme Greedy:

---Recursiu---
El algorisme greedy ha de situar-se en el primer fill i comprovar des de la primera posicio que te davant fins a la posicio final.
Mentre fa aixo es queda amb el cost minim local i la posicio d'on ha agafat aquest cost.
Un cop acabada la comprovacio es situa en la posicio del cost minim i torna a fer el mateix procediment.
Es un algorisme de profunditat i acabara quan s'arribi al ultim fill del arbre o si totes les rames del cost local acaben donant impossible.

---Iteratiu---
Al cas iteratiu el que fem es utilitzar un bucle aniuat ja que el algorisme es molt senzill i no requereix cap pila.


# Algorisme Backtracking:

---Recursiu---
El algorisme backtracking es un algorisme de força bruta en aquest cas, ja que volem totes les solucions possibles i ens quedem amb la que te el cost minim.
La idea es que si mirem el problema com un arbre n-ari complet, s'ha de visitar totes les rames i totes les fulles i calcular costos i possibilitats de construccio.
Si per exemple tots els camins donen impossible el algorisme ha de printar impossible.
Per altra banda si no es el cas, guardarem el cost mes baix i l'anirem comparant amb els calculs de altres camins.
Al final retornarem el cost optim.			

---Iteratiu---
En el cas del iteratiu el que fem es crear una classe Context on tenim variables auxiliar i un entry point.
La idea de darrere es emular la pila del algorisme recursiu canviant entre dos estats "resume" i "call".
Començant per "call" es el push que cridara al seguent push i tambe on tenim el cas base que retorna el calcul del ultim pilar
El "resume" es el lloc on es fan els calculs i depenent del numero de fills que te un punt es fan afegeixen mes entrades a la pila amb en entry a "call".
Depenent dels casos on estem canviarem el entry actual a "call" o "resume" o farem un pop de la pila quan ja no sigui necessari el top actual.
Al final retornem el cost optim com al recursiu.


#Algorisme Dynamic Programming:
---Recursiu---
En el cas del algorisme dynamic tenim que es casi identic al algorisme de backtracking amb la peculiaritat de una memoria.
Al nostre cas la memoria de un array bidimensional on guardem resultats.
La idea es guardar el resultat de les crides recursives en la memoria si no tenim el calcul ja fet mentre anem fent tot per força bruta.
En el cas de que si que tenim el resultat guardat l'agafem i l'utilitzem. Aixo ens permet guanyar operacions ja que no hem de tornar a fer comprovacions de punts.
Al final retornem el cost optim.

---Iteratiu---
El comportament del dynamic es casi identic al backtracking. Tenim la mateixa estructura amb la diferencia de que tornem a tindre la memoria.
En el resume ens assegurem de comprovar si ja tenim el calcul que volem fet i en cas afirmatiu l'agafem del array bidimensional. Sino calculem i el guardem al array.
Per la resta funciona exactament igual que el backtracking i retorna el cost optim.
