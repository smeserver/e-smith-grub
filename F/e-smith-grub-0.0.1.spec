Summary: e-smith module to configure grub
%define name e-smith-grub
Name: %{name}
%define version 0.0.1
%define release 14sme02
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
Patch7: e-smith-grub-0.0.1-12.mitel_patch
Patch8: e-smith-grub-0.0.1-13.mitel_patch
Patch9: e-smith-grub-0.0.1-14.mitel_patch
Patch100: e-smith-grub-0.0.1-grubinstallraid.patch
Packager: e-smith developers <bugs@e-smith.com>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-lib
Requires: grub >= 0.95-13sme01
Provides: system-logos
Obsoletes: e-smith-lilo
Obsoletes: lilo
AutoReqProv: no

%changelog
* Thu Oct 20 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-14sme02
- Re-instate grub-install-raid in post-upgrade/post-install [SF: 1233029]
- Change it to just call "grub-install --recheck /dev/md1"

* Thu Oct 20 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-14sme01
- Update Requires to depend on patched grub version
- Delete grub-install-raid script and links [SF: 1233029]

* Mon Oct 17 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-14]
- Type on grub-install-raid log output [MN00100874, SF: 1233029]

* Mon Oct 17 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-13]
- Add grub-install-raid action to force to install onto a RAID1 set
  [MN00100874, SF: 1233029]

* Mon Sep 19 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-12]
- Preserve current default setting in grub.conf template if
  none of the available kernels matches the currently running
  kernel. This will allow anaconda SMP detection to determine
  initial boot setting. [MN00097833]

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
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch100 -p1

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

