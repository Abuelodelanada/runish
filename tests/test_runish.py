from runish.main import find_charname, name_character


def test_name():
    result = name_character("/")
    assert result == "SOLIDUS"


def test_find():
    result = find_charname("SOLIDUS")
    assert result == "/"
