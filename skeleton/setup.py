#!/usr/bin/env python
# encoding: utf-8

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'zzm',
    'url': 'http://www.google.com',
    'download_url': 'http://www.google.com',
    'author_email': 'zhaozhiming003@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'], 'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
