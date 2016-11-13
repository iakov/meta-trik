env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/opt/toolchains/greenphone/gcc-4.1.1-glibc-2.3.6/arm-linux",
    "NATIVE_TOOLS": "/opt/toolchains/greenphone/i386",
    "TARGET_PLATFORM": "arm-linux",
    "TARGET_PLATFORM_CC": "arm-linux-gcc",
    "TARGET_PLATFORM_CXX": "arm-linux-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-linux-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-g++",
    "TARGETDIR": "/mnt/sd/Qtopia",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

# Full ARM build:
qt_options = ["-opensource",
              "-release",
              "-xplatform qws/" + env["TARGET_PLATFORM_SPEC"],
              "-embedded arm",
              "-no-qvfb",
              "-depths 16,32",
              "-qt-libjpeg",
              "-qt-libmng",
              "-qt-libpng",
              "-qt-zlib",
              "-qt-mouse-linuxtp",
              "-no-accessibility",
              "-no-qt3support"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
