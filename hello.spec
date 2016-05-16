Name:           hello
Version:        2.10
Release:        1%{?dist}
Summary:        The "Hello World" program from GNU

License:        GPLv3+
URL:            http://ftp.gnu.org/gnu/%{name}
Source0:        http://ftp.gnu.org/gnu/%{name}/%{name}-%{version}.tar.gz





%description
The "Hello World" program, done with all bells and whistles of a proper FOSS 
project, including configuration, build, internationalization, help files, etc.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
%make_install
%find_lang %{name}
rm -f %{buildroot}/%{_infodir}/dir




%files -f %{name}.lang
%{_mandir}/man1/hello.1.*
%{_infodir}/hello.info.*
%{_bindir}/hello

%doc AUTHORS ChangeLog NEWS README THANKS TODO COPYING
