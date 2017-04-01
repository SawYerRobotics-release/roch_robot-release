Name:           ros-indigo-roch-description
Version:        1.0.13
Release:        3%{?dist}
Summary:        ROS roch_description package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/roch_descrption
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-ur-description
Requires:       ros-indigo-urdf
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-roslaunch

%description
SawYer Roch URDF description

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Apr 01 2017 Carl <wzhang@softrobtech.com> - 1.0.13-3
- Autogenerated by Bloom

* Fri Mar 31 2017 Carl <wzhang@softrobtech.com> - 1.0.13-2
- Autogenerated by Bloom

* Thu Mar 30 2017 Carl <wzhang@softrobtech.com> - 1.0.13-1
- Autogenerated by Bloom

* Thu Mar 23 2017 Carl <wzhang@softrobtech.com> - 1.0.13-0
- Autogenerated by Bloom

* Thu Feb 23 2017 Carl <wzhang@softrobtech.com> - 1.0.12-0
- Autogenerated by Bloom

* Tue Feb 07 2017 Carl <wzhang@softrobtech.com> - 1.0.11-0
- Autogenerated by Bloom

* Tue Jan 24 2017 Carl <carl@softrobtech.com> - 1.0.10-0
- Autogenerated by Bloom

* Sun Jan 22 2017 Carl <carl@softrobtech.com> - 1.0.8-0
- Autogenerated by Bloom

* Sat Jan 21 2017 Carl <carl@softrobtech.com> - 1.0.7-0
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <carl@softrobtech.com> - 1.0.6-1
- Autogenerated by Bloom

* Fri Jan 20 2017 Carl <carl@softrobtech.com> - 1.0.6-0
- Autogenerated by Bloom

