from setuptools import find_packages, setup

# fake to satisfy mypy
__version__ = "0.0.0"
exec(open("HVACAgent/version.py").read())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ElectroBot",
    version=__version__,
    description="Collection of MD tools for use with language models",
    author="Jorge Medina",
    author_email="jmedina9@ur.rochester.edu",
    license="MIT",
    packages=find_packages(),
    install_requires=["beautifulsoup4",
    "langchain",
    "rmrkl",
    "nbformat",
    "requests",
    "python-dotenv",
    "matplotlib",
    "rdkit",
    "openai",
    "pdfminer.six",
    "pypdf",
    "pdfdataextractor @ git+https://github.com/Jgmedina95/PDFDataExtractor.git@textabstract",
    "tiktoken",
    "wikipedia",
],
    test_suite="tests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)