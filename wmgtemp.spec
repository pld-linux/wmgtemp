Summary:	Temperature sensor dock app for WindowMaker
Summary(pl):	Dokowalny czujnik temperatury dla WindowMakera
Name:		wmgtemp
Version:	0.5
Release:	2
License:	Artistic
Vendor:		Roger Dunce <kronos@fluxcode.net>
Group:		X11/Window Managers/Tools
Source0:	http://www.fluxcode.net/%{name}-%{version}.tar.gz
Patch0:		%{name}-add-it87-chip.patch
Patch1:		%{name}-spelling.patch
Patch2:		%{name}-fix-configure-sensors.patch
Patch3:		%{name}-add-chip-scanning.patch
Patch4:		%{name}-fix-output.patch
Patch5:		%{name}-add-global-configuration-file.patch
Patch6:		%{name}-fix-makefiles.patch
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

%description -l pl
wmgtemp jest dokowalnym czujnikiem temperatury przeznaczonym do u¿ycia
z WindowMakerem. Wy¶wietla on temperatury CPU i p³yty g³ównej (zarówno
w postaci warto¶ci jak i graficznie) u¿ywaj±c pakietu lm_sensors i
biblioteki libsensors. Przy przekroczeniu zadanej przez u¿ytkownika
temperatury wy¶wietla ostrzegaj±ce ¶wiate³ka.

Wspieranymi urz±dzeniami (czujnikami) s± VIA686A, W83781D, W83627HF,
AS99127F i ADM1021. Jest tak¿e dostêpne wsparcie dla innych urz±dzeñ
za pomoc± skanowania po dostêpnych czujnikach. Oryginalnie pakiet ten
zosta³ napisany dla VIA686A i jest przetestowany tylko dla tego
czujnika.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
%{__make} depend all \
	CC="%{__cc}" CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR="%{_mandir}" \
	BINDIR="%{_bindir}"

install examples/wmgtemprc $RPM_BUILD_ROOT%{_sysconfdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Artistic BUGS CREDITS README TODO
%attr(755,root,root) %{_bindir}/wmgtemp
%{_mandir}/man1/wmgtemp.1*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wmgtemprc
