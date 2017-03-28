#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'pygatt[GATTTOOL]>=3.0.0,<4.0'
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='blebutton',
    version='0.1.0',
    description="BLE Driver for v.alert button.",
    long_description=readme + '\n\n' + history,
    author="Ilya Sukhanov",
    author_email='ilya@sukhanov.net',
    url='https://github.com/IlyaSukhanov/blebutton',
    packages=[
        'blebutton',
    ],
    package_dir={'blebutton':
                 'blebutton'},
    entry_points={
        'console_scripts': [
            'blebutton=blebutton.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='blebutton',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
