from setuptools import setup

from hooky import __version__

NAME = "hooky"

VERSION = __version__

DESCRIPTION = 'Python module, List/Dict classes with hook point to call when the instance is changed.'


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
