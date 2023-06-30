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

## Interface
En Python, contrairement à certains autres langages de programmation orientée objet, il n'existe pas de structure intégrée spécifique pour les interfaces. Cependant, vous pouvez utiliser des classes abstraites pour créer une forme d'interface en Python en utilisant le module abc (Abstract Base Classes) du module standard de Python.

```python
class Interface(ABC):
    @abstractmethod
    def transform(self):
        pass

class WordManager(Interface):
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

Dans cet exemple, nous créons une classe abstraite **Interface** qui hérite de la classe **ABC** du module *abc*. La méthode **transform** est décorée avec le décorateur @abstractmethod, ce qui la rend obligatoire à implémenter dans les classes dérivées.

Ensuite, nous définissons une classe **WordManager** qui implémente l'interface **Interface** en fournissant une implémentation de la méthode **transform**.

Lorsque nous instancions **WordManager** et appelons la méthode **transform**, l'implémentation de la classe **WordManager** est utilisée.

En utilisant des classes abstraites et des méthodes abstraites, vous pouvez définir des contrats d'interface et obliger les classes dérivées à fournir une implémentation spécifique. Bien qu'il ne s'agisse pas d'une véritable interface en termes de restriction de la signature des méthodes, cela permet de créer une structure similaire à une interface et de garantir une certaine cohérence dans l'utilisation des classes dérivées.

Il est important de noter que l'utilisation des interfaces est une pratique optionnelle en Python. Dans de nombreux cas, il est possible de concevoir des classes sans interfaces explicites en tirant parti du duck typing et de la flexibilité inhérente de Python.

## Méthodes et attributs d'objets
En programmation orientée objet (POO) en Python, vous pouvez utiliser des méthodes et des attributs d'objets pour interagir avec les objets créés à partir de classes. Voici comment utiliser ces méthodes et attributs :

### Méthodes d'objet :
Les méthodes d'objet sont des fonctions définies à l'intérieur d'une classe et sont spécifiques à chaque instance de la classe. Vous pouvez appeler ces méthodes sur des objets individuels pour effectuer des opérations spécifiques. Par exemple :

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

La méthode **setWords()** est définie dans la classe **Engine** et peut être appelée sur des instances spécifiques de la classe en utilisant la notation **Engine.setWords()**. Dans ce cas présent la classe **Engine** appel sa propre méthode **setWords()** avec la notation suivante **self.setWords()**.

### Attributs d'objet :
Les attributs d'objet sont des variables qui sont définies à l'intérieur d'une classe et sont spécifiques à chaque instance de la classe. Vous pouvez accéder et modifier ces attributs en utilisant la notation dot (.) sur les objets individuels. Par exemple :

```python
self.setWords(Uppercase(self.words).possibilities)

class Uppercase(WordManager):

    def __init__(self, words):
        super().__init__(words)

    def transform(self):
        result = []
        for word in self.words:
            result.append(word.upper())
        return result

class WordManager(Interface):
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

L'attribut **possibilities** est défini dans la méthode __init__() de la classe **Uppercase** elle même hérité de la classe **WordManager** et peut être accédé ou modifié en utilisant **Uppercase.possibilities**.

Les méthodes d'objet permettent aux objets de réaliser des actions et d'effectuer des calculs spécifiques, tandis que les attributs d'objet permettent aux objets de stocker et de maintenir des informations spécifiques à eux-mêmes.

Lorsque vous créez des classes et des objets, vous pouvez définir et utiliser des méthodes et des attributs selon les besoins de votre programme. Cela vous permet de modéliser des comportements et des états spécifiques pour vos objets et d'interagir avec eux de manière appropriée.

## Méthodes et attributs statiques
En programmation orientée objet (POO) en Python, vous pouvez définir des méthodes et des attributs statiques dans une classe. Les méthodes et les attributs statiques appartiennent à la classe elle-même plutôt qu'à une instance spécifique de la classe. Ils sont partagés par toutes les instances de la classe et peuvent être utilisés sans avoir besoin d'instancier la classe.

### Méthodes statiques :
Les méthodes statiques sont des méthodes définies dans une classe qui n'opèrent pas sur une instance spécifique de la classe. Elles sont décorées avec le décorateur @staticmethod. Vous pouvez appeler ces méthodes directement sur la classe elle-même, sans avoir besoin d'instancier la classe. Par exemple :

