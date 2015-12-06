from setuptools import setup

setup(name='dbConnect',
      version='1.3',
      description='MySQL for Humans',
      keywords='dbConnect mysql simple easy, light connection module',
      url='https://github.com/mastizada/dbConnect',
      author='Emin Mastizada',
      author_email='emin@linux.com',
      license='MPLv2',
      packages=['dbConnect'],
      install_requires=[
          'mysql-connector-python', 'setuptools',
      ],
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Environment :: Plugins',
      ],
      scripts=['dbConnect/dbConnect.py'],
      zip_safe=False)
