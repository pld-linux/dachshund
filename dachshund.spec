Summary:	UML Visual Modeling Tool
Name:		dachshund
Version:	0.1.0
Release:	1
Copyright:	GPL
Group:		Gnome/Development
Source:		%{name}-%{version}.tar.gz
URL:		http://dachshund.sourceforge.net/
BuildRoot:	/var/tmp/%{name}-%{version}-root
Prefix:		/usr

Requires: gtk2 >= 1.3.11
Requires: libgnome >= 1.96.0
Requires: libgnomeui >= 1.96.0
Requires: libxml2 >= 2.4.12

%description
Dachshund is UML visual modeling tool for GNOME.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure --prefix=%prefix --sysconfdir=/etc

if [ "$SMP" != "" ]; then
	make -j$SMP "MAKE=make -j$SMP"
else
	make
fi

%install
make prefix=$RPM_BUILD_ROOT%{prefix} sysconfdir=$RPM_BUILD_ROOT/etc install

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{prefix}/bin/*
%{prefix}/share/dachshund/%{version}/pixmaps/*/*
%{prefix}/share/dachshund/%{version}/python/*/*

%changelog
* Fri Mar 29 2002 David Bryant <daveb@acres.com.au>
- files only includes the dachshund binary now
- added checks for the required libraries

* Thu Oct 4 2001 David Bryant <daveb@acres.com.au>
- wrote this file
