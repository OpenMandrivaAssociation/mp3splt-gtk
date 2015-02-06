Name:		mp3splt-gtk
Version:	0.7.1
Release:	4
Summary:	GTK2 utility to split MP3 and Ogg Files without decoding
Source0:	http://prdownloads.sourceforge.net/mp3splt/mp3splt-gtk-%{version}.tar.gz
URL:		http://mp3splt.sourceforge.net
Group:		Sound
License:	GPLv2+
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	libmp3splt-devel
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libpng)
#BuildRequires:	pkgconfig(audacious)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(libgnomeui-2.0)
BuildRequires:	rarian

%description
%{name} is a GTK2 utility to split mp3 and ogg files selecting a begin
and an end time position, without decoding. It is very useful to split
large mp3/ogg to make smaller files or to split entire albums to obtain
original tracks.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--disable-audacious
%make

%install
%makeinstall_std

# desktop file
install -Dpm0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}*.*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*


%changelog
* Thu Nov 24 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7.1-1mdv2011.0
+ Revision: 733216
- Disable Audacious support for now
- New version 0.7.1

* Thu Aug 18 2011 Andrey Bondrov <abondrov@mandriva.org> 0.7-1
+ Revision: 695194
- New version 0.7

* Sun Mar 06 2011 Jani Välimaa <wally@mandriva.org> 0.6.1a-1
+ Revision: 642305
- new version 0.6.1a
- add patches to fix Makefile and .desktop file
- use upstream .desktop file

* Fri Oct 01 2010 Jani Välimaa <wally@mandriva.org> 0.6-1mdv2011.0
+ Revision: 582294
- new version 0.6
- drop unneeded patch

* Fri Aug 27 2010 Jani Välimaa <wally@mandriva.org> 0.5.9-1mdv2011.0
+ Revision: 573592
- import mp3splt-gtk

