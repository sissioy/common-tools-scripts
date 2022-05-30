#!/bin/bash
wget https://gitee.com/Mosiki/github/raw/master/github_hosts.txt
cp /etc/hosts.bk /etc/hosts.bak
cat github_hosts.txt >> /etc/hosts.bk
mv -f /etc/hosts.bk /etc/hosts
mv /etc/hosts.bak /etc/hosts.bk
rm -f github_hosts.txt
