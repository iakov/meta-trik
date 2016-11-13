SUMMARY = "Python Qt4 Bindings"
#AUTHOR = "Phil Thomson @ riverbank.co.uk"
#HOMEPAGE = "http://riverbankcomputing.co.uk"
#SECTION = "devel/python"
LICENSE = "GPLv2 & GPLv3 & GPL_EXCEPTION"
PARALLEL_MAKE = ""

inherit qmake2 pythonnative python-dir

SRCREV="${AUTOREV}"
SRCDIR="pyqt4e-src"
SRC_URI="hg://bitbucket.org/dboddie/pyqt4-for-embedded-linux;module=${SRCDIR}"
