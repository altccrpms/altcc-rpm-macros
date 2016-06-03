# altcc-rpm-macros
RPM macros for creating AltCCRPM packages.  The macros are:

## altcc_init
Intializes the AltCCRPM macros.  Call before Name.
Usage:
```
%{?altcc_init:altcc_init -n <name> -v <version>}
```
or
```
%global shortname <name>
%global ver <version>
%{?altcc_init}
```

## altcc_pkg_suffix
Expands to a suffix containing the version of the main package, the name and version of the compiler, and the name and version of the MPI library used if applicable.  Add %{?altcc_pkg_suffix} to Name.
```
Name: %{shortname}%{?altcc_pkg_suffix}
```

## altcc_name_suffix
Expands to a suffix containing the version of the main package, and the name and version of the compiler used.  Add %{?altcc_name_suffix} to Name of packages as an alternative to %{?altcc_pkg_suffix} that do not have MPI versions.  Not strictly necessary if the package is not built with an MPI module loaded.

## altcc_dep_suffix
Expands to a suffix containting the name and version of the compiler, and the name and version of the MPI library used if applicable.  Add %{?altcc_dep_suffix} to the name of any dependencies that have altcc versions.

## altcc_cc_dep_suffix
Expands to a suffix containting the name and version of the compiler used.  Add %{?altcc_cc_dep_suffix} to the name of any dependencies that have altcc versions, but no MPI versions.

## altcc
True if building in AltCCRPM mode (COMPILER_NAME set).  False otherwise.  Use to conditionalize the spec, e.g.: `%{!?altcc:BuildRequires: gcc-fortran}` or `%{?altcc:module load hdf5}`

## altcc_reqmodules
Expands to `Requires: environment(modules)`.  Add to the package that contains the environment module file if needed.

## altcc_provide
Expands to version-less provides for ease of installing the latest version of a package, e.g. install hdf5-intel-openmpi.  Add to each package definition.  Takes a sub-package name as an arguement and can take -n option change the base package name.  Usage: `%?altcc_provide` or `%{?altcc:%altcc_provide [-n name] [name]}`

## altcc_writemodule
Used in %install to write the environment module from the source.  Takes the source as an argument: `%{?altcc:%altcc_writemodule %SOURCE2}`

## altcc_doc
Used in %install to create %{_defaultdocdir}.  May be needed for proper directory ownership in files with -d option to %altcc_files

## altcc_license
Used in %install to create %{_licensedir}.  Needed for proper directory ownership in files with -l option to %altcc_files

## altcc_files
Emits %dir ownership of the install tree.  Takes a list of directories, e.g.:
```
%{?altcc:%altcc_files -lm %{_bindir} %{_libdir} %{_mandir}/man1}
```
Add a "-d" option to the package(s) that contain %doc files.  You may need to also call %{?altcc:%altcc_doc} in %install.
Add a "-l" option to the package(s) that contain %license files.  Be sure to also call %{?altcc:%altcc_license} in %install.
Add a "-m" option to the package that contains the module file.  This is generally the main package unless there is a -libs sub-package.
Only the unique leaf trees need to be specified.  Directories between the install prefix and the given directories will be owned automatically as well.

## altcc_reqmpi
Expands to a requires on the current version of the MPI development package.  Add to -devel pacakges.

## altcc_with_mpi
True if buildwith with MPI, false if not.

## altcc_cc_name
Same as $COMPILER_NAME
