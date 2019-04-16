%define major 0
%define libname %mklibname fife %{major}
%define devname %mklibname fife -d

Name:		unknown-horizons
Version:	2019.1
Release:	1
Source0:	https://github.com/unknown-horizons/unknown-horizons/releases/download/%{version}/unknown-horizons-%{version}.tar.gz
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
Requires:	python
Requires:	python-fifengine

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
%py3_build build_i18n

# force generation of atlas.sql
python3 horizons/engine/generate_atlases.py 2048

%install
%py3_install --root=%{buildroot}

desktop-file-install --dir %{buildroot}%{_datadir}/applications build/share/applications/unknown-horizons.desktop

%find_lang %{name}
%find_lang %{name}-server

%files -f %{name}.lang -f %{name}-server.lang
%{_bindir}/unknown-horizons
%{_datadir}/applications/unknown-horizons.desktop
%{_datadir}/unknown-horizons
%{_datadir}/pixmaps/unknown-horizons.xpm
%{_mandir}/man6/unknown-horizons.6*
%{python_sitelib}/horizons
%{python_sitelib}/UnknownHorizons*.egg-info
