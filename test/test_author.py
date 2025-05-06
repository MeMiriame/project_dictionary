from author import Author

def test_author_initialization():
    author = Author(1, "George", "Orwell", "Denkmark")
    assert author.id == 1
    assert author.first_name == "George"
    assert author.last_name == "Orwell"
    assert author.country == "Denkmark"

def test_author_invalid_id():
    try:
        Author("abc", "George", "Orwell", "Denkmark")
        assert False, "TypeError not raised"
    except TypeError as e:
        assert str(e) == "ID must be an integer"
