%global modname txZMQ

Name:             python-txzmq
Version:          0.8.0
Release:          13%{?dist}
Summary:          Twisted bindings for ZeroMQ

License:          GPLv2
URL:              https://github.com/smira/%{modname}
Source0:          %{url}/archive/%{version}.tar.gz

BuildArch:        noarch

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-nose
BuildRequires:    python3-zmq >= 13.0.0
BuildRequires:    python3-twisted
BuildRequires:    python3-six

%global _description\
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop\
(reactor).

%description %_description

%package -n python3-txzmq
Summary:          Twisted bindings for ZeroMQ

Requires:         python3-zmq >= 13.0.0
Requires:         python3-twisted
Requires:         python3-six

%description -n python3-txzmq
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop
(reactor).


%prep
%setup -q -n %{modname}-%{version}

# Patch out the setuptools requirement on Twisted since epel doesn't ship
# twisted egg-info
%if 0%{?rhel}
%{__sed} -i 's/"Twisted",//' setup.py
%endif


%build
%py3_build

%check
PYTHONPATH=$(pwd) nosetests-%{python3_version}

%install
%py3_install

%files -n python3-txzmq
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/txzmq/
%{python3_sitelib}/txZMQ-%{version}*.egg-info

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-12
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 28 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-11
- Subpackage python2-txzmq has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.8.0-6
- Rebuilt for Python 3.7

* Mon Feb 12 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.8.0-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.8.0-3
- Python 2 binary package renamed to python2-txzmq
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 17 2017 Lumir Balhar <lbalhar@redhat.com> - 0.8.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-7.git772df64
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.7.4-6.git772df64
- Rebuild for Python 3.6

* Tue Jul 26 2016 Lumir Balhar <lbalhar@redhat.com> - 0.7.4-5.git772df64
- Enabled Py3 support
- Changed source to the latest commit on GitHub

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Mar 24 2015 Ralph Bean <rbean@redhat.com> - 0.7.4-1
- new version

* Wed Aug 20 2014 Ralph Bean <rbean@redhat.com> - 0.7.3-1
- Latest upstream with support for zmq reconnect options.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Apr 19 2014 Ralph Bean <rbean@redhat.com> - 0.7.2-1
- Latest upstream with python3 support -- woot, woot!

* Tue Jan 28 2014 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- Latest upstream.
- Dropped support for older pyzmq.

* Tue Jan 14 2014 Ralph Bean <rbean@redhat.com> - 0.6.2-3
- Narrow dep down to the twisted-core subpackage.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Ralph Bean <rbean@redhat.com> - 0.6.2-1
- Latest upstream including our patches.
- Removed patches 2 through 5 for pyzmq compat.

* Wed Mar 27 2013 Ralph Bean <rbean@redhat.com> - 0.6.1-5
- Added three patches to support old and new pyzmq.
- More explicit file ownership in %%{python_sitelib}.
- Removed some trailing whitespace.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 05 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-3
- Patch to add support for tcp keepalives with zeromq3.
- Fixed "bad" rhel conditional.

* Mon Oct 29 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-2
- Patch (again) to support older pyzmq on f17 and el6.

* Mon Oct 29 2012 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Upstream integrates zeromq3 support.  Dropping patches.

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-3
- Patch to support older pyzmq on f17 and el6.
- Fix changelog.

* Wed Oct 10 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-2
- Added three patches to support zeromq3.

* Tue Oct 02 2012 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- Latest upstream with new socket types.
- Remove old epgm-disabling patch.
- Add new egpm-disabling patch.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-2
- Patch out setuptools dep on Twisted for epel.

* Mon May 21 2012 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Removed FSF address patch.
- Packaged new upstream version.
- Replaced txZMQ with %%{modname}

* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> - 0.3.1-2
- Changed BuildRequires python-devel to python2-devel.
- Dropped the %%defattr macro .
- Patched to disable the EPGM test.  libpgm isn't packaged for fedora yet.
- Added %%check section to run nosetests.

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com> - 0.3.1-1
- initial package for Fedora
