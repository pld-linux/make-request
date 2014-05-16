%define		githash	044d04b
Summary:	Tool for sending PLD-specific build requests
Summary(pl.UTF-8):	Narzędzie do wysyłania żądań budowania specyficznych dla PLD
Name:		make-request
Version:	1.87
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://git.pld-linux.org/?p=projects/pld-builder.new.git;a=blob_plain;f=client/make-request.sh;hb=%{githash};/%{name}-%{version}.sh
# Source0-md5:	c191c8b460f0cb47edf1ca51d926b833
URL:		http://git.pld-linux.org/?p=projects/pld-builder.new.git;a=summary
Requires:	/usr/lib/sendmail
Requires:	gnupg
Obsoletes:	pld-builder-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool which, based on the way it's configured and on the cmdline
parameters given to it, generates an XML-formated build request, which
it then signs with the requester's PGP key (using the gpg utility) and
then sends it to the source builder via a sendmail compatible command
line application (by default invoking "sendmail -t").

Two modes of operation are:
- sending requests to build chosen package(s) on a specified group of
  builders
- sending a chosen command to be executed on a specified group of
  builders

It works with PLD (or compatible) package builders.

%description -l pl.UTF-8
Narzędzie, które w zależności od konfiguracji i parametrów linii
poleceń, generuje żądanie budowania w formacie XML, podpisuje je
kluczem PGP zlecającego (przy użyciu narzędzia gpg), a następnie
wysyła na builder źródłowy przy użyciu polecenia sendmail (domyślnie
"sendmail -t").

Dostępne są dwa tryby operacji:
- wysyłanie żądań zbudowania określonych pakietów na określonej grupie
  builderów
- wysłanie podanego polecenia do wykonania na określonej grupie
  builderów

Narzędzie działa z builderami pakietów PLD (lub kompatybilnymi).

%prep

%build
ver=$(awk -F= '/^VERSION=/{print $2}' %{SOURCE0})
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
