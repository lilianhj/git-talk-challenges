from main import echo

def test_sanity():
    assert True

def test_that_strings_work():
    assert "Hello, world!" == "Hello, " + "world!"

def test_echo():
    assert echo("Hi, world!") == "	Hi, world!"

def test_multi_echo():
    assert echo("Hi, ") + echo("world!") == "	Hi,	world!"

def test_linear_echo():
    assert echo("Hi, " + "	world!") == echo("Hi, ") + " " + echo("world!")
