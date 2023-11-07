import src.inc_dec as inc_dec    # The code to test


def test_increment():
    """ hola"""
    assert inc_dec.increment(3) == 4


# si no esta este test no detecta los otros.. ignorarlo
