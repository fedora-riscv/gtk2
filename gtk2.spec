# Note that this is NOT a relocatable package

# Something's not quite right with libtool....
%define __libtoolize :

%define glib2_base_version 2.0.1
%define glib2_version %{glib2_base_version}-1
%define pango_base_version 1.0.0
%define pango_version %{pango_base_version}-1
%define atk_base_version 1.0.0
%define atk_version %{atk_base_version}-1

%define base_version 2.0.2
%define bin_version 2.0.0



Summary: The GIMP ToolKit (GTK+), a library for creating GUIs for X.
Name: gtk2
Version: %{base_version}
#Version: %{base_version}
Release: 3
License: LGPL
Group: System Environment/Libraries
Source: gtk+-%{version}.tar.gz
Source1: gtk-beta-rc-default
Source2: fixed-ltmain.sh
Patch1: gtk+-1.3.7-installdir.patch
# Don't use GTK_RC_FILES, since it causes problems with what
# KDE does to customize GTK+ themes, use GTK2_RC_FILES instead
Patch2: gtk+-2.0.2-gtkrc.patch
BuildPrereq: atk-devel >= %{atk_version}
BuildPrereq: pango-devel >= %{pango_version}
BuildPrereq: glib2-devel >= %{glib2_version}
BuildPrereq: libtiff-devel
BuildPrereq: libjpeg-devel
BuildPrereq: libpng-devel
BuildPrereq: automake

BuildRoot: /var/tmp/gtk-%{PACKAGE_VERSION}-root
Obsoletes: gtk+-gtkbeta
Obsoletes: Inti

URL: http://www.gtk.org

# We need to prereq these so we can run gtk-query-immodules-2.0
Prereq: glib2 >= %{glib2_version}
Prereq: atk >= %{atk_version}
Prereq: pango >= %{pango_version}

%description
GTK+ is a multi-platform toolkit for creating graphical user
interfaces. Offering a complete set of widgets, GTK+ is suitable for
projects ranging from small one-off tools to complete application
suites.

%package devel
Summary: Development tools for GTK+ applications.
Group: Development/Libraries
Requires: gtk2 = %{PACKAGE_VERSION}
Requires: pango-devel >= %{pango_version}
Requires: atk-devel >= %{atk_version}
Requires: glib2-devel >= %{glib2_version}
Requires: XFree86-devel
Obsoletes: gtk+-gtkbeta-devel
Obsoletes: Inti-devel
## avoid header collisions
Conflicts: gtk+-devel <= 1.2.8
Conflicts: gdk-pixbuf-devel <= 0.11

%description devel
The gtk+-devel package contains the header files and developer
docs for the GTK+ widget toolkit.  

%changelog
* Thu Apr 11 2002 Tim Powers <timp@redhat.com> 2.0.0-3
- bump release number

