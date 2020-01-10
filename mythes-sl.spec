Name: mythes-sl
Summary: Slovenian thesaurus
%define upstreamid 20130130
Version: 0.%{upstreamid}
Release: 2%{?dist}
Source: http://193.2.66.133:85/download/thes_sl_SI_v2.zip
Group: Applications/Text
URL: http://www.tezaver.si/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: LGPLv2+
BuildArch: noarch
Requires: mythes

%description
Slovenian thesaurus.

%prep
%setup -q -c

%build
chmod -x *
for i in README_th_sl_SI_v2.txt; do
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_sl_SI_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_th_sl_SI_v2.txt
%{_datadir}/mythes/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20130130-2
- Mass rebuild 2013-12-27

* Thu Jan 31 2013 Caolán McNamara <caolanm@redhat.com> - 0.20130130-1
- Resolves: rhbz#905955 latest version

* Wed Sep 12 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120912-1
- latest version

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20120613-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jun 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120613-1
- latest version

* Wed Apr 13 2012 Caolán McNamara <caolanm@redhat.com> - 0.20120413-1
- latest version

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20111017-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 17 2011 Caolán McNamara <caolanm@redhat.com> - 0.20111017-1
- latest version

* Mon Aug 08 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110808-1
- latest version

* Thu Jun 09 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110609-1
- latest version

* Fri Mar 18 2011 Caolán McNamara <caolanm@redhat.com> - 0.20110318-1
- latest version

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20101221-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Dec 21 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101221-1
- latest version

* Sun Oct 31 2010 Caolán McNamara <caolanm@redhat.com> - 0.20101031-1
- latest version

* Fri Sep 24 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100924-1
- latest version

* Mon Aug 23 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100823-1
- latest version

* Tue Jul 20 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100720-1
- latest version

* Sat Jun 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100619-1
- latest version

* Wed May 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100519-1
- latest version

* Mon Apr 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100419-1
- latest version

* Sun Apr 04 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100319-2
- mythes now owns /usr/share/mythes

* Fri Mar 19 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100319-1
- latest version

* Thu Feb 18 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100218-1
- latest version

* Mon Jan 18 2010 Caolán McNamara <caolanm@redhat.com> - 0.20100118-1
- latest version

* Thu Dec 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091217-1
- latest version

* Tue Nov 17 2009 Caolán McNamara <caolanm@redhat.com> - 0.20091117-1
- latest version

* Tue Sep 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090908-1
- latest version

* Sat Aug 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090808-1
- latest version

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090708-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sat Jul 11 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090708-2
- tidy spec

* Wed Jul 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090708-1
- latest version

* Mon Jun 08 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090608-1
- latest version

* Sat Mar 28 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090328-1
- latest version

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20090222-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 22 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090222-1
- latest version

* Wed Jan 21 2009 Caolán McNamara <caolanm@redhat.com> - 0.20090121-1
- initial version
