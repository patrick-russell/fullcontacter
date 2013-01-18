from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='fullcontacter',
      version='0.2',
      description="Library for interacting with Fullcontact's APIs.",
      long_description=readme(),
      classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='contact information fullcontact',
      url='http://github.com/patrick-russell/fullcontacter',
      author='Patrick Russell',
      author_email='prussell@gmail.com',
      license='MIT',
      packages=['fullcontacter'],
      zip_safe=False)
