from cc import hello


def test_hello():
    # make a minor change
    assert hello() == "Hello World!"
