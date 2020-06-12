import win32api
import arrow

d = arrow.now()
print(d)
print(d.to("US/Eastern").format("HH:mm:ss"))


drives = win32api.GetLogicalDriveStrings()
drives = drives.split('\000')[:-1]
print(drives)
