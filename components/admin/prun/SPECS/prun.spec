#----------------------------------------------------------------------------bh-
# This RPM .spec file is part of the Performance Peak project.
#
# It may have been modified from the default version supplied by the underlying
# release package (if available) in order to apply patches, perform customized
# build/install configurations, and supply additional files to support
# desired integration conventions.
#
#----------------------------------------------------------------------------eh-

%include %{_sourcedir}/FSP_macros

%define pname prun
%{!?PROJ_DELIM:%define PROJ_DELIM %{nil}}

Summary:   Convenience utility for parallel job launch
Name:      %{pname}%{PROJ_DELIM}
Version:   0.1.0
Release:   1
License:   BSD
Group:     fsp/admin
BuildArch: noarch
Source0:   %{pname}
Source1:   FSP_macros
BuildRoot: %{_tmppath}/%{pname}-%{version}-%{release}-root

%define package_target %{FSP_PUB}/%{pname}/%{version}

%description

prun provides a script-based wrapper for launching parallel jobs
within a resource manager for a variety of MPI families.

%prep


%build
# Binary pass-through - empty build section

%install

rm -rf $RPM_BUILD_ROOT

%{__mkdir} -p %{buildroot}/%{package_target}
install -D -m 0755 %SOURCE0 %{buildroot}/%{package_target}

# FSP moduelfile

%{__mkdir} -p %{buildroot}/%{FSP_MODULES}/%{pname}
%{__cat} << EOF > %{buildroot}/%{FSP_MODULES}/%{pname}/%{version}
#%Module1.0#####################################################################
proc ModulesHelp { } {

puts stderr " "
puts stderr "This module loads the prun job launch utility"
puts stderr " "
puts stderr "Version %{version}"
puts stderr " "

}

module-whatis "Name: prun job launch utility"
module-whatis "Version: %{version}"
module-whatis "Category: resource manager tools"
module-whatis "Description: job launch utility for multiple MPI families"

set     version                 %{version}

prepend-path    PATH            %{package_target}

EOF

%{__cat} << EOF > %{buildroot}/%{FSP_MODULES}/%{pname}/.version.%{version}
#%Module1.0#####################################################################
set     ModulesVersion      "%{version}"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun


%files
%defattr(-,root,root,-)
%{FSP_HOME}



