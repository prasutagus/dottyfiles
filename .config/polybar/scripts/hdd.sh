#/bin/sh
df -h | grep /dev/sda3 | awk '{print $4}'
