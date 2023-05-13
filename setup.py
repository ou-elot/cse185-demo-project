from setuptools import setup, find_packages
  
setup(
    name='mypileup',
    version='0.0',
    description='CSE185 Demo Project',
    author='Melissa Gymrek',
    author_email='mgymrek@ucsd.edu',
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mypileup=src.mypileup:main"
        ],
    },
)