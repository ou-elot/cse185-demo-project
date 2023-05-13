from setuptools import setup
  
setup(
    name='mypileup',
    version='0.0',
    description='CSE185 Demo Project',
    author='Melissa Gymrek',
    author_email='mgymrek@ucsd.edu',
    packages=["src"],
    entry_points={
        "console_scripts": [
            "mypileup=src.mypileup:main"
        ],
    },
)