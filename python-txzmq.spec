%global modname txZMQ

Name:             python-txzmq
Version:          0.5.0
Release:          2%{?dist}
Summary:          Twisted bindings for ZeroMQ

Group:            Development/Languages
License:          GPLv2
URL:              http://pypi.python.org/pypi/%{modname}
Source0:          http://pypi.python.org/packages/source/t/%{modname}/%{modname}-%{version}.tar.gz
Patch0:           0002-Disable-EPGM-test.patch

BuildArch:        noarch


BuildRequires:    python2-devel
BuildRequires:    python-setuptools
BuildRequires:    python-nose
BuildRequires:    python-zmq
BuildRequires:    python-twisted

Requires:         python-zmq
Requires:         python-twisted

%description
txZMQ allows to integrate easily `ZeroMQ <http://zeromq.org>`_ sockets into
Twisted event loop (reactor).

%prep
%setup -q -n %{modname}-%{version}
%patch0 -p1 -b .disable_epgm_test

# Patch out the setuptools requirement on Twisted since epel doesn't ship
# twisted egg-info
%if %{?rhel}%{!?rhel:0} >= 6
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

%{python_sitelib}/* 

%changelog
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
