from setuptools import setup, find_packages


setup(
    name='sqlalchemydatabase',
    version='1.0',
    description='Abstraction classes for SQLAlchemy connections.',
    author='Blair Craft',
    author_email='blair@blaircraft.net',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'SQLAlchemy',
    ],
)
