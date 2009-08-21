Header header
string name
# Circuit States:
#  STATE_NOPOWER, STATE_STANDBY, STATE_PUMPING, STATE_ON, STATE_DISABLED
int8[3] circuit_state
float64[3] circuit_voltage
int8 run_stop
int8 wireless_stop
