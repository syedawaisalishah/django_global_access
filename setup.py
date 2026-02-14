from setuptools import setup, find_packages

setup(
    name='django-global-access',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'Django>=3.2'
    ],
    description='Make your Django app accessible globally',
    author='Syed Awais Ali Shah',
    author_email="syedawaisali.shah@gmail.com",
)
