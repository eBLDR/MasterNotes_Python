# Package information
# Should contain a single call to setup()

import setuptools


def readme():
    with open('README.md') as f:
        return f.read()


setuptools.setup(
    name="example_pkg",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    log_description=readme(),  # Will be picked as 'homepage' for the project
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/example-project",
    packages=setuptools.find_packages(),
    install_requires=['package_dependecy'],  # List here all the depencies used in the package, if any
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
