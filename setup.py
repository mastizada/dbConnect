from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='dbConnect',
    version='1.5.0',
    description='MySQL for Humans',
    long_description=readme,
    keywords='dbConnect mysql simple easy, light connection module',
    url='https://github.com/mastizada/dbConnect',
    author='Emin Mastizada',
    author_email='emin@linux.com',
    license='MPLv2',
    packages=['dbConnect'],
    install_requires=[
        'setuptools',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Database :: Front-Ends',
        'Environment :: Plugins',
    ],
    scripts=['dbConnect/dbConnect.py'],
    zip_safe=False
)
