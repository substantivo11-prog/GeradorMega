[app]

# (str) Title of your application
title = Gerador Mega-Sena

# (str) Package name
package.name = megasenalinhas

# (str) Package domain (needed for android packaging)
package.domain = org.megasena

# (str) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# comma separated e.g. requirements = python3,kivy
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minapi = 21

# (list) The android archs to build for,, in order of importance.
android.archs = arm64-v8a, armeabi-v7a

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0