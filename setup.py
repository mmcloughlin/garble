from setuptools import setup, find_packages
import re

pkg_init_file = open('garble/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

setup(name='garble',
      version=metadata['version'],
      description='Randomize your data',
      url='https://github.com/mmcloughlin/garble',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      packages=find_packages(),
      entry_points={
          'console_scripts': [
              'garble = garble.__main__:main',
              ]
          },
      install_requires=[
          'iso8601',
          'pytz',
          ],
      test_suite='nose.collector',
      tests_require=['nose'],
      )
