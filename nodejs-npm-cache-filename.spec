%{?scl:%scl_package nodejs-npm-cache-filename}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

Name:           %{?scl_prefix}nodejs-npm-cache-filename
Version:        1.0.2
Release:        2%{?dist}
Summary:        Return NPM cache folder
License:        ISC
Group:          Development/Languages/Other
Url:            https://github.com/npm/npm-cache-filename
Source:         http://registry.npmjs.org/npm-cache-filename/-/npm-cache-filename-%{version}.tgz
BuildRequires:  %{?scl_prefix}nodejs
BuildRoot:      %{_tmppath}/%{pkg_name}-%{version}-build
BuildArch:      noarch
ExclusiveArch:  %{ix86} x86_64 %{arm} noarch

%description
Given a cache folder and url, return the appropriate cache folder. 

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/npm-cache-filename
cp -pr package.json index.js \
        %{buildroot}%{nodejs_sitelib}/npm-cache-filename/

%files
%defattr(-,root,root,-)
%doc README.md LICENSE
%{nodejs_sitelib}/npm-cache-filename

%changelog
* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.2-2
- rebuilt

* Mon Nov 30 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.2-1
- Rebase to latest upstream version

* Tue Jan 13 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-3
- Remove undefined macro

* Fri Jan 09 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-2
- Add dist makro

* Tue Jan 06 2015 Tomas Hrcka <thrcka@redhat.com> - 1.0.1-1
- rebuilt

