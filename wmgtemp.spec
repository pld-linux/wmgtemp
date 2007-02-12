Summary:	Temperature sensor dock app for WindowMaker
Summary(pl.UTF-8):	Dokowalny czujnik temperatury dla WindowMakera
Name:		wmgtemp
Version:	0.7
Release:	2
License:	Artistic
Vendor:		Roger Dunce <kronos@fluxcode.net>
Group:		X11/Window Managers/Tools
Source0:	http://www.fluxcode.net/%{name}-%{version}.tar.gz
# Source0-md5:	11b179fbb2f667db7e0c8ddb63a986ce
Source1:	%{name}.desktop
Patch0:		%{name}-fix-output.patch
Patch1:		%{name}-add-global-configuration-file.patch
Patch2:		%{name}-fix-makefiles.patch
URL:		http://www.fluxcode.net/
BuildRequires:	XFree86-devel
BuildRequires:	lm_sensors-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmgtemp is a dockable/swallowed applet intended for use with
WindowMaker. It displays the CPU and System temperatures (both in
numerically and graphically) using the lm_sensors package and
libsensors library. It provides high temperature warning lights.

Supported devices are VIA686A, W83781D, W83627HF, AS99127F and
ADM1021. There is also generic sensors support. This package is tested
to work only with VIA686A.

%description -l pl.UTF-8
wmgtemp jest dokowalnym czujnikiem temperatury przeznaczonym do użycia
z WindowMakerem. Wyświetla on temperatury CPU i płyty głównej (zarówno
w postaci wartości jak i graficznie) używając pakietu lm_sensors i
biblioteki libsensors. Przy przekroczeniu zadanej przez użytkownika
temperatury wyświetla ostrzegające światełka.

Wspieranymi urządzeniami (czujnikami) są VIA686A, W83781D, W83627HF,
AS99127F i ADM1021. Jest także dostępne wsparcie dla innych urządzeń
za pomocą skanowania po dostępnych czujnikach. Oryginalnie pakiet ten
został napisany dla VIA686A i jest przetestowany tylko dla tego
czujnika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} depend all \
	CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR="%{_mandir}" \
	BINDIR="%{_bindir}"

install examples/wmgtemprc $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Artistic BUGS CREDITS README TODO
%attr(755,root,root) %{_bindir}/wmgtemp
%{_mandir}/man1/wmgtemp.1*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/wmgtemprc
%{_desktopdir}/docklets/*
