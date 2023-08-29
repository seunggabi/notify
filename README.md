## notify
```shell
vi ./sh/env.sh
```
```shell
./sh/install.sh
./sh/start.sh
```

### start
```shell
sh ./sh/install.sh
```
```shell
ENV=test sh ./sh/start.sh
```
```shell
lsof -ti:12345 | xargs kill -9
```

### slack
```
# Bot User OAuth Access Token: xoxb-**************

# scope
- chat:write
- files:write
```

### HTTP (GET & POST)
```
http://localhost:12345/slack/v1/send?test=true&message=test
http://localhost:12345/slack/v1/send?test=true&image=https://t1.daumcdn.net/cfile/tistory/27738433597DCB1312
http://localhost:12345/email/v1/send?to=test%40seunggabi.com&cc=test%40seunggabi.com&bcc=test%40seunggabi.com&subject=%5BTEST%5D%20mail&text=test
```
