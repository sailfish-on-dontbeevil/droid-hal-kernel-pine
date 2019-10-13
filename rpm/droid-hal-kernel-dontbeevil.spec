# Thanks to Neochapay: https://build.merproject.org/package/show/home:neochapay:mer:release:2018.05:hardware:pine64/kernel-dont_be_evil
%define debug_package %{nil}

Name:       droid-hal-kernel-dontbeevil
Summary:    Linux kernel for PinePhone64
Version:    5.3
Release:    0
Group:      System/Kernel
License:    GPLv2
URL:        https://github.com/neochapay/kernel-dont_be_evil
Source0:    linux_modules.tar.bz2
Source1:    sun50i-a64-dontbeevil.dtb
Source2:    sun50i-a64-dontbeevil.dts
Source3:    Image

%description
This package contains the mainline kernel package for
PinePhone.

%package modules
Summary: Linux kernel modules for the PinePhone
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

cp -R lib $RPM_BUILD_ROOT/

%files
/boot/

%files modules
/lib/modules
