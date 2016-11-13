env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/usr",
    "NATIVE_TOOLS": "/build/tools",
    "TARGET_PLATFORM": "arm-ip-linux-gnueabi",
    "TARGET_PLATFORM_CC": "arm-ip-linux-gnueabi-gcc",
    "TARGET_PLATFORM_CXX": "arm-ip-linux-gnueabi-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-ip-linux-gnueabi-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-ip-gnueabi-g++",
    "TARGETDIR": "/usr/local",
    #"DESTDIR": "/build/rootfs/",
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
              "-qt-mouse-tslib", # -qt-mouse-linuxtp
              "-no-accessibility",
              "-no-qt3support",
              "-no-dbus",
              "-no-scripttools",
              "-no-webkit",
              "-no-phonon",
              "-ldl"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
