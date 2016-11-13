env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/opt/freescale/usr/local/gcc-4.1.2-glibc-2.5-nptl-3/arm-none-linux-gnueabi",
    "NATIVE_TOOLS": "/tmp/i386-toolchain",
    "TARGET_PLATFORM": "arm-none-linux-gnueabi",
    "TARGET_PLATFORM_CC": "arm-none-linux-gnueabi-gcc",
    "TARGET_PLATFORM_CXX": "arm-none-linux-gnueabi-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-none-linux-gnueabi-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-none-gnueabi-g++",
    "TARGETDIR": "/opt/qt",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

# Medium ARM build:
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
              "-no-qt3support",
              "-no-scripttools",
              "-no-webkit",
              "-no-declarative"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = [
    "PyQt_qreal_double", "PyQt_OpenSSL"
    ]
