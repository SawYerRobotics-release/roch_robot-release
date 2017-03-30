^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package roch_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
2.0.13 (2017-03-23)
-------------------

2.0.12 (2017-03-23)
-------------------

1.0.10 (2017-02-17)
-------------------
* Add Roch Image.
* Remove unused param events/bumper and events/wheel_drop.
* Add rocon_concert files, such as concert_minimal.launch and concert_client.launch.
* Add param files for capabilities.
* Support Orbbec Astra.
* Add interactions.
* Add missing dependences: laser_filters, rgbd_launch, nodelet, robot_sate_publisher, diagnostic_aggregator
* Modify XML file of rplidar that string of serial_port to /dev/rplidar and frame_id to base_laser.

1.0.9 (2017-02-07)
-------------------

1.0.8 (2017-01-23)
-------------------
* Changes permissions of python files.

1.0.7 (2017-01-17)
-------------------
* Fixed bugs which will cant not find roch_safety_controller.

1.0.6 (2017-01-17)
-------------------

0.0.5 (2017-01-17)
-------------------
* Add new env that enable of if use 3d sensor in navigation or not is ROCH_SENSOR_NAV_ENABLE.
* Modify all structures because of ROCH_SENSOR_NAV_ENABLE.
* Modify R200.launch.xml for support roch_follower.

0.0.4 (2016-12-14)
-------------------
* Aupport Rplidar A1
* Contributors: Carl

0.0.3 (2016-12-02)
-------------------
* Aupport Intel RealSensor 200
* Contributors: Carl

0.0.2 (2016-11-14)
-------------------
* Add laser_filters of lidar
* Contributors: Carl

0.0.1 (2016-09-13)
-------------------
* Catkinize package.
* First cut of a new install script.
* Contributors: Carl
