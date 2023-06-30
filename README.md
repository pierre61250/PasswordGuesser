# PasswordGuesser

## Polymorphisme

Le polymorphisme en programmation est un concept qui permet à un objet de prendre différentes formes ou comportements en fonction du contexte dans lequel il est utilisé. En Python, le polymorphisme peut être réalisé à l'aide de deux mécanismes principaux : le polymorphisme de sous-typage (ou d'héritage) et le polymorphisme ad hoc (ou de surcharge).

### Polymorphisme de sous-typage (héritage) :
Dans ce mécanisme, plusieurs classes dérivées peuvent être traitées comme des instances de leur classe de base commune. Cela signifie que vous pouvez appeler les mêmes méthodes sur des objets de différentes classes dérivées, et le comportement sera spécifique à chaque classe. Voici un exemple :

```python
class WordManager():
    @abstractmethod
    def __init__(self, words):
        self.words = words
        self.possibilities = self.run()

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];

class Accent(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(unidecode(word))
        return result

class Capitalize(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(word.capitalize())
        return result
```

Dans cet exemple, la classe **WordManager** définit une méthode **transform** qui est ensuite redéfinie dans les classes dérivées **Accent** et **Capitalize**. Lorsque la fonction run de **WordManager** est appelée avec un objet de type **Accent** ou **Capitalize**, la méthode appropriée est exécutée en fonction du type de l'objet.

### Polymorphisme ad hoc (surcharge) :
Ce mécanisme permet à des fonctions ou à des opérateurs d'agir différemment en fonction du type des objets sur lesquels ils sont appliqués. Il est également connu sous le nom de surcharge d'opérateur. Par exemple : (**Je n'ai pas pu l'implémenter dans mon code mais voici un exemple**)

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)
p3 = p1 + p2
print(p3.x, p3.y)  # Affiche "4 6"
```

Dans cet exemple, la classe Point définit une méthode spéciale __add__, qui est appelée lorsque l'opérateur + est utilisé entre deux objets Point. Cette méthode retourne un nouvel objet Point dont les coordonnées sont la somme des coordonnées des deux objets.

Le polymorphisme permet d'écrire du code plus générique et réutilisable en traitant différents types d'objets de manière uniforme. Il facilite également l'extension du code, car de nouveaux types peuvent être ajoutés sans modifier le code existant qui utilise ces types.

## L'encapsulation
L'encapsulation est un principe fondamental de la programmation orientée objet (POO) qui consiste à regrouper des données et des méthodes connexes dans une seule entité appelée classe. En Python, l'encapsulation est réalisée en utilisant des conventions de nommage et des attributs spéciaux.

### Attributs privés :
En Python, il n'existe pas de véritable notion d'attributs privés qui sont totalement inaccessibles en dehors de la classe. Cependant, il est d'usage de préfixer le nom des attributs avec un double tiret bas (__) pour indiquer qu'ils sont destinés à un usage interne à la classe. Par exemple :

```python
class WordManager():
    @abstractmethod
    def __init__(self, words):
        self.__words = words
        self.possibilities = self.run()

    def words(self):
        return self.__words

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];
```

Bien que l'attribut **__words** soit accessible depuis l'intérieur de la classe, son accès direct depuis l'extérieur de la classe générera une erreur.

### Propriétés (getters et setters) :
Les propriétés en Python permettent de contrôler l'accès aux attributs d'une classe en fournissant des méthodes spéciales appelées "getters" et "setters". Cela permet de définir des règles de validation ou de transformation lors de l'accès aux attributs. Par exemple :

```python
class WordManager():
    @abstractmethod
    def __init__(self, words):
        self.__words = words
        self.possibilities = self.run()

    @property
    def words(self):
        return self.__words

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];
```

Dans cet exemple, la méthode **words** est définie comme une propriété en utilisant le décorateur @property. Cela permet d'accéder à l'attribut **__words** en utilisant la syntaxe **WordManager.words** plutôt que **WordManager.words()**.
Le setter est défini à l'aide du décorateur @attribut.setter et permet de valider la valeur affectée à l'attribut avant de l'affecter réellement. Dans cette exemple il n'y a pas de setter pour **words** afin de protéger la liste de mots initial.

L'encapsulation en Python vise à restreindre l'accès direct aux attributs d'une classe et à fournir des méthodes appropriées pour interagir avec ces attributs. Cela permet de protéger les données internes d'une classe, de maintenir l'intégrité des objets et de faciliter la modification interne de la classe sans impacter les utilisateurs externes.

## Composition
La composition en programmation orientée objet (POO) est un concept qui permet à une classe d'inclure des objets d'autres classes comme membres, formant ainsi une relation de tout-à-partie. En Python, la composition est mise en œuvre en créant une instance d'une classe à l'intérieur d'une autre classe et en utilisant cette instance pour effectuer des opérations ou accéder à des fonctionnalités spécifiques.

```python
class Engine:

    def __init__(self, words, options = []):
        self.words = words
        self.options = options
        self.possibilities = []
        self.charManager = CharManager()
        self.passwords = self.run()

    def run(self):
        if 'upper' in self.options:
            self.setWords(Uppercase(self.words).possibilities)
        if 'lower' in self.options:
            self.setWords(Lowercase(self.words).possibilities)
        if 'capitalize' in self.options:
            self.setWords(Capitalize(self.words).possibilities)
        if 'accent' in self.options:
            self.setWords(Accent(self.words).possibilities)
        if 'leet' in self.options:
            self.setWords(Leet(self.words).possibilities)
        if 'char' in self.options:
            self.setWords(self.charManager.char)
        if 'allChar' in self.options:
            self.setWords(self.charManager.allChar)

        print(self.words)

        # Mets en place toutes les combinaisons
        self.permute_and_combine_list()
        # Créer une list avec toutes les combinaisons sous forme de string
        return self.fromArrayToString()
    
    def setWords(self, newWords):
        self.words = list(set(self.words + newWords))

    def permute_and_combine_list(self):
        """
        Permute et combine les éléments de la liste donnée en utilisant les méthodes
        permutations et combinations de la bibliothèque itertools et retourne une liste de
        toutes les permutations et combinaisons possibles.
        """
        limit = 4 if len(self.words) > 5 else len(self.words)+1
        for i in range(1, limit):
            # génère toutes les combinaisons de longueur i
            for combo in combinations(self.words, i):
                # génère toutes les permutations pour chaque combinaison
                for perm in permutations(combo):
                    self.possibilities.append(perm)
    
    def fromArrayToString(self):
        result = []
        for item in self.possibilities:
            result.append(''.join(item))
        return result
