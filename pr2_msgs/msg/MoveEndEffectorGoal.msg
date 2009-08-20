Header header
# The desired joint configuratin
mechanism_msgs/JointState[] configuration

# Indicate if the goal is being enabled or disabled
byte enable

# Timelimit for the controller, if a plan is not
# found by this time, abort. Set it to zero for unlimited.
float64 timeout
