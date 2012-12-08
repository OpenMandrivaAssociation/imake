Name: imake
Version: 1.0.4
Release: %mkrel 3
Summary: C preprocessor interface to the make utility
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
Patch0: cleanlinks.patch
Patch1: imake-1.0.2-Wformat-security=error.patch
License: MIT
BuildRoot: %{_tmppath}/%{name}-root
Requires: x11-util-cf-files >= 1.0.2-%{mkrel 3}

BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: x11-proto-devel

%description
Imake is used to generate Makefiles from a template, a set of cpp macro
functions,  and  a  per-directory input file called an Imakefile.  This allows
machine dependencies (such as compiler options,  alternate com- mand  names,
and  special  make  rules)  to  be kept separate from the descriptions of
the various items to be built.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0 -b .cleanlinks_fix
%patch1 -p1

%build
%configure2_5x	--with-config-dir=%{_datadir}/X11/config \
		--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/imake
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%{_mandir}/man1/ccmakedep.*
%{_mandir}/man1/cleanlinks.*
%{_mandir}/man1/imake.*
%{_mandir}/man1/makeg.*
%{_mandir}/man1/mergelib.*
%{_mandir}/man1/mkdirhier.*
%{_mandir}/man1/mkhtmlindex.*
%{_mandir}/man1/revpath.*
%{_mandir}/man1/xmkmf.*




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-2mdv2011.0
+ Revision: 665508
- mass rebuild

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.0.4-1mdv2011.0
+ Revision: 591889
- new release

* Fri Apr 16 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.3-1mdv2010.1
+ Revision: 535446
- New version: 1.0.3

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-9mdv2010.1
+ Revision: 520125
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-8mdv2010.0
+ Revision: 425333
- rebuild

* Thu Apr 02 2009 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-7mdv2009.1
+ Revision: 363591
- Correct build failure due to -Wformat-security=error, and rebuild to
  properly match x11-util-cf-files location.

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2009.0
+ Revision: 264682
- rebuild early 2009.0 package (before pixel changes)

* Fri May 30 2008 Olivier Blin <oblin@mandriva.com> 1.0.2-5mdv2009.0
+ Revision: 213520
- restore BuildRoot

* Wed Dec 19 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2008.1
+ Revision: 134096
- rebuild

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 127018
- kill re-definition of %%buildroot on Pixel's request
- fix man pages extension


* Tue Mar 06 2007 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-3mdv2007.0
+ Revision: 133983
- added a patch not to remove symlinks to directories in cleanlinks (#19855)

* Thu Dec 14 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 1.0.2-2mdv2007.1
+ Revision: 96966
- Cope with new x11-util-cf-files

* Thu Aug 03 2006 Gustavo Pichorim Boiko <boiko@mandriva.com> 1.0.2-1mdv2007.0
+ Revision: 43003
- new upstream release (1.0.2):
  * Allow specifying TMPDIR environment variable to use instead of /tmp, for
  systems on which /tmp is mounted noexec.
- rebuild to fix cooker uploading
- added missing buildrequires
- adding package imake

  + Andreas Hasenack <andreas@mandriva.com>
    - renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

  + Pixel <pixel@mandriva.com>
    - add "Requires: x11-util-cf-files"