```

Dans cet exemple, la classe **Engine** possède un membre **charManager** qui est une instance de la classe **CharManager**. Lorsque l'attribut **charManager** est appelée sur un objet Engine, il utilise l'instance de **CharManger** pour utiliser les différentes listes de caractères.

La composition permet de créer des relations plus flexibles et dynamiques entre les classes. Les objets inclus peuvent être utilisés pour accéder à leurs fonctionnalités spécifiques tout en maintenant une séparation claire entre les différentes responsabilités des classes.

Il est important de noter que la composition diffère de l'héritage (ou de la relation tout-est-un). Avec la composition, une classe peut inclure plusieurs objets d'autres classes, tandis que l'héritage permet à une classe de dériver les fonctionnalités d'une seule classe de base.

En utilisant la composition, vous pouvez construire des structures de classes plus modulaires, réutilisables et évolutives, en favorisant le principe de séparation des préoccupations et en permettant des associations flexibles entre les objets.

## L'héritage
L'héritage est un concept fondamental de la programmation orientée objet (POO) qui permet à une classe de hériter des caractéristiques (attributs et méthodes) d'une autre classe appelée classe de base ou classe parente. En Python, l'héritage est mis en œuvre en définissant une classe dérivée (ou classe enfant) qui hérite des propriétés d'une classe de base (ou classe parente).

```python
class WordManager():
    @abstractmethod
    def __init__(self, words):
        self.__words = words
        self.possibilities = self.run()

    @property
    def words(self):
        return self.__words

    def run(self):
        # Lance la methode de transformation
        return self.transform()

    def transform(self):
        return [];

class Uppercase(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(word.upper())
        return result
```

Dans cet exemple, la classe **WordManager** est la classe de base avec une méthode **transform()** qui effectue une action de transformation des mots fourni à la classe. La classe **Uppercase** est une classe dérivée de **WordManager** qui hérite de la méthode **transform()**.

Lorsque vous créez une instance de la classe dérivée **Uppercase**, elle possède à la fois les attributs et les méthodes de la classe de base **WordManager** ainsi que les attributs et les méthodes spécifiques de la classe **Uppercase**. Vous pouvez accéder aux méthodes héritées en utilisant l'instance de la classe dérivée.

L'héritage permet d'établir une hiérarchie de classes, où les classes dérivées peuvent étendre ou spécialiser les fonctionnalités de la classe de base. Cela favorise la réutilisabilité du code, la modularité et permet de créer des relations logiques entre les classes.

En plus de l'héritage simple, Python prend également en charge d'autres concepts d'héritage, tels que l'héritage multiple (une classe peut hériter de plusieurs classes de base) et l'héritage hiérarchique (une classe peut être à la fois une classe de base pour une classe dérivée et une classe dérivée d'une autre classe). Ces concepts supplémentaires offrent une plus grande flexibilité lors de la conception des classes dans vos programmes Python.

