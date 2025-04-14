from classes_dictionary import Kniha


kniha = Kniha(1, "Voda", "Neznámý", 2020, "crimi", 4.5, False)
print(kniha.name+"\nAuthor: "+kniha.author)

try:
    kniha = Kniha("text", "1984", "George Orwell", 2009, "novel", 4.6, True)
except TypeError as chyba:
    print(f'Chyba pri zadani: {chyba}')
