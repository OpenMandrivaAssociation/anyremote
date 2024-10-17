Name:		anyremote
Version:	6.7.3
Release:	1
Summary:	Remote control through bluetooth or IR connection
License:	GPLv2+
Group:		System/Kernel and hardware
URL:		https://anyremote.sourceforge.net/
Source0:	http://nchc.dl.sourceforge.net/sourceforge/anyremote/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(bluez)
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(xtst)
BuildRequires:  pkgconfig(xi)

Requires:	bluez
Requires:	irda-utils
Suggests:	kanyremote
Suggests:	anyremote2html

%description
The overall goal of this project is to provide wireless remote control program
on Linux through Bluetooth, InfraRed, Wi-Fi or just TCP/IP connection.

anyRemote supports wide range of modern cell phones line Nokia, SonyEricsson,
Motorola and others.

anyRemote was developed as thin "communication" layer between Buetooth
(IR, Wi-Fi) capable phone and Linux, and in principle could be configured to
manage almost any software.

anyRemote could be used with:
* bluetooth connection with java client if cell phone is JSR82 compatible
* Wi-Fi connection with java client if phone supports Wi-Fi
* IR connection with java client if java realization in phone supports access
  to IR port
* ordinary TCP/IP connection with java client, if PC is connectable from
  the Internet
* bluetooth, infrared or cable connection using AT "modem" commands
* web interface
* it supports some of IR remotes supplied with TV tuner cards (like LIRC)
* it has limited support for Bemused clients 

anyRemote is a console application, but in addition there are GUI front ends
for Gnome and KDE.

%package doc
Summary:	Documentations for anyRemote
Group:		System/Kernel and hardware
Conflicts:	%{name} < 4.14
BuildArch:	noarch

%description doc
Documentation for anyRemote.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

# we'll cp our own doc files
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc NEWS README AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.*

%files doc
%doc doc-html/*
