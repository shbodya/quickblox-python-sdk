#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='QuickBlox',
    version='0.0.3',
    packages=['QuickBlox'],
    description='Quickblox API client',
    author='QuickBlox Tech Team',
    author_email='bogdan.shaparenko@injoit.com',
    url='https://github.com/shbodya/quickblox-python-sdk',
    license='Apache License, Version 2.0',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
    keywords='chat api quickbolox quickblox.com',
    install_requires=[
        'requests',
    ],
)
