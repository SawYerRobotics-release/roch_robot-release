Name:           ros-kinetic-roch-control
Version:        2.0.13
Release:        0%{?dist}
Summary:        ROS roch_control package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/roch_control
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-controller-manager
Requires:       ros-kinetic-create-node
Requires:       ros-kinetic-diff-drive-controller
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-interactive-marker-twist-server
Requires:       ros-kinetic-joint-state-controller
Requires:       ros-kinetic-joint-trajectory-controller
Requires:       ros-kinetic-joy
Requires:       ros-kinetic-robot-localization
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-rostopic
Requires:       ros-kinetic-teleop-twist-joy
Requires:       ros-kinetic-twist-mux
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-joy
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslaunch

%description
SawYer roch controller configurations

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
* Fri Mar 24 2017 Carl <wzhang@softrobtech.com> - 2.0.13-0
- Autogenerated by Bloom

