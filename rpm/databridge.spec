%define _build_id_links none

%define __spec_prep_post true
%define __spec_prep_pre true
%define __spec_build_post true
%define __spec_build_pre true
%define __spec_install_post true
%define __spec_install_pre true
%define __spec_clean_post true
%define __spec_clean_pre true
%{?systemd_requires}
%define _binary_filedigest_algorithm 1
%define _build_binary_file_digest_algo 1
%define _binary_payload w9.gzdio

%define component databridge
%define user psale
%define source_build_path /opt/psale/build
%define source_unit_file /opt/psale/build/rpm/%{component}.service
%define source_path_config /opt/psale/build/etc/%{component}.yml
%define working_dir /opt/psale/%{component}

Name: %{component}
Version: 0.1
Release: %{release}
Summary: no description given
AutoReqProv: no
BuildRoot: /root/rpm

Prefix: /

Group: default
License: Apache License Version 2.0
Vendor: Quintagroup, Ltd.
URL: http://quintagroup.com/
Packager: <info@quintagroup.com>

BuildRequires: systemd
Requires: systemd python2-libs libyaml libffi

%description
no description given

%prep
rm -rf %{buildroot}
mkdir -p %{buildroot}%{working_dir}
mkdir -p %{buildroot}/usr/lib/systemd/system/
mkdir -p %{buildroot}/etc/%{component}/
cp -r %{source_build_path}/*  %{buildroot}/%{working_dir}/
cp %{source_unit_file} %{buildroot}/usr/lib/systemd/system/%{component}.service
cp %{source_path_config} %{buildroot}/etc/%{component}/

%build
# noop

%install
# noop

%clean
# noop

%pre
getent group %{user} >/dev/null || groupadd -r %{user}
getent passwd %{user} >/dev/null || useradd -r -g %{user} -s /sbin/nologin %{user}
exit 0

%post
%systemd_user_post %{component}.service

%preun
%systemd_user_preun %{component}.service

%files
%defattr(-,%{user},%{user},-)
%attr(0755,%{user},%{user}) %{working_dir}
%attr(-,root,root) %{_unitdir}/%{component}.service
%config(noreplace) /etc/%{component}

%changelog

