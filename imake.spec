Name: imake
Version: 1.0.2
Release: %mkrel 3
Summary: C preprocessor interface to the make utility
Group: System/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.bz2
Patch0: cleanlinks.patch
License: MIT
Packager: Gustavo Pichorim Boiko <boiko@mandriva.com> 
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
%{_mandir}/man1/ccmakedep.1x.bz2
%{_mandir}/man1/cleanlinks.1x.bz2
%{_mandir}/man1/imake.1x.bz2
%{_mandir}/man1/makeg.1x.bz2
%{_mandir}/man1/mergelib.1x.bz2
%{_mandir}/man1/mkdirhier.1x.bz2
%{_mandir}/man1/mkhtmlindex.1x.bz2
%{_mandir}/man1/revpath.1x.bz2
%{_mandir}/man1/xmkmf.1x.bz2


