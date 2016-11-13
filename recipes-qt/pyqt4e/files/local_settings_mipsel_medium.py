env = {
    "HOST_PLATFORM": "amd64",
    "TARGET_TOOLS": "/usr",
    "NATIVE_TOOLS": "/home/build/tools",
    "TARGET_ARCH": "mipsel",
    "TARGET_PLATFORM": "mipsel-linux-gnu",
    "TARGET_PLATFORM_CC": "mipsel-linux-gnu-gcc",
    "TARGET_PLATFORM_CXX": "mipsel-linux-gnu-g++",
    "TARGET_PLATFORM_LDSHARED": "mipsel-linux-gnu-g++",
    "TARGET_PLATFORM_SPEC": "linux-mipsel-gnu-g++",
    "TARGETDIR": "/usr/local/mipsel-linux-gnu",
    #"DESTDIR": "/home/build/rootfs/",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

# Medium ARM build:
qt_options = ["-opensource",
              "-release",
              "-xplatform qws/" + env["TARGET_PLATFORM_SPEC"],
              "-embedded mips",
              "-little-endian",
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

qt_configuration_profile = "medium"

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES",
    "QT_NO_RAWFONT"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
