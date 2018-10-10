import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="addlicense",
    version="0.0.2",
    author="Hossein Ghodse",
    author_email="hossein.ghodse@gmail.com",
    description="addlicense automatically inserts a specified license file or copyright message at the top of one or more source code files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hossg/addlicense",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['addlicense=addlicense.addlicense:main'],
    }
)