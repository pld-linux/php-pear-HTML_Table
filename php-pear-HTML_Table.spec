%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	Table
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - makes the design of HTML tables easy, flexible, reusable and efficient
Summary(pl):	%{_pearname} - czyni tworzenie tabel HTML ³atwym, elastycznym, efektywnym
Name:		php-pear-%{_pearname}
Version:	1.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
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

%description -l pl
Klasa PEAR::HTML_Table dostarcza metody do ³atwego i efektywnego
tworzenia tabel HTML.
- wiele opcji dostosowawczych.
- tabele mog± byæ modyfikowane w ka¿dym momencie.
- logika jest taka sama jak w standardowych edytorach HTML-a.
- obs³uga atrybutów col i rowspans.
- kod PHP jest krótszy, ³atwiejszy do czytania i konserwacji.
- opcje tabel mog± byæ ponownie u¿ywane.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
