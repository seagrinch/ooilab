from setuptools import setup

setup(name='ooilab',
      version='0.2',
      description='Functions to facilitate data requests from the OOI Data Portal',
      url='https://github.com/seagrinch/ooilab',
      author='Sage Lichtenwalner',
      author_email='sage@marine.rutgers.edu',
      license='MIT',
      packages=['ooilab'],
      keywords=['oceanography', 'ooi'],
      install_requires=['numpy','xarray','netcdf4'],
      zip_safe=False)
