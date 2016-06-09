%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           altcc-rpm-macros
Version:        3
Release:        2%{?dist}
Summary:        AltCCRPMs rpm macros
URL:            https://github.com/altccrpms/altcc-rpm-macros

License:        MIT
Source0:        https://github.com/altccrpms/altcc-rpm-macros/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch

%description
This package contains the RPM macros for the AltCCRPMs project.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{macrosdir}
install -pm 644 macros.altcc %{buildroot}%{macrosdir}

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%{macrosdir}/macros.altcc

%changelog
* Thu Jun 9 2016 Orion Poplawski <orion@cora.nwra.com> - 3-2
- Handle EL6 rpm macros dir

* Fri Jun 3 2016 Orion Poplawski <orion@cora.nwra.com> - 3-1
- Add handling of %%doc and %%license
- Automatically own parent directories
- Allow %%altcc_init to use %%shortname and %%ver directly

* Thu Jun 2 2016 Orion Poplawski <orion@cora.nwra.com> - 2-1
- Fix usage of altcc_modulefiledir

* Tue May 31 2016 Orion Poplawski <orion@cora.nwra.com> - 1-1
- Initial package
