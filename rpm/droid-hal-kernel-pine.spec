# Thanks to Neochapay: https://build.merproject.org/package/show/home:neochapay:mer:release:2018.05:hardware:pine64/kernel-dont_be_evil
%define debug_package %{nil}

Name:       droid-hal-kernel-pine
Summary:    Linux kernel for PinePhone64
Version:    5.3
Release:    0
Group:      System/Kernel
License:    GPLv2
URL:        https://github.com/neochapay/kernel-dont_be_evil
Source0:    linux_modules.tar.bz2
Source1:    sun50i-a64-pinephone.dtb
Source2:    sun50i-a64-pinephone.dts
Source3:    sun50i-a64-pinetab.dtb
Source4:    sun50i-a64-pinetab.dts
Source5:    sun50i-a64-dontbeevil.dtb
Source6:    sun50i-a64-dontbeevil.dts
Source7:    Image

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
mkdir -p $RPM_BUILD_ROOT/boot
cp %{SOURCE1} $RPM_BUILD_ROOT/boot/
cp %{SOURCE2} $RPM_BUILD_ROOT/boot/
cp %{SOURCE3} $RPM_BUILD_ROOT/boot/
cp %{SOURCE4} $RPM_BUILD_ROOT/boot/
cp %{SOURCE5} $RPM_BUILD_ROOT/boot/
cp %{SOURCE6} $RPM_BUILD_ROOT/boot/
cp %{SOURCE7} $RPM_BUILD_ROOT/boot/

cp -R lib $RPM_BUILD_ROOT/

%files
/boot/

%files modules
/lib/modules
