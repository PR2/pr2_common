int8 STATE_NOPOWER=0
int8 STATE_STANDBY=1
int8 STATE_PUMPING=2
int8 STATE_ON=3
int8 STATE_DISABLED=4

Header header
string name # Name with serial number
uint32 serial_num # Serial number for this board's message
float64 input_voltage # Input voltage to power board
#
# Circuit States:
#  STATE_NOPOWER, STATE_STANDBY, STATE_PUMPING, STATE_ON, STATE_DISABLED
int8[3] circuit_state # One of the above states
float64[3] circuit_voltage  # Output voltage of each circuit

# True if robot should be enabled
bool run_stop           #Note - if the wireless run-stop is hit, this will be unobservable
bool wireless_stop 
