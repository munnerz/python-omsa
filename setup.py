import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='python-omsa',
    version='0.0.1',
    packages=['omsa'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A python module for interfacing with Dell OMSA',
    long_description=README,
    url='https://gitlab.com/munnerz/python-omsa',
    author='James Munnelly',
    author_email='james@munnelly.eu',
    classifiers=[
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License', # example license
        'Operating System :: POSIX :: Linux'
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
    ],
    install_requires=[
    ],
)