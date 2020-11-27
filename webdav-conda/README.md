# Notes

Note that the webdav package is currently a dependency of the cloudstor package but is not
available on conda. This is the conda build for that dependency - all it actually does is to
pull the code from the original git repository and build. There is no source code in this 
repository.

## Usage

`conda build webdav-conda`
`anaconda upload /path/to/webdav-1.1.6-h39e3cac_0.tar.bz2`


