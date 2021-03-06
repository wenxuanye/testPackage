import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="test_package_wenxuanye",
  version="0.0.3",
  author="WENXUAN YE",
  author_email="lehighwenxuanye@gmail.com",
  description="A small example package",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/wenxuanye/testPackage.git",
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
  package_dir={"": "src"},
  packages = setuptools.find_packages(where="src"),
  python_requires=">=3.6",
)
