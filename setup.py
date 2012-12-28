#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name="br_documents",
    version="0.0.1-p1",
    author="Felipe 'chronos' Prenholato",
    author_email="philipe.rp@gmail.com",
    maintainer="Felipe 'chronos' Prenholato",
    maintainer_email="philipe.rp@gmail.com",
    url="http://github.com/chronossc/br_documents",
    packages = find_packages(),
    description="Provide objects for brazilian documents like CPF and others, with validation",
    long_description="Provide objects for brazilian documents like CPF and others, with validation",
    classifiers=[
        "Development Status :: 4 - Beta",
        #"Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
