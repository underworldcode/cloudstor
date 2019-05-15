
def test_cloudstor_import():
    import cloudstor
    print("Cloudstor was imported from {}".format(cloudstor.__file__))
    return

def test_cloudstor_docs_import():
    from cloudstor import documentation
    print("cloudstor.documentation was imported successfully")
    return

def test_cloudstor_webdav_import():
    from cloudstor import cloudstor
    print("cloudstor.cloudstor was imported successfully")
    return

if __name__ == "__main__":
    test_cloudstor_import()
