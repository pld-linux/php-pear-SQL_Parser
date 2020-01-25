%define		status		devel
%define		pearname	SQL_Parser
Summary:	%{pearname} - an SQL Parser
Summary(pl.UTF-8):	%{pearname} - parser SQL-a
Name:		php-pear-%{pearname}
Version:	0.7.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	de71135d2148008ac5f1cbc29b00be57
Patch0:		no-pure-ctype.patch
URL:		http://pear.php.net/package/SQL_Parser/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php(ctype)
Requires:	php-pear
Obsoletes:	php-pear-SQL_Parser-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class is primarily an SQL parser, written with influences from a
variety of sources (mSQL, CPAN's SQL-Statement, mySQL). It also
includes a tokenizer (lexer) class.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Ta klasa jest przede wszystkim parserem SQL-a, napisanym pod wpływem
wielu źródeł (mSQL, SQL-Statement z CPAN, mySQL). Zawiera także klasę
tokenizera (leksera).

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup
%patch0 -p1

install -d docs
mv .%{php_pear_dir}/data/SQL_Parser/TODO docs

# use php ext instead
%{__rm} .%{php_pear_dir}/SQL/Parser/ctype.php

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
