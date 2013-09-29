Summary:	Tool for sending build requests
Name:		make-request
Version:	1.85
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://git.pld-linux.org/?p=projects/pld-builder.new.git;a=blob_plain;f=client/make-request.sh;h=195fa352089e444d951c43aa361537e3538b2c26;hb=aeaf1b73b36ef2bb4d14a682279aeeb512719088;/%{name}-%{version}.sh
# Source0-md5:	8ba22399e2c7a31930f84118fd3cdb44
URL:		http://git.pld-linux.org/?p=projects/pld-builder.new.git;a=summary
Requires:	/usr/sbin/sendmail
Requires:	gnupg
Obsoletes:	pld-builder-client
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tool which, based on the way it's configured and on the cmdline
parameters given to it, generates an xml-formated build request, which
it then signs with the requester's PGP key (using the gpg utility) and
then sends it to the source builder via a sendmail compatible command
line application (by default invoking "sendmail -t").

Two modes of operation are:
- sending requests to build chosen package(s) on a specified group of
  builders
- sending a chosen command to be executed on a specified group of
  builders

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -p %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
