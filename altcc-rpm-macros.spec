Name:           altcc-rpm-macros
Version:        1
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
* Tue May 31 2016 Orion Poplawski <orion@cora.nwra.com> - 1-1
- Initial package
