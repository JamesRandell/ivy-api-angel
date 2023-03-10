from setuptools import setup, find_packages

requires = [
    'Flask',
    'flask-jsonpify',
    'flask-restx',
    'flask_jwt_extended',
    'pyyaml',
    'Quart',
    'psycopg2',
    'ivyorm'
]

setup(
    name='ivy-api-angel',
    version='0.1',
    description='Ivy Angel REST interface',
    author='James Randell',
    author_email='jamesrandell@me.com',
    keywords='Ivy REST API',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)