%define icon_name      uk

Name:		unknown-horizons
Version:	2011.2
Release:	%mkrel 1
License:	GPLv2+ ; CC-BY-SA 3.0 ; OFL ;
Summary:	A popular economy and city building 2D RTS game
Url:		http://www.unknown-horizons.org
Group:		Games/Strategy
Source:		%{name}-%{version}.tar.bz2
Source1:	%{name}.svg
# Required, docbook-xsl-stylesheets : to build man page
BuildRequires:	docbook-style-xsl
BuildRequires:	fdupes
BuildRequires:	fife-devel
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

%description
Unknown Horizons is a 2D real-time strategy simulation with an emphasis
on economy and city building. Expand your small settlement to a strong
and wealthy colony, collect taxes and supply your inhabitants with
valuable goods. Increase your power with a well balanced economy and
with strategic trade and diplomacy.

%prep
%setup -q -n %{name}

%build
# Build Unknown Horizons
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install \
  --prefix=%{_prefix} \
  --root=%{buildroot}
%find_lang %{name}

%{__rm} %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
# KDE has problems handling icon files starting with 'unknown' followed by a dash
# (ex: unknown-horizons.svg) and displays unknown.* icon. We fix this by changing
# the icon name in .desktop file.
sed -i "s/Icon=unknown-horizons/Icon=%{icon_name}/" %{buildroot}%{_datadir}/applications/%{name}.desktop
install -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{icon_name}.svg

desktop-file-install --vendor="" \
                     --dir %{buildroot}%{_datadir}/applications \
                     --remove-category="Simulation" \
                     %{buildroot}%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc doc/AUTHORS doc/GPL doc/GPL_fontexception doc/LICENSE doc/CC doc/OFL
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6.*
%{python_sitelib}/*.egg-info
%{python_sitelib}/horizons/
%dir %{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{icon_name}.svg
%{_datadir}/%{name}/settings-dist.xml
%{_datadir}/%{name}/content/

