#
# Conditional build:
%bcond_without	verify	# don't verify database

Summary:	Wireless regulatory database for Linux drivers
Summary(pl.UTF-8):	Baza danych przepisów dotyczących sieci bezprzewodowych dla sterowników linuksowych
Name:		wireless-regdb
Version:	2020.04.29
Release:	1
License:	ISC
Group:		Networking/Daemons
Source0:	https://www.kernel.org/pub/software/network/wireless-regdb/%{name}-%{version}.tar.xz
# Source0-md5:	cc239c4bf79c72ceb265563007069c5f
URL:		https://wireless.wiki.kernel.org/en/developers/Regulatory
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{?with_verify:BuildRequires:	crda}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_datadir	/lib

%description
This package contains the wireless regulatory database used by all
cfg80211 based Linux wireless drivers.

%description -l pl.UTF-8
Ten pakiet zawiera bazę danych przepisów dotyczących częstotliwości
dopuszczonych dla sieci bezprzewodowych, wykorzystywaną przez
wszystkie linuksowe sterowniki bezprzewodowe oparte na cfg80211.

%prep
%setup -q

%build
%if %{with verify}
PATH=/sbin:$PATH \
regdbdump regulatory.bin > dump.txt
test -s dump.txt
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib/firmware,%{_datadir}/crda,%{_mandir}/man5}
cp -p regulatory.db regulatory.db.p7s $RPM_BUILD_ROOT/lib/firmware
cp -p regulatory.bin $RPM_BUILD_ROOT%{_datadir}/crda/regulatory.bin
cp -p regulatory.bin.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
/lib/firmware/regulatory.db
/lib/firmware/regulatory.db.p7s
%{_datadir}/crda
%{_mandir}/man5/regulatory.bin.5*
