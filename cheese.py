class Cheese:
    """main cheese class"""

    def __init__(self):
        self.name = None
        self.emoji = '🧀'
        self.origin = None
        self.is_stinky = False

    def eat(self):
        """Eat cheese"""
        if not self.name:
            raise AttributeError('current cheese has no name')
        return f"{self.name} is yummy"

    # origin of cheese
    def get_origin(self):
        if not self.origin:
            raise AttributeError('current cheese has no origin')
        return self.origin

    def throw_away(self):
        raise Exception("No")


class Camembert(Cheese):
    """Camembert cheese class"""
    def __init__(self):
        super().__init__()
        self.name = "Camembert"
        self.is_stinky = True
        self.origin = 'France'

    def eat(self):
        return f"J'aime manger du camembert"


class Manchego(Cheese):
    """Manchego cheese class"""
    def __init__(self):
        super().__init__()
        self.name = "Manchego"
        self.is_stinky = False
        self.origin = 'Spain'

    def eat(self):
        return "Me encanta el queso manchego"


class Stilton(Cheese):
    def __init__(self):
        super().__init__()
        self.name = "Stilton"
        self.is_stinky = True
        self.origin = 'England'
