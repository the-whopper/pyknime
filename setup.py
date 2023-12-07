from setuptools import setup,find_packages


setup(
    name='pyknime',
    version='0.0.0.4',
    url='https://github.com/the-whopper/pyknime',
    author='Andrew',
    license="MIT",
    packages=find_packages(),
    install_requires=[
    'boto3',
],
python_requires=">=3.9",
)