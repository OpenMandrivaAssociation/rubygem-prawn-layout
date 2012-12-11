%define oname prawn-layout

Summary:    An extension to Prawn that provides table support
Name:       rubygem-%{oname}
Version:    0.8.4
Release:    %mkrel 1
Group:      Development/Ruby
License:    Ruby or GPLv2
URL:        http://prawn.majesticseacreature.com
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
Requires:   rubygem(prawn-core)
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
An extension to Prawn that provides table support and other layout
functionality

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/examples/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/spec/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/README
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sat Oct 09 2010 Rémy Clouard <shikamaru@mandriva.org> 0.8.4-1mdv2011.0
+ Revision: 584390
- import rubygem-prawn-layout

