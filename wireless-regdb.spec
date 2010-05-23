Summary:	http://wireless.kernel.org/en/developers/Regulatory
Name:		wireless-regdb
Version:	2009.11.25
Release:	1
License:	ISC
Group:		Networking/Daemons
Source0:	http://wireless.kernel.org/download/wireless-regdb/%{name}-%{version}.tar.bz2
# Source0-md5:	73166199a4df3854fa81500b5c9a639b
URL:		http://wireless.kernel.org/en/developers/Regulatory
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/crda,%{_mandir}/man5}

install regulatory.bin $RPM_BUILD_ROOT%{_datadir}/crda/regulatory.bin
install regulatory.bin.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/crda
%{_mandir}/man5/*.5*
