import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="easy-tic-toc",
    version="0.0.1",
    author="Shakib Rahimi",
    author_email="shakibrahimy@gmail.com",
    description='The easiest way to calculate the execution time of any part of the program in Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shakib-rahimi/tictoc",
    packages=setuptools.find_packages(),
    py_modules = ["tictoc"],
    package_dir = {'':'src'},   
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)