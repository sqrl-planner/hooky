from setuptools import setup
import os

NAME = "hooky"

VERSION = '0.2.0'

DESCRIPTION = 'Python module, classes with hook point to imitate list and dict for add and del'

LONG_DESCRIPTION = ''
if os.path.exists('long_description.rst'):
    LONG_DESCRIPTION = open('long_description.rst').read()


URL = 'https://github.com/meng89/{}'.format(NAME)

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(name=NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Chen Meng',
      author_email='ObserverChan@gmail.com',
      license='MIT',
      url=URL,
      classifiers=CLASSIFIERS,
      py_modules=['hooky'],
      )
