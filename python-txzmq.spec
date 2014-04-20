%if 0%{?fedora}
# Well, damnit.  I did the work to port this to python3, but we don't have
# python3-twisted-core in Fedora yet.  Disabling this for now.
%global with_python3 0
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2:        %global __python2 /usr/bin/python2}
%{!?python2_sitelib:  %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

%global modname txZMQ

Name:             python-txzmq
Version:          0.7.2
Release:          1%{?dist}
Summary:          Twisted bindings for ZeroMQ

Group:            Development/Languages
License:          GPLv2
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
Patch0:           0001-Disable-epgm-test.patch

BuildArch:        noarch

BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-nose
BuildRequires:    python-zmq >= 13.0.0
BuildRequires:    python-twisted-core
BuildRequires:    python-six

Requires:         python-zmq >= 13.0.0
Requires:         python-twisted-core
Requires:         python-six

%if 0%{?with_python3}
BuildRequires:    python3-devel
BuildRequires:    python3-setuptools
BuildRequires:    python3-nose
BuildRequires:    python3-zmq >= 13.0.0
BuildRequires:    python3-twisted-core
BuildRequires:    python3-six
%endif

%description
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop
(reactor).

%if 0%{?with_python3}
%package -n python3-txzmq
Summary:          Twisted bindings for ZeroMQ
Group:            Development/Languages

Requires:         python3-zmq >= 13.0.0
Requires:         python3-twisted-core
Requires:         python3-six

%description -n python3-txzmq
txZMQ allows to integrate easily ZeroMQ sockets into Twisted event loop
(reactor).
%endif


%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .disable_epgm_test

# Patch out the setuptools requirement on Twisted since epel doesn't ship
# twisted egg-info
%if 0%{?rhel}
%{__sed} -i 's/"Twisted",//' setup.py
%endif

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
%endif

%build
%{__python2} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif

%check
PYTHONPATH=$(pwd) nosetests

%if 0%{?with_python3}
pushd %{py3dir}
PYTHONPATH=$(pwd) nosetests-%{python3_version}
popd
%endif

%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
popd
%endif

%files
%doc README.rst LICENSE.txt
%{python2_sitelib}/txzmq/
%{python2_sitelib}/txZMQ-%{version}*.egg-info

%if 0%{?with_python3}
%files -n python3-txzmq
%doc README.rst LICENSE.txt
%{python3_sitelib}/txzmq/
%{python3_sitelib}/txZMQ-%{version}*.egg-info
%endif

%changelog
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
