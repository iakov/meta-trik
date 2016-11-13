# This is a template settings file.

env = {
    "HOST_PLATFORM": "",
    # The architecture of the platform used to build the tools for the target
    # platform: i386, arm, mips, ...
    
    "TARGET_TOOLS": "",
    # Contains a path to a directory containing executables and libraries used
    # to generate target platform binaries. The path should contain bin and lib
    # directories containing cross-compilation tools and associated libraries
    # respectively.
    
    "NATIVE_TOOLS": "",
    # Contains a path to a directory containing native tools used to configure
    # the build process for the software for the target platform.
    
    "TARGET_PLATFORM": "",
    # GCC-style platform description: arm-linux, ...
    
    "TARGET_PLATFORM_CC": "",
    # C compiler to use for target platform binaries: arm-linux-gcc, ...
    
    "TARGET_PLATFORM_CXX": "",
    # C++ compiler to use for target platform binaries: arm-linux-g++, ...
    
    "TARGET_PLATFORM_LDSHARED": "",
    # linker to use for target platform binaries: arm-linux-ld, ...
    
    "TARGET_PLATFORM_SPEC": "",
    # qmake specification for the target platform: linux-arm-g++, ...
    
    "TARGETDIR": "",
    # Contains a path to a directory where the software will be installed.
    # This will usually be the same as the path used on the target device.
    
    "HOST_COMPILERS": "1",
    # Number of compilers to use when compiling native tools.
    
    "TARGET_COMPILERS": "1"
    # Number of compilers to use when compiling software for the target
    # platform.
    }

# Options used to configure Qt for the target platform.
qt_options = ["-opensource",
              "-release",
              "-xplatform qws/" + env["TARGET_PLATFORM_SPEC"],
              "-embedded arm",  # arm, i386, mips, ...
              "-no-qvfb",       # Include this option for target builds.
              "-depths 16,32",  # Pixel depths supported by the target device.
              "-qt-libjpeg",
              "-qt-libmng",
              "-qt-libpng",
              "-qt-zlib",
              "-qt-mouse-linuxtp",
              "-no-accessibility",
              "-no-qt3support"]

# Profile to use for the Qt libraries: None (full build), "large", "medium",
# "small", "minimal".
qt_configuration_profile = None

# Extra preprocessor definitions used to fine-tune the Qt configuration.
extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY", "QT_NO_CURSOR", "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER", "QT_QWS_SCREEN_COORDINATES"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

# PyQt-specific features to exclude from the build.
extra_pyqt_configuration = [
    "PyQt_qreal_double",    # Disable high-precision floating point support.
    "PyQt_OpenSSL"          # Disable OpenSSL support.
    ]
