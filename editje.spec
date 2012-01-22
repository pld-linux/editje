Summary:	WYSIWYG editor for Edje files
Summary(pl.UTF-8):	Edytor WYSIWYG do plików Edje
Name:		editje
Version:	0.9.3
Release:	1
License:	LGPL v3
Group:		Applications
Source0:	http://download.enlightenment.org/snapshots/2010-11-12/%{name}-%{version}.tar.bz2
# Source0-md5:	bc7d54c1b2a1837da8675cc1169fdd0f
URL:		http://trac.enlightenment.org/e/wiki/Editje
BuildRequires:	edje
BuildRequires:	edje-devel
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.5
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	edje
Requires:	python >= 1:2.5
Requires:	python-edje
Requires:	python-elementary
Requires:	python-evas
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Editje is a tool designed to make the development of user interfaces
for Edje easy and quick. It's a WYSIWYG (What You See Is What You Get)
editor for Edje (.edc/.edj) files.

It is written in Python-Elementary and it's Free Software released
under the GNU GPL  License version 3 (GPL v3).

%description -l pl.UTF-8
Editje to narzędzia mające ułątwić i przyspieszyć tworzenie
interfejsów użytkownika dla Edje. Jest to edytor WYSIWYG do plików
Edje (.edc/.edj).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

# icon is not themed, so install to %{_pixmapsdir}
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	icondir=%{_pixmapsdir}

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/editje-bin
# obsolete gnome specific file?
#%{_datadir}/application-registry/editje.applications
%{_datadir}/editje
%{_desktopdir}/editje.desktop
%{_pixmapsdir}/editje.png
%{py_sitescriptdir}/editje
