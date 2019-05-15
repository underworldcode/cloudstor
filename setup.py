from setuptools import setup, find_packages
from numpy.distutils.core import setup, Extension
from os import path
import io

## instructions for upload to pypi




this_directory = path.abspath(path.dirname(__file__))
with io.open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

if __name__ == "__main__":
    setup(name = 'cloudstor',
          author            = "Louis Moresi",
          author_email      = "louis.moresi@anu.edu.au",
          url               = "https://github.com/underworldcode/cloudstor",
          version           = "0.1.1",
          description       = "Python access to AARNET cloudstor (owncloud) storage via webdav",
          long_description  = long_description,
          long_description_content_type='text/markdown',
          packages          = ['cloudstor'],
          install_requires  = ['webdav'],
          setup_requires    = ["pytest-runner", 'webdav'],
          tests_require     = ["pytest", 'webdav'],
          # package_data      = {'quagmire': ['Examples/Notebooks/data',
          #                                   'Examples/Notebooks/WorkedExamples/*.ipynb',  ## Leave out Unsupported
          #                                   'Examples/Notebooks/Tutorial/*.ipynb',
          #                                   'Examples/Scripts/IdealisedExamples',
          #                                   'Examples/Scripts/LandscapeEvolution',
          #                                   'Examples/Scripts/LandscapePreprocessing',    ## Leave out Unsupported
          #                                   'Examples/Scripts/Scripts/*.py']},
          #
          classifiers       = ['Programming Language :: Python :: 3',
                               'Programming Language :: Python :: 3.3',
                               'Programming Language :: Python :: 3.4',
                               'Programming Language :: Python :: 3.5',
                               'Programming Language :: Python :: 3.6',
                               'Programming Language :: Python :: 3.7',]
          )
