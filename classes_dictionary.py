class Kniha:
    def __init__(self, id: int, name: str, author: str, year_publication: int, category: str, review: float,
                 borrow: bool) -> None:
        self.id = id
        self.name = name
        self.author = author
        self.year_publication = year_publication
        self.category = category
        self.review = review
        self.borrow = borrow

    def borrow(self):
        if not self.borrow:
            self.borrow = True
            print(f"Kniha {self.name} borrowed")
        if self.borrow:
            self.borrow = False
            print(f"Kniha {self.name} is free")

