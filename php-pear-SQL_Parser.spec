%include	/usr/lib/rpm/macros.php
%define		_status		devel
%define		_pearname	SQL_Parser
Summary:	%{_pearname} - an SQL Parser
Summary(pl.UTF-8):	%{_pearname} - parser SQL-a
Name:		php-pear-%{_pearname}
Version:	0.6.0
Release:	2
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	9ca052adc0c79f5df83b23c5786f5757
URL:		http://pear.php.net/package/SQL_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-SQL_Parser-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is primarily an SQL parser, written with influences from a
variety of sources (mSQL, CPAN's SQL-Statement, mySQL). It also
includes a tokenizer (lexer) class and a reimplementation of the ctype
extension in PHP.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ta klasa jest przede wszystkim parserem SQL-a, napisanym pod wpływem
wielu źródeł (mSQL, SQL-Statement z CPAN, mySQL). Zawiera także klasę
tokenizera (leksera) i własną implementację rozszerzenia ctype z PHP.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs
mv .%{php_pear_dir}/data/SQL_Parser/TODO docs

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/*
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/SQL
%{php_pear_dir}/SQL/Parser.php
%{php_pear_dir}/SQL/Parser
