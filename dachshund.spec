Summary:	UML Visual Modeling Tool
Summary(pl):	Narzêdzie do wizualnego modelowania UML
Name:		dachshund
Version:	0.1.0
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://prdownloads.sourceforge.net/dachshund/%{name}-%{version}.tar.gz
URL:		http://dachshund.sourceforge.net/
BuildRequires:	gtk+2-decel
BuildRequires:	libgnome-devel >= 1.96.0
BuildRequires:	libgnomeui-devel >= 1.96.0
BuildRequires:	libxml2-devel >= 2.4.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dachshund is UML visual modeling tool for GNOME.

%description -l pl
Dachshund to narzêdzie do wizualnego modelowania UML dla GNOME.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
# cannot these be simplified?
%dir %{_datadir}/dachshund
%dir %{_datadir}/dachshund/%{version}
%dir %{_datadir}/dachshund/%{version}/pixmaps
%dir %{_datadir}/dachshund/%{version}/pixmaps/*
%{_datadir}/dachshund/%{version}/pixmaps/*/*
%dir %{_datadir}/dachshund/%{version}/python
%dir %{_datadir}/dachshund/%{version}/python/*
%{_datadir}/dachshund/%{version}/python/*/*
