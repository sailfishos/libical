Name:       libical
Summary:    iCalendar library implementation in C (runtime)
Version:    3.0.8
Release:    1
License:    LGPLv2 or MPLv2.0
URL:        https://libical.github.io/libical/
Source0:    %{name}-%{version}.tar.gz
BuildRequires:  tzdata
BuildRequires:  cmake
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gobject-2.0) >= 2.32
BuildRequires:  pkgconfig(libxml-2.0) >= 2.7.3
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(icu-uc)
Requires:       tzdata
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libical is an open source implementation of the IETFs iCalendar calendaring
and scheduling protocols (RFC 2445, 2446, and 2447). It parses iCal 
components and provides a C API for manipulating the component properties, 
parameters, and subcomponents.

This package contains the files necessary for running applications that use
the libical library.

%package devel
Summary:    iCalendar library implementation in C (development)
Requires:   %{name} = %{version}-%{release}

%description devel
libical is an open source implementation of the IETFs iCalendar 
calendaring and scheduling protocols (RFC 2445, 2446, and 2447). It 
parses iCal components and provides a C API for manipulating the 
component properties, parameters, and subcomponents.

This package contains the files necessary for developing applications
that use the libical library.

%package glib
Summary:    GObject wrapper for libical library
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description glib
This package provides a GObject wrapper for libical library with support of GObject Introspection.

%package glib-devel
Summary:    Development files for building against %{name}-glib
Requires:   %{name}-devel = %{version}-%{release}
Requires:   %{name}-glib = %{version}-%{release}

%description glib-devel
Development files needed for building things which link against %{name}-glib.

%prep
%autosetup -n %{name}-%{version}/libical

%build
%cmake -DICAL_BUILD_DOCS:BOOL=false \
       -DICAL_GLIB:BOOL=true \
       -DGOBJECT_INTROSPECTION:BOOL=false \
       -DLIBICAL_BUILD_TESTING:BOOL=false \
       -DSHARED_ONLY:BOOL=true
%make_build

%install
%make_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%post glib -p /sbin/ldconfig
%postun glib -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE LICENSE.LGPL21.txt LICENSE.MPL2.txt
%{_libdir}/libical.so.*
%{_libdir}/libical_cxx.so.*
%{_libdir}/libicalss.so.*
%{_libdir}/libicalss_cxx.so.*
%{_libdir}/libicalvcal.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libical/
%{_libdir}/libical.so
%{_libdir}/libical_cxx.so
%{_libdir}/libicalss.so
%{_libdir}/libicalss_cxx.so
%{_libdir}/libicalvcal.so
%{_libdir}/pkgconfig/libical.pc
%{_libdir}/cmake/LibIcal/

%files glib
%defattr(-,root,root-)
%{_libdir}/libical-glib.so.*

%files glib-devel
%defattr(-,root,root,-)
%{_includedir}/libical-glib/
%{_libdir}/libical-glib.so
%{_libdir}/pkgconfig/libical-glib.pc
