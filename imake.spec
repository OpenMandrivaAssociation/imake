Name:		imake
Version:	1.0.10
Release:	1
Summary:	C preprocessor interface to the make utility
License:	Free
Group:		System/X11
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/util/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
Requires:	x11-util-cf-files

%description
Imake is used to generate Makefiles from a template, a set of cpp macro
functions,  and  a  per-directory input file called an Imakefile.  This allows
machine dependencies (such as compiler options,  alternate com- mand  names,
and  special  make  rules)  to  be kept separate from the descriptions of
the various items to be built.

%prep
%autosetup -p1

%build
%configure \
	--with-config-dir=%{_datadir}/X11/config \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
%make_install

%files
%{_bindir}/ccmakedep
%{_bindir}/cleanlinks
%{_bindir}/imake
%{_bindir}/makeg
%{_bindir}/mergelib
%{_bindir}/mkdirhier
%{_bindir}/mkhtmlindex
%{_bindir}/revpath
%{_bindir}/xmkmf
%doc %{_mandir}/man1/ccmakedep.*
%doc %{_mandir}/man1/cleanlinks.*
%doc %{_mandir}/man1/imake.*
%doc %{_mandir}/man1/makeg.*
%doc %{_mandir}/man1/mergelib.*
%doc %{_mandir}/man1/mkdirhier.*
%doc %{_mandir}/man1/mkhtmlindex.*
%doc %{_mandir}/man1/revpath.*
%doc %{_mandir}/man1/xmkmf.*
