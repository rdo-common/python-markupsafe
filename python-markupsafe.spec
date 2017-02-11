%if 0%{?fedora}
%global with_python3 1
%endif

Name: python-markupsafe
Version: 0.23
Release: 13%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python

Group: Development/Languages
License: BSD
URL: http://pypi.python.org/pypi/MarkupSafe
Source0: http://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-%{version}.tar.gz

BuildRequires: python2-devel python2-setuptools

%if 0%{?with_python3}
BuildRequires: python3-devel python3-setuptools
%endif # if with_python3


%description
A library for safe markup escaping.

%package -n python2-markupsafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 2
Group: Development/Languages
%{?python_provide:%python_provide python2-markupsafe}

%description -n python2-markupsafe
A library for safe markup escaping.

%if 0%{?with_python3}
%package -n python3-markupsafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 3
Group: Development/Languages
%{?python_provide:%python_provide python3-markupsafe}

%description -n python3-markupsafe
A library for safe markup escaping.
%endif #if with_python3

%prep
%setup -q -n MarkupSafe-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif # with_python3


%install
%py2_install
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python2_sitearch}/markupsafe/*.c

%if 0%{?with_python3}
%py3_install
%endif # with_python3
# C code errantly gets installed
rm $RPM_BUILD_ROOT/%{python3_sitearch}/markupsafe/*.c


%check
%{__python2} setup.py test

%if 0%{?with_python3}
%{__python3} setup.py test
%endif # with_python3


%files -n python2-markupsafe
%license LICENSE
%doc AUTHORS README.rst
%{python2_sitearch}/*

%if 0%{?with_python3}
%files -n python3-markupsafe
%doc AUTHORS LICENSE README.rst
%{python3_sitearch}/*
%endif # with_python3


%changelog
* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 0.23-12
- Rebuild for Python 3.6

* Thu Sep 22 2016 Orion Poplawski <orion@cora.nwra.com> - 0.23-11
- Ship python2-markupsafe
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-10
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.23-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> - 0.23-8
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.23-5
- Replace the python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-3
- Really rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-2
- Rebuild for Python 3.4

* Fri May  9 2014 Orion Poplawski <orion@cora.nwra.com> - 0.23-1
- Update to 0.23

* Fri Oct 11 2013 Luke Macken <lmacken@redhat.com> - 0.18-1
- Update to 0.18 (#678537)

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-7
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 0.11-6
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec 29 2010 David Malcolm <dmalcolm@redhat.com> - 0.11-2
- rebuild for newer python3

* Thu Sep 30 2010 Luke Macken <lmacken@redhat.com> - 0.11-1
- Update to 0.11

* Wed Aug 25 2010 Thomas Spura <tomspur@fedoraproject.org> - 0.9.2-5
- rebuild with python3.2
  http://lists.fedoraproject.org/pipermail/devel/2010-August/141368.html

* Fri Jul 23 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-3
- Fix missing setuptools BuildRequires.

* Thu Jun 24 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-2
- Fixed sitearch and python3 definitions to work better with older Fedora/RHEL.

* Wed Jun 23 2010 Kyle VanderBeek <kylev@kylev.com> - 0.9.2-1
- Initial version.
