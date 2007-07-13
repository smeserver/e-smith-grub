Summary: e-smith module to configure grub
%define name e-smith-grub
Name: %{name}
%define version 1.0.0
%define release 6
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Source1: smeserver.xpm.gz
Patch0: e-smith-grub-1.0.0-NoGrubInstallRAID.patch
Patch1: e-smith-grub-1.0.0-NoGrubInstallRAID.patch2
Patch2: e-smith-grub-1.0.0-updatekernel.patch
Patch3: e-smith-grub-1.0.0-splash.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildRequires: e-smith-devtools
BuildArchitectures: noarch
Requires: e-smith-lib >= 1.15.3-17
Requires: grub
Provides: system-logos
Obsoletes: e-smith-lilo
Provides: e-smith-bootloader
Obsoletes: lilo
AutoReqProv: no

%changelog
* Fri Jul 13 2007 Shad L. Lords <slords@mail.com> 1.0.0-6
- Add smeserver splash screen for grub [SME: 3152]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Jan 04 2007 Shad L. Lords <slords@mail.com> 1.0.0-5
- Update /etc/sysconfig/kernel on boot too. [SME: 1930]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Tue Dec 05 2006 Shad L. Lords <slords@mail.com> 1.0.0-03
- Remove grub-install-raid completely as it doesn't handle more 
  than raid1 [SME: 2131]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-02
- Rebuild without the test release tag [SME: 1197]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01test01
- Remove grub-install-raid from post-{install,upgrade} [SME: 1197]

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-01
- Roll stable stream version. [SME: 1016]

* Wed Feb 8 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-24
- Add --no-floppy to the grub --batch calls. Systems with the
  floppy controller enabled but no floppy drive installed "hang"
  in post-upgrade otherwise. [SME: 696]

* Mon Jan 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-23
- Re-add call to grub-install-raid in post-upgrade [SME: 151]

* Mon Jan 30 2006 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-22
- Add --no-floppy to grub-install call in grub-install-raid [SME: 151]
- Don't call grub-install-raid in post-upgrade, only post-install  [SME: 151]
- Cleaned up old comments in grub-install-raid

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.1-21
- Bump release number only

* Tue Nov 15 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-20]
- Add defined test on $EVENT  for cleanliness [MN00106104]

* Tue Nov 15 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-19]
- Only update default kernel choice in the local event [MN00106104]
- Update dependency on e-smith-lib to require version of 
  generic_template_expand which sets EVENT in the template hash

* Sun Nov 13 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-18]
- Correct path in last fix [SF: 1335937]

* Mon Oct 24 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-17]
- Create "update-bootloader" symlink in /sbin/e-smith, for use by add_mirror
  script. Add "Provides: e-smith-bootloader", so that e-smith-base can add
  a generic "Requires:". [SF: 1335937]

* Fri Oct 21 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-16]
- Expand grub.conf template in post-install and post-upgrade, to correct
  errant hd1,0 references. [SF: 1233029]

* Fri Oct 21 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.1-15]
- Fix errant hd1,0 references in /boot/grub/grub.conf. This is just a
  workaround - we should be able to fix anaconda/booty so that they never
  appear. Tidy up UpdateDefault while we are here. [SF: 1233029]
- Update grub-install-raid so that it runs grub for each disk, with each
  device set as hd0. [SF: 1233029]

* Mon Oct 17 2005 Gordon Rowell <gordonr@e-smith.com>
- [0.0.1-14]
- Typo in grub-install-raid log output [MN00100874, SF: 1233029]

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
cp %{SOURCE1} root/boot/grub/
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
perl createlinks
mkdir -p root/etc/e-smith/events/local/templates2expand/etc/sysconfig
touch root/etc/e-smith/events/local/templates2expand/etc/sysconfig/kernel

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

