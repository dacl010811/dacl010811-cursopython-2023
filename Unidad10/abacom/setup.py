# setup.py
from setuptools import setup, find_packages

setup(
    name='abacom',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        # Lista de dependencias si las tienes
    ],
    entry_points={
        'console_scripts': [
            # Puedes especificar scripts ejecutables aquí
        ],
    },
    author='Darwin Calle',
    author_email='dacl010811@gmail.com',
    description='Una descripción corta de tu paquete',
    long_description=open('README.md').read(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
