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
        send "put ${FILE}\n"
    }

}

expect {
    "sftp" {
        send "cd ~/Anna/file/"
        exp_continue
    }

    "sftp" {
        send "put ${FILE}"
    }
}

expect {
    "sftp" {
        exit 0
    }
}















































