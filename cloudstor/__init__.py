import webdav.client as _wdc

class cloudstor(_wdc.Client):

    def __init__(self, private=False, url=None, password=None, username=None):
        """Initialise a cloudstor webdav access instance for public or private
           access. Password is not stored anywhere unless you provide it in your
           script. It is not advisable to code a password directly in any script
           that you publish anywhere.

           Cloudstore allows public access to any file or directory with read-only or
           read-write options and (temporary) password protection if needed.

           You can also obtain an app password that you can control separately to
           your online account password but this still provides unlimited access to
           your files.

           You can also provide any password information via environment variables
           if you prefer (see Examples)
        """

        import webdav
        from requests.auth import HTTPBasicAuth
        import getpass

        if not private:
            if url is None:
                print("The public url to the cloudstor shared resource is required")
                print("It should be of the form:")
                print("\t https://cloudstor.aarnet.edu.au/plus/s/UNoxqDf8nevZk")
                print("\t or just specify the key string ....... UNoxqDf8nevZk")
                print("\n")
                raise(RuntimeError("The public url to the cloudstor shared resource is required"))
            else:
                username = url.replace("https://cloudstor.aarnet.edu.au/plus/s/","")

            public_url = "https://cloudstor.aarnet.edu.au/plus/s/" + username

            if password is None:
                password = getpass.getpass("Password for {}".format(public_url))

            # Note the auth dict is different for public / private access
            auth = HTTPBasicAuth(username, password)
            auth_dict = {'webdav_hostname':"https://cloudstor.aarnet.edu.au",
                         'webdav_auth': auth,
                         'webdav_root': "/plus/public.php/webdav/"
                         }

        else:
            if username is None:
                raise(RuntimeError("The username for the cloudstore resource is required"))

            url = "https://cloudstor.aarnet.edu.au"

            if password is None:
                password = getpass.getpass("Cloudstore password for {}".format(username))

            auth = HTTPBasicAuth(username, password)
            auth_dict = {'webdav_hostname':"https://cloudstor.aarnet.edu.au",
                         'webdav_auth': auth,
                         'webdav_root': "/plus/remote.php/webdav/"
             }


        super(cloudstor, self).__init__(options=auth_dict)
        if self.check():
            print("Cloudstore connection established")
        else:
            print("Cloudstore connection failed silently")

        return
