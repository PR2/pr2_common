# These registers are per battery
time      last_battery_update     # last time any battery update occurred
int16[48] battery_register        # value of this register in the battery
bool[48]  battery_update_flag     # Has this register ever been updated
time[48]  battery_register_update # last time this specific register was updated
