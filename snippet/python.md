```
apt install python3-pip

pip3 install telethon

python3 vps/snippet/telethon_send_message.py
```


```
8 10 * * * cd /root/vps/snippet; ~/anaconda3/bin/python3 telethon_send_message.py >> tg.log 2>&1
```