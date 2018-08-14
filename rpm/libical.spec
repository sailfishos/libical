Name:       libical
Summary:    iCalendar library implementation in C (runtime)
Version:    3.0.3
Release:    1
Group:      System/Libraries
License:    LGPLv2.1 or MPLv2.0
URL:        http://libical.github.io/libical/
Source0:    %{name}-%{version}.tar.gz
Requires:   tzdata
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  tzdata
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)

%description
libical is an open source implementation of the IETFs iCalendar calendaring
and scheduling protocols (RFC 2445, 2446, and 2447). It parses iCal 
components and provides a C API for manipulating the component properties, 
parameters, and subcomponents.

This package contains the files necessary for running applications that use
the libical library.

%package devel
Summary:    iCalendar library implementation in C (development)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
libical is an open source implementation of the IETFs iCalendar 
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It 
parses iCal components and provides a C API for manipulating the 
component properties, parameters, and subcomponents.

This package contains the files necessary for developing applications
that use the libical library.

%package glib
Summary:	GObject wrapper for libical library
Requires:	%{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description glib
This package provides a GObject wrapper for libical library with support of GObject Introspection.

%package glib-devel
Summary:	Development files for building against %{name}-glib
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-glib = %{version}-%{release}

%description glib-devel
Development files needed for building things which link against %{name}-glib.

%prep
%setup -q -n %{name}-%{version}

%build
pushd libical
%cmake
make
popd

%install
rm -rf %{buildroot}
pushd libical
make install DESTDIR=%{buildroot}
popd

# Remove unpackaged files - static libraries
rm -f %{buildroot}%{_libdir}/libical*.a

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/libical.so.*
%{_libdir}/libical_cxx.so.*
%{_libdir}/libicalss.so.*
%{_libdir}/libicalss_cxx.so.*
%{_libdir}/libicalvcal.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libical/*.h
%{_libdir}/libical.so
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss.so
%{_libdir}/libicalss_cxx.so
%{_libdir}/libicalvcal.so
%{_libdir}/pkgconfig/libical.pc
%dir %{_libdir}/cmake/LibIcal/
%{_libdir}/cmake/LibIcal/*

%files glib
%defattr(-,root,root-)
%{_libdir}/libical-glib.so.*

%files glib-devel
%{_includedir}/libical-glib/*.h
%{_libdir}/pkgconfig/libical-glib.pc
%{_libdir}/libical-glib.so
