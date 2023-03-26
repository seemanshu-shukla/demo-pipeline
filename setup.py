from setuptools import setup, find_packages

setup(name="census-income-packaged",
      version="0.0.1",
      author="Seemanshu Shukla",
      author_email="seemanshu.shukla11@gmail.com",
      packages=find_packages(),
      install_requires=["pandas","numpy","flask"]
      )