Summary:	ATI video driver
Summary(pl):	Sterownik video ATI
Name:		xorg-driver-video-ati
Version:	6.5.6.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/driver/xf86-video-ati-%{version}.tar.bz2
# Source0-md5:	2dfc216efba787ce8b985dcb84251031
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	Mesa-devel
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ATI video driver.

%description -l pl
Sterownik video ATI.

%prep
%setup -q -n xf86-video-ati-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*{.la,.a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xorg/modules/*/*.so
%{_mandir}/man4x/*.4x*
