# Operationalizing Machine Learning

## An overview of the project


In this project by using Azure Machine Learing Studio
- configure a cloud-based machine learning in Automated ML (Machione Learning)
- deploy the best performing model generated with Automated ML
- consume the deployed model
- Enable the loggin to monitor the the operation
- Using Apache Benchmark tool to measure perfomance when consuming the deployed model
Also using Python SDK in Jupyter Notebook to 
- automate Machine Learning as MLOps by creating, publishing, and consuming a pipeline

We work with the Bank Marketing dataset.
The Bank Marketing dataset contains information about a bank marketing campaign.
The objective field indicates if a customer subscribed to a fixed-term deposit or not.
We run inferense with REST calls by consuming the deployed model stated above.

## An Architectural Diagram

## Architectural Diagram

![](work/architecture.svg)

## Screen Recording

As the movie cannot be combined in my env,
please go through the following 3 videos in the order.

Operations in Azure ML Studio
https://youtu.be/jmRlyRRxztY
Python code
https://youtu.be/4yG-T66apco
Execution of the Python code
https://youtu.be/CtSpOLKu9BM
## how to improve the project in the future

The model performance wise, we can consider about 2 options for improvement
- Feature engineering the dataset
- Run deep learning models learning for more accuracy

To fully operate with MLOps appraoch, we should create a monitoring app to monitor the classification discrepancy.
Using that, trigger service bus or others to trigger AutoML process piplines to update the model and publish the model to the end points.

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

### Service principle and workspace

service principle created

![](work/Inked2021-07-11-00-02-56_LI.jpg)

![](work/Inked2021-07-11-00-03-32_LI.jpg)


az ml workspace share worked
![](work/Inked2021-07-11-00-00-29_LI.jpg)

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


Actually corrected requests as below in the Azure porta.
![](work/2021-07-12-01-38-49.png)

![](work/2021-07-12-02-00-29.png)

#### Logging is enabled by running the provided logs.py script

![](work/2021-07-16-00-17-36.png)

```
$ python logs.py
Failure while loading azureml_run_type_providers. Failed to load entrypoint hyperdrive = azureml.train.hyperdrive:HyperDriveRun._from_run_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Failure while loading azureml_run_type_providers. Failed to load entrypoint automl = azureml.train.automl.run:AutoMLRun._from_run_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Failure while loading azureml_run_type_providers. Failed to load entrypoint azureml.PipelineRun = azureml.pipeline.core.run:PipelineRun._from_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Failure while loading azureml_run_type_providers. Failed to load entrypoint azureml.ReusedStepRun = azureml.pipeline.core.run:StepRun._from_reused_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Failure while loading azureml_run_type_providers. Failed to load entrypoint azureml.StepRun = azureml.pipeline.core.run:StepRun._from_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Failure while loading azureml_run_type_providers. Failed to load entrypoint azureml.scriptrun = azureml.core.script_run:ScriptRun._from_run_dto with exception (cryptography 2.8 (/usr/lib/python3/dist-packages), Requirement.parse('cryptography>=3.2'), {'pyopenssl'}).
Warning: Falling back to use azure cli login credentials.
If you run your code in unattended mode, i.e., where you can't give a user input, then we recommend to use ServicePrincipalAuthentication or MsiAuthentication.
Please refer to aka.ms/aml-notebook-auth for different authentication mechanisms in azureml-sdk.
2021-07-12T08:33:26,670768400+00:00 - iot-server/run 
2021-07-12T08:33:26,689795800+00:00 - rsyslog/run 
2021-07-12T08:33:26,696474200+00:00 - gunicorn/run 
2021-07-12T08:33:26,832383400+00:00 - nginx/run 
/usr/sbin/nginx: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libcrypto.so.1.0.0: no version information available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libcrypto.so.1.0.0: no version information available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libssl.so.1.0.0: no version information available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libssl.so.1.0.0: no version information available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libssl.so.1.0.0: no version information available (required by /usr/sbin/nginx)
rsyslogd: /azureml-envs/azureml_429e58b1641c78c2352efc8ad21c49d9/lib/libuuid.so.1: no version information available (required by rsyslogd)
Starting gunicorn 20.1.0
Listening at: http://127.0.0.1:31311 (60)
Using worker: sync
worker timeout is set to 300
Booting worker with pid: 88
EdgeHubConnectionString and IOTEDGE_IOTHUBHOSTNAME are not set. Exiting...
2021-07-12T08:33:27,880060000+00:00 - iot-server/finish 1 0
2021-07-12T08:33:27,882374300+00:00 - Exit code 1 is normal. Not restarting iot-server.
SPARK_HOME not set. Skipping PySpark Initialization.
Generating new fontManager, this may take some time...
Initializing logger
2021-07-12 08:33:30,192 | root | INFO | Starting up app insights client
2021-07-12 08:33:30,193 | root | INFO | Starting up request id generator
2021-07-12 08:33:30,193 | root | INFO | Starting up app insight hooks

```

```
127.0.0.1 - - [15/Jul/2021:03:49:12 +0000] "GET /?a=fetch&content=%3Cphp%3Edie%28%40md5%28HelloThinkCMF%29%29%3C%2Fphp%3E HTTP/1.0" 200 7 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
2021-07-15 11:02:57,464 | root | INFO | Validation Request Content-Type
2021-07-15 11:02:57,466 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:02:57,563 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:02:57 +0000] "POST /score HTTP/1.0" 200 33 "-" "vscode-restclient"
2021-07-15 11:26:11,236 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:11,238 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:11,365 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:11 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:11,405 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:11,406 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:11,590 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:11 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:11,639 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:11,640 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:11,790 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:11 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:11,839 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:11,840 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,009 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,050 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,051 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,227 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,259 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,261 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,400 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,434 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,435 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,561 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,604 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,605 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,738 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,770 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,771 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:12,906 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:12 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 11:26:12,940 | root | INFO | Validation Request Content-Type
2021-07-15 11:26:12,941 | root | INFO | Scoring Timer is set to 60.0 seconds
2021-07-15 11:26:13,085 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:11:26:13 +0000] "POST /score HTTP/1.0" 200 33 "-" "ApacheBench/2.3"
2021-07-15 15:07:51,342 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:15:07:51 +0000] "GET /swagger.json HTTP/1.0" 200 3517 "-" "Go-http-client/1.1"
2021-07-15 15:08:00,056 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:15:08:00 +0000] "GET /swagger.json HTTP/1.0" 200 3517 "-" "Go-http-client/1.1"
2021-07-15 15:10:25,233 | root | INFO | 200
127.0.0.1 - - [15/Jul/2021:15:10:25 +0000] "GET /swagger.json HTTP/1.0" 200 3517 "-" "Go-http-client/1.1"

```


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