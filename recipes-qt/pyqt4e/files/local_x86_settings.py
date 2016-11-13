env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/mnt/sd/Qtopia-native",
    "NATIVE_TOOLS": "/mnt/sd/Qtopia-native",
    "TARGET_PLATFORM": "i386",
    "TARGET_PLATFORM_CC": "gcc",
    "TARGET_PLATFORM_CXX": "g++",
    "TARGET_PLATFORM_LDSHARED": "ld",
    "TARGET_PLATFORM_SPEC": "linux-x86-g++",
    "TARGETDIR": "/mnt/sd/Qtopia-native",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

# Full native x86 build with VNC:
qt_options = ["-opensource",
              "-release",
              "-embedded x86",
              "-no-qvfb",
              "-depths 16,32",
              "-no-qt3support",
              "-no-dbus",
              "-qt-gfx-vnc"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_OpenSSL"]
