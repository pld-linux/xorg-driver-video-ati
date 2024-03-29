#
# Conditional build:
%bcond_without	glamor		# glamor, new GL-based acceleration
#
%define	libdrm_ver	2.4.89
Summary:	X.org video drivers for ATI Radeon adapters
Summary(pl.UTF-8):	Sterowniki obrazu X.org do kart graficznych ATI Radeon
Name:		xorg-driver-video-ati
Version:	22.0.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/driver/xf86-video-ati-%{version}.tar.xz
# Source0-md5:	33c7b049c526aa9bf3654890c4d7b860
URL:		https://xorg.freedesktop.org/
BuildRequires:	Mesa-libGL-devel
BuildRequires:	Mesa-libgbm-devel >= 10.6
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libdrm-devel >= %{libdrm_ver}
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.16
BuildRequires:	xz
%{?requires_xorg_xserver_videodrv}
Requires:	Mesa-libgbm >= 10.6
Requires:	libdrm >= %{libdrm_ver}
Requires:	xorg-xserver-libdri >= 1.16
Requires:	xorg-xserver-libglx >= 1.16
Requires:	xorg-xserver-server >= 1.16
Provides:	xorg-driver-video
Obsoletes:	X11-driver-ati < 1:7.0.0
Obsoletes:	X11-driver-radeon < 1:7.0.0
Obsoletes:	XFree86-ATI < 4
Obsoletes:	XFree86-driver-ati < 1:7.0.0
Obsoletes:	XFree86-driver-radeon < 1:7.0.0
Conflicts:	vbetool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains X.org drivers for ATI video adapters:
- "ati" wrapper driver, which automatically loads proper driver
  depending on hardware: radeon (included in this package),
  r128 (included in xorg-driver-video-r128 package), mach64
  (included in xorg-driver-video-mach64 package);
- "radeon" driver for ATI Radeon adapters.
The "radeon" driver supports PCI and AGP video cards based on the
following ATI chips:
- R100 (Radeon 7200),
- RV100 (Radeon 7000(VE), M6, RN50/ES1000),
- RS100 (Radeon IGP320(M)),
- RV200 (Radeon 7500, M7, FireGL 7800),
- RS200 (Radeon IGP330(M)/IGP340(M)),
- RS250 (Radeon Mobility 7000 IGP),
- R200 (Radeon 8500, 9100, FireGL 8800/8700),
- RV250 (Radeon 9000PRO/9000, M9),
- RV280 (Radeon 9200PRO/9200/9200SE/9250, M9+),
- RS300 (Radeon 9100 IGP),
- RS350 (Radeon 9200 IGP),
- RS400/RS480 (Radeon XPRESS 200/200M/1100 IGP),
- R300 (Radeon 9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1),
- R350 (Radeon 9800PRO/9800SE/9800, FireGL X2),
- R360 (Radeon 9800XT),
- RV350 (Radeon 9600PRO/9600SE/9600/9550, M10/M11, FireGL T2),
- RV360 (Radeon 9600XT),
- RV370 (Radeon X300, M22),
- RV380 (Radeon X600, M24),
- RV410 (Radeon X700, M26 PCIE),
- R420 (Radeon X800 AGP),
- R423/R430 (Radeon X800, M28 PCIE),
- R480/R481 (Radeon X850 PCIE/AGP),
- RV505/RV515/RV516/RV550 (Radeon X1300/X1400/X1500/X2300),
- R520 (Radeon X1800),
- RV530/RV560 (Radeon X1600/X1650/X1700),
- RV570/R580 (Radeon X1900/X1950),
- RS600/RS690/RS740 (Radeon X1200/X1250/X2100),
- R600 (Radeon HD 2900),
- RV610/RV630 (Radeon HD 2400/2600/2700/4200/4225/4250),
- RV620/RV635 (Radeon HD 3410/3430/3450/3470/3650/3670),
- RV670 (Radeon HD 3850/3870),
- RS780/RS880 (Radeon HD 3100/3200/3300/4100/4200/4250/4290),
- RV710/RV730 (Radeon HD 4330/4350/4550/4650/4670/5145/5165/530v/545v/560v/565v),
- RV740/RV770/RV790 (Radeon HD 4770/4730/4830/4850/4860/4870/4890),
- CEDAR (Radeon HD 5430/5450/6330/6350/6370),
- REDWOOD (Radeon HD 5550/5570/5650/5670/5730/5750/5770/6530/6550/6570),
- JUNIPER (Radeon HD 5750/5770/5830/5850/5870/6750/6770/6830/6850/6870),
- CYPRESS (Radeon HD 5850/5850/5870),
- HEMLOCK (Radeon HD 5970),
- PALM (Radeon HD 6310/6250),
- SUMO/SUMO2 (Radeon HD 6370/6380/6410/6480/6520/6530/6550/6620),
- BARTS (Radeon HD 6790/6850/6870/6950/6970/6990),
- TURKS (Radeon HD 6570/6630/6650/6670/6730/6750/6770),
- CAICOS (Radeon HD 6430/6450/6470/6490),
- CAYMAN (Radeon HD 6950/6970/6990),
- ARUBA (Radeon HD 7000 series),
- TAHITI (Radeon HD 7900 series),
- PITCAIRN (Radeon HD 7800 series),
- VERDE (Radeon HD 7700 series),
- OLAND (Radeon HD 8000 series),
- HAINAN (Radeon HD 8000 series),
- BONAIRE (Radeon HD 7790 series),
- KAVERI (APU),
- KABINI (APU),
- HAWAII (Radeon R9 series),
- MULLINS (APU).

