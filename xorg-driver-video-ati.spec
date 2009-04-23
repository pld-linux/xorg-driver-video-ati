Summary:	X.org video drivers for ATI Radeon adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI Radeon
Name:		xorg-driver-video-ati
Version:	6.12.2
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.bz2
# Source0-md5:	2bf50461378771497501ca7f678d36f3
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-glproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-libdri >= 1.1.0
Requires:	xorg-xserver-libglx >= 1.1.0
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	X11-driver-ati < 1:7.0.0
Obsoletes:	X11-driver-radeon < 1:7.0.0
Obsoletes:	XFree86-ATI
Obsoletes:	XFree86-driver-ati < 1:7.0.0
Obsoletes:	XFree86-driver-radeon < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video drivers for ATI Radeon adapters; supports PCI and AGP
video cards based on the following ATI chips:
- R100 (Radeon 7200),
- RV100 (Radeon 7000(VE), M6, RN50/ES1000),
- RS100 (Radeon IGP320(M)),
- RV200 (Radeon 7500, M7, FireGL 7800),
- RS200 (Radeon IGP330(M)/IGP340(M)),
- RS250 (Radeon Mobility 7000 IGP),
- R200 (Radeon 8500, 9100, FireGL 8800/8700),
- RV250 (Radeon 9000PRO/9000, M9),
- RS300 (Radeon 9100 IGP),
- RS350 (Radeon 9200 IGP),
- RS400 (Radeon XPRESS 200/200M IGP),
- RV280 (Radeon 9200PRO/9200/9200SE, M9+),
- R300 (Radeon 9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1),
- R350 (Radeon 9800PRO/9800SE/9800, FireGL X2),
- R360 (Radeon 9800XT),
- RV350 (Radeon 9600PRO/9600SE/9600, M10/M11, FireGL T2),
- RV360 (Radeon 9600XT),
- RV370 (Radeon X300, M22),
- RV380 (Radeon X600, M24),
- RV410 (Radeon X700, M26 PCIE),
- R420 (Radeon X800 AGP),
- R423/R430 (Radeon X800, M28 PCIE),
- R480/R481 (Radeon X850 PCIE/AGP),
- RV515 (Radeon X1300/X1400/X1500),
- R520 (Radeon X1800),
- RV530/RV560 (Radeon X1600/X1650/X1700),
- RV570/R580 (Radeon X1900/X1950),
- RS600/RS690 (Radeon X1200),
- R600 (Radeon HD 2900),
- RV610/RV630 (Radeon HD 2400/2600),
- RV670 (Radeon HD 3850/3870),
- RV620/RV635 (Radeon HD 3450/3470),
- RS780 (Radeon HD 3200).

%description -l pl.UTF-8
Sterownik obrazu X.org do kart graficznych ATI Radeon; obsługuje karty
graficzne PCI i AGP oparte na następujących układach ATI:
- R100 (Radeon 7200),
- RV100 (Radeon 7000(VE), M6, RN50/ES1000),
- RS100 (Radeon IGP320(M)),
- RV200 (Radeon 7500, M7, FireGL 7800),
- RS200 (Radeon IGP330(M)/IGP340(M)),
- RS250 (Radeon Mobility 7000 IGP),
- R200 (Radeon 8500, 9100, FireGL 8800/8700),
- RV250 (Radeon 9000PRO/9000, M9),
- RS300 (Radeon 9100 IGP),
- RS350 (Radeon 9200 IGP),
- RS400 (Radeon XPRESS 200/200M IGP),
- RV280 (Radeon 9200PRO/9200/9200SE, M9+),
- R300 (Radeon 9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1),
- R350 (Radeon 9800PRO/9800SE/9800, FireGL X2),
- R360 (Radeon 9800XT),
- RV350 (Radeon 9600PRO/9600SE/9600, M10/M11, FireGL T2),
- RV360 (Radeon 9600XT),
- RV370 (Radeon X300, M22),
- RV380 (Radeon X600),
- RV410 (Radeon X700, M26 PCIE),
- R420 (Radeon X800 AGP),
- R423/R430 (Radeon X800, M28 PCIE),
- R480/R481 (Radeon X850 PCIE/AGP),
- RV515 (Radeon X1300/X1400/X1500),
- R520 (Radeon X1800),
- RV530/RV560 (Radeon X1600/X1650/X1700),
- RV570/R580 (Radeon X1900/X1950),
- RS600/RS690 (Radeon X1200),
- R600 (Radeon HD 2900),
- RV610/RV630 (Radeon HD 2400/2600),
- RV670 (Radeon HD 3850/3870),
- RV620/RV635 (Radeon HD 3450/3470),
- RS780 (Radeon HD 3200).

%prep
%setup -q -n xf86-video-ati-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ati_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeon_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre200_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre_drv.so
%if %{with tv_output}
%doc src/README.tvout
%{_libdir}/xorg/modules/multimedia/theater_out_drv.so
%endif
%{_mandir}/man4/ati.4*
%{_mandir}/man4/radeon.4*
