%include	/usr/lib/rpm/macros.php
%define		_class		DB
%define		_subclass	DataObject_FormBuilder_Frontend
%define		_status		beta
%define		_pearname	DB_DataObject_FormBuilder_Frontend
%include    %{_sourcedir}/php-pear-build-macros
Summary:	%{_pearname} - A frontend for data editing, inserting, and deleting based on DB_DataObject_FormBuilder and Structures_DataGrid
Name:		php-pear-%{_pearname}
Version:	0.7.0
Release:	0.6
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pearified.com/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8763423e6173f74f827b9bb5f95d7b43
URL:		http://pearified.com/package/DB_DataObject_FormBuilder_Frontend/
BuildRequires:	php-pear-PEAR >= 1:1.4.9
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-DB_DataObject_FormBuilder >= 1.0.0-2.RC5
Requires:	php-pear-HTML_Table >= 1.7.3
Requires:	php-pear-PEAR-core >= 1:1.4.9
Requires:	php-pear-Structures_DataGrid >= 0.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package gives a working framework for a DB data editor with
automatic link support and super-extensibility through DB_DataObject
and DB_DataObject_FormBuilder.

In PEAR status of this package is: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup
rm -f docs/%{_pearname}/docs/LGPL.txt

mv ./%{php_pear_dir}/{Pearified/DB,DB}
grep -rl Pearified/DB/DataObject/ . | xargs %{__sed} -i -e 's,Pearified/DB/DataObject/,DB/DataObject/,'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
#%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/DB/DataObject/FormBuilder/Frontend
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/AddRecord.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/ChooseTable.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/Controller.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/DeleteRecords.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/EditRecord.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/LimitColumn.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/ShowTable.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend/Search.php
%{php_pear_dir}/DB/DataObject/FormBuilder/Frontend.php
