import os
import subprocess

from setuptools import setup, find_packages

data_files = []

setup(
    name='iot',
    version='1.0',
    description='Sawtooth IoT DApp Example',
    author='Garrocho',
    packages=find_packages(),
    install_requires=[
        'aiohttp',
        'colorlog',
        'protobuf',
        'sawtooth-sdk',
        'sawtooth-signing',
        'PyYAML',
    ],
    data_files=data_files,
    entry_points={
        'console_scripts': [
            'iot = iot_dapp:main',
        ]
    })