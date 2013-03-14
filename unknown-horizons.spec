%define icon_name      uk

Name:		unknown-horizons
Version:	2013.1b
Release:	1
Summary:	A popular economy and city building 2D RTS game
License:	GPLv2+ ; CC-BY-SA 3.0 ; OFL ;
Group:		Games/Strategy
Url:		http://www.unknown-horizons.org
Source:		%{name}-%{version}.tar.xz
Source1:	%{name}.svg
# Required, docbook-xsl-stylesheets : to build man page
BuildRequires:	docbook-style-xsl
BuildRequires:	fdupes
BuildRequires:	fife-devel >= 0.3.4
BuildRequires:	intltool
# Required, libxslt : to build man page
BuildRequires:	xsltproc
BuildRequires:	libxslt-devel
BuildRequires:	pkgconfig
BuildRequires:	python-devel
BuildRequires:	python-distutils-extra
BuildRequires:	desktop-file-utils
#Required imagemagick to fix desktop icon
BuildRequires:	imagemagick
Requires:	fife
Requires:	python
Requires:	python-yaml
Requires:	%{name}-data = %{version}
BuildArch:	noarch

%description
Unknown Horizons is a 2D real-time strategy simulation with an emphasis
on economy and city building. Expand your small settlement to a strong
and wealthy colony, collect taxes and supply your inhabitants with
valuable goods. Increase your power with a well balanced economy and
with strategic trade and diplomacy.

%package data
Summary:	Games data for the %{name} game
Conflicts:	%{name} < 2012.1
Requires:	%{name} = %{version}
BuildArch:	noarch

%description data
This package contains data files for %{name} game.

%prep
%setup -q -n %{name}

%build
# Build Unknown Horizons
python setup.py build

%install
python setup.py install \
  --prefix=%{_prefix} \
  --root=%{buildroot}
%find_lang %{name} %{name}-server %{name}.lang

rm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
# KDE has problems handling icon files starting with 'unknown' followed by a dash
# (ex: unknown-horizons.svg) and displays unknown.* icon. We fix this by changing
# the icon name in .desktop file.
sed -i "s/Icon=unknown-horizons/Icon=%{icon_name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{icon_name}.svg

desktop-file-install --vendor="" \
                     --dir %{buildroot}%{_datadir}/applications \
                     --remove-category="Simulation" \
                     %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%doc doc/AUTHORS.md doc/GPL doc/GPL_fontexception doc/LICENSE doc/CC doc/OFL doc/CHANGELOG
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{python_sitelib}/*.egg-info
%{python_sitelib}/horizons/
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/scalable/apps/%{icon_name}.svg

%files data
%{_datadir}/%{name}

