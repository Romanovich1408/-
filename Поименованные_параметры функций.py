class Human:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f'{self.name} {self.surname} {self.age}'
human_1 = Human('Maxim', 'Tolstous', 33)
print(human_1)