%global modname txZMQ

Name:             python-txzmq
Version:          0.6.2
Release:          3%{?dist}
Summary:          Twisted bindings for ZeroMQ

Group:            Development/Languages
License:          GPLv2
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
Patch0:           0001-Disable-epgm-test.patch
Patch1:           0002-Support-older-pyzmq.patch

BuildArch:        noarch

BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-nose
BuildRequires:    python-zmq
BuildRequires:    python-twisted-core

Requires:         python-zmq
Requires:         python-twisted-core

%description
txZMQ allows to integrate easily `ZeroMQ <http://zeromq.org>`_ sockets into
Twisted event loop (reactor).

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .disable_epgm_test
%patch1 -p1 -b .disable-older-pyzmq

# Patch out the setuptools requirement on Twisted since epel doesn't ship
# twisted egg-info
%if 0%{?rhel}
%{__sed} -i 's/"Twisted",//' setup.py
%endif

%build
%{__python} setup.py build

%check
PYTHONPATH=$(pwd) nosetests

%install
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%files
%doc README.rst LICENSE.txt
%{python_sitelib}/txzmq/
%{python_sitelib}/txZMQ-%{version}*.egg-info

%changelog
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
