Summary:	Wacom model feature query library
Summary(pl.UTF-8):	Biblioteka identyfikująca modele i możliwości tabletów Wacom
Name:		libwacom
Version:	1.9
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/linuxwacom/libwacom/releases
Source0:	https://github.com/linuxwacom/libwacom/releases/download/%{name}-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	67aec245e7c1ee7f585a85a2c27db9d8
URL:		https://linuxwacom.github.io/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glib2-devel >= 1:2.36
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	librsvg-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRequires:	udev-glib-devel
Requires:	glib2 >= 1:2.36
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwacom is a library to identify Wacom tablets and their
model-specific features.

%description -l pl.UTF-8
libwacom to biblioteka identyfikująca tablety Wacom oraz ich
możliwości zależne od modelu.

%package devel
Summary:	Header files for libwacom library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwacom
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.36

%description devel
Header files for libwacom library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libwacom.

%package static
Summary:	Static libwacom library
Summary(pl.UTF-8):	Statyczna biblioteka libwacom
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libwacom library.

%description static -l pl.UTF-8
Statyczna biblioteka libwacom.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' tools/show-stylus.py

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	--with-udev-dir=/lib/udev
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING NEWS README.md
%attr(755,root,root) %{_bindir}/libwacom-list-local-devices
%attr(755,root,root) %{_bindir}/libwacom-show-stylus
%attr(755,root,root) %{_libdir}/libwacom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwacom.so.2
%{_datadir}/libwacom
/lib/udev/hwdb.d/65-libwacom.hwdb
/lib/udev/rules.d/65-libwacom.rules
%{_mandir}/man1/libwacom-list-local-devices.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwacom.so
%{_includedir}/libwacom-1.0
%{_pkgconfigdir}/libwacom.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwacom.a
