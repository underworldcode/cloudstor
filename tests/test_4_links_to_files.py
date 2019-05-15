from cloudstor import cloudstor
import pytest

public_file = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/s1z3yiL0j4sq3A9", password='')
public_rw = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/l3PMHovJuA9zBz9", password='')

def test_remote_type():
    assert "dir" in public_rw.remote_type
    assert "file" in public_file.remote_type


def test_is_file():
    assert public_file.is_file("")
    assert public_file.is_file("/")

def test_read_file():
    with public_file.open("") as f:
        a = f.read()
    assert "information" in a


## open ... is intercepted ... so ...
