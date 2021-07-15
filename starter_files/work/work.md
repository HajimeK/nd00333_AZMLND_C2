
![](https://video.udacity-data.com/topher/2020/September/5f611a94_screen-shot-2020-09-15-at-12.36.11-pm/screen-shot-2020-09-15-at-12.36.11-pm.png)



service principle created

![](2021-07-11-00-02-56.png)

![](2021-07-11-00-03-32.png)


az ml workspace share worked
![](2021-07-11-00-00-29.png)


App Insights


![](2021-07-12-01-37-47.png)

Swagger is also there
![](2021-07-12-02-02-50.png)


enpoint.py
![](2021-07-15-11-08-11.png)

![](2021-07-12-01-38-49.png)

![](2021-07-12-02-00-29.png)


![](2021-07-14-16-27-07.png)


Apache Benchmark

Top
![](2021-07-15-04-30-49.png)

End
![](2021-07-15-04-31-40.png)



```
$ bash ./benchmark.sh 
This is ApacheBench, Version 2.3 <$Revision: 1843412 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking d8e9f6ad-4112-4417-97c0-01b4246b284a.japaneast.azurecontainer.io (be patient)...INFO: POST header == 
---
POST /score HTTP/1.0
Content-length: 812
Content-type: application/json
Authorization: Bearer sYDHOfPPfLTb0w5gDucnNQfT8VinfhBf
Host: d8e9f6ad-4112-4417-97c0-01b4246b284a.japaneast.azurecontainer.io
User-Agent: ApacheBench/2.3
Accept: */*


---
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:11 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: dd35567f-11e3-41dd-ab90-dd1fc4fd250d
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:11 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: 6f9f5c9b-5a43-405b-a899-77f31a960529
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:11 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: e86ffa3f-27eb-4d78-9af3-1509308b07fb
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: 1fa18b00-3636-4e41-a33d-dd1df69eb666
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: 66d94e9b-cf67-48bc-8f86-9bcf4c3db848
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: 0ad7ec00-1792-4d89-bcb5-1f7083dabe51
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: eecc9f75-2c61-4beb-9044-8ca2778da6f4
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: b3a9a8a3-a8b4-4bf8-8ae8-45e112cd8f9d
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:12 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: 1650d79a-a7c1-4da0-a451-0f9dfdfa7ab0
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
LOG: header received:
HTTP/1.0 200 OK
Content-Length: 33
Content-Type: application/json
Date: Thu, 15 Jul 2021 11:26:13 GMT
Server: nginx/1.10.3 (Ubuntu)
X-Ms-Request-Id: caeb8554-2c82-4c05-859e-803e83810b8e
X-Ms-Run-Function-Failed: False

"{\"result\": [\"yes\", \"no\"]}"
LOG: Response code = 200
..done


Server Software:        nginx/1.10.3
Server Hostname:        d8e9f6ad-4112-4417-97c0-01b4246b284a.japaneast.azurecontainer.io
Server Port:            80

Document Path:          /score
Document Length:        33 bytes

Concurrency Level:      1
Time taken for tests:   1.885 seconds
Complete requests:      10
Failed requests:        0
Total transferred:      2600 bytes
Total body sent:        10590
HTML transferred:       330 bytes
Requests per second:    5.30 [#/sec] (mean)
Time per request:       188.517 [ms] (mean)
Time per request:       188.517 [ms] (mean, across all concurrent requests)
Transfer rate:          1.35 [Kbytes/sec] received
                        5.49 kb/s sent
                        6.83 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:       11   13   3.1     12      19
Processing:   149  175  22.6    170     214
Waiting:      148  173  22.0    170     209
Total:        160  188  24.2    182     226

Percentage of the requests served within a certain time (ms)
  50%    182
  66%    204
  75%    210
  80%    219
  90%    226
  95%    226
  98%    226
  99%    226
 100%    226 (longest request)

```

Scheduled run
![](2021-07-14-16-27-16.png)

Dataset

![](2021-07-14-16-30-55.png)

![](2021-07-14-16-31-34.png)

Pipeline running with Jupyter notebook

![](2021-07-14-16-33-23.png)

In the ML Studio

![](2021-07-14-16-34-15.png)

Piepline endpoints
![](2021-07-14-16-34-59.png)

Published pipeline
![](2021-07-14-16-46-43.png)