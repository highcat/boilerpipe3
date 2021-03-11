import tarfile
from fnmatch import fnmatch
from os.path import basename, exists, dirname, abspath, join
from distutils.core import setup

import sys
if sys.version_info[0] < 3:
    print("This module can only be used with Python 3.")
    print("For a Python 2 version, see:\nhttps://github.com/misja/python-boilerpipe")
    sys.exit(1)

__version__ = '1.3'
boilerpipe_version = '1.2.0'


setup(
    name='boilerpipe3',
    version=__version__,
    packages=['boilerpipe', 'boilerpipe.extract'],
    package_dir={'': 'src'},
    package_data={
        'boilerpipe': [
            'data/boilerpipe-1.2.2/boilerpipe-core-1.2.2.jar',
            'data/boilerpipe-1.2.2/README',
            'data/boilerpipe-1.2.2/lib/*.jar',
        ],
    },
    install_requires=[
        'JPype1',
        'charade',
    ],
    author='Aditya Kresna Permana',
    author_email='zeandcode@gmail.com',
    maintainer = 'Aditya Kresna Permana',
    maintainer_email = 'zeandcode@gmail.com',
    url = 'https://github.com/highcat/boilerpipe3',
    classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Apache Software License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.4',
          'Natural Language :: English',
      ],
      keywords='boilerpipe',
      license='Apache 2.0',

    description='Python interface to Boilerpipe, Boilerplate Removal and Fulltext Extraction from HTML pages with Python 3 support'
)
