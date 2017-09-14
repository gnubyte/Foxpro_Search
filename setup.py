# ####
# @Author: Patrick Hastings
# @Purpose: Installation of the Application files and packages
#
# ####
from setuptools import setup

setup(
    name='crsserver',
    author="Patrick Hastings",
    author_email='phastings@openmobo.com',
    version='0.1dev',
    packages=['crsserver'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pyodbc',
        'unittest',
        'time',
        'logging'
    ],
)