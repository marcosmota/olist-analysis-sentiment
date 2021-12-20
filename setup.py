from setuptools import setup, find_packages

def requirements_from_pip(filename='requirements.txt'):
    with open(filename, 'r') as pip:
        return [l.strip() for l in pip if not l.startswith('#') and l.strip()]

core_deps = requirements_from_pip()

setup(
    name='source',
    version='1.0.0',
    packages=find_packages(include=['source', 'source.*']),
)