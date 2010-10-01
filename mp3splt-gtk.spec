Name:		mp3splt-gtk
Version:	0.6
Release:	%mkrel 1
Summary:	GTK2 utility to split MP3 and Ogg Files without decoding
Source0:	http://prdownloads.sourceforge.net/mp3splt/mp3splt-gtk-%{version}.tar.gz
URL:		http://mp3splt.sourceforge.net
Group:		Sound
License:	GPLv2+
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:  gstreamer0.10-devel
BuildRequires:  libgstreamer-plugins-base-devel
BuildRequires:	libmp3splt-devel
BuildRequires:	gtk2-devel >= 2.12.0
BuildRequires:	libpng-devel
BuildRequires:	audacious-devel

%description
%{name} is a GTK2 utility to split mp3 and ogg files selecting a begin and an
end time position, without decoding. It is very useful to split large mp3/ogg
to make smaller files or to split entire albums to obtain original tracks.

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--enable-audacious
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# desktop file
mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=mp3splt
GenericName=MP3/Ogg Splitter
Terminal=false
Icon=mp3splt-gtk
Exec=mp3splt-gtk
Type=Application
StartupNotify=false
Categories=Audio;AudioVideo;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*