PR="r6"
DESCRIPTION = "TRIK core base v2"
IMAGE_FEATURES += "package-management x11-base"
IMAGE_INSTALL = "packagegroup-base \
		packagegroup-core-boot \
		${ROOTFS_PKGMANAGE_BOOTSTRAP} \
		${CORE_IMAGE_EXTRA_INSTALL} \
		trik-hostname \
		packagegroup-wifi \
		packagegroup-qte-trik \
		packagegroup-core-ssh-dropbear \
		localedef \
		packagegroup-firmware \
		packagegroup-utils \
		packagegroup-multimedia \
		packagegroup-core-tools-debug \
		packagegroup-core-tools-profile\
		udev-extraconf \
		mspbsl \
		rc-local\
		trik-runtime \
		trik-models \
		dsp-modules \
		softap-udhcpd-config \
		trik-network \
		fuse \
		eglibc-utils \
		packagegroup-triksensors \
		distro-feed-configs \
                roslaunch \
"
#		python 
#		python-pip 

#		locale-base-ru-ru 
#		locale-default 


#		mono
#		fsharp

IMAGE_LINGUAS = "en-us ru-ru"

LICENSE = "MIT"

inherit core-image

IMAGE_ROOTFS_SIZE = "1572864"

# remove not needed ipkg informations
#ROOTFS_POSTPROCESS_COMMAND += "remove_packaging_data_files ; "


