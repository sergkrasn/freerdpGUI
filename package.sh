#!/bin/sh
# Create folders.
[ -e package ] && rm -r package
mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps
mkdir -p package/usr/share/mime/packages
mkdir -p package/usr/bin

# Copy files (change icon names, add lines for non-scaled icons)
cp -r dist/freerdpgui package/opt/freerdpgui
cp resource/freerdpgui-icon.svg package/usr/share/icons/hicolor/scalable/apps/freerdpgui-icon.svg
cp resource/freerdpgui-mime.xml package/usr/share/mime/packages/freerdpgui-mime.xml
cp resource/FreerdpGUI.desktop package/usr/share/applications
cp resource/freerdpgui package/usr/bin/freerdpgui

# Change permissions
find package/opt/freerdpgui -type f -exec chmod 644 -- {} +
find package/opt/freerdpgui -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/freerdpgui/freerdpgui
chmod +x package/usr/bin/freerdpgui