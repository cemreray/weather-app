class Person:
      
      address = 'no information'

      def __init__(self, name,year):
        self.name = name
        self.year = year
        print("init metodu çalıştı")

p1 = Person('Ayşe',2001)
p2 = Person('Fatma', 2003) 
p3 = Person(name = 'Ahmet', year = 2006)

def intro(self):
          print('Hello')
print(p1)
print(p2)
print(p3)
print(p1 == p2)

p1.name = 'Ali'
p1.address = 'Isparta'
print(f'p1:name {p1.name} year: {p1.year} address: {p1.address}')