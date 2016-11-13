env = {
    "HOST_PLATFORM": "i386",
    "TARGET_TOOLS": "/opt/toolchains/greenphone/gcc-4.1.1-glibc-2.3.6/arm-linux",
    "NATIVE_TOOLS": "/opt/toolchains/greenphone/i386",
    "TARGET_PLATFORM": "arm-linux",
    "TARGET_PLATFORM_CC": "arm-linux-gcc",
    "TARGET_PLATFORM_CXX": "arm-linux-g++",
    "TARGET_PLATFORM_LDSHARED": "arm-linux-g++",
    "TARGET_PLATFORM_SPEC": "linux-arm-g++",
    "TARGETDIR": "/mnt/sd/Qtopia-minimal",
    "HOST_COMPILERS": "1",
    "TARGET_COMPILERS": "1"
    }

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
              "-no-dbus",
              "-no-scripttools",
              "-no-webkit",
              "-no-multimedia",
              "-no-phonon",
              "-no-declarative"]

qt_configuration_profile = "minimal"

extra_qt_configuration = []

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_qreal_double", "PyQt_OpenSSL"]
