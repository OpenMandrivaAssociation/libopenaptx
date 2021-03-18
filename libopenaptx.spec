%global debug_package %{nil}

%define libname %mklibname openaptx %{major}
%define develname %mklibname openaptx -d

%define major 0

Name: libopenaptx
Version: 0.2.0
Release: 1
Summary: Open Source implementation of aptX codec
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/pali/libopenaptx
Source0: https://github.com/pali/libopenaptx/releases/download/%{version}/%{name}-%{version}.tar.gz

%description
This is Open Source implementation of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%package -n %{libname}
Summary:       Library for Open Source implementation of aptX codec
Group:         System/Libraries

%description -n %{libname}
This is Open Source implementation library of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

%package -n %{develname}
Summary: aptX header files
Group: Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package provides files needed to develop programms which use %name.

%prep
%autosetup -p1
# don't strip binaries
sed -i '/^LDFLAGS = -s/d' Makefile

%build
%define _optlevel 3
%make_build

%install
%make_install PREFIX=%_prefix LIBDIR=%_lib

%files
#_bindir/%{_name}dec
#_bindir/%{_name}enc

%files -n %{libname}
#_libdir/%name.so.*
%doc README

%files -n %{develname}
#_includedir/%_name.h
#_libdir/%name.so
#_pkgconfigdir/%name.pc

%exclude %_libdir/%name.a


