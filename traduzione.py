class Traduzione:

    def __init__(self, alieno, italiano):
        self.alieno = alieno
        self.italiano = italiano

    def __str__(self):
        string=""
        for i in self.italiano:
            string += f"{i} "
        return f"{self.alieno} {string} "