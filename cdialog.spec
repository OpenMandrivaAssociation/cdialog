%define fname dialog
%define date 20160209

Summary:	A utility for creating TTY dialog boxes
Name:		cdialog
Version:	1.3
Release:	0.%{date}.1
License:	LGPLv2+
Group:		Development/Other
Url:		http://invisible-island.net/dialog/
Source0:	ftp://invisible-island.net/dialog/%{fname}-%{version}-%{date}.tgz
Patch0:		dialog-1.2-20150920-fix-linking-with-llvm-ar.patch
BuildRequires:	pkgconfig(ncursesw)
%rename		%{fname}

%description
Dialog is a utility that allows you to show dialog boxes (containing
questions or messages) in TTY (text mode) interfaces.  Dialog is called
from within a shell script.  The following dialog boxes are implemented:
yes/no, menu, input, message, text, info, checklist, radiolist, and
gauge.

Install dialog if you would like to create TTY dialog boxes.

%prep
%setup -qn %{fname}-%{version}-%{date}
%apply_patches

%build
%configure \
    --enable-nls \
    --with-ncursesw \
    --disable-rpath-hack

%make

%install

%makeinstall_std -C system
rm -f %{buildroot}%{_libdir}/*.a

%find_lang %{fname}

%files -f %{fname}.lang
%doc README
%{_bindir}/%{fname}
%{_mandir}/man1/%{fname}.*
