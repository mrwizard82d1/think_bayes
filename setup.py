
from distutils.core import setup

setup(
    name='think_bayes',
    version='0.1.0',
    author='Lawrence Allan Jones',
    author_email='mrwizard82d1@earthlink.net',
    packages=['think_bayes', 'think_bayes.test'],
    scripts=['bin/think_bayes.py',],
    url='http://pypi.python.org/pypi/think_bayes/',
    license='LICENSE.txt',
    description='Useful think_bayes stuff.',
    long_description=open('README.txt').read(),
    install_requires=[],
    )
