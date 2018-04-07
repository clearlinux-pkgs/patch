#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD5BF9FEB0313653A (agruen@gnu.org)
#
Name     : patch
Version  : 2.7.6
Release  : 29
URL      : http://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz
Source0  : http://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz
Source99 : http://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: patch-bin
Requires: patch-doc
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: cve-2018-6951.patch
Patch2: 0001-Allow-input-files-to-be-missing-for-ed-style-patches.patch
Patch3: 0002-Fix-arbitrary-command-execution-in-ed-style-patches-.patch
Patch4: 0003-Invoke-ed-directly-instead-of-using-the-shell.patch

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
%setup -q -n patch-2.7.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523108837
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1523108837
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
