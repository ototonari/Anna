#!/usr/bin/expect

set FILE [lindex $argv 0]
set IPADDRESS [lindex $argv 1]

set timeout -1

spawn env LANG=C /usr/bin/sftp pi@${IPADDRESS}
expect {
    "(yes/no)?" {
        send "yes\n"
        exp_continue
    }

    "sftp" {
        send "cd ~/Anna/file/\n"
    }

    "sftp" {
        send "put ${FILE}\n"
    }

}

expect {
    "sftp" {
        exit 0
    }
}















































