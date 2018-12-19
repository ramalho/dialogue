import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dialogue_tester",
    version="1.0b",
    author="Luciano Ramalho",
    description="Dialogue class for testing REPLs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ramalho/dialogue",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
)

