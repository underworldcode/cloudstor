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

        if self.is_dir("/"):
            self._remote_type = "directory"
        else:
            self._remote_type = "file"

        return

    def is_file(self, remote_path):
        if self.check(remote_path):
            if self.is_dir(remote_path):
                return False
            else:
                return True
        else:
            raise(RuntimeError("Invalid remote_path"))

    ## Workaround for the assumption that the remote file name has information in it
    def open(self, remote_file=None, **kwargs):
        if "dir" in self.remote_type:
            return super(cloudstor, self).open(remote_file, **kwargs)
        else:
            import os, tempfile
            local_tmp_file = os.path.join(tempfile.gettempdir(), next(tempfile._get_candidate_names()))
            if remote_file is None:
                remote_file = "/"
            self.download_file(remote_file, local_tmp_file)
            return open(local_tmp_file, **kwargs)

    @property
    def remote_type(self):
        return self._remote_type

    # @remote_type.setter
    # def remote_type(self, value):
    #
    #     if "directory" in value:
    #         self._remote_type = "directory"
    #     else:
    #         self.remote_type = "file"

        return
