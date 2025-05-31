class MySet:
    def __init__(self, elements=None):
        self.dictionary = {}
        if elements:
            for element in elements:
                self.dictionary[element] = True

    def add(self, element):
        self.dictionary[element] = True

    def delete(self, element):
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        return element in self.dictionary

    def size(self):
        return len(self.dictionary)
