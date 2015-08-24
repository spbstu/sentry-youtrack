#!/usr/bin/env python
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from sentry_youtrack import VERSION
import os
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test_settings')


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='sentry-youtrack',
    version=VERSION,
    author='Adam Bogdal',
    author_email='adam@bogdal.pl',
    url='http://github.com/bogdal/sentry-youtrack',
    description='A Sentry extension which integrates with YouTrack',
    long_description=open('README.rst').read(),
    license='BSD',
    packages=find_packages(),
    install_requires=[
       'sentry>=6.1.0',
    ],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'sentry.apps': [
            'sentry_youtrack = sentry_youtrack',
        ],
        'sentry.plugins': [
            'sentry_youtrack = sentry_youtrack.plugin:YouTrackPlugin'
        ],
    },
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
    ],
    cmdclass={
        'test': PyTest
    },
    tests_require=[
        'mock==1.3.0',
        'pytest',
    ]
)
