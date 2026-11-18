## Nodes

### pr2_dashboard_aggregator

`pr2_dashboard_aggregator` is the node that collects and republishes
data that is commonly visualized by [pr2_dashboard](pr2_dashboard). This
node is launched when bringing up a robot, e.g., in
[pr2_robot](https://index.ros.org/p/pr2_robot)/`pr2.launch`.
`pr2_dashboard_aggregator` also keeps track of which messages are
"stale". For each message it subscribes to (and subsequently
re-publishes), it maintains a "valid" flag which indicates if the data
is "new enough" to be used.

#### Subscribed Topics

- `power_board/state`
  ([pr2_msgs/msg/PowerBoardState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerBoardState.html)):
  The state of the PR2 power board
- `power_state`
  ([pr2_msgs/msg/PowerState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/PowerState.html)):
  The state of the PR2 power system
- `ddwrt/accesspoint`
  ([pr2_msgs/msg/AccessPoint](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/AccessPoint.html)):
  The state of the PR2 wireless access point
- `pr2_etherCAT/motors_halted`
  ([std_msgs/msg/Bool](https://docs.ros.org/en/rolling/p/std_msgs/msg/Bool.html)):
  Whether the motors are halted

#### Published Topics

- `dashboard_agg`
  ([pr2_msgs/msg/DashboardState](https://docs.ros.org/en/rolling/p/pr2_msgs/msg/DashboardState.html)):
  Aggregated state information.
