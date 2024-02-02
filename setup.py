from setuptools import setup, find_packages
import os
import codecs

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    LON_DESCRIPTION = "\n" + fh.read()

VERSION = "0.0.1"
DESCRIPTION = "dataloom stands as a bespoke Object-Relational Mapping (ORM) solution meticulously crafted to empower Python developers in efficiently managing diverse databases. Unlike conventional ORMs, Dataloom has been built from the ground up, providing native support for SQLite3, PostgreSQL, and MySQL. Navigate effortlessly between database engines while enjoying a tailored and performant ORM experience."
# setting up
setup(
    name="dataloom",
    version=VERSION,
    author="Crispen Gari",
    author_email="<crispengari@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LON_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        "mysql-connector-python==8.3.0",
        "psycopg2==2.9.9",
        "typing_extensions==4.9.0",
    ],
    keywords=["ORM", "database", "data management", "SQLAlchemy"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.12",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
)
