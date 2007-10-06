
Summary:	X.org video drivers for ATI adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI
Name:		xorg-driver-video-ati
Version:	6.7.195
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.bz2
# Source0-md5:	2f11b8e699fadd93e6932b07cc01bc64
Patch0:		%{name}-radeon-ddc6.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel >= 2.0
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.1.0
BuildRequires:  rpmbuild(macros) >= 1.389
%requires_xorg_xserver_videodrv
Requires:	xorg-xserver-server >= 1.1.0
Obsoletes:	X11-driver-ati < 1:7.0.0
Obsoletes:	X11-driver-r128 < 1:7.0.0
Obsoletes:	X11-driver-radeon < 1:7.0.0
Obsoletes:	XFree86-ATI
Obsoletes:	XFree86-Mach32
Obsoletes:	XFree86-Mach64
Obsoletes:	XFree86-Rage128
Obsoletes:	XFree86-driver-ati < 1:7.0.0
Obsoletes:	XFree86-driver-r128 < 1:7.0.0
Obsoletes:	XFree86-driver-radeon < 1:7.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video drivers for ATI adapters:
- ati driver which supports most of chips from VGAWonder series
  (18800, 18800-1, 28800-2, 28800-4, 28800-5, 28800-6), Mach32 series
  (68800-3, 68800-6, 68800AX, 68800LX) and Mach64 series (88800GX-C,
  88800GX-D, 88800GX-E, 88800GX-F, 88800CX, 264CT, 264ET, 264VT, 264GT
  (3D Rage), 264VT-B, 264VT3, 264VT4, 264GT-B (3D Rage II), 3D Rage
  IIc, 3D Rage Pro, 3D Rage LT, 3D Rage LT Pro, 3D Rage XL, 3D Rage
  XC, 3D Rage Mobility (including the -M and -P variants)),
- r128 driver which supports all ATI Rage 128 based video cards
  including the Rage Fury AGP 32MB, the XPERT 128 AGP 16MB and the
  XPERT 99 AGP 8MB,
- radeon driver which supports PCI and AGP video cards based on the
  following ATI chips: R100 (Radeon 7200), RV100 (Radeon 7000(VE),
  M6), RS100 (Radeon IGP320(M)), RV200 (Radeon 7500, M7, FireGL 7800),
  RS200 (Radeon IGP330(M)/IGP340(M)), RS250 (Radeon Mobility 7000
  IGP), R200 (Radeon 8500, 9100, FireGL 8800/8700), RV250 (Radeon
  9000PRO/9000, M9), RS300 (Radeon 9100 IGP), RS350 (Radeon 9200 IGP),
  RS400 (Radeon XPRESS 200/200M IGP), RV280 (Radeon 9200PRO/9200/
  9200SE, M9+); additionally it partially (2D only) supports video
  cards based on the following chips: R300 (Radeon 9700PRO/9700/
  9500PRO/9500/9600TX, FireGL X1/Z1), R350 (Radeon 9800PRO/9800SE/
  9800, FireGL X2), R360 (Radeon 9800XT), RV350 (Radeon 9600PRO/
  9600SE/9600, M10/M11, FireGL T2), RV360 (Radeon 9600XT), RV370
  (Radeon X300, M22), RV380 (Radeon X600), RV410 (Radeon X700, M26
  PCIE), R420 (Radeon X800 AGP), R423/R430 (Radeon X800, M28 PCIE),
  R480/R481 (Radeon X850 PCIE/AGP).

%description -l pl.UTF-8
Sterowniki obrazu X.org do kart graficznych ATI:
- sterownik ati obsługujący większość kart z serii VGAWonder (18800,
  18800-1, 28800-2, 28800-4, 28800-5, 28800-6), Mach32 (68800-3,
  68800-6, 68800AX, 68800LX) oraz Mach64 (88800GX-C, 88800GX-D,
  88800GX-E, 88800GX-F, 88800CX, 264CT, 264ET, 264VT, 264GT (3D Rage),
  264VT-B, 264VT3, 264VT4, 264GT-B (3D Rage II), 3D Rage IIc, 3D Rage
  Pro, 3D Rage LT, 3D Rage LT Pro, 3D Rage XL, 3D Rage XC, 3D Rage
  Mobility (włącznie z wariantami -M i -P)),
- sterownik r128 obsługujący wszystkie karty graficzne oparte na
  układzie ATI Rage 128, włącznie z Rage Fury AGP 32MB, XPERT 128 AGP
  16MB i XPERT 99 AGP 8MB,
- sterownik radeon obsługujący karty graficzne PCI i AGP oparte na
  następujących układach ATI: R100 (Radeon 7200), RV100 (Radeon
  7000(VE), M6), RS100 (Radeon IGP320(M)), RV200 (Radeon 7500, M7,
  FireGL 7800), RS200 (Radeon IGP330(M)/IGP340(M)), RS250 (Radeon
  Mobility 7000 IGP), R200 (Radeon 8500, 9100, FireGL 8800/8700),
  RV250 (Radeon 9000PRO/9000, M9), RS300 (Radeon 9100 IGP), RS350
  (Radeon 9200 IGP), RS400 (Radeon XPRESS 200/200M IGP), RV280 (Radeon
  9200PRO/9200/9200SE, M9+); a ponadto częściowo (tylko 2D)
  obsługujący karty oparte na następujących układach: R300 (Radeon
  9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1), R350 (Radeon
  9800PRO/9800SE/9800, FireGL X2), R360 (Radeon 9800XT), RV350 (Radeon
  9600PRO/9600SE/9600, M10/M11, FireGL T2), RV360 (Radeon 9600XT),
  RV370 (Radeon X300, M22), RV380 (Radeon X600), RV410 (Radeon X700,
  M26 PCIE), R420 (Radeon X800 AGP), R423/R430 (Radeon X800, M28
  PCIE), R480/R481 (Radeon X850 PCIE/AGP).

%prep
%setup -q -n xf86-video-ati-%{version}
%patch0 -p1

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
%doc COPYING README.ati README.r128
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ati_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/atimisc_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/r128_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeon_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre200_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre_detect_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/theatre_drv.so
%if %{with tv_output}
%doc src/README.tvout
%{_libdir}/xorg/modules/multimedia/theater_out_drv.so
%endif
%{_mandir}/man4/ati.4*
%{_mandir}/man4/r128.4*
%{_mandir}/man4/radeon.4*
