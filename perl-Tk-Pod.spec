%define upstream_name    Tk-Pod
%define upstream_version 0.9942

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Simple Pod browser with hypertext capabilities
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tk/Tk-Pod-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Pod::Simple)
BuildRequires:	perl(Text::English)
BuildRequires:	perl(Tk)
BuildRequires:	perl(Tk::HistEntry)

BuildArch:	noarch

%description
Simple Pod browser with hypertext capabilities in a 'Toplevel' widget

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests hang on build-system
#xvfb-run %make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_bindir}/tk*
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.993.900-2mdv2011.0
+ Revision: 658554
- rebuild for updated spec-helper

* Sat Jul 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.993.900-1mdv2011.0
+ Revision: 554487
- skip tests, they hang on the build-system
- import perl-Tk-Pod


* Tue May 18 2010 cpan2dist 0.9939-1mdv
- initial mdv release, generated with cpan2dist


