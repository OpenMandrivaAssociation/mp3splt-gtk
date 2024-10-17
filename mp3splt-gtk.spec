Name:		mp3splt-gtk
Version:	0.9.2
Release:	1
Summary:	GTK2 utility to split MP3 and Ogg Files without decoding
Source0:	http://prdownloads.sourceforge.net/mp3splt/mp3splt-gtk-%{version}.tar.gz
URL:		https://mp3splt.sourceforge.net
Group:		Sound
License:	GPLv2+
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	libmp3splt-devel
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(gnome-doc-utils)
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

