%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Table
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - makes the design of HTML tables easy, flexible, reusable and efficient
Summary(pl.UTF-8):	%{_pearname} - czyni tworzenie tabel HTML łatwym, elastycznym, efektywnym
Name:		php-pear-%{_pearname}
Version:	1.8.4
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	26a416f2d51c8b5ab4083f731f66dd5a
URL:		http://pear.php.net/package/HTML_Table/
BuildRequires:	php-pear-PEAR >= 1:1.5.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear >= 4:1.0-8.1
Requires:	php-pear-HTML_Common >= 1.2.3
Obsoletes:	php-pear-HTML_Table-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The PEAR::HTML_Table package provides methods for easy and efficient
design of HTML tables.
- Lots of customization options.
- Tables can be modified at any time.
- The logic is the same as standard HTML editors.
- Handles col and rowspans.
- PHP code is shorter, easier to read and to maintain.
- Tables options can be reused.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa PEAR::HTML_Table dostarcza metody do łatwego i efektywnego
tworzenia tabel HTML.
- wiele opcji dostosowawczych.
- tabele mogą być modyfikowane w każdym momencie.
- logika jest taka sama jak w standardowych edytorach HTML-a.
- obsługa atrybutów col i rowspans.
- kod PHP jest krótszy, łatwiejszy do czytania i konserwacji.
- opcje tabel mogą być ponownie używane.

Ta klasa ma w PEAR status: %{_status}.

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
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
