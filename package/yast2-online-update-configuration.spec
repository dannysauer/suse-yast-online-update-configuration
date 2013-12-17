#
# spec file for package yast2-online-update-configuration
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-online-update-configuration
Version:        3.1.2
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2

Group:          System/YaST
License:        GPL-2.0
# Wizard::SetDesktopTitleAndIcon
Requires:       yast2 >= 2.21.0
Requires:       yast2-packager >= 2.17.0
Requires:       yast2-pkg-bindings >= 2.17.20
Conflicts:      yast2-registration <= 2.19.1
Provides:       yast2-registration:/usr/share/YaST2/clients/online_update_configuration.ycp

PreReq:         %fillup_prereq
BuildRequires:  yast2 >= 2.17.0
BuildRequires:  perl-XML-Writer update-desktop-files yast2-packager yast2-testsuite
BuildRequires:  yast2-devtools >= 3.1.10
BuildRequires:  yast2-pkg-bindings >= 2.17.20
BuildArch:      noarch

Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        Configuration of Online Update

%description
Allows to configure automatic online update.

%post
%{fillup_only -ns automatic_online_update yast2-online-update-configuration}

%prep
%setup -n %{name}-%{version}

%build
%yast_build

%install
%yast_install


%files
%defattr(-,root,root)
%doc %{yast_docdir}
%dir %{yast_yncludedir}/online-update-configuration
%{yast_yncludedir}/online-update-configuration/*
%{yast_clientdir}/*.rb
%{yast_moduledir}/*.rb
%{yast_desktopdir}/online_update_configuration.desktop
%{yast_schemadir}/autoyast/rnc/*.rnc
/usr/lib/YaST2/bin/online_update
# agent
%{yast_scrconfdir}/cfg_automatic_online_update.scr
# fillup
/var/adm/fillup-templates/sysconfig.automatic_online_update-yast2-online-update-configuration
