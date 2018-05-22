from setuptools import setup

setup(
    name='stripe_sdk',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='1.0',

    description='The STRIPE SDK is a python client for the STRIPE PAYMENT GATEWAY.',

    # The project's main homepage.
    url='',

    # Author details
    author='Abdul Jabbar',
    author_email='m.jabbar.bcs@gmail.com',
    install_requires=[
        'stripe',
    ],
    packages=['stripe_sdk']
)
