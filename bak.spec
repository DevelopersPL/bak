Summary: Backup script utilizing rsync, hard links, and rotation
Name: bak
Version: 0.1
Release: 1
License: GPL
Group: 
URL: http://notes.brooks.nu
Source0: %{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
Backup script utilizing rsync, hard links, and rotation

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
make install

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/etc/bak.conf
/etc/cron.daily/bak


%changelog
* Mon Sep 29 2008 Lane Brooks <lane@dome.lane.brooks.nu> - 
- Initial build.

