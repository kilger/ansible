script to update kali
$nano kali_update.sh
#add
apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y
#end
$ chmod +x kali_update.sh
$ ./kali_update.sh