from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()
with open('requirements.txt','r') as fr:
    requires = fr.read().split('\n')

setup(
    name='ValiMail',
    version='0.1.0',
    description='A library for advanced email verification.',
    author='Adel Faisal',
    author_email='Tomclans002@email.com',
    packages=find_packages(),
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
