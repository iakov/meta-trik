env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/opt/toolchains/arm-unknown-linux-gnueabi",
    "NATIVE_TOOLS": "/tmp/i386-toolchain",
    "TARGET_PLATFORM": "arm-unknown-linux-gnueabi",
    "TARGET_PLATFORM_CC": "arm-unknown-linux-gnueabi-gcc",
    "TARGET_PLATFORM_CXX": "arm-unknown-linux-gnueabi-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-unknown-linux-gnueabi-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-unknown-gnueabi-g++",
    "TARGETDIR": "/mnt/sd/Qtopia-medium-4.7-ctng",
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

qt_configuration_profile = "medium"

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = [
    "PyQt_qreal_double", "PyQt_OpenSSL"
    ]
