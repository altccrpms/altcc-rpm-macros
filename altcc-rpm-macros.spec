%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:           altcc-rpm-macros
Version:        12
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
mkdir -p %{buildroot}%{macrosdir}
install -pm 644 macros.altcc %{buildroot}%{macrosdir}

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc README.md
%{macrosdir}/macros.altcc

%changelog
* Fri Feb 24 2017 Orion Poplawski <orion@cora.nwra.com> - 12-1
- Use %%dir for extra MPI implementation paths to own
- Fix conditionals for owning alternative mpi prefixes

* Thu Sep 29 2016 Orion Poplawski <orion@cora.nwra.com> - 11-1
- Substitute @NAME@ and @NAME_UC@ in modulefiles

* Wed Sep 28 2016 Orion Poplawski <orion@cora.nwra.com> - 10-1
- Add -F option to %%altcc_init to use full MPI version in package name/prefix

* Tue Sep 27 2016 Orion Poplawski <orion@cora.nwra.com> - 9-1
- Add -f option to %%altcc_init to use full compiler version in package name/prefix

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 8-1
- Do not add package version to package name if installing into a different prefix
- Add mpi version provides if using a different version for module path

* Mon Sep 26 2016 Orion Poplawski <orion@cora.nwra.com> - 7-1
- Create proper MPI modulefiles path

* Fri Sep 23 2016 Orion Poplawski <orion@cora.nwra.com> - 6-1
- Add -p option to %%altcc_init to allow installing into a shared prefix dir
- Have %%altcc_init -m take a version to specify the MPI module path version

* Mon Jul 25 2016 Orion Poplawski <orion@cora.nwra.com> - 5-1
- Do not try to support %%{_licensedir} if it is not defined (EL6)

* Tue Jun 21 2016 Orion Poplawski <orion@cora.nwra.com> - 4-1
- Define altcc_mpi_name

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
