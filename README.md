# NVMeAutomation
This is a automation test framework for NVMe SSD. Through this framework we can verify the functionality of the device, include admin and IO.
Some admin test cases have been developed in the framework, users can use them directly, or they can develop their own test cases in the framework.

## Environmental requirements
Support system: Linux<br>
Develop language: Python<br>

## Architecture
Basically divided into three layers<br>
* NVMe ioctrl library, through ioctrl communicate with the driver layer of the system, in this layer, we can send Admin or IO command to driver
* Common library, include Admin, io and Buffer python library, this library develop on ioctrl library, provide NVMe interface to test case
* Test case and test suite, base on library, user develop related test case, verify ssd functionality

 ![Architecture](/images/Architecture.png)