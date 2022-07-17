printf "rm * -r" | VblogConn
VblogUpload at_server_setup.sh at_server_setup.sh
printf "chmod +x at_server_setup.sh; ./at_server_setup.sh" | VblogConn
printf "rm at_server_setup.sh" | VblogConn
