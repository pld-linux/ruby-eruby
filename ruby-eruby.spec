Summary:	Embedded Ruby
Summary(pl):	Osadzony Ruby
Name:		ruby-ERuby
Version:	1.0.5
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	http://modruby.net/archive/eruby-%{version}.tar.gz
# Source0-md5:	af294fe34dc6cf24228aec95167b3099
BuildRequires:	rpmbuild(macros) >= 1.263
BuildRequires:	ruby
Requires:	ruby
Obsoletes:	ruby-eruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
eRuby is a language to embed Ruby codes into text files. For example,
you can embed Ruby codes into HTML files.

%description -l pl
eRuby to jêzyk do osadzania kodu w jêzyku Ruby w plikach tekstowych.
Mo¿na na przyk³ad osadziæ kod w Rubym w plikach HTML.

%prep
%setup -q -n eruby-%{version}

%build
ruby configure.rb
%{__make}

rdoc --ri --op ri
rdoc --op rdoc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_sitearchdir},%{_bindir},%{ruby_ridir}}

install eruby.so $RPM_BUILD_ROOT%{ruby_sitearchdir}
install eruby $RPM_BUILD_ROOT%{_bindir}

cp -a ri/ri/* $RPM_BUILD_ROOT%{ruby_ridir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README* rdoc
%attr(755,root,root) %{ruby_sitearchdir}/*
%attr(755,root,root) %{_bindir}/eruby
%{ruby_ridir}/ERuby
