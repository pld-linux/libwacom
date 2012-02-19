Summary:	Wacom model feature query library
Name:		libwacom
Version:	0.3
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://downloads.sourceforge.net/linuxwacom/%{name}-%{version}.tar.bz2
# Source0-md5:	08890c25fc73471f94ed2bc3ab34d080
URL:		http://linuxwacom.sourceforge.net/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	doxygen
BuildRequires:	glib2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	udev-glib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libwacom is a library to identify wacom tablets and their
model-specific features.

%package devel
Summary:	Header files for libwacom library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libwacom
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel

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

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
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
%doc NEWS README
%attr(755,root,root) %{_libdir}/libwacom.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwacom.so.2
%{_datadir}/libwacom

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwacom.so
%{_includedir}/libwacom-1.0
%{_pkgconfigdir}/libwacom.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libwacom.a
