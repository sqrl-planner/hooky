from setuptools import setup

from hooky import __version__

NAME = "hooky"

VERSION = __version__

DESCRIPTION = 'a Python module, List/Dict classes with hook point to call when the instance is changed.'


URL = 'https://github.com/meng89/{}'.format(NAME)

CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: Implementation :: CPython',
    'Programming Language :: Python :: Implementation :: PyPy',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      # long_description=LONG_DESCRIPTION,
      author='Chen Meng',
      author_email='ObserverChan@gmail.com',
      license='MIT',
      url=URL,
      classifiers=CLASSIFIERS,
      py_modules=['hooky'],
      tests_require=['nose'],
      test_suite='nose.collector',
      )
