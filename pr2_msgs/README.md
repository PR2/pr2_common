This package defines PR2-specific message and service types. Most users
will not use these types directly, but rather through PR2-specific
visualizations and utilities.

Where two versions of a message or service are defined, the version
defined with a suffix of `2` is preferred; the non-suffix version is
deprecated (e.g., we use
[pr2_msgs/msg/BatteryServer2](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/BatteryServer2.html)
instead of
[pr2_msgs/msg/BatteryServer](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/BatteryServer.html)).
