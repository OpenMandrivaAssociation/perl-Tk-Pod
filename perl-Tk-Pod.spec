%define upstream_name    Tk-Pod
%define upstream_version 0.9939

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Simple Pod browser with hypertext capabilities
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tk/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Temp)
BuildRequires: perl(Pod::Simple)
BuildRequires: perl(Text::English)
BuildRequires: perl(Tk)
BuildRequires: perl(Tk::HistEntry)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Simple Pod browser with hypertext capabilities in a 'Toplevel' widget

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
# tests hang on build-system
#xvfb-run %make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_bindir}/tk*
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*

