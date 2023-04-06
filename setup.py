#!/usr/bin/env python

import codecs
from os import system, path
import sys

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with codecs.open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = "\n" + f.read()

from pipenv.project import Project
from pipenv.utils.dependencies import convert_deps_to_pip

proj = Project(chdir=False)
pfile = proj.parsed_pipfile
requires = convert_deps_to_pip(pfile['packages'], False)
extras = convert_deps_to_pip(pfile['dev-packages'], False)

about = {}
ver_path = path.join(here, "audio_maffia", "version.py")
with open(ver_path) as f:
    exec(f.read(), about)

if sys.argv[-1] == "publish":
    system("python setup.py sdist bdist_wheel upload")
    sys.exit()

setup(
    name="audio_maffia",
    version=str(about["version"]),
    description="A Maffia-based audio game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Michael Connor Buchan",
    author_email="mikey@blindcomputing.org",
    url="https://github.com/lower-elements/audio-maffia",
    packages=find_packages(),
    entry_points={
        "gui_scripts": [
            "audio-maffia=audio_maffia.__main__:main",
        ]
    },
    package_data={
        "": ["LICENSE"],
    },
    python_requires=f">={proj.required_python_version}",
    zip_safe=True,
    setup_requires=[],
    install_requires=requires,
    extras_require={
        "dev": extras,
                    },
    include_package_data=True,
    license="gpl-3-or-later",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Intended Audience :: End Users/Desktop",
    ],
)
