from setuptools import setup
from setuptools import find_packages

REQUIREMENTS = [
    'pandas',
    'sklearn',
    'tqdm',
    'uniseg',
    'jiwer',
    'Jinja2',
]

setup(
    name='fre',
    version='1.1',
    description='',
    author='Laurence Dyer',
    author_email='ljdyer@gmail.com',
    url='https://github.com/ljdyer/Feature-Restoration-Evaluator',
    packages=['fre'],
    install_requires=REQUIREMENTS
)
