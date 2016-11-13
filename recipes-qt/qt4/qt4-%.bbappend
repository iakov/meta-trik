#QT_EMBEDDED_EXTRA_FLAGS_prepend = " -nomake demos -nomake examples "
QT_DISTRO_FLAGS  = " -no-accessibility -no-sm -stl -plugin-sql-sqlite\
    -plugin-sql-sqlite2 -system-sqlite -system-zlib -system-libpng -no-libtiff\
    -system-libjpeg -no-gtkstyle -no-glib \
    -no-pch -qpa -continue -optimized-qmake -nomake docs -nomake demos -nomake examples"
