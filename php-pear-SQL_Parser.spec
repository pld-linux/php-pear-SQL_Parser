%include	/usr/lib/rpm/macros.php
%define		_class		SQL
%define		_subclass	Parser
%define		_status		devel

%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - an SQL Parser
Summary(pl):	%{_pearname} - parser SQL-a
Name:		php-pear-%{_pearname}
Version:	0.3
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
# Source0-md5:	816263d9d9a0c590edc7098a2771738a
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is primarily an SQL parser, written with influences from a
variety of sources (mSQL, CPAN's SQL-Statement, mySQL). It also
includes a tokenizer (lexer) class and a reimplementation of the ctype
extension in PHP.

This class has in PEAR status: %{_status}

%description -l pl
Ta klasa jest przede wszystkim parserem SQL-a, napisanym pod wp³ywem
wielu ¼róde³ (mSQL, SQL-Statement z CPAN, mySQL). Zawiera tak¿e klasê
tokenizera (leksera) i w³asn± implementacjê rozszerzenia ctype z PHP.

Ta klasa ma w PEAR status: %{_status}

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/tests/*
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
