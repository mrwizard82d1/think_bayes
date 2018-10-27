# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='think_bayes',
    version='0.1.0',
    description='Code from the book _Think Bayes_',
    long_description=readme,
    author='Larry Jones',
    author_email='winnihilo1b59@gmail.com',
    url='https://github.com/mrwizard82d1/think_bayes',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

