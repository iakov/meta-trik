env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/usr/local/src/Software/Gumstix/overo-oe/tmp/cross/armv7a",
    "NATIVE_TOOLS": "/opt/toolchains/greenphone/i386",
    "TARGET_PLATFORM": "arm-linux",
    "TARGET_PLATFORM_CC": "arm-linux-gcc",
    "TARGET_PLATFORM_CXX": "arm-linux-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-linux-g++",
    "TARGET_PLATFORM_SPEC": "linux-armv6-g++",
    "TARGETDIR": "/mnt/card/Qt-Embedded",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

# Full ARM build:
qt_options = ["-opensource",
              "-release",
              "-xplatform qws/" + env["TARGET_PLATFORM_SPEC"],
              "-embedded armv6",
              "-little-endian",
              "-no-qvfb",
              "-depths 15,16,18,24,32",
              "-qt-libjpeg",
              "-qt-libmng",
              "-qt-libpng",
              "-qt-zlib",
              "-qt-mouse-tslib", # -qt-mouse-linuxtp
              "-no-accessibility",
              "-no-phonon",
              "-no-qt3support",
              "-no-scripttools",
              "-no-webkit"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

# Features we exclude from the build.
extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
