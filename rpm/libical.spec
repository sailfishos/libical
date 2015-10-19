Name:       libical
Summary:    iCalendar library implementation in C (runtime)
Version:    1.0.1
Release:    1
Group:      System/Libraries
License:    LGPLv2.1 or MPLv1.0
URL:        http://libical.github.io/libical/
Source0:    %{name}-%{version}.tar.gz
Requires:   tzdata
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  tzdata
BuildRequires:  cmake

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



%prep
%setup -q -n %{name}-%{version}

%build
pushd libical
%cmake
make %{?jobs:-j%jobs}
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



%files
%defattr(-,root,root,-)
%{_libdir}/libical.so.*
%{_libdir}/libicalss.so.*
%{_libdir}/libicalvcal.so.*


%files devel
%defattr(-,root,root,-)
%{_includedir}/ical.h
%{_includedir}/libical/*.h
%{_libdir}/libical.so
%{_libdir}/libicalss.so
%{_libdir}/libicalvcal.so
%{_libdir}/pkgconfig/libical.pc
%dir %{_libdir}/cmake/LibIcal/
%{_libdir}/cmake/LibIcal/*

