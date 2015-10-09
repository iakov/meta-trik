DECRIPTION = "Runtime for TRIK controller"
LICENSE = "Apache-2.0"
LIC_FILES_CHKSUM = "file://LICENSE;md5=175792518e4ac015ab6696d16c4f607e"
RDEPENDS_${PN} = "locale-default espeak alsa-utils"
RRECOMMENDS_${PN} = "vlc"

inherit qt4e

BRANCH  = "master"
SRCREV	= "${AUTOREV}"
SRC_URI = "git://github.com/trikset/trikRuntime.git;branch=${BRANCH} \
	  file://trikGui.sh \
	  file://qws_display.sh"

S = "${WORKDIR}/git"

do_compile(){
        export CROSS_COMPILE="${TARGET_PREFIX}"
        oe_runmake
}

do_install() {
        oe_runmake INSTALL_ROOT=${D}/ install
}
FILES_${PN} += "/usr/share/"
pkg_postinst_${PN} () {
        killall trikGui || true
        sleep 3
        killall -9 trikGui 2> /dev/null || true
}

