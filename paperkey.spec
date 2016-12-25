Summary:	OpenPGP key archiver
Summary(pl.UTF-8):	Archiwizator kluczy OpenPGP
Name:		paperkey
Version:	1.4
Release:	1
License:	GPL v2+
Group:		Applications/Archiving
Source0:	http://www.jabberwocky.com/software/paperkey/%{name}-%{version}.tar.gz
# Source0-md5:	7c12873562bcff32f8aebd2811708df1
URL:		http://www.jabberwocky.com/software/paperkey/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A reasonable way to achieve a long term backup of OpenPGP (PGP, GnuPG,
etc) keys is to print them out on paper.  Paper and ink have amazingly
long retention qualities - far longer than the magnetic or optical
means that are generally used to back up computer data.  A paper
backup isn't a replacement for the usual machine readable (tape, CD-R,
DVD-R, etc) backups, but rather as an if-all-else-fails method of
restoring a key.

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
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
