# countdown-solver
This program easily and efficiently solves the tasks given on the popular TV-show Countdown (and 8 Out Of 10 Cats Does Countdown).

## Letters Game
The program takes in the stack of given letters as a single string without a seperator (e.g. `"vonrmeods"`) and outputs all valid words of 6 letters and above, or until it finds a solution. The letters game is solved using a comprehensive list of over 466k english words. Please note that despite the list only containing valid english words, not all words follow the rules for accepted solutions on Countdown.

### Example Input and Output

#### Input
```
Input letters: igtesgilo
```
#### Output
```
Number of 9-letter words: 0

Number of 8-letter words: 1
['loggiest']

Number of 7-letter words: 9
['toggles', 'oligist', 'oiliest', 'logiest', 'loggets', 'iolites', 'goglets', 'giglots', 'giglets']

Number of 6-letter words: 27
['toiles', 'toggle', 'toggel', 'Tigges', 'stogie', 'sigloi', 'seggio', 'logist', 'loggie', 'logget', 'Listie', 'Ligget', 'Ligeti', 'legits', 'legist', 'iolite', 'goslet', 'goglet', 'gilgie', 'Gilges', 'gigots', 'giglot', 'Giglio', 'giglet', 'gestio', 'estoil', 'egoist']
```

