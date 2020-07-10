import os
from setuptools import setup


def ingest_file(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().splitlines()


requirements = ingest_file('requirements.txt')

setup(
    name="pytest-test",
    packages=[
        "foo",
    ],
    version="0.0.1",
    description="Testing an issue with pytest 6.0.0rc1",
    author="Sam Hart",
    author_email="hartsn@gmail.com",
    url="https://github.com/criswell/pytest-tests",
    install_requires=requirements,
    setup_requires=['pytest-runner'],
    tests_require=requirements,
)
