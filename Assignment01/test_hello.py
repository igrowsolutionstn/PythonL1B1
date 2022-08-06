import pytest
import hello    # The code to test

def test_increment():
    assert hello.increment(3) == 4

def test_decrement():
    assert hello.decrement(3) == 2