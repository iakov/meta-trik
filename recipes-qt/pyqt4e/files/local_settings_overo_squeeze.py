env = {
    "HOST_PLATFORM": "amd64",
    "TARGET_TOOLS": "/usr",
    "NATIVE_TOOLS": "/home/build/tools",
    "TARGET_ARCH": "armel",
    "TARGET_PLATFORM": "arm-linux-gnueabi",
    "TARGET_PLATFORM_CC": "arm-linux-gnueabi-gcc",
    "TARGET_PLATFORM_CXX": "arm-linux-gnueabi-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-linux-gnueabi-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-gnueabi-g++",
    "TARGETDIR": "/usr/local/arm-linux-gnueabi",
    #"DESTDIR": "/home/build/rootfs/",
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
              "-qt-mouse-linuxinput",
              "-no-accessibility",
              "-no-qt3support",
              "-no-scripttools",
              "-no-webkit",
              "-no-declarative",
              "-ldl"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES",
    "QT_NO_RAWFONT"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
