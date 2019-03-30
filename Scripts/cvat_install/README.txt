Dependencies:
	Docker CE (installation script provided)

Command:
	sudo bash cvat_install.sh
	[if required] sudo bash wo-docker.sh

-------------------------------------------------------------------------------------------------------

Installs CVAT on machine, as well as Docker CE if lacking.
Wo-docker.sh may require modifications in line 10, depending on the the machine. Detailed instructions
are provided within the script.

-------------------------------------------------------------------------------------------------------

After Installation:
	Go to localhost:8080. A login page should be displayed.

NOTE:
	If it refuses to upload files to CVAT, a superuser must be created. Running createSuper.sh and
	then typing in the name/passw for the super on the login page will resovle this. 
