Summary: e-smith module to configure grub
%define name e-smith-grub
Name: %{name}
%define version 0.0.1
%define release 11
Version: %{version}
Release: %{release}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: e-smith-grub-0.0.1-02.mitel_patch
Patch1: e-smith-grub-0.0.1-03.mitel_patch
Patch2: e-smith-grub-0.0.1-04.mitel_patch
Patch3: e-smith-grub-0.0.1-05.mitel_patch
Patch4: e-smith-grub-0.0.1-07.mitel_patch
Patch5: e-smith-grub-0.0.1-08.mitel_patch
Patch6: e-smith-grub-0.0.1-11.mitel_patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: grub
Provides: system-logos
Obsoletes: e-smith-lilo
Obsoletes: lilo
AutoReqProv: no

%changelog
* Tue Aug 30 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-11]
- Move splashscreen symlink into e-smith-support RPM.

* Wed Jul 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-10]
- Obsolete lilo RPM, so that it is removed on upgrade. [SF: 1232519]

* Tue Jul  5 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-09]
- Obsolete e-smith-lilo RPM. [SF: 1232519]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-08]
- Move grub.conf template.metadata file a well. [SF: 1226839]

* Fri Jun 24 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-07]
- Template /boot/grub/grub.conf, not /etc/grub.conf. [SF: 1226839]

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-06]
- Add "Provides: system-logos" to satisfy grub dependency.

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-05]
- Add linuxinside splashscreen.

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-04]
- Add tux splashscreen, and use it for grub config.

* Wed Jun  8 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-03]
- Add missing template.metadata file to strip blank lines from
  grub.conf file.

* Tue Jun  7 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-02]
- Fix grub.conf template expansion.
- Put splash.xpm.gz in correct place.

* Mon Jun 06 2005 Charlie Brady <charlieb@e-smith.com>
- initial release

%description
e-smith server enhancement to grub bootloader.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
gzip root/boot/grub/tux.xpm
gzip root/boot/grub/linuxinside.xpm
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

