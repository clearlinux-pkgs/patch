#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : patch
Version  : 2.7.5
Release  : 15
URL      : http://mirrors.kernel.org/gnu/patch/patch-2.7.5.tar.gz
Source0  : http://mirrors.kernel.org/gnu/patch/patch-2.7.5.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0+ GPL-3.0
Requires: patch-bin
Requires: patch-doc
BuildRequires : attr-dev

%description
This is GNU patch, which applies diff files to original files.
This version of patch has many changes made by the Free Software Foundation.
They add support for:
* handling arbitrary binary data and large files
* the unified context diff format that GNU diff can produce
* merging into files instead of creating reject files
* making GNU Emacs-style backup files
* improved interaction with RCS and SCCS
* the GNU conventions for option parsing and configuring and compilation.
* better POSIX compliance
They also fix some bugs.

%package bin
Summary: bin components for the patch package.
Group: Binaries

%description bin
bin components for the patch package.


%package doc
Summary: doc components for the patch package.
Group: Documentation

%description doc
doc components for the patch package.


%prep
%setup -q -n patch-2.7.5

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/patch

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
