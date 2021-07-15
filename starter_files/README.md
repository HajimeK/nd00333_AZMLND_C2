# Operationalizing Machine Learning

## An overview of the project

## An Architectural Diagram


## Architectural Diagram
*TODO*: Provide an architectual diagram of the project and give an introduction of each step. An architectural diagram is an image that helps visualize the flow of operations from start to finish. In this case, it has to be related to the completed project, with its various stages that are critical to the overall flow. For example, one stage for managing models could be "using Automated ML to determine the best model". 

## Key Steps
*TODO*: Write a short discription of the key steps. Remeber to include all the screenshots required to demonstrate key steps. 

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.


## A short description of how to improve the project in the future


## Screenshots required with a short description to demonstrate key steps


## VIdeo

The screencast should meet the following criteria:

    Screencast is 1-5 minutes in length
    Audio is clear and understandable
    Video is 1080P or higher with 16:9 aspect ratio
    text is readable
Operationalizing Machine Learning
The screencast shows the entire process of the working ML application, including a demonstration of:

    Working deployed ML model endpoint.
    Deployed Pipeline
    Available AutoML Model
    Successful API requests to the endpoint with a JSON payload

## Screenshots for Deploy model in Azure ML Studio

### Create a new AutoML run

#### “Registered Datasets” in ML Studio shows "Bankmarketing" dataset available

![](work/2021-07-14-16-30-55.png)

![](work/2021-07-14-16-31-34.png)

#### The experiment is shown as completed.

![](work/2021-07-15-23-49-35.png)

### Deploy a model and consume a model endpoint via an HTTP API


#### Endpoints section in Azure ML Studio, showing that “Application Insights enabled” says “true”.

App Insights is enabled
![](work/2021-07-12-01-37-47.png)

#### Logging is enabled by running the provided logs.py script


Actually corrected requests as below in the Azure porta.
![](work/2021-07-12-01-38-49.png)

![](work/2021-07-12-02-00-29.png)

#### Swagger runs on localhost showing the HTTP API methods and responses for the model

Swagger is also there in the endpoint
![](work/2021-07-12-02-02-50.png)

*swagger.json* file is obtained here, and deployed to the locally running docker container for swagger.

![](work/Swagger%20UI.png)

#### endpoint.py script runs against the API producing JSON output from the model.

![](work/2021-07-15-11-08-11.png)

#### Apache Benchmark (ab) runs against the HTTP API using authentication keys to retrieve performance results. (optional)


![](work/2021-07-15-04-30-49.png)
![](work/2021-07-15-04-31-40.png)


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



## Screenshots of Publish an ML Pipeline

### Create and publish a pipeline

#### The pipeline section of Azure ML studio, showing that the pipeline has been created

![](work/2021-07-14-16-34-15.png)

#### The Bankmarketing dataset with the AutoML module



#### The “Published Pipeline overview”, showing a REST endpoint and a status of ACTIVE

![](work/2021-07-14-16-34-59.png)

### Configure a pipeline with the Python SDK

#### A screenshot of the Jupyter Notebook is included in the submission showing the “Use RunDetails Widget” with the step runs

![](work/2021-07-14-16-33-23.png)

### Use a REST endpoint to interact with a Pipeline

#### ML studio showing the pipeline endpoint as Active

Published pipeline
![](work/2021-07-14-16-46-43.png)

#### ML studio showing the scheduled run

![](work/2021-07-14-16-27-16.png)