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
              "-depths 16",
              "-qt-libjpeg",
              "-qt-libmng",
              "-qt-libpng",
              "-qt-zlib",
              "-qt-mouse-linuxinput",
              "-plugin-gfx-transformed",
              "-no-accessibility",
              "-no-qt3support",
              "-no-script",
              "-no-scripttools",
              "-no-webkit",
              "-no-declarative",
              "-ldl"]

qt_configuration_profile = None

extra_qt_configuration = [
    "QT_NO_ACCESSIBILITY",
    "QT_NO_CURSOR",
    "QT_NO_QWS_CURSOR",
    "QT_NO_SESSIONMANAGER",
    "QT_QWS_SCREEN_COORDINATES",
    "QT_NO_RAWFONT",
    "QT_NO_COLORDIALOG",
    "QT_NO_EFFECTS",
    "QT_NO_ERRORMESSAGE",
    "QT_NO_FILEDIALOG",
    "QT_NO_FONTDIALOG",
    "QT_NO_GRAPHICSVIEW",
    "QT_NO_INPUTDIALOG",
    "QT_NO_ITEMVIEWS",
    "QT_NO_LISTVIEW",
    "QT_NO_MAINWINDOW",
    "QT_NO_MDIAREA",
    "QT_NO_PRINTDIALOG",
    "QT_NO_PRINTPREVIEWDIALOG",
    "QT_NO_PRINTPREVIEWWIDGET",
    "QT_NO_PROGRESSDIALOG",
    "QT_NO_PROXYMODEL",
    "QT_NO_SOUND",
    "QT_NO_STL",
    "QT_NO_STYLE_STYLESHEET",
    "QT_NO_TABDIALOG",
    "QT_NO_TABLETEVENT",
    "QT_NO_TABLEVIEW",
    "QT_NO_TEXTODFWRITER",
    "QT_NO_TOOLBAR",
    "QT_NO_TOOLBOX",
    "QT_NO_TREEVIEW",
    "QT_NO_WHEELEVENT",
    "QT_NO_WIZARD",
    "QT_NO_WORKSPACE"
    ]

sip_target_platform = env["TARGET_PLATFORM_SPEC"]

extra_pyqt_configuration = ["PyQt_OpenSSL"]
