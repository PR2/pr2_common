Header header
int32 MAX_BAT_COUNT=4
int32 MAX_BAT_REG=48
int32 id  # unique ID for each battery server
# Battery System Stats
time last_system_update  # last time the system stats where updated
time time_left           # in minutes
int32 average_charge     # in percent
string message           # message from the ocean server
# Battery Controller Flags, one per battery
time last_controller_update # last time a flag below was updated
bool[4] present       # is this pack present
bool[4] charging      # is this pack charging
bool[4] discharging   # is this pack discharging
bool[4] reserved      #
bool[4] power_present # is there an input voltage
bool[4] power_no_good # is there a fault (No Good)
bool[4] inhibited     # is this pack disabled for some reason
# for each battery
pr2_msgs/BatteryState2[] battery
