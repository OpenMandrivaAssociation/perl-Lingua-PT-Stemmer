%define upstream_name	 Lingua-PT-Stemmer
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Portuguese language stemming
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Lingua/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Lingua-PT-Stemmer module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3*/*

%changelog
* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2010.0
+ Revision: 402571
- update to 0.56

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.01-7mdv2009.0
+ Revision: 257582
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.01-6mdv2009.0
+ Revision: 245625
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.01-4mdv2008.1
+ Revision: 122860
- kill re-definition of %%buildroot on Pixel's request


* Mon Dec 04 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-4mdv2007.0
+ Revision: 90374
- spec cleanup
- Import perl-Lingua-PT-Stemmer

* Wed Nov 30 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-3mdk
- Rebuild

* Sat Oct 16 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.01-2mdk
- fix deps
- fix standard-dir-owned-by-package
- do cleanup

