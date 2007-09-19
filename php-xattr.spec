%define modname xattr
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A27_%{modname}.ini

Summary:	Provides a interface to Extended attributes for PHP
Name:		php-%{modname}
Version:	1.0
Release:	%mkrel 18
Group:		Development/PHP
URL:		http://pecl.php.net/package/xattr
License:	PHP License
Source0:	xattr-%{version}.tar.bz2
Patch0:		xattr-1.0-version.diff
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	attr-devel
Epoch:		1
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package allows to manipulate extended attributes on filesystems that
support them. Requires libattr from Linux XFS project.

%prep

%setup -q -n xattr-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .

%patch0 -p0

%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
    --with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot} 

install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc tests CREDITS package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}
