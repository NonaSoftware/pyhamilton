from setuptools import setup, find_packages

long_description = open('README.md', encoding='utf-8').read()

setup(
    name='pyhamilton',
    version='1.235',
    packages=find_packages(exclude="tools"),
    license='MIT',
    description='Python for Hamilton liquid handling robots',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=['win32gui', 'win32con'],
    package_data={'pyhamilton': ['star-oem/*', 'star-oem/VENUS_Method/*']},
    url='https://github.com/dgretton/pyhamilton.git',
    author='Dana Gretton',
    author_email='dgretton@mit.edu',
)
