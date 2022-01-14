from setuptools import setup
setup(
    name = 'gfm-recurring-cli',
    version = '0.2.0',
    packages = ['gfmRecurring', 'gfmRecurring/model'],
    entry_points = {
        'console_scripts': [
            'gfm-recurring = gfmRecurring.__main__:main'
        ]
    })
