
# Mélanger des cartes / Documentation FR

## Présentation

* Langage : Python
* Plateforme : Gamebuino META
* Description : fonction pour mélanger un jeu de 52 cartes
* Fonction principale : `mixCards`

## Commandes

Pendant l'affichage des cartes :

* Bouton Gauche / Droite : afficher le reste des cartes
* Bouton Menu : afficher nombre de mélanges actuel
* Bouton A : effectuer une opération de mélange des cartes

Pendant l'affichage du nombre de mélange :

* Bouton Menu : afficher cartes

## Explications

A chaque opération de mélange :

* On répartie les cartes selon quatre sous jeux de cartes.
* On assemble ses quatre sous jeux tel que le jeu de cartes résultant soit la concaténation du sous jeu 3, 2, 4, puis 1.

Voici un aperçu de deux opérations de mélanges :

![2 mélanges](img/mix_cards.png)

## Code de la fonction principale

```
def mixCards():
	subSet1 = []
	subSet2 = []
	subSet3 = []
	subSet4 = []
	# Mix cards
	for i in range(52):
		s = i % 4
		if s == 0:
			subSet1.append(cards[i])
		elif s == 1:
			subSet2.append(cards[i])
		elif s == 2:
			subSet3.append(cards[i])
		else:
			subSet4.append(cards[i])
	# Re-order cards
	n = 0
	for s in range(4):
		subSet = subSet1
		if s == 0:
			subSet = subSet3
		elif s == 1:
			subSet = subSet2
		elif s == 2:
			subSet = subSet4
		for c in range(13):
			cards[n] = subSet[c]
			n += 1
	game['nbMix'] += 1
```

Note : la dernière ligne `game['nbMix'] += 1` n'est utile que pour ce programme de démonstration.
