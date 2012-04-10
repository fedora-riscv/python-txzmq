Name:             python-txzmq
Version:          0.3.1
Release:          2%{?dist}
Summary:          Twisted bindings for ZeroMQ

Group:            Development/Languages
License:          GPLv2
URL:              http://pypi.python.org/pypi/txZMQ
Source0:          http://pypi.python.org/packages/source/t/txZMQ/txZMQ-0.3.1.tar.gz
Patch0:           0001-Corrected-FSF-address.patch
Patch1:           0002-Disable-EPGM-test.patch

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
%setup -q -n txZMQ-%{version}
%patch0 -p1 -b .correct_fsf_address
%patch1 -p1 -b .disable_epgm_test

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
* Mon Apr 09 2012 Ralph Bean <rbean@redhat.com> 0.3.1-2
- Changed BuildRequires python-devel to python2-devel.
- Dropped the %defattr macro .
- Patched to disable the EPGM test.  libpgm isn't packaged for fedora yet.
- Added %check section to run nosetests.

* Thu Apr 05 2012 Ralph Bean <rbean@redhat.com> 0.3.1-1
- initial package for Fedora
