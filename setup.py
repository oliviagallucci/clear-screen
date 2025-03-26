from setuptools import setup, find_packages

setup(
    name='clear_screen',
    version='0.1',
    packages=find_packages(),
    description='A module to detect the host OS and clear the screen',
    author='Olivia Gallucci',
    author_email='olivia@oliviagallucci.com',
    url='https://github.com/oliviagallucci/clear-screen',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6'
)

