%global debug_package %{nil}
%define major 0
%define libname %mklibname fife %{major}
%define devname %mklibname fife -d

Name:		unknown-horizons
Version:	2019.1
Release:	4
Source0:	https://github.com/unknown-horizons/unknown-horizons/releases/download/%{version}/unknown-horizons-%{version}.tar.gz
Patch0:		unknown-horizons-2019.1-replace-deprecated-to-distro-package.patch
Summary:	2D Realtime Strategy Simulation
URL:		https://unknown-horizons.org/
License:	GPL
Group:		System/Libraries
BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:	python-fifengine
BuildRequires:	python-setuptools
BuildRequires:	gettext
BuildRequires:	pkgconfig(python)
BuildRequires:  python-pillow
BuildRequires:  python-distro
Requires:	python
Requires:	python-fifengine
Requires:	python-future

%description
A 2D realtime strategy simulation with an emphasis on economy and city
building.

Expand your small settlement to a strong and wealthy colony, collect
taxes and supply your inhabitants with valuable goods.

Increase your power with a well balanced economy and with strategic trade
and diplomacy.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%py3_build

# force generation of atlas.sql
python3 horizons/engine/generate_atlases.py 2048

%install
%py3_install

desktop-file-install --dir %{buildroot}%{_datadir}/applications build/share/applications/unknown-horizons.desktop

cd %{buildroot}
find . -name "*.mo" |while read r; do
	L=`echo $r |cut -d/ -f7`
	echo "%%lang($L) /$(echo $r |cut -d/ -f2-)" >>%{name}.lang
done
cd -
mv %{buildroot}/%{name}.lang .

%files -f %{name}.lang
%{_gamesbindir}/%{name}
%{_datadir}/applications/unknown-horizons.desktop
%dir %{_datadir}/unknown-horizons
%{_datadir}/unknown-horizons/*.xml
%dir %{_datadir}/unknown-horizons/content
%{_datadir}/unknown-horizons/content/*.*
%{_datadir}/unknown-horizons/content/audio
%{_datadir}/unknown-horizons/content/fonts
%{_datadir}/unknown-horizons/content/gfx
%{_datadir}/unknown-horizons/content/gui
%dir %{_datadir}/unknown-horizons/content/lang
%{_datadir}/unknown-horizons/content/lang/*.*
%{_datadir}/unknown-horizons/content/maps
%{_datadir}/unknown-horizons/content/objects
%{_datadir}/unknown-horizons/content/packages
%{_datadir}/unknown-horizons/content/scenarios
%{_datadir}/pixmaps/unknown-horizons.xpm
%{_mandir}/man6/unknown-horizons.6*
%{python_sitelib}/horizons
%{python_sitelib}/UnknownHorizons*.egg-info
