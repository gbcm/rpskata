from setuptools import setup

setup(
    name='rpscli',
    version='0.1.0',
    packages=['RPS'],
    entry_points={
        'console_scripts': [
            'rpscli = RPS.__main__:main'
        ]
    })
