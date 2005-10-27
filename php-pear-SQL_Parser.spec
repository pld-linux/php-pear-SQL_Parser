%include	/usr/lib/rpm/macros.php
%define		_class		SQL
%define		_subclass	Parser
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - an SQL Parser
Summary(pl):	%{_pearname} - parser SQL-a
Name:		php-pear-%{_pearname}
Version:	0.5
Release:	3
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a5b76c31e1914f5b1ce605d9d52c1751
URL:		http://pear.php.net/package/SQL_Parser/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is primarily an SQL parser, written with influences from a
variety of sources (mSQL, CPAN's SQL-Statement, mySQL). It also
includes a tokenizer (lexer) class and a reimplementation of the ctype
extension in PHP.

In PEAR status of this package is: %{_status}.

%description -l pl
Ta klasa jest przede wszystkim parserem SQL-a, napisanym pod wp³ywem
wielu ¼róde³ (mSQL, SQL-Statement z CPAN, mySQL). Zawiera tak¿e klasê
tokenizera (leksera) i w³asn± implementacjê rozszerzenia ctype z PHP.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
