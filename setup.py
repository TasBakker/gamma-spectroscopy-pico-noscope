import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gamma-spectroscopy",
    version="0.9",
    author="David Fokkema",
    author_email="davidfokkema@icloud.com",
    description="A GUI for gamma spectroscopy using a PicoScope",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/davidfokkema/gamma-spectroscopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Physics",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
)