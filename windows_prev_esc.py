import os


def os_windows_system():
	os.system("cls")
	if windows != 0:
		print("Check the windows info")
		os.system("systeminfo")
		os_user_info()
	else:
		os.system("cls")
		print("Check the windows info")
		os.system("systeminfo")
		gotomain = input("Press Enter to return to Main Menu")
		main()

def os_user_info():
	if windows != 0:
		print("Check The User Info - Prev-esc")
		os.system("whomai /all")
		os.system("net users")
		os.system("net user Administrators")
		os.system("net group /domain")
		os.system("net localgroup")
		os.system("net localgroup Administrators")
		os.system("net accounts")
		os.system("net share")
		os_updates_patches()
	else:
		os.system("cls")
		print("Check The User Info - Prev-esc")
		os.system("whomai /all")
		os.system("net users")
		os.system("net user Administrators")
		os.system("net group /domain")
		os.system("net localgroup")
		os.system("net localgroup Administrators")
		os.system("net accounts")
		os.system("net share")
		gotomain = input("Press Enter to return to Main Menu")
		main()


def os_updates_patches():
	if windows != 0:
		print("OS-Updates and Patches")
		os.system("icacls config\SAM")
		os.system("wmic qfe")
		os.system("Get-ChildItem Env: | ft Key,Value")
		os.system("wmic logicaldisk get caption,description,providername")
		gotomain = input("Press Enter to return to Main Menu")
		main()
	else:
		os.system("cls")
		os.system("icacls config\SAM")
		os.system("wmic qfe")
		os.system("Get-ChildItem Env: | ft Key,Value")
		os.system("wmic logicaldisk get caption,description,providername")
		gotomain = input("Press Enter to return to Main Menu")
		main()

def main():
	global windows
	windows = 0
	os.system("cls")
	print("""

█░█░█ █ █▄░█ █▀▄ █▀█ █░█░█ █▀   █▀█ █▀█ █▀▀ █░█   █▀▀ █▀ █▀▀
▀▄▀▄▀ █ █░▀█ █▄▀ █▄█ ▀▄▀▄▀ ▄█   █▀▀ █▀▄ ██▄ ▀▄▀   ██▄ ▄█ █▄▄
""")
	options = input("""
		1). Check windows info
		2). Check User info
		3). Check Updates info
		4). Full Scan 
		5). Exit


		WXP>> """)

	if options == "1":
		os_windows_system()
	elif options == "2":
		os_user_info()
	elif options == "3":
		os_updates_patches()
	elif options == "4":
		windows = windows + 1
		os_windows_system()
	elif options =="5":
		exit()
	else:
		Bad_option = input("Press Enter to return the main menu")
		main()


main()