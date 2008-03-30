Summary:	Tool for sending build requests
Name:		make-request
Version:	1.48
Release:	0.1
License:	GPL
Group:		Development/Tools
Source0:	http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-builder.new/client/%{name}.sh?rev=%{version}
# Source0-md5:	c9f98f1ef3a5aaa1172d7d82f8d716e1
URL:		http://cvs.pld-linux.org/cgi-bin/cvsweb/pld-builder.new/client/make-request.sh
Requires:	/usr/sbin/sendmail
Requires:	gnupg
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
install %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
