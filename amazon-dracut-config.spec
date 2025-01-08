#
# spec file for package amazon-dracut-config
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           amazon-dracut-config
Version:        0.0.4
Release:        0
Summary:        Amazon Dracut config overlay files
License:        Apache-2.0
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/amazon-dracut-config
Source:         %{name}-%{version}.tar.gz
BuildRequires:  dracut
Provides:       dracut-instance-change-config
Conflicts:      otherproviders(dracut-instance-change-config)
BuildArch:      noarch

%description

%prep
%autosetup -p1 -n %{name}

%build

%install
install -D -m 644 usr/lib/dracut/dracut.conf.d/07-aws-type-switch.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/07-aws-type-switch.conf
install -D -m 644 usr/lib/dracut/dracut.conf.d/07-nvme.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/07-nvme.conf
install -D -m 644 usr/lib/dracut/dracut.conf.d/07-ext4.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/07-ext4.conf
install -D -m 644 usr/lib/dracut/dracut.conf.d/07-virtio.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/07-virtio.conf
install -D -m 644 usr/lib/dracut/dracut.conf.d/07-xfs.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/07-xfs.conf
install -D -m 644 usr/lib/dracut/dracut.conf.d/11-resume.conf \
    %{buildroot}/usr/lib/dracut/dracut.conf.d/11-resume.conf

%check

%files
%doc README.md
%license LICENSE
%dir /usr/lib/dracut/
%dir /usr/lib/dracut/dracut.conf.d/
/usr/lib/dracut/dracut.conf.d/07-aws-type-switch.conf
/usr/lib/dracut/dracut.conf.d/07-nvme.conf
/usr/lib/dracut/dracut.conf.d/07-ext4.conf
/usr/lib/dracut/dracut.conf.d/07-virtio.conf
/usr/lib/dracut/dracut.conf.d/07-xfs.conf
/usr/lib/dracut/dracut.conf.d/11-resume.conf

%changelog
