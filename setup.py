from setuptools import setup, find_packages


setup(
    name = 'AmyModelPackage',
    versionversion = '0.0.1',
    description = 'Accuracy of Models',
    Long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = '',
    author = 'Amy Nuno',
    author_email = 'amynuno98@gmail.com',
    License = 'MIT',
    packages = find_packages(),
    install_requires = [''],

    keywords=['python', 'Forecast Accuracy'],
    classifiers = [
    'Development Status :: 5 - Production/stable',
    'Intended Audience :: Education',
    'Operating System :: MacOS :: MacOS X',
    'Licence :: OSI Approved :: MIT License',
    "Programming Language :: Python :: 3"
    ]

)
