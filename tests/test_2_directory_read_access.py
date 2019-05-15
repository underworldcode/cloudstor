from cloudstor import cloudstor
import pytest

public_cs = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/KueHALSsgizCxpd", password='')
public_csk = cloudstor(url="KueHALSsgizCxpd", password='')
public_csp = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/F7yegRFEcsTH0QZ", password='ThisIsNotASecure1!!')
public_cspk = cloudstor(url="F7yegRFEcsTH0QZ", password='ThisIsNotASecure1!!')

## File listing (if previous tests pass, then we should really not need to be exhaustive here)

@pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
def test_public_list(test_target):
    # Check that a public directory (owned by louis.moresi@anu.edu.au) is available
    files = test_target.list()
    assert "Readme.txt" in files

## File read

@pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
def test_public_read(test_target):
    with public_cs.open("Readme.txt") as f:
        a = f.read()
        assert "Test File" in a

## File download

@pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
def test_public_read(test_target, tmp_path):
    import os

    ## Note, I cannot convince the download module to accept the tmp path as valid
    tmp_location = tmp_path / "Readme.txt"
    public_cs.download("Readme.txt","Readme.txt")
    os.rename("Readme.txt", tmp_location)
    with open(tmp_location) as f:
        a = f.read()
        assert "Test File" in a
