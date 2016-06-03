Name:           altcc-rpm-macros
Version:        3
Release:        1%{?dist}
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
mkdir -p %{buildroot}/%{_rpmconfigdir}/macros.d/
install -pm 644 macros.altcc %{buildroot}/%{_rpmconfigdir}/macros.d/

%files
%license LICENSE
%doc README.md
%{_rpmconfigdir}/macros.d/macros.altcc

%changelog
* Fri Jun 3 2016 Orion Poplawski <orion@cora.nwra.com> - 3-1
- Add handling of %%doc and %%license
- Automatically own parent directories
- Allow %%altcc_init to use %%shortname and %%ver directly

* Thu Jun 2 2016 Orion Poplawski <orion@cora.nwra.com> - 2-1
- Fix usage of altcc_modulefiledir

* Tue May 31 2016 Orion Poplawski <orion@cora.nwra.com> - 1-1
- Initial package
