%define modname xattr
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A27_%{modname}.ini

Summary:	Provides a interface to Extended attributes for PHP
Name:		php-%{modname}
Epoch:		1
Version:	1.2.0
Release:	11
Group:		Development/PHP
License:	PHP License
Url:		https://pecl.php.net/package/xattr
Source0:	http://pecl.php.net/get/xattr-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	attr-devel

%description
This package allows to manipulate extended attributes on filesystems that
support them. Requires libattr from Linux XFS project.

%prep
%setup -qn xattr-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .


%build
%serverbuild

phpize
%configure2_5x \
	--with-libdir=%{_lib} \
	--with-%{modname}=shared,%{_prefix}

%make
mv modules/*.so .

%install
install -d %{buildroot}%{_libdir}/php/extensions
install -d %{buildroot}%{_sysconfdir}/php.d

install -m755 %{soname} %{buildroot}%{_libdir}/php/extensions/

cat > %{buildroot}%{_sysconfdir}/php.d/%{inifile} << EOF
extension = %{soname}
EOF

%post
if [ -f /var/lock/subsys/httpd ]; then
    %{_initrddir}/httpd restart >/dev/null || :
fi

%postun
if [ "$1" = "0" ]; then
    if [ -f /var/lock/subsys/httpd ]; then
	%{_initrddir}/httpd restart >/dev/null || :
    fi
fi

%files 
%doc tests CREDITS package.xml
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/php.d/%{inifile}
%attr(0755,root,root) %{_libdir}/php/extensions/%{soname}

