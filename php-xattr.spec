%define modname xattr
%define dirname %{modname}
%define soname %{modname}.so
%define inifile A27_%{modname}.ini

Summary:	Provides a interface to Extended attributes for PHP
Name:		php-%{modname}
Version:	1.2.0
Release:	1
Group:		Development/PHP
License:	PHP License
URL:		http://pecl.php.net/package/xattr
Source0:	http://pecl.php.net/get/xattr-%{version}.tgz
BuildRequires:	php-devel >= 3:5.2.0
BuildRequires:	attr-devel
Epoch:		1

%description
This package allows to manipulate extended attributes on filesystems that
support them. Requires libattr from Linux XFS project.

%prep

%setup -q -n xattr-%{version}
[ "../package.xml" != "/" ] && mv ../package.xml .


%build
%serverbuild

phpize
%configure2_5x --with-libdir=%{_lib} \
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


%changelog
* Wed May 02 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-23mdv2012.0
+ Revision: 794959
- added fixes from upstream svn
- rebuild for php-5.4.x

* Sun Jan 15 2012 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-22
+ Revision: 761127
- rebuild

* Wed Aug 24 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-21
+ Revision: 696379
- rebuilt for php-5.3.8

* Fri Aug 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-20
+ Revision: 695324
- rebuilt for php-5.3.7

* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-19
+ Revision: 667767
- mass rebuild

* Sat Mar 19 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-18
+ Revision: 646563
- rebuilt for php-5.3.6

* Sat Jan 08 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-17mdv2011.0
+ Revision: 629755
- rebuilt for php-5.3.5

* Mon Jan 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-16mdv2011.0
+ Revision: 628057
- ensure it's built without automake1.7

* Tue Nov 23 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-15mdv2011.0
+ Revision: 600189
- rebuild

* Sun Oct 24 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-14mdv2011.0
+ Revision: 588728
- rebuild

* Fri Mar 05 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-13mdv2010.1
+ Revision: 514715
- rebuilt for php-5.3.2

* Sun Feb 21 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-12mdv2010.1
+ Revision: 509097
- rebuild

* Sat Jan 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-11mdv2010.1
+ Revision: 485270
- rebuilt for php-5.3.2RC1

* Sat Nov 21 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-10mdv2010.1
+ Revision: 468097
- rebuilt against php-5.3.1

* Wed Sep 30 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-9mdv2010.0
+ Revision: 451227
- rebuild

* Sun Jul 19 2009 Raphaël Gertz <rapsys@mandriva.org> 1:1.1.0-8mdv2010.0
+ Revision: 397294
- Rebuild

* Wed May 13 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-7mdv2010.0
+ Revision: 375368
- rebuilt against php-5.3.0RC2

* Sun Mar 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-6mdv2009.1
+ Revision: 346704
- rebuilt for php-5.2.9

* Tue Feb 17 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-5mdv2009.1
+ Revision: 341518
- rebuilt against php-5.2.9RC2

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-4mdv2009.1
+ Revision: 321965
- rebuild

* Fri Dec 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-3mdv2009.1
+ Revision: 310228
- rebuilt against php-5.2.7

* Tue Jul 15 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-2mdv2009.0
+ Revision: 235885
- rebuild

* Mon Jul 07 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.1.0-1mdv2009.0
+ Revision: 232370
- 1.1.0

* Fri May 02 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-21mdv2009.0
+ Revision: 200121
- rebuilt against php-5.2.6

* Mon Feb 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-20mdv2008.1
+ Revision: 161961
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Nov 11 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-19mdv2008.1
+ Revision: 107581
- restart apache if needed

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1:1.0-18mdv2008.0
+ Revision: 90161
- rebuild

* Sat Sep 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-17mdv2008.0
+ Revision: 77466
- rebuilt against php-5.2.4

* Thu Aug 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-16mdv2008.0
+ Revision: 64310
- use the new %%serverbuild macro

* Thu Jun 14 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-15mdv2008.0
+ Revision: 39393
- use distro conditional -fstack-protector

* Fri Jun 01 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-14mdv2008.0
+ Revision: 33787
- rebuilt against new upstream version (5.2.3)

* Thu May 03 2007 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-13mdv2008.0
+ Revision: 21036
- rebuilt against new upstream version (5.2.2)


* Fri Feb 09 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0-12mdv2007.0
+ Revision: 118559
- rebuilt against new upstream php version (5.2.1)

* Wed Nov 08 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-11mdv2007.0
+ Revision: 78362
- fix deps

* Tue Nov 07 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-10mdv2007.0
+ Revision: 77413
- rebuilt for php-5.2.0

* Thu Nov 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-9mdv2007.1
+ Revision: 75381
- Import php-xattr

* Mon Aug 28 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-9
- rebuilt for php-5.1.6

* Thu Jul 27 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-8mdk
- rebuild

* Sat May 06 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-7mdk
- rebuilt for php-5.1.4

* Fri May 05 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-6mdk
- rebuilt for php-5.1.3

* Thu Feb 02 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-5mdk
- new group (Development/PHP) and iurt rebuild

* Sun Jan 15 2006 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-4mdk
- rebuilt against php-5.1.2

* Tue Nov 29 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-3mdk
- rebuilt against php-5.1.1

* Sat Nov 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-2mdk
- rebuilt against php-5.1.0

* Thu Nov 03 2005 Oden Eriksson <oeriksson@mandriva.com> 1:1.0-1mdk
- rebuilt against php-5.1.0RC4
- fix versioning

* Sun Oct 30 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0_1.0-0.RC1.2mdk
- rebuilt to provide a -debug package too

* Sun Oct 02 2005 Oden Eriksson <oeriksson@mandriva.com> 5.1.0_1.0-0.RC1.1mdk
- rebuilt against php-5.1.0RC1

* Wed Sep 07 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.5_1.0-1mdk
- rebuilt against php-5.0.5 (Major security fixes)

* Fri May 27 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4_1.0-1mdk
- rename the package

* Sun Apr 17 2005 Oden Eriksson <oeriksson@mandriva.com> 5.0.4_1.0-1mdk
- 5.0.4

* Sun Mar 20 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_1.0-4mdk
- use the %%mkrel macro

* Sat Feb 12 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_1.0-3mdk
- rebuilt against a non hardened-php aware php lib

* Sun Jan 16 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_1.0-2mdk
- rebuild due to hardened-php-0.2.6

* Fri Dec 17 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.3_1.0-1mdk
- rebuilt for php-5.0.3

* Sat Sep 25 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.2_1.0-1mdk
- rebuilt for php-5.0.2

* Tue Aug 24 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 5.0.1_1.0-1mdk
- initial mandrake package


