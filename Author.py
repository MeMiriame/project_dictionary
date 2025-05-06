class Author:
    def __init__(self, id: int, first_name: str, last_name: str, country: str) -> None:
        if not isinstance(id, int):
            raise TypeError("ID must be an integer")
        if not isinstance(first_name, str):
            raise TypeError("First name must be a string")
        if not isinstance(last_name, str):
            raise TypeError("Last name must be a string")
        if not isinstance(country, str):
            raise TypeError("Country must be a string")
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.country = country