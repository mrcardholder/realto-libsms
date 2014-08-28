import os
from setuptools import setup

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='realto-libsms',
    version='0.1',
    packages=['libsms', 'libsms.backends'],
    include_package_data=True,
    url='http://github.com/mrcardholder/realto-libsms',
    license='BSD License',
    description='Realto assessment.',
    long_description=open('README.rst').read(),
    author='Eshengazin Kuat',
    author_email='eskuat@gmail.com',
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ]
)
