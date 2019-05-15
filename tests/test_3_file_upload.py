from cloudstor import cloudstor
import pytest

public_rw = cloudstor(url="https://cloudstor.aarnet.edu.au/plus/s/l3PMHovJuA9zBz9", password='')

def test_public_mkdir():
    public_rw.mkdir("tmp_test")
    assert public_rw.is_dir("tmp_test")


def test_public_upload(tmp_path):
    with open(tmp_path / "tmp_file.txt", mode="w") as f:
        f.write("This is an empty file")

    local_path = tmp_path / "tmp_file.txt"
    public_rw.upload(local_path = local_path, remote_path="tmp_file.txt")
    assert public_rw.check("tmp_file.txt")


def test_public_delete(tmp_path):

    # Execute this again to upload the file (fail again if impossible)
    test_public_upload(tmp_path)

    public_rw.clean("tmp_file.txt")
    assert public_rw.check("tmp_file.txt") == False





#
# @pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
# def test_public_upload(test_target):
#     # Check that a public directory (owned by louis.moresi@anu.edu.au) is available
#
#
#     files = test_target.list()
#     assert "Readme.txt" in files
#
# ## File read
#
# @pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
# def test_public_read(test_target):
#     with public_cs.open("Readme.txt") as f:
#         a = f.read()
#         assert "Test File" in a
#
# ## File download
#
# @pytest.mark.parametrize("test_target", [public_cs, public_csk, public_csp, public_cspk])
# def test_public_read(test_target, tmp_path):
#     import os
#
#     ## Note, I cannot convince the download module to accept the tmp path as valid
#     tmp_location = tmp_path / "Readme.txt"
#     public_cs.download("Readme.txt","Readme.txt")
#     os.rename("Readme.txt", tmp_location)
#     with open(tmp_location) as f:
#         a = f.read()
#         assert "Test File" in a
