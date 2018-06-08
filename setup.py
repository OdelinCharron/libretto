# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="libretto",
    version="0.0.1",
    author="Odelin Charron",
    author_email="audy322@hotmail.fr",
    description="Log reader",
    keywords="libretto",
    url="",
    download_url='',
    packages=find_packages(exclude=('tests', 'docs')),
    scripts=['libretto'],
    long_description=read('README.md'),
    license=read('LICENSE')
)