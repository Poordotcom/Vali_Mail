import setuptools
from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='valimail',
    version='0.1.5',
    description='A library for advanced email verification.',
    author='Adel Faisal',
    author_email='Tomclans002@email.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Poordotcom/Vali_Mail',
    package_dir={"":"src"},
    packages=setuptools.find_packages("src"),
    install_requires=[
        "requests",
        "disposable-email-domains",
        "beautifulsoup4",
        "python-whois",
        "sockets"

    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
