from cloudstor import cloudstor

def test_public_connection():
    # Check that a public directory (owned by louis.moresi@anu.edu.au) is available
    public_cs = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/KueHALSsgizCxpd", password='')
    assert public_cs.check()

def test_public_connection_key_only():
    # Check that a public directory (owned by louis.moresi@anu.edu.au) is available via the key link
    public_cs = cloudstor(url="KueHALSsgizCxpd", password='')
    assert public_cs.check()

def test_public_password_connection():
    # Check that a different public directory (owned by louis.moresi@anu.edu.au) is available with the password
    public_cs = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/F7yegRFEcsTH0QZ", password='ThisIsNotASecure1!!')
    assert public_cs.check()

def test_public_password_connection_key_only():
    # Check that a different public directory (owned by louis.moresi@anu.edu.au) is available with the password
    public_cs = cloudstor(url="F7yegRFEcsTH0QZ", password='ThisIsNotASecure1!!')
    assert public_cs.check()
