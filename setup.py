"""Модуль для сборки meeseeks-happy-birthder. """

from setuptools import setup, find_packages


with open('requirements.txt', encoding='utf8') as outfile:
    REQUIREMENTS_LIST = outfile.read().splitlines()


setup(
    name='meeseeks-happy-birthder',
    version='1.0.0',
    packages=find_packages(),
    install_requires=REQUIREMENTS_LIST,
)
