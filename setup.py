#!/usr/bin/env python
from os.path import dirname, join
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import threadsafe_tkinter


try:
    curr_dir = dirname(__file__)
    try:
        long_desc = open(join(curr_dir, "readme.rst")).read()
    except Exception:
        long_desc = open(join(curr_dir, "readme.md")).read()
except Exception:
    long_desc = 'Could not read long description from readme.'

setup(
    name='threadsafe_tkinter',
    description='A thread-safe version of Tkinter for Python3.',
    long_description=long_desc,
    version='%s.%s.%s' % threadsafe_tkinter.__version__,
    author='Devin Bobadilla',
    author_email='MosesBobadilla@gmail.com',
    license='MIT',
    packages=[
        'threadsafe_tkinter',
        ],
    package_data={
        '': ['*.TXT', '*.md', '*.rst'],
        },
    platforms=["POSIX", "Windows"],
    keywords="tkinter, thread, multithread, threadsafe",
    provides=['threadsafe_tkinter'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        ],
    zip_safe=True,
    )
