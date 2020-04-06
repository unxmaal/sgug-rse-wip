Name:     libopusenc
Version:  0.2.1
Release:  3%{?dist}
Summary:  A library that provides an easy way to encode Ogg Opus files
License:  BSD
URL:      https://opus-codec.org/

Source0:  https://archive.mozilla.org/pub/opus/%{name}-%{version}.tar.gz

BuildRequires: gcc
# BuildRequires: doxygen
BuildRequires: opus-devel

%description
A library that provides an easy way to encode Ogg Opus files.

%package  devel
Summary:  Development package for libopusenc
Requires: opus-devel
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for development with libopusenc.

%prep
%setup -q

%build
%configure --disable-static

%make_build

%install
%make_install

# Remove libtool archives
find %{buildroot} -type f -name "*.la" -delete
rm -rf %{buildroot}%{_datadir}/doc/libopusenc/

%check
make check %{?_smp_mflags} V=1

#%%ldconfig_scriptlets

%files
%license COPYING
%{_libdir}/libopusenc.so.*

#%%files devel
#%%doc doc/html
%{_includedir}/opus/opusenc.h
%{_libdir}/libopusenc.so
%{_libdir}/pkgconfig/libopusenc.pc

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan  7 2019 Peter Robinson <pbrobinson@fedoraproject.org> 0.2.1-1
- New upstream 0.2.1 release

* Wed Sep 19 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.2-1
- New upstream 0.2 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar  7 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.1-3
- Add gcc BR

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Nov 13 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.1.1-1
- New upstream 0.1.1 release

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun  9 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-1
- Initial package
