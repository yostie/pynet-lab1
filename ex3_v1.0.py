# IMPORT LIBRARIES

from snmp_helper import snmp_get_oid,snmp_extract

# CONSTANTS

ROUTER_IP = 'x.x.x.x'
SNMP_PORT = xxxx
COMMUNITY_STRING = 'xxxxx'
OID_HISTORY_RUNNING_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.1.0'
OID_HISTORY_STARTUP_LAST_CHANGED = '1.3.6.1.4.1.9.9.43.1.1.3.0'

# BEGIN CODE

r1 = (ROUTER_IP, COMMUNITY_STRING, SNMP_PORT)

r1_run_last_changed_raw = snmp_get_oid(r1, oid=OID_HISTORY_RUNNING_LAST_CHANGED)
r1_start_last_changed_raw = snmp_get_oid(r1, oid=OID_HISTORY_STARTUP_LAST_CHANGED)

r1_run_last_changed = int(snmp_extract(r1_run_last_changed_raw))
r1_start_last_changed = int(snmp_extract(r1_start_last_changed_raw))

if r1_start_last_changed == 0:
    print "RunningLastChanged = " + str(r1_run_last_changed)
    print "StartupLastChanged = " + str(r1_start_last_change)
    print "The startup configuration has not been changed since the last time the system was booted."

elif r1_start_last_changed >= r1_run_last_changed:
    print "RunningLastChanged = " + str(r1_run_last_changed)
    print "StartupLastChanged = " + str(r1_start_last_changed)
    print "The running configuration has been saved to the startup configuration."

else:
    print "RunningLastChanged = " + str(r1_run_last_changed)
    print "StartupLastChanged = " + str(r1_start_last_changed)
    print "The running configuration has NOT been saved."

