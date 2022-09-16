from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
    name             = 'opencv',
    version          = '0.1',
    description      = 'An app to ...',
    long_description = readme,
    author           = 'vikasmulaje',
    author_email     = 'vikasmulaje@gmail.com',
    url              = 'http://wiki',
    packages         = ['opencv'],
    install_requires = ['chrisapp'],
    test_suite       = 'nose.collector',
    tests_require    = ['nose'],
    license          = 'MIT',
    zip_safe         = False,
    python_requires  = '>=3.6',
    entry_points     = {
        'console_scripts': [
            'opencv = opencv.__main__:main'
            ]
        }
)
