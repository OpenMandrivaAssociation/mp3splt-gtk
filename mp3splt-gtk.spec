Name:		mp3splt-gtk
Version:	0.6.1a
Release:	%mkrel 1
Summary:	GTK2 utility to split MP3 and Ogg Files without decoding
Source0:	http://prdownloads.sourceforge.net/mp3splt/mp3splt-gtk-%{version}.tar.gz
Patch0:		mp3splt-gtk-0.6.1-fix_makefile.patch
Patch1:		mp3splt-gtk-0.6.1-fix_desktop_file.patch
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
BuildRequires:	gnome-doc-utils
BuildRequires:	gnomeui2-devel

%description
%{name} is a GTK2 utility to split mp3 and ogg files selecting a begin and an
end time position, without decoding. It is very useful to split large mp3/ogg
to make smaller files or to split entire albums to obtain original tracks.

%prep
%setup -q
%patch0 -p0 -b .fix
%patch1 -p0 -b .desktop_fix

%build
%configure2_5x \
	--disable-rpath
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# desktop file
install -Dpm0644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name} --with-gnome

#there's no automatic way to add .omf files to lang list
for omf in %{buildroot}%{_datadir}/omf/%{name}/*-??*.omf;do 
echo "%lang($(basename $omf|sed -e s/.*-// -e s/.omf//)) $(echo $omf|sed -e s!%{buildroot}!!)" >> %{name}.lang
done

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}*.*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.*
