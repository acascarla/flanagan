from setuptools import setup
from setuptools import find_packages

__version__ = '0.0.1'

setup(
    name='calidae-flanagan',
    version=__version__,
    long_description='Light App Made with Love by Calidae',
    packages=find_packages(),
    package_data={
        '': [
            'flanagan/views/*',
            '*.js',
            'flanagan/templates/*.html',
        ],
    },
    include_package_data=True,
    install_requires=[
        'Flask',
        'Flask-WTF',
        'python-dotenv',
    ],
)
