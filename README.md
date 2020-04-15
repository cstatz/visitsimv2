===
 visitsimv2 README
===

Introduction
===
visitsimv2 wraps VisIt's simv2 insitu library based on the included SWIG wrapper for Python 2 and 3.
It can be installed using Pythons distutils/setuptools.

Installation
===
In order to install this package the path to VisIt's "visit" executable needs to be set, otherwise an OSError is thrown. 

Usage
===
In your limsim(V2) instrumented simulation:
Change the import statement to use visitsimv2 instead of simV2
