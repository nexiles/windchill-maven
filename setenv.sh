echo "Windchill 10.2 (proxmoxx)"

# Java Version to use
JAVA_VERSION="1.7"

# Mount point to mount VM to
MOUNT_POINT="/Volumes/nexiles-wt-102"
ADMINPWD=$(security find-internet-password -a Administrator -s 192.168.100.80 -w)
test -z "$ADMINPWD" && error "need ADMINPWD"

# IP/Hostname of VM
IP="192.168.100.80"

# Windchill WT_HOME and windchill user
export WT_HOME="$MOUNT_POINT/ptc/Windchill_10.2/Windchill"
export WTUSER="wcadmin"
export WTPASS="wcadmin"

#--------------------------------------------------------------------------

function error() {
    echo "FATAL: $1"
}

test -d "$MOUNT_POINT" || mkdir $MOUNT_POINT || error "mkdir $MOUNT_POINT"

mount | grep $(basename $MOUNT_POINT) >/dev/null || {
    echo "Mounting vm ..."
    mount -t smbfs smb://Administrator:$ADMINPWD@$IP/D$ $MOUNT_POINT || error "error mounting VM."
}

export JAVA_HOME=$(/usr/libexec/java_home -v$JAVA_VERSION)

echo "JAVA_HOME=$JAVA_HOME"
echo "WT_HOME=$WT_HOME"
