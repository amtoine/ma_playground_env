import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="playground",
    version="0.0.1",
    author="Antoine Stevan",
    # author_email="author@example.com",
    description="The modified environment of the IMAGINE research paper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/a2n-s/ma_playground",
    project_urls={
        "Bug Tracker": "https://github.com/a2n-s/ma_playground/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: GNU",
        "Operating System :: Arch linux",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)