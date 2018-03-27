# couchdb_exp

## exp用途
 CVE-2017-12635 垂直权限绕过
 CVE-2017-12636 远程命令执行
 
## 影响版本
 小于 1.7.0 以及 小于 2.1.1

## Usage
`
python3 couchdb_exp.py http://your-ip:your-port
`

## Notice
无回显命令执行，配合dnslog等回显

自定义命令：修改command=“”

## 致谢
[phith0n](https://www.leavesongs.com/)@[vulhub](https://vulhub.org)