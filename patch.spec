#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xD5BF9FEB0313653A (agruen@gnu.org)
#
Name     : patch
Version  : 2.7.6
Release  : 45
URL      : https://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz
Source0  : https://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz
Source1  : https://mirrors.kernel.org/gnu/patch/patch-2.7.6.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: patch-bin = %{version}-%{release}
Requires: patch-license = %{version}-%{release}
Requires: patch-man = %{version}-%{release}
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : ed
BuildRequires : gettext-bin
BuildRequires : glibc-locale
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: cve-2018-6951.patch
Patch2: 0001-Allow-input-files-to-be-missing-for-ed-style-patches.patch
Patch3: 0002-Fix-arbitrary-command-execution-in-ed-style-patches-.patch
Patch4: 0003-Invoke-ed-directly-instead-of-using-the-shell.patch
Patch5: 0001-Don-t-leak-temporary-file-on-failed-ed-style-patch.patch
Patch6: cve-2018-1000156.patch
Patch7: cve-2018-6952.patch
Patch8: CVE-2019-13636.patch

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
Requires: patch-license = %{version}-%{release}

%description bin
bin components for the patch package.


%package license
Summary: license components for the patch package.
Group: Default

%description license
license components for the patch package.


%package man
Summary: man components for the patch package.
Group: Default

%description man
man components for the patch package.


%prep
%setup -q -n patch-2.7.6
cd %{_builddir}/patch-2.7.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604362861
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -fzero-call-used-regs=used "
%reconfigure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1604362861
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/patch
cp %{_builddir}/patch-2.7.6/COPYING %{buildroot}/usr/share/package-licenses/patch/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/patch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/patch/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/patch.1
