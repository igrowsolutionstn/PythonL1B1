import pytest
import bank    # The code to test

def test_withdraw():
    assert bank.withdraw(10,10) == 0

def test_deposit():
    assert bank.deposit(10,10) == 20

def test_name():
    assert bank.name=='Tom'

def test_variable_count():
    len(locals)