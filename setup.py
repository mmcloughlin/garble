from setuptools import setup
import re

pkg_init_file = open('garble/__init__.py').read()
metadata = dict(re.findall("__([a-z]+)__\s*=\s*'([^']+)'", pkg_init_file))

def readme():
    return open('./README.rst').read()

setup(name='garble',
      version=metadata['version'],
      description='Randomize your data',
      long_description=readme(),
      url='https://github.com/mmcloughlin/garble',
      author='Michael McLoughlin',
      author_email='mmcloughlin@gmail.com',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],
      )
