# setup.py

version = '0.0'

import sys
from setuptools import setup, find_packages

with open("README.md") as f:
    long_description = f.read()
    
with open("requirements.txt") as f:
    requirements = list(filter(None,f.read().split('\n')))

setup(
    name = 'my-package',
    description = 'A Python package',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    version = version,
    url = '',
    author = '',
    author_email = '',
    license = 'http://www.opensource.org/licenses/bsd-license.php',
    packages = find_packages(exclude=['tests']),
    package_data = {'my_package': ['data/my_data.json']},
    install_requires = requirements,
    python_requires = '>=3.10,<=3.14',
    entry_points = {
        'console_scripts': [
            'my-command=my_package.scripts.my_script:run',
        ]
    }
)