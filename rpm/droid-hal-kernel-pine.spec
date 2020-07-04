# Thanks to Neochapay: https://build.merproject.org/package/show/home:neochapay:mer:release:2018.05:hardware:pine64/kernel-dont_be_evil
%define debug_package %{nil}

Name:       droid-hal-kernel-pine
Summary:    Linux kernel for PinePhone64
Version:    5.6
Release:    0
Group:      System/Kernel
License:    GPLv2
URL:        https://github.com/sailfish-on-dontbeevil/droid-hal-kernel-pine
Source0:    linux_modules.tar.bz2
Source1:    sun50i-a64-pinephone-1.0.dtb
Source2:    sun50i-a64-pinephone-1.0.dts
Source3:    sun50i-a64-pinephone-1.1.dtb
Source4:    sun50i-a64-pinephone-1.1.dts
Source5:    sun50i-a64-pinetab.dtb
Source6:    sun50i-a64-pinetab.dts
Source7:    sun50i-a64-dontbeevil.dtb
Source8:    sun50i-a64-dontbeevil.dts
Source9:    sun50i-a64-pinephone-1.2.dtb
Source10:   sun50i-a64-pinephone-1.2.dts
Source11:   Image

%description
This package contains the mainline kernel package for
PinePhone and PineTab.

%package modules
Summary: Linux kernel modules for the PinePhone and PineTab
Group:   System/Kernel

%description modules
%{Summary}

%prep
%setup -q -n linux_modules

%build
ls .

%install
mkdir -p $RPM_BUILD_ROOT/boot/allwinner
cp %{SOURCE1} $RPM_BUILD_ROOT/boot/sun50i-a64-pinephone-1.0.dtb
cp %{SOURCE2} $RPM_BUILD_ROOT/boot/sun50i-a64-pinephone-1.0.dts
cp %{SOURCE3} $RPM_BUILD_ROOT/boot/sun50i-a64-pinephone-1.1.dtb
cp %{SOURCE4} $RPM_BUILD_ROOT/boot/sun50i-a64-pinephone-1.1.dts
cp %{SOURCE5} $RPM_BUILD_ROOT/boot/sun50i-a64-pinetab.dtb
cp %{SOURCE6} $RPM_BUILD_ROOT/boot/sun50i-a64-pinetab.dts
cp %{SOURCE7} $RPM_BUILD_ROOT/boot/sun50i-a64-dontbeevil.dtb
cp %{SOURCE8} $RPM_BUILD_ROOT/boot/sun50i-a64-dontbeevil.dts
cp %{SOURCE11} $RPM_BUILD_ROOT/boot/Image

# Copy DTBs from production batches in /boot/allwinner so that they
# can be picked up by bootscripts looking at ${fdtfile} set by u-boot
cp %{SOURCE3} $RPM_BUILD_ROOT/boot/allwinner/sun50i-a64-pinephone-1.1.dtb
cp %{SOURCE4} $RPM_BUILD_ROOT/boot/allwinner/sun50i-a64-pinephone-1.1.dts
cp %{SOURCE9} $RPM_BUILD_ROOT/boot/allwinner/sun50i-a64-pinephone-1.2.dtb
cp %{SOURCE10} $RPM_BUILD_ROOT/boot/allwinner/sun50i-a64-pinephone-1.2.dts

cp -R lib $RPM_BUILD_ROOT/

%files
/boot/sun50i-a64-pinephone-1.0.dtb
/boot/sun50i-a64-pinephone-1.0.dts
/boot/sun50i-a64-pinephone-1.1.dtb
/boot/sun50i-a64-pinephone-1.1.dts
/boot/sun50i-a64-pinetab.dtb
/boot/sun50i-a64-pinetab.dts
/boot/sun50i-a64-dontbeevil.dtb
/boot/sun50i-a64-dontbeevil.dts
/boot/Image
/boot/allwinner/sun50i-a64-pinephone-1.1.dtb
/boot/allwinner/sun50i-a64-pinephone-1.1.dts
/boot/allwinner/sun50i-a64-pinephone-1.2.dtb
/boot/allwinner/sun50i-a64-pinephone-1.2.dts

%files modules
/lib/modules

%post
### Add these users for dbus like droid-hal-device does
/usr/sbin/useradd -r -d / -s /sbin/nologin nfc
/usr/sbin/useradd -r -d / -s /sbin/nologin radio
