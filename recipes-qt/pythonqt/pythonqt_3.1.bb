LICENSE = "LGPLv2.1"
LIC_FILES_CHKSUM = "file://COPYING;md5=fbc093901857fcd118f065f900982c24"

BBCLASSEXTEND += "native"
SRC_URI[sha256sum] = "2fcb07f6e3e63bc5299ff968b64ca35e05c3f599fe0965285ae92b2317f0f940"
inherit qt4e
SRC_URI = "http://downloads.sourceforge.net/project/pythonqt/pythonqt/PythonQt-3.1/PythonQt3.1.zip"
S = "${WORKDIR}/PythonQt${PV}"

DEPENDS_class-target = "pythonqt-native"
DEPENDS_class-native = ""

DEPENDS += "python"
QT_DIR_NAME_class-native = "qt4"
#QT_DIRNAME_class-native_append = "qt4"
