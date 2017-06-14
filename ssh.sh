#!/usr/bin/expect

set FILE [lindex $argv 0]
set IPADDRESS [lindex $argv 1]

set timeout -1

spawn env LANG=C /usr/bin/ssh pi@${IPADDRESS}
expect {
    "(yes/no)?" {
        send "yes\n"
        exp_continue
    }
    "\\\$" {
        send "cd ~/Anna/file/\n"
    }
}

expect {
    "\\\$" {
        send "play ${FILE}\n"
    }
}

expect {
    "\\\$" {
        exit 0
    }
}