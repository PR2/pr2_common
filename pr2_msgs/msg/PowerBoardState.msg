int8 STATE_NOPOWER=0
int8 STATE_STANDBY=1
int8 STATE_PUMPING=2
int8 STATE_ON=3
int8 STATE_DISABLED=4

Header header
string name
uint32 serial_num
# Circuit States:
#  STATE_NOPOWER, STATE_STANDBY, STATE_PUMPING, STATE_ON, STATE_DISABLED
float64 input_voltage
int8[3] circuit_state
float64[3] circuit_voltage
int8 run_stop
int8 wireless_stop
