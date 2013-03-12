"""
Flask-Pigeon
------------

Flask extension for Pigeon
"""
from setuptools import setup

setup(name='Flask-Pigeon',
      version='0.1',
      description='Flask messages extension.',
      long_description=__doc__,
      author='reterVision',
      author_email='reterclose@gmail.com',
      url='http://github.com/reterVision/flask-pigeon',
      license='MIT',
      packages=['flaskext'],
      platforms="any",
      zip_safe=True,
      install_requires=[
      'setuptools',
      'Flask>=0.8',
      ],
      classifiers=[
      'Environment :: Web Environment',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
      'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      )
