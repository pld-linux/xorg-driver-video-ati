Summary:	ATI video adapters driver
Summary(pl):	Sterownik do kart graficznych ATI
Name:		xorg-driver-video-ati
Version:	6.5.6.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-ati-%{version}.tar.bz2
# Source0-md5:	2dfc216efba787ce8b985dcb84251031
URL:		http://xorg.freedesktop.org/
BuildRequires:	Mesa-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libdrm-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86driproto-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-proto-xineramaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.1
BuildRequires:	xorg-xserver-server-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATI video adapters driver.

%description -l pl
Sterownik do kart graficznych ATI.

%prep
%setup -q -n xf86-video-ati-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	drivermandir=%{_mandir}/man4

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.ati README.r128
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/*.so
%attr(755,root,root) %{_libdir}/xorg/modules/multimedia/*.so
%{_mandir}/man4/*.4x*
