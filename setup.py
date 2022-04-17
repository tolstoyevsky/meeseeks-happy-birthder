"""Модуль для сборки meeseeks-happy-birthder. """

from setuptools import setup, find_packages

setup(
    name='meeseeks-happy-birthder',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.1',
        'alembic==1.7.5',
        'APScheduler==3.8.1',
        'configparser==5.2.0',
        'gino==1.0.1',
        'python-dotenv==0.19.1',
        'psycopg2-binary==2.9.3',
        'tabulate==0.8.9',
    ],
)
