#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE793007AD22DF7E (tsujan2000@gmail.com)
#
Name     : lxqt-qtplugin
Version  : 0.15.1
Release  : 15
URL      : https://github.com/lxqt/lxqt-qtplugin/releases/download/0.15.1/lxqt-qtplugin-0.15.1.tar.xz
Source0  : https://github.com/lxqt/lxqt-qtplugin/releases/download/0.15.1/lxqt-qtplugin-0.15.1.tar.xz
Source1  : https://github.com/lxqt/lxqt-qtplugin/releases/download/0.15.1/lxqt-qtplugin-0.15.1.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-qtplugin-lib = %{version}-%{release}
Requires: lxqt-qtplugin-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libdbusmenu-qt-dev
BuildRequires : libfm-qt-dev
BuildRequires : liblxqt-data
BuildRequires : libqtxdg-dev
BuildRequires : lxqt-build-tools
BuildRequires : qtbase-dev
BuildRequires : qttools-dev

%description
# lxqt-qtplugin
## Overview
This repository is providing a library `libqtlxqt` to integrate Qt with LXQt.

%package lib
Summary: lib components for the lxqt-qtplugin package.
Group: Libraries
Requires: lxqt-qtplugin-license = %{version}-%{release}

%description lib
lib components for the lxqt-qtplugin package.


%package license
Summary: license components for the lxqt-qtplugin package.
Group: Default

%description license
license components for the lxqt-qtplugin package.


%prep
%setup -q -n lxqt-qtplugin-0.15.1
cd %{_builddir}/lxqt-qtplugin-0.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1598900783
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1598900783
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-qtplugin
cp %{_builddir}/lxqt-qtplugin-0.15.1/LICENSE %{buildroot}/usr/share/package-licenses/lxqt-qtplugin/7fab4cd4eb7f499d60fe183607f046484acd6e2d
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/platformthemes/libqtlxqt.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/lxqt-qtplugin/7fab4cd4eb7f499d60fe183607f046484acd6e2d