```python
class DateManager():
    def __init__(self, date):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.possibilities = self.run()

    @staticmethod
    def isDate(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def run(self):
        # Lance la methode de transformation
        return self.transform()
    
    @staticmethod
    def transformToFrench(month):
        months_english = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        months_french = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
        if month in months_english:
            index = months_english.index(month)
            return months_french[index]
    
    def numberToLetter(self):
        month = self.date.strftime("%B");
        return [month, self.transformToFrench(month)]
    
    def dateDecomposition(self):
        return [self.date.strftime("%m"), self.date.strftime("%d"), self.date.strftime("%Y"), str(self.date.month), str(self.date.day), self.date.strftime("%y")]

    def transform(self):
        return self.numberToLetter() + self.dateDecomposition();

# Exemple d'utilisation :
for word in self.words:
    if DateManager.isDate(word):
        self.setWords(DateManager(word).possibilities)
```

La méthode **isDate()** est définie en utilisant le décorateur @staticmethod et peut être appelée directement sur la classe DateManager sans avoir besoin d'instancier la classe.

### Attributs statiques :
Les attributs statiques sont des variables qui sont définies dans une classe et partagées par toutes les instances de la classe. Ils sont définis à l'intérieur de la classe, mais à l'extérieur des méthodes, en tant que variables de classe. Par exemple :

```python
class DateManager():
    months_english = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_french = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    
    def __init__(self, date):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.possibilities = self.run()

    @staticmethod
    def isDate(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def run(self):
        # Lance la methode de transformation
        return self.transform()
    
    @staticmethod
    def transformToFrench(month):
        if month in DateManager.months_english:
            index = DateManager.months_english.index(month)
            return DateManager.months_french[index]
    
    def numberToLetter(self):
        month = self.date.strftime("%B");
        return [month, self.transformToFrench(month)]
    
    def dateDecomposition(self):
        return [self.date.strftime("%m"), self.date.strftime("%d"), self.date.strftime("%Y"), str(self.date.month), str(self.date.day), self.date.strftime("%y")]

    def transform(self):
        return self.numberToLetter() + self.dateDecomposition();
```

L'attribut **months_english** est défini à l'intérieur de la classe **DateManager** et peut être accédé directement sur la classe elle-même.

Les méthodes et les attributs statiques sont utiles lorsque vous avez des fonctionnalités qui ne dépendent pas de l'état spécifique d'une instance de classe, mais plutôt de la classe elle-même ou de données partagées par toutes les instances de la classe. Ils offrent une manière pratique d'organiser et de regrouper ces fonctionnalités au sein de la classe.

Il est important de noter que les méthodes et les attributs statiques en Python ne nécessitent pas l'utilisation du mot-clé static comme dans certains autres langages de programmation. Vous pouvez simplement utiliser les décorateurs @staticmethod pour les méthodes statiques et définir les attributs statiques en tant que variables de classe.

## Méthodes et les attributs de classe
En programmation orientée objet (POO) en Python, les méthodes et les attributs de classe sont associés à la classe elle-même plutôt qu'à une instance spécifique de la classe. Vous pouvez les définir en utilisant le décorateur @classmethod pour les méthodes de classe et en les déclarant directement dans la classe pour les attributs de classe. Voici un exemple :

```python
class DateManager():
    months_english = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    months_french = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre']
    
    def __init__(self, date):
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.possibilities = self.run()

    @staticmethod
    def isDate(date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    def run(self):
        # Lance la methode de transformation
        return self.transform()
    
    @staticmethod
    def transformToFrench(month):
        if month in DateManager.months_english:
            index = DateManager.months_english.index(month)
            return DateManager.months_french[index]
    
    def numberToLetter(self):
        month = self.date.strftime("%B");
        return [month, self.transformToFrench(month)]
    
    def dateDecomposition(self):
        return [self.date.strftime("%m"), self.date.strftime("%d"), self.date.strftime("%Y"), str(self.date.month), str(self.date.day), self.date.strftime("%y")]

    @classmethod
    def transform(self):
        return self.numberToLetter() + self.dateDecomposition();
```

Dans cet exemple, nous définissons une classe **DateManager** avec un attribut de classe **months_french** et deux méthodes : **transform** et **transformToFrench**.

L'attribut de classe **months_french** est déclaré directement à l'intérieur de la classe **DateManager**. Il peut être accédé en utilisant le nom de la classe suivi du nom de l'attribut (**DateManager.months_french**).

La méthode de classe class_method est décorée avec @classmethod. Elle prend un premier argument cls qui fait référence à la classe elle-même. Vous pouvez utiliser cls pour accéder aux attributs de classe ou appeler d'autres méthodes de classe.

La méthode statique static_method est déclarée en utilisant le décorateur @staticmethod. Contrairement à la méthode de classe, elle n'a pas de premier argument spécial pour la classe. Vous pouvez l'appeler directement à partir de la classe sans créer d'instance de la classe.

L'exemple montre comment accéder à un attribut de classe, appeler une méthode de classe et appeler une méthode statique.

Il est important de noter que les méthodes de classe et les attributs de classe sont partagés par toutes les instances de la classe et peuvent être utilisés sans avoir besoin d'instancier la classe.