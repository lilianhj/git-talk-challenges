from main import echo

def test_sanity():
    assert True

def test_that_strings_work():
    assert "Hello, world!" == "Hello, " + "world!"

def test_echo():
    assert echo("Hello, world!") == "Hello, world!"

def test_multi_echo():
    assert echo("Hello, ") + echo("world!") == "Hello, world!"

def test_linear_echo():
    assert echo("Hello, " + "world!") == echo("Hello, ") + echo("world!")

def test_double_space_echo():
    assert echo("Hello,  world!") == "Hello, world!"
