#global debug_package %{nil}
%define _empty_manifest_terminate_build 0

%define libname %mklibname openaptx %{major}
%define develname %mklibname openaptx -d
%define oname openaptx

%define major 0

Name: libopenaptx
Epoch:   2
Version: 0.2.1
Release: 1
Summary: Open Source implementation of aptX codec
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/pali/libopenaptx
Source0: https://github.com/pali/libopenaptx/releases/download/%{version}/%{name}-%{version}.tar.gz

%package -n %{oname}
Summary:       Library for Open Source implementation of aptX codec
Group:         System/Libraries

%description -n %{oname}
This is Open Source implementation library of Audio Processing Technology codec
(aptX) derived from ffmpeg 4.0 project and licensed under LGPLv2.1+. This
codec is mainly used in Bluetooth A2DP profile.

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
Requires:	%{libname} = %{epoch}:%{version}-%{release}

%description -n %{develname}
This package provides files needed to develop programms which use %name.

%prep
%autosetup -p1
# don't strip binaries
sed -i '/^LDFLAGS = -s/d' Makefile

%build
%ifarch %{ix86}
export CC=gcc
export CXX=g++
%endif
%make_build

%install
%make_install PREFIX=%_prefix LIBDIR=%_lib

%files -n %{oname}
%{_bindir}/openaptxdec
%{_bindir}/openaptxenc

%files -n %{libname}
%{_libdir}/libopenaptx.so.%{major}
%{_libdir}/libopenaptx.so.%{version}
%doc README

%files -n %{develname}
%{_includedir}/openaptx.h
%{_libdir}/libopenaptx.so
%{_libdir}/pkgconfig/libopenaptx.pc

%exclude %_libdir/%name.a
