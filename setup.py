import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sneruz", # Replace with your own username
    version="0.0.1",
    author="Zach Lefin",
    author_email="zachlefin@gmail.com",
    description="A logic library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Sn00pbom/sneruz",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
