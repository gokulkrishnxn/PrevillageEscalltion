#!/usr/bin/env python3

import os

def os_kernel_check():
	if full_scan != 0:
		os.system("clear")
		print("========OS-Kernel-Check========")
		os.system("uname -a")
		os.system("uname -r")
		os.system("cat /proc/version")
		os.system("cat /etc/os-release")
		os.system("cat /etc/issue")
		os.system("cat /etc/hostname")
		os.system("hostnamectl | grep Kernel")
		os.system("systemctl | grep Kernel")
		os.system("hostnamectl")
		print("------------------------------------------------")
		root_service_check()
	else:
		os.system("clear")
		print("========OS-Kernel-Check========")
		os.system("uname -a")
		os.system("uname -r")
		os.system("cat /proc/version")
		os.system("cat /etc/os-release")
		os.system("cat /etc/issue")
		os.system("cat /etc/hostname")
		os.system("hostnamectl | grep Kernel")
		os.system("systemctl | grep Kernel")
		os.system("hostnamectl")
	gotomain = input("Press Enter to return to main")
	main()
	
def root_service_check():
	if full_scan != 0:
		print("========Root-Service-Check==========")
		os.system("id")
		os.system("whoami")
		os.system("grep root /etc/passwd")
		os.system("ps -elf| grep root")
# Checking for kernel exploit using modprobe to get access to root 
		os.system("cat /proc/sys/kernel/modprobe") 
		os.system("locate modprobe")
		print("-----------------------------------------------------")
		suid_guid_check()
	else:
		os.system("clear")
		print("========Root-Service-Check==========")
		os.system("id")
		os.system("whoami")
		os.system("grep root /etc/passwd")
		os.system("ps -elf| grep root")
# Checking for kernel exploit using modprobe to get access to root 
		os.system("cat /proc/sys/kernel/modprobe") 
		os.system("locate modprobe")
	gotomain = input("Press Enter to return to main")
	main()
	
def suid_guid_check():
	if full_scan != 0:	
		print("=======SUID-GUID-Check============")
		print("")
		print("-----SUID Check-----")
		os.system("find / -perm -u=s -type f 2>/dev/null")
		print("")
		print("-----GUID Check-----")
		os.system("find / -perm -g=s -type f 2>/dev/null")
		print("---------------------------------------------------------")
	else:
		os.system("clear")
		print("=======SUID-GUID-Check============")
		print("")
		print("-----SUID Check-----")
		os.system("find / -perm -u=s -type f 2>/dev/null")
		print("")
		print("-----GUID Check-----")
		os.system("find / -perm -g=s -type f 2>/dev/null")
		print("----------------------------------------------------------")
		
	gotomain = input("Press Enter to return to main")
	main()
	
def main():
	global full_scan
	full_scan = 0
	
	os.system("clear")
# Print the Banner LPC
	print("""
	  _      _____ _   _ _    ___   __  _____      _       _ _                   ______               _       _   _             
 | |    |_   _| \ | | |  | \ \ / / |  __ \    (_)     (_) |                 |  ____|             | |     | | (_)            
 | |      | | |  \| | |  | |\ V /  | |__) | __ ___   ___| | ___  __ _  ___  | |__   ___  ___ __ _| | __ _| |_ _  ___  _ __  
 | |      | | | . ` | |  | | > <   |  ___/ '__| \ \ / / | |/ _ \/ _` |/ _ \ |  __| / __|/ __/ _` | |/ _` | __| |/ _ \| '_ \ 
 | |____ _| |_| |\  | |__| |/ . \  | |   | |  | |\ V /| | |  __/ (_| |  __/ | |____\__ \ (_| (_| | | (_| | |_| | (_) | | | |
 |______|_____|_| \_|\____//_/ \_\ |_|   |_|  |_| \_/ |_|_|\___|\__, |\___| |______|___/\___\__,_|_|\__,_|\__|_|\___/|_| |_|
                                                                 __/ |                                                      
                                                                |___/                                                       


	""")
	options = input("""
	1) OS-Kernel-Check
	2) Root Service check
	3) Suid-guid check
	4) Full Scan check
	5) Exit
	
	Shell>> """)
	
	if options == "1":
		os_kernel_check()
	elif options == "2":
		root_service_check()
	elif options == "3":
		suid_guid_check()
	elif options == "4":
		full_scan = full_scan + 1
		os_kernel_check()
	elif options == "5":
		exit()
	else:
		bad_options = input("Press Enter to return to main menu")
		
main()