Name: perl-Crypt-OpenPGP
Source9999: version
Version: %(echo `awk '{ print $1 }' %{SOURCE9999}`)
Release: %(echo `awk '{ print $2 }' %{SOURCE9999}`)%{?dist}
Summary: Crypt-OpenPGP Perl module
License: distributable
Group: Development/Libraries
URL: http://search.cpan.org/search?mode=module&query=Crypt%3a%3aOpenPGP
BuildRoot: %{_tmppath}/%{name}-root
Buildarch: noarch
BuildRequires: perl >= 2:5.8.0
Requires: %(perl -MConfig -le 'if (defined $Config{useithreads}) { print "perl(:WITH_ITHREADS)" } else { print "perl(:WITHOUT_ITHREADS)" }')
Requires: %(perl -MConfig -le 'if (defined $Config{usethreads}) { print "perl(:WITH_THREADS)" } else { print "perl(:WITHOUT_THREADS)" }')
Requires: %(perl -MConfig -le 'if (defined $Config{uselargefiles}) { print "perl(:WITH_LARGEFILES)" } else { print "perl(:WITHOUT_LARGEFILES)" }')
Source0: Crypt-OpenPGP-1.03.tar.gz
BuildRequires: perl(Module::Build)
BuildRequires: perl(Data::Buffer)
Requires: perl(Data::Buffer)
BuildRequires: perl(Math::Pari)
Requires: perl(Math::Pari)
BuildRequires: perl(Compress::Zlib)
Requires: perl(Compress::Zlib)
BuildRequires: perl(LWP::UserAgent)
Requires: perl(LWP::UserAgent)
BuildRequires: perl(URI::Escape)
Requires: perl(URI::Escape)
BuildRequires: perl(Crypt::DSA)
Requires: perl(Crypt::DSA)
BuildRequires: perl(Crypt::RSA)
Requires: perl(Crypt::RSA)
BuildRequires: perl(Crypt::RIPEMD160)
Requires: perl(Crypt::RIPEMD160)
BuildRequires: perl(Crypt::Rijndael)
BuildRequires: perl(Crypt::CAST5_PP)

%description
Crypt-OpenPGP Perl module
%prep
%setup -q -n Crypt-OpenPGP-%{version} 

%build
CFLAGS="$RPM_OPT_FLAGS" perl Makefile.PL PREFIX=$RPM_BUILD_ROOT/usr 
make
make test

%clean
rm -rf $RPM_BUILD_ROOT
%install

rm -rf $RPM_BUILD_ROOT
eval `perl '-V:installarchlib'`
mkdir -p $RPM_BUILD_ROOT/$installarchlib
make install

[ -x /usr/lib/rpm/brp-compress ] && /usr/lib/rpm/brp-compress

rm -f `find $RPM_BUILD_ROOT -type f -name perllocal.pod -o -name .packlist`
find $RPM_BUILD_ROOT/usr -type f -print | \
	sed "s@^$RPM_BUILD_ROOT@@g" | \
	grep -v perllocal.pod | \
	grep -v "\.packlist" > Crypt-OpenPGP-%{version}-filelist
if [ "$(cat Crypt-OpenPGP-%{version}-filelist)X" = "X" ] ; then
    echo "ERROR: EMPTY FILE LIST"
    exit 1
fi

%files -f Crypt-OpenPGP-%{version}-filelist
%defattr(-,root,root)

%changelog
* Tue Dec 10 2002 cturner@redhat.com
- Specfile autogenerated

