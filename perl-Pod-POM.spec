#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Pod-POM
Version  : 2.01
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Pod-POM-2.01.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Pod-POM-2.01.tar.gz
Summary  : POD Object Model
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Pod-POM-bin = %{version}-%{release}
Requires: perl-Pod-POM-license = %{version}-%{release}
Requires: perl-Pod-POM-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Slurper)
BuildRequires : perl(Test::Differences)
BuildRequires : perl(Text::Diff)

%description
Pod::POM - POD Object Model
---------------------------
This module implements a parser to convert Pod documents into a simple object
model form known hereafter as the Pod Object Model (POM). The object model is
generated as a hierarchical tree of nodes, each of which represents a
different element of the original document.  The tree can be walked manually
and the nodes examined, printed or otherwise manipulated.  In addition,
Pod::POM supports and provides view objects which can automatically traverse
the tree, or section thereof, and generate an output representation in one
form or another.  The Template Toolkit Pod plugin interfaces to this module.

%package bin
Summary: bin components for the perl-Pod-POM package.
Group: Binaries
Requires: perl-Pod-POM-license = %{version}-%{release}

%description bin
bin components for the perl-Pod-POM package.


%package dev
Summary: dev components for the perl-Pod-POM package.
Group: Development
Requires: perl-Pod-POM-bin = %{version}-%{release}
Provides: perl-Pod-POM-devel = %{version}-%{release}
Requires: perl-Pod-POM = %{version}-%{release}

%description dev
dev components for the perl-Pod-POM package.


%package license
Summary: license components for the perl-Pod-POM package.
Group: Default

%description license
license components for the perl-Pod-POM package.


%package man
Summary: man components for the perl-Pod-POM package.
Group: Default

%description man
man components for the perl-Pod-POM package.


%prep
%setup -q -n Pod-POM-2.01

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Pod-POM
cp LICENSE %{buildroot}/usr/share/package-licenses/perl-Pod-POM/LICENSE
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Constants.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Begin.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Code.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Content.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/For.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Head1.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Head2.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Head3.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Head4.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Item.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Over.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Pod.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Sequence.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Text.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Node/Verbatim.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Nodes.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/Test.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/View.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/View/HTML.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/View/Pod.pm
/usr/lib/perl5/vendor_perl/5.28.2/Pod/POM/View/Text.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/podlint
/usr/bin/pom2
/usr/bin/pomdump

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Pod::POM.3
/usr/share/man/man3/Pod::POM::Constants.3
/usr/share/man/man3/Pod::POM::Node.3
/usr/share/man/man3/Pod::POM::Node::Begin.3
/usr/share/man/man3/Pod::POM::Node::Code.3
/usr/share/man/man3/Pod::POM::Node::Content.3
/usr/share/man/man3/Pod::POM::Node::For.3
/usr/share/man/man3/Pod::POM::Node::Head1.3
/usr/share/man/man3/Pod::POM::Node::Head2.3
/usr/share/man/man3/Pod::POM::Node::Head3.3
/usr/share/man/man3/Pod::POM::Node::Head4.3
/usr/share/man/man3/Pod::POM::Node::Item.3
/usr/share/man/man3/Pod::POM::Node::Over.3
/usr/share/man/man3/Pod::POM::Node::Pod.3
/usr/share/man/man3/Pod::POM::Node::Sequence.3
/usr/share/man/man3/Pod::POM::Node::Text.3
/usr/share/man/man3/Pod::POM::Node::Verbatim.3
/usr/share/man/man3/Pod::POM::Nodes.3
/usr/share/man/man3/Pod::POM::View.3
/usr/share/man/man3/Pod::POM::View::HTML.3
/usr/share/man/man3/Pod::POM::View::Pod.3
/usr/share/man/man3/Pod::POM::View::Text.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Pod-POM/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/podlint.1
/usr/share/man/man1/pom2.1
/usr/share/man/man1/pomdump.1
