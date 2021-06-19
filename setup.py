from setuptools import setup, find_packages

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="pytorch_vision_utils",
    version="0.2.0",
    author="Nicole Gu",
    author_email="nicoleguob@gmail.com",
    description="PyTorch training and data visualization utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nclgbd/PyTorch-Utilities",
    packages=find_packages(include=["custom_models","pytorch_vision_utils",]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)