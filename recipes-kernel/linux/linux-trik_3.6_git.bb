SECTION = "Kernel"
DESCRIPTION = "Linux Kernel for TRIK board"
LICENSE = "GPLv2"
KERNEL_IMAGETYPE = "uImage"
KERNEL_VERSION ="3.6.7"

PR = "r4"

inherit kernel

KERNEL_MODULE_AUTOLOAD += "jex_epwm"
KERNEL_MODULE_AUTOLOAD += "jcx_pwm"

MULTI_CONFIG_BASE_SUFFIX = ""
SRCREV = "${AUTOREV}"
BRANCH = "trik-linux-3.6.7-release-2014-12-19"
SRC_URI = "git://github.com/trikset/trik-linux.git;branch=${BRANCH} \
	   file://defconfig"

S = "${WORKDIR}/git"

LIC_FILES_CHKSUM="file://COPYING;beginline=1;endline=355;md5=bad9197b13faffd10dfc69bd78fd072e"

