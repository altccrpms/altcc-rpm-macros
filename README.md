# altcc-rpm-macros
RPM macros for creating AltCCRPM packages.  The macros are:

## altcc_init
Intializes the AltCCRPM macros.  Call before Name.
Usage: `%{?altcc_init:altcc_init -n %{shortname} -v %{ver}}`

## altcc_pkg_suffix
Expands to a suffix containing the version of the main package, the name and version of the compiler, and the name and version of the MPI library used if applicable.  Add %{?altcc_pkg_suffix} to Name.
```
Name: %{shortname}%{?altcc_pkg_suffix}
```

## altcc
True if building in AltCCRPM mode (COMPILER_NAME set).  False otherwise.  Use to conditionalize the spec, e.g.: `%{!?altcc:BuildRequires: gcc-fortran}` or `%{?altcc:module load hdf5}`

## altcc_reqmodules
Expands to `Requires: environment(modules)`.  Add to the package that contains the environment module file if needed.

## altcc_prvide
Expands to version-less provides for ease of installing the latest version of a package, e.g. install hdf5-intel-openmpi.  Add to each package definition.  Takes a sub-package name as an arguement and can take -n option change the base package name.  Usage: `%?altcc_provide` or `%{?altcc:%altcc_provide [-n name] [name]}`

## altcc_writemodule
Used in %install to write the environment module from the source.  Takes the source as an argument: `%{?altcc:%altcc_writemodule %SOURCE2}`

## altcc_files
Emits %dir ownership of the install tree.  Takes a list of directories, e.g.:
```
%{?altcc:%altcc_files %{_bindir} %{_libdir} %{_mandir} %{_mandir}/man1}
```
/pre>
Add a "-m" option to the package that contains the module file.  This is generally the main package unless there is a -libs sub-package.

## altcc_with_mpi
True if buildwith with MPI, false if not.
