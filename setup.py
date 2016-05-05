#!/usr/bin/env python

from setuptools import setup, find_packages
LONG_DESCRIPTION = open('README.rst').read()

setup(
    name='Eve-Swagger',
    version='0.1.0',
    url='https://github.com/cliixtech/eve-swagger',
    author='Nicola Iarocci',
    description='Generates documentation for Eve APIs using Swagger',
    long_description=LONG_DESCRIPTION,
    license=open('LICENSE').read(),
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Eve>=0.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
