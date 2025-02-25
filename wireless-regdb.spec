#
# Conditional build:
%bcond_without	verify	# don't verify database

Summary:	Wireless regulatory database for Linux drivers
Summary(pl.UTF-8):	Baza danych przepisów dotyczących sieci bezprzewodowych dla sterowników linuksowych
Name:		wireless-regdb
Version:	2025.02.20
Release:	2
License:	ISC
Group:		Networking/Daemons
Source0:	https://www.kernel.org/pub/software/network/wireless-regdb/%{name}-%{version}.tar.xz
# Source0-md5:	7454c55208ca51bae6461ca7932559ab
URL:		https://wireless.wiki.kernel.org/en/developers/Regulatory
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%{?with_verify:BuildRequires:	crda}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d $RPM_BUILD_ROOT{/lib/firmware,/lib/crda,%{_mandir}/man5}
cp -p regulatory.db regulatory.db.p7s $RPM_BUILD_ROOT/lib/firmware
cp -p regulatory.bin $RPM_BUILD_ROOT/lib/crda/regulatory.bin
cp -p regulatory.bin.5 $RPM_BUILD_ROOT%{_mandir}/man5

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README
/lib/firmware/regulatory.db
/lib/firmware/regulatory.db.p7s
/lib/crda
%{_mandir}/man5/regulatory.bin.5*
