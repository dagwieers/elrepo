Name: flashcache-utils	
Version: 0.0	
Release: 2%{?dist}
Summary: Utility packages for flashcache
Group: System Environment/Base
License: GPLv2
URL: https://github.com/facebook/flashcache

BuildRequires: redhat-rpm-config

# Sources.
Source0:  %{name}-%{version}.tar.gz
Source5:  GPL-v2.0.txt

# Disable the building of the debug package(s).
%define debug_package %{nil}

%description
The %{name} package contains utility packages for flashcache including
flashcache_create, flashcache_load and flashcache_destroy. It is expected
that the majority of users can use these utilities instead of dmsetup.

%prep
%setup -q -n %{name}-%{version}
%{__cp} -a %{SOURCE5} .

%build
%{__make} -s %{?_smp_mflags}

%install
%{__make} -s install DESTDIR="%{buildroot}"
%{__install} -m 755 flashstat %{buildroot}/sbin/
%{__install} -d %{buildroot}%{_defaultdocdir}/%{name}-%{version}/
%{__install} GPL-v2.0.txt %{buildroot}%{_defaultdocdir}/%{name}-%{version}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
/sbin/flashcache_create
/sbin/flashcache_destroy
/sbin/flashcache_load
/sbin/flashstat
%doc /usr/share/doc/%{name}-%{version}/GPL-v2.0.txt

%changelog
* Sat Mar 03 2012 Akemi Yagi <toracat@elrepo.org> - 0.0-2
- Packaging style now conforms to the ELRepo standard. [Alan Bartlett]

* Sun Feb 12 2012 Akemi Yagi <toracat@elrepo.org> - 0.0-1
- Initial build for EL6.
