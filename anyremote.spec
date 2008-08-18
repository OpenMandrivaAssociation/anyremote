%define name anyremote
%define version 4.7.1
%define release %mkrel 1

Summary: Remote control through bluetooth or IR connection
Name: %{name}
Version: %{version}
Release: %{release}
License: GPLv2+
Group: System/Kernel and hardware
BuildRequires: bluez-devel libxtst-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0: http://nchc.dl.sourceforge.net/sourceforge/anyremote/%name-%version.tar.gz
URL: http://anyremote.sourceforge.net/

%description
The overall goal of this project is to provide remote control service on Linux 
through Bluetooth, InfraRed, Wi-Fi or TCP/IP connection.
anyRemote supports wide range of modern cell phones like Nokia, SonyEricsson, 
Motorola and others. 

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# we'll cp our own doc files
rm -rf %buildroot%_datadir/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc NEWS README AUTHORS
%doc doc-html
%{_bindir}/%name
%{_datadir}/%name
%{_mandir}/man1/%name.*
