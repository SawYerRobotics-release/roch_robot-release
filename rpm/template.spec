Name:           ros-kinetic-roch-capabilities
Version:        2.0.13
Release:        2%{?dist}
Summary:        ROS roch_capabilities package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roch_capabilities
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-nodelet
Requires:       ros-kinetic-roch-base
Requires:       ros-kinetic-rocon-app-manager
Requires:       ros-kinetic-rocon-apps
Requires:       ros-kinetic-std-capabilities
BuildRequires:  ros-kinetic-catkin

%description
Capabilities for Roch

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Mar 30 2017 Carl <wzhang@softrobtech.com> - 2.0.13-2
- Autogenerated by Bloom

* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-1
- Autogenerated by Bloom

* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-0
- Autogenerated by Bloom

