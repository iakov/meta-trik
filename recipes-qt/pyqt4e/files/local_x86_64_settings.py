env = {
    "HOST_PLATFORM": "x86_64",
    "TARGET_TOOLS": "/opt/PyQt-Embedded",
    "NATIVE_TOOLS": "/opt/PyQt-Embedded-native",
    "TARGET_PLATFORM": "x86_64",
    "TARGET_PLATFORM_CC": "gcc",
    "TARGET_PLATFORM_CXX": "g++",
    "TARGET_PLATFORM_LDSHARED": "g++",
    "TARGET_PLATFORM_SPEC": "linux-x86_64-g++",
    "TARGETDIR": "/opt/PyQt-Embedded",
    "HOST_COMPILERS": "2",
    "TARGET_COMPILERS": "1"
    }

# Full native x86 build with VNC:
qt_options = ["-opensource",
              "-release",
              "-embedded x86_64",
              "-no-qvfb",
              "-depths 8,16,32",
              "-no-qt3support",
              "-dbus",
#              "-no-webkit",
              "-qt-gfx-vnc",
              "-qt-mouse-linuxtp",
              "-no-declarative",
              "-no-multimedia",
              "-no-phonon",
#              "-no-javascript-jit",
              "-no-scripttools"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES",
    "QT_NO_RAWFONT"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = [] # ["PyQt_OpenSSL"]
