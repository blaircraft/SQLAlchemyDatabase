from setuptools import setup, find_packages


setup(
    name='sqlalchemydatabase',
    version='1.01',
    description='Abstraction classes for SQLAlchemy connections.',
    author='Blair Craft',
    author_email='blair@blaircraft.net',
    url='https://github.com/blaircraft/SQLAlchemyDatabase',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'SQLAlchemy',
    ],
)