* Thu Apr 11 2002 Owen Taylor <otaylor@redhat.com>
- Add reference docs to -devel package (#61184)
- Use GTK2_RC_FILES, not GTK_RC_FILES, since KDE points GTK_RC_FILES 
  to gtk-1.2 ~/.gtkrc

* Wed Apr  3 2002 Alex Larsson <alexl@redhat.com>
- Change dependency for glib2 since gtk and glib versions mismatch

* Wed Apr  3 2002 Alex Larsson <alexl@redhat.com>
- Update to version 2.0.2

* Fri Mar  8 2002 Owen Taylor <otaylor@redhat.com>
- Version 2.0.0

* Mon Feb 25 2002 Alex Larsson <alexl@redhat.com>
- Update to 1.3.15

* Thu Feb 21 2002 Alex Larsson <alexl@redhat.com>
- Bump for rebuild

* Mon Feb 18 2002 Alex Larsson <alexl@redhat.com>
- Update to 1.3.14

* Fri Feb 15 2002 Havoc Pennington <hp@redhat.com>
- add horrible buildrequires hack

* Thu Feb 14 2002 Havoc Pennington <hp@redhat.com>
- 1.3.13.91 snapshot

* Mon Feb 11 2002 Matt Wilson <msw@redhat.com>
- build from CVS snapshot
- use setup -q

* Wed Jan 30 2002 Owen Taylor <otaylor@redhat.com>
- Version 1.3.13

* Tue Jan 22 2002 Havoc Pennington <hp@redhat.com>
- automake14

* Wed Jan  2 2002 Havoc Pennington <hp@redhat.com>
- 1.3.12.90 snapshot

* Sun Nov 25 2001 Havoc Pennington <hp@redhat.com>
- Version 1.3.11
- check atk/pango versions explicitly prior to build,
  so that --nodeps tricks don't result in bad binary RPMs

* Fri Oct  5 2001 Havoc Pennington <hp@redhat.com>
- pixbuf loaders were missing from file list
- conflict with gdk-pixbuf-devel <= 0.11

* Thu Oct  4 2001 Havoc Pennington <hp@redhat.com>
- cvs snap

* Thu Sep 27 2001 Havoc Pennington <hp@redhat.com>
- sync with Owen's version

* Thu Sep 20 2001 Havoc Pennington <hp@redhat.com>
- smp_mflags
- langify

* Wed Sep 19 2001 Havoc Pennington <hp@redhat.com>
- 1.3.8
- add automake hackarounds

* Thu Sep 13 2001 Havoc Pennington <hp@redhat.com>
- conflict with old GTK with headers not moved
- prereq new version of pango

* Mon Sep 10 2001 Havoc Pennington <hp@redhat.com>
- update to CVS snapshot

* Wed Sep  5 2001 Havoc Pennington <hp@redhat.com>
- build require specific versions of dependencies

* Tue Sep  4 2001 Owen Taylor <otaylor@redhat.com>
- Version 1.3.7

* Thu Jul 26 2001 Havoc Pennington <hp@redhat.com>
- Obsolete Inti and Inti-devel, #49967

* Sat Jul 21 2001 Owen Taylor <otaylor@redhat.com>
- PreReq specific pango and atk versions (#49434)
- Don't package gtk.immodules (#49584)
- Added BuildPrereq for libtiff-devel, libjpeg-devel, libpng-devel (#49495)
- Configure with --disable-gtk-doc (#48987)
- Package libgdk_pixbuf_xlib (#47753)

* Sat Jul  7 2001 Tim Powers <timp@redhat.com>
- languify to satisfy rpmlint

* Thu Jun 21 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- use something better than libtool

* Wed Jun 13 2001 Havoc Pennington <hp@redhat.com>
- 1.3.6
- libtool hackery
- obsolete gtk+-gtkbeta-devel

* Fri May  4 2001 Owen Taylor <otaylor@redhat.com>
- Version 1.3.5
- Rename to gtk2

* Fri Nov 17 2000 Owen Taylor <otaylor@redhat.com>
- Final 1.3.2

* Tue Nov 14 2000 Owen Taylor <otaylor@redhat.com>
- New snapshot

* Mon Nov 13 2000 Owen Taylor <otaylor@redhat.com>
- 1.3.2pre1 snapshot version

* Sun Aug 13 2000 Owen Taylor <otaylor@redhat.com>
- Rename to 1.3.1b to avoid version increment difficulties

* Thu Aug 10 2000 Havoc Pennington <hp@redhat.com>
- Fix .pc files to not contain -I/usr/include

* Thu Aug 10 2000 Havoc Pennington <hp@redhat.com>
- Update to a CVS snapshot

* Fri Jul 14 2000 Owen Taylor <otaylor@redhat.com>
- Removed stray b from %%postun
- Real 1.3.1 tarball fixing stupid omission in gtk-config

* Fri Jul 07 2000 Owen Taylor <otaylor@redhat.com>
- Version 1.3.1
- move back to /usr
- Remove gtk-config.1 manpage from build since
  it conflicts with gtk+-devel. When we go to 
  gtk+ gtk+1.2 setup, we should add it back

* Fri Jun 30 2000 Owen Taylor <otaylor@redhat.com>
- Rename gtkrc-default source so that it GTK+ package can't remove it

* Thu Jun 8 2000  Owen Taylor <otaylor@redhat.com>
- Rebuild with a prefix of /opt/gtk-beta

* Wed May 31 2000 Owen Taylor <otaylor@redhat.com>
- New version

* Tue Apr 25 2000 Owen Taylor <otaylor@redhat.com>
- Snapshot version to install in /opt/pango

* Mon Feb 21 2000 Owen Taylor <otaylor@redhat.com>
- Fix weird excess  problem that somehow turned up in /etc/gtkrc.LANG

* Mon Feb 14 2000 Owen Taylor <otaylor@redhat.com>
- More patches from 1.2.7

* Fri Feb 04 2000 Owen Taylor <otaylor@redhat.com>
- Set the charset explicitely for the default font to avoid
  problems with XFree86-4.0 where the default charset is
  iso10646-1, not iso8859-1.
- Fix problems with size requisitions for scrolled windows
  that was causing looping. (RH bug #7997)

* Thu Feb 03 2000 Owen Taylor <otaylor@redhat.com>
- Explicitely set the foreground of the tooltips to black
  to avoid bad interactions with themes that set a
  light foreground color.

* Thu Feb 03 2000 Owen Taylor <otaylor@redhat.com>
- Added large patch of bugfixes in stable branch of CVS

* Tue Oct 12 1999 Owen Taylor <otaylor@redhat.com>
- Added Akira Higuti's patch for line-wrapping in GTK+

* Thu Oct 7  1999 Owen Taylor <otaylor@redhat.com>
- version 1.2.6

* Thu Sep 23 1999 Owen Taylor <otaylor@redhat.com>
- version 1.2.5
- install tutorial GIFs

* Wed Sep 22  1999 Owen Taylor <otaylor@redhat.com>
- Upgrade to real 1.2.5pre2
- Changed name so upgrade to 1.2.5 will work :-(
- Add extra gtkrc files
- Add examples and English language tutorial to -devel package

* Fri Sep 17 1999 Owen Taylor <otaylor@redhat.com>
- Upgraded to 1.2.5pre2. (Actually, pre-pre-2)

* Tue Aug 17 1999 Michael Fulbright <drmike@redhat.com>
- added threaded patch

* Mon Jun 7 1999 Owen Taylor <otaylor@redhat.com>
- Update for GTK+-1.2.3
- Patches that will be in GTK+-1.2.4
- Patch to keep GTK+ from coredumping on X IO errors
- Patch to improve compatilibity with GTK-1.2.1 (allow
  event mask to be set on realized widgets)

* Mon Apr 19 1999 Michael Fulbright <drmike@redhat.com>
- fixes memory leak

* Mon Apr 12 1999 Owen Taylor <otaylor@redhat.com>
- The important bug fixes that will be in GTK+-1.2.2

* Thu Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- patches from owen to handle various gdk bugs

* Sun Mar 28 1999 Michael Fulbright <drmike@redhat.com>
- added XFree86-devel requirement for gtk+-devel

* Thu Mar 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.1

* Wed Mar 17 1999 Michael Fulbright <drmike@redhat.com>
- removed /usr/info/dir.gz file from package

* Fri Feb 26 1999 Michael Fulbright <drmike@redhat.com>
- Version 1.2.0

* Thu Feb 25 1999 Michael Fulbright <drmike@redhat.com>
- version 1.2.0pre2, patched to use --sysconfdir=/etc

* Mon Feb 15 1999 Michael Fulbright <drmike@redhat.com>
- patched in Owen's patch to fix Metal theme

* Fri Feb 05 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.15

* Wed Feb 03 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.14

* Mon Jan 18 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.13

* Wed Jan 06 1999 Michael Fulbright <drmike@redhat.com>
- bumped up to 1.1.12

* Wed Dec 16 1998 Michael Fulbright <drmike@redhat.com>
- added Theme directory to file list
- up to 1.1.7 for GNOME freeze

* Sun Oct 25 1998 Shawn T. Amundson <amundson@gtk.org>
- Fixed Source: to point to v1.1 

* Tue Aug 04 1998 Michael Fulbright <msf@redhat.com>
- change %postun to %preun

* Mon Jun 27 1998 Shawn T. Amundson
- Changed version to 1.1.0

* Thu Jun 11 1998 Dick Porter <dick@cymru.net>
- Removed glib, since it is its own module now

* Mon Apr 13 1998 Marc Ewing <marc@redhat.com>
- Split out glib package

* Tue Apr  8 1998 Shawn T. Amundson <amundson@gtk.org>
- Changed version to 1.0.0

* Tue Apr  7 1998 Owen Taylor <otaylor@gtk.org>
- Changed version to 0.99.10

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.9
- Changed gtk home page to www.gtk.org

* Thu Mar 19 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.8

* Sun Mar 15 1998 Marc Ewing <marc@redhat.com>
- Added aclocal and bin stuff to file list.
- Added -k to the SMP make line.
- Added lib/glib to file list.

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Changed version to 0.99.7

* Fri Mar 14 1998 Shawn T. Amundson <amundson@gimp.org>
- Updated ftp url and changed version to 0.99.6

* Thu Mar 12 1998 Marc Ewing <marc@redhat.com>
- Reworked to integrate into gtk+ source tree
- Truncated ChangeLog.  Previous Authors:
  Trond Eivind Glomsrod <teg@pvv.ntnu.no>
  Michael K. Johnson <johnsonm@redhat.com>
  Otto Hammersmith <otto@redhat.com>
  
%prep
%setup -q -n gtk+-%{version}
%patch1 -p1 -b .installdir
%patch2 -p1 -b .gtkrc
for i in config.guess config.sub ; do
	test -f /usr/share/libtool/$i && cp /usr/share/libtool/$i .
done

%build


rm ltmain.sh && cp %{SOURCE2} ltmain.sh
# Patch1 modifies modules/input/Makefile.am
aclocal
automake
autoconf

%configure --with-xinput=xfree --disable-gtk-doc
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%find_lang %name

#
# Install a default RC file
#
./mkinstalldirs $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0
install -m 444 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/gtk-2.0/gtkrc

#
# Make cleaned-up versions of examples and tutorial for installation
#
./mkinstalldirs tmpdocs/tutorial
# install -m 0644 docs/html/gtk_tut.html docs/html/gtk_tut-[0-9]*.html docs/html/*.gif tmpdocs/tutorial
for dir in examples/* ; do
    if [ -d $dir ] ; then
       ./mkinstalldirs tmpdocs/$dir
       for file in $dir/* ; do
          case $file in
	     *pre1.2.7)
	        ;;
	     *)
                install -m 0644 $file tmpdocs/$dir
		;;
	  esac
       done
    fi
done

# Install the demo programs
cd tests
../libtool --mode=install install testgtk $RPM_BUILD_ROOT%{_prefix}/bin
../libtool --mode=install install testtext $RPM_BUILD_ROOT%{_prefix}/bin

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%{_prefix}/bin/gtk-query-immodules-2.0 > /etc/gtk-2.0/gtk.immodules

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-, root, root)

%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_prefix}/bin/testtext
%{_prefix}/bin/testgtk
%{_prefix}/bin/gtk-demo
%{_prefix}/bin/gtk-query-immodules-2.0
%{_prefix}/lib/libgtk-x11-2.0.so.*
%{_prefix}/lib/libgdk-x11-2.0.so.*
%{_prefix}/lib/libgdk_pixbuf-2.0.so.*
%{_prefix}/lib/libgdk_pixbuf_xlib-2.0.so.*
%dir %{_prefix}/lib/gtk-2.0
%{_prefix}/lib/gtk-2.0/%{bin_version}
%{_prefix}/share/gtk-2.0
%{_prefix}/share/themes/Default/gtk-2.0
%dir %{_sysconfdir}/gtk-2.0
%config %{_sysconfdir}/gtk-2.0/gtkrc


%files devel
%defattr(-, root, root)

%{_prefix}/lib/lib*.so
%dir %{_prefix}/lib/gtk-2.0
%{_prefix}/lib/gtk-2.0/include
%{_datadir}/gtk-doc/
%{_mandir}/man1/*
%{_prefix}/include/*
%{_prefix}/share/aclocal/*
%{_prefix}/bin/gdk-pixbuf-csource
%{_prefix}/lib/pkgconfig/*
%doc tmpdocs/tutorial
%doc tmpdocs/examples
