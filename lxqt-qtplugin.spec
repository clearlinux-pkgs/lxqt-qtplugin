#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x42C9C8D3AF5EA5E3 (agaida@siduction.org)
#
Name     : lxqt-qtplugin
Version  : 0.14.0
Release  : 3
URL      : https://downloads.lxqt.org/downloads/lxqt-qtplugin/0.14.0/lxqt-qtplugin-0.14.0.tar.xz
Source0  : https://downloads.lxqt.org/downloads/lxqt-qtplugin/0.14.0/lxqt-qtplugin-0.14.0.tar.xz
Source99 : https://downloads.lxqt.org/downloads/lxqt-qtplugin/0.14.0/lxqt-qtplugin-0.14.0.tar.xz.asc
Summary  : LXQt platform integration for Qt
Group    : Development/Tools
License  : LGPL-2.1
Requires: lxqt-qtplugin-lib = %{version}-%{release}
Requires: lxqt-qtplugin-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libdbusmenu-qt-dev
BuildRequires : libqtxdg-dev
BuildRequires : lxqt-build-tools
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
%setup -q -n lxqt-qtplugin-0.14.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549550045
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549550045
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/lxqt-qtplugin
cp LICENSE %{buildroot}/usr/share/package-licenses/lxqt-qtplugin/LICENSE
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
/usr/share/package-licenses/lxqt-qtplugin/LICENSE