%description -l pl.UTF-8
Ten pakiet zawiera sterowniki obrazu X.org do kart graficznych ATI:
- sterownik obudowujący "ati", który automatycznie wczytuje właściwy
  sterownik w zależności od sprzętu: radeon (załączony w tym
  pakiecie), r128 (z pakietu xorg-driver-video-r128), mach64 (z
  pakietu xorg-driver-video-mach64);
- sterownik "radeon" do kart ATI Radeon.
Sterownik "radeon" obsługuje karty graficzne PCI i AGP oparte na
następujących układach ATI:
- R100 (Radeon 7200),
- RV100 (Radeon 7000(VE), M6, RN50/ES1000),
- RS100 (Radeon IGP320(M)),
- RV200 (Radeon 7500, M7, FireGL 7800),
- RS200 (Radeon IGP330(M)/IGP340(M)),
- RS250 (Radeon Mobility 7000 IGP),
- R200 (Radeon 8500, 9100, FireGL 8800/8700),
- RV250 (Radeon 9000PRO/9000, M9),
- RV280 (Radeon 9200PRO/9200/9200SE/9250, M9+),
- RS300 (Radeon 9100 IGP),
- RS350 (Radeon 9200 IGP),
- RS400/RS480 (Radeon XPRESS 200/200M/1100 IGP),
- R300 (Radeon 9700PRO/9700/9500PRO/9500/9600TX, FireGL X1/Z1),
- R350 (Radeon 9800PRO/9800SE/9800, FireGL X2),
- R360 (Radeon 9800XT),
- RV350 (Radeon 9600PRO/9600SE/9600/9550, M10/M11, FireGL T2),
- RV360 (Radeon 9600XT),
- RV370 (Radeon X300, M22),
- RV380 (Radeon X600, M24),
- RV410 (Radeon X700, M26 PCIE),
- R420 (Radeon X800 AGP),
- R423/R430 (Radeon X800, M28 PCIE),
- R480/R481 (Radeon X850 PCIE/AGP),
- RV505/RV515/RV516/RV550 (Radeon X1300/X1400/X1500/X2300),
- R520 (Radeon X1800),
- RV530/RV560 (Radeon X1600/X1650/X1700),
- RV570/R580 (Radeon X1900/X1950),
- RS600/RS690/RS740 (Radeon X1200/X1250/X2100),
- R600 (Radeon HD 2900),
- RV610/RV630 (Radeon HD 2400/2600/2700/4200/4225/4250),
- RV620/RV635 (Radeon HD 3410/3430/3450/3470/3650/3670),
- RV670 (Radeon HD 3850/3870),
- RS780/RS880 (Radeon HD 3100/3200/3300/4100/4200/4250/4290),
- RV710/RV730 (Radeon HD 4330/4350/4550/4650/4670/5145/5165/530v/545v/560v/565v),
- RV740/RV770/RV790 (Radeon HD 4770/4730/4830/4850/4860/4870/4890),
- CEDAR (Radeon HD 5430/5450/6330/6350/6370),
- REDWOOD (Radeon HD 5550/5570/5650/5670/5730/5750/5770/6530/6550/6570),
- JUNIPER (Radeon HD 5750/5770/5830/5850/5870/6750/6770/6830/6850/6870),
- CYPRESS (Radeon HD 5850/5850/5870),
- HEMLOCK (Radeon HD 5970),
- PALM (Radeon HD 6310/6250),
- SUMO/SUMO2 (Radeon HD 6370/6380/6410/6480/6520/6530/6550/6620),
- BARTS (Radeon HD 6790/6850/6870/6950/6970/6990),
- TURKS (Radeon HD 6570/6630/6650/6670/6730/6750/6770),
- CAICOS (Radeon HD 6430/6450/6470/6490),
- CAYMAN (Radeon HD 6950/6970/6990),
- ARUBA (Radeon HD z serii 7000),
- TAHITI (Radeon HD z serii 7900),
- PITCAIRN (Radeon HD z serii 7800),
- VERDE (Radeon HD z serii 7700),
- OLAND (Radeon HD z serii 8000),
- HAINAN (Radeon HD z serii 8000),
- BONAIRE (Radeon HD z serii 7790),
- KAVERI (APU),
- KABINI (APU),
- HAWAII (Radeon z serii R9),
- MULLINS (APU).

%prep
%setup -q -n xf86-video-ati-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{!?with_glamor:--disable-glamor}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ati_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/radeon_drv.so
%{_datadir}/X11/xorg.conf.d/10-radeon.conf
%{_mandir}/man4/ati.4*
%{_mandir}/man4/radeon.4*
