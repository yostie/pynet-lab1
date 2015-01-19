#...
#
#Author: Mike Yost
#
#Version: 1.1
#
#Purpose: Determine whether or not the running-config of a Cisco device has been saved to the startup-config
#
#...

# IMPORT LIBRARIES

from snmp_helper import snmp_get_oid,snmp_extract

# CONSTANTS

ROUTER_IP = 'x.x.x.x'
R1_SNMP_PORT = xxxx
R2_SNMP_PORT = xxxx
COMMUNITY_STRING = 'xxxx'
OID_RUN_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_START_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.3.0'
OID_SYSNAME = '1.3.6.1.2.1.1.5.0'

# DEFINE FUNCTIONS

def check_saved_config(start_time, run_time):

	if start_time == 0:
		return 'no_change_since_boot'

	elif start_time >= run_time:
		return 'run_saved'

	else:
		return 'run_not_saved'

def main():

	r1 = (ROUTER_IP, COMMUNITY_STRING, R1_SNMP_PORT)
	r2 = (ROUTER_IP, COMMUNITY_STRING, R2_SNMP_PORT)
	device_list = (r1,r2)

	for device in device_list:

		print "\n"
		
		sysname_raw = snmp_get_oid(device,oid=OID_SYSNAME)
		sysname = snmp_extract(sysname_raw)
		
		run_last_changed_raw = snmp_get_oid(device, oid=OID_RUN_LAST_CHANGED)
		run_last_changed = int(snmp_extract(run_last_changed_raw))
		
		start_last_changed_raw = snmp_get_oid(device, oid=OID_START_LAST_CHANGED)
		start_last_changed = int(snmp_extract(start_last_changed_raw))
	
		save_status = check_saved_config(start_last_changed, run_last_changed)
		
		if save_status is 'no_change_since_boot':
			print "*********************************************"
			print "Device = " + sysname
			print "RunningLastChanged Time = " + str(run_last_changed)
			print "StartupLastChanged Time = " + str(start_last_changed)
			print "Save Status: The startup configuration has not been changed since the last time the system was booted."
			print "*********************************************"
		elif save_status is 'run_saved':
			print "*********************************************"
			print "Device = " + sysname
			print "RunningLastChanged Time = " + str(run_last_changed)
			print "StartupLastChanged Time = " + str(start_last_changed)
			print "Save Status: The running configuration has been saved to the startup configuration."
			print "*********************************************"
		else:
			print "*********************************************"
			print "Device = " + sysname
			print "RunningLastChanged Time = " + str(run_last_changed)
			print "StartupLastChanged Time = " + str(start_last_changed)
			print "Save Status: The running configuration has NOT been saved to the startup configuration."
			print "*********************************************"

if __name__ == '__main__':

    main()

