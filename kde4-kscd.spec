%define		_state		stable
%define		orgname		kscd
%define		qtver		4.8.1

Summary:	KDE CD Player
Summary(pl.UTF-8):	Odtwarzacz CD dla KDE
Name:		kde4-%{orgname}
Version:	4.9.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	dbd066e2b10c8083ab3700ce051c92be
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libmusicbrainz3-devel >= 1:3.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	kde4-libkcddb-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-libkcddb >= %{version}
Requires:	kde4-kdebase >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CD Player with CDDB support. It can automatically update its CD
database with the Internet and show graphical interpretation of played
sounds.

%description -l pl.UTF-8
Odtwarzacz CD z obsługą CDDB. Automatycznie uaktualnia swoją bazę
danych o płytach CD z Internetem. Potrafi także wyświetlić ładną
graficzną interpretację granych dźwięków.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

#%find_lang kscd		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
# -f kscd.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kscd
%{_desktopdir}/kde4/kscd.desktop
%{_datadir}/config.kcfg/kscd.kcfg
%{_datadir}/apps/solid/actions/kscd-play-audiocd.desktop
%{_datadir}/apps/kscd
%{_iconsdir}/hicolor/*/apps/kscd.png
%{_iconsdir}/oxygen/*/actions/kscd-dock.png
%{_datadir}/dbus-1/interfaces/org.kde.kscd.cdplayer.xml
