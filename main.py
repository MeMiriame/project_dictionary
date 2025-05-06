from Users import Book, Author, User
from Users import users


book = Book(1, "Marco", "Adler Olsen", 2020, "crimi", 4.5, False)
print(book.name+"\nAuthor: "+book.author)

try:
    book = Book("text", "1984", "George Orwell", 2009, "novel", 4.6, True)
except TypeError as chyba:
    print(f'Chyba pri zadani: {chyba}')

def check_login (write_email, write_password, users):
    user_found = False
    for user in users:
        if user.email == write_email and user.password == write_password:
            user_found = True
            print("Login.")
            return
    print("Invalid email or password")

write_email = input("Write your e-mail: ")
write_password = input("Write your password: ")

check_login(write_email, write_password, users)


