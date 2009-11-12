Header header
int32 MAX_BAT_COUNT=4
int32 MAX_BAT_REG=48
int32 id  # unique ID for each battery server
# Battery System Stats
time lastTimeSystem #epoch time
time timeLeft      # in minutes
int32 averageCharge # in percent
string message
# Battery Controller Flags
time lastTimeController #epoch time
bool[4] present
bool[4] charging
bool[4] discharging
bool[4] reserved
bool[4] powerPresent
bool[4] powerNG
bool[4] inhibited
# for each battery
pr2_msgs/BatteryState2[] battery
