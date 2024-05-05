import setuptools


with open('requirements.txt') as f:
    requirements = f.read().splitlines()

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bluestacksadb",
    version="1.0",
    author="Bing Syuan Wang",
    author_email="",
    description="A Python module to interact with BlueStacks using ADB",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SyXuan/BlueStacksADB",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9, <3.12',
    license='MIT',
)
