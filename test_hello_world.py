from hello_world import hello_world

def test_hw():
    assert hello_world() == "Hello World!"

def test_hw_1():
    value = "Hello World!"
    assert len(hello_world()) == len(value)