# These and other macros are documented in
# ../droid-configs-device/droid-configs.inc

%define device shieldtablet
%define vendor nvidia

%define vendor_pretty Nvidia
%define device_pretty Shield Tablet

%define dcd_path ./

# Adjust this for your device
%define pixel_ratio 2.0

# We assume most devices will
%define have_modem 1

%include droid-configs-device/droid-configs.inc
