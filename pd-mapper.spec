Name:           pd-mapper
Version:        1.0
Release:        1%{?dist}
Summary:        pd-mapper package

License:        BSD3
URL:            https://github.com/andersson/pd-mapper
Source0:        https://github.com/andersson/%{name}/archive/refs/tags/v%{version}.tar.gz


BuildRequires:  gcc systemd-rpm-macros qrtr
Requires: qrtr

%description
pd-mapper package description

%prep
%autosetup

%build
%make_build prefix=%{_prefix}

%install
%make_install prefix=%{_prefix}

%files
%license LICENSE

# These were generated mostly by _not_ having anything here, and then silencing the errors
# during rpmbuild -bb ~/rpmbuild/SPECS/pd-mapper.spec

# The below is pretty lazily done, this package would probably be best split into
# multiple subpackages here for the -devel, etc variants.
%{_bindir}/*
%{_unitdir}/*

%changelog
* Fri May 05 2023 Markus Rathgeb <maggu2810@gmail.com>
- Bump to version 1.0
* Wed Oct 12 2022 Andrew Halaney <ahalaney@redhat.com>
- Add warning and exit for missing firmware files (in review upstream)
  in pd-mapper.c. I tried to use diff/patch appropriately but
  failed, there's gotta be a better way than tarballing a git tree
  up for all of this and instead work _with_ git.
* Thu Oct 06 2022 Andrew Halaney <ahalaney@redhat.com>
- Initial RPM
