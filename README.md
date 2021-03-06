# NVMeAutomation
This is a automation test framework for NVMe SSD. Through this framework we can verify the functionality of the device, include admin and IO.
Some admin test cases have been developed in the framework, users can use them directly, or they can develop their own test cases in the framework.

## Why develop this platform
* Current NVMe device testing tools are expensive, usually need to buy hardware and software license(当前NVMe SSD的测试工具都很昂贵，需要购买测试硬件，还要购买软件的license)
* Provide an open source test platform to make it easier to test NVMe chips. (提供一个开源的测试平台，可以更加容易对NVMe芯片进行测试) 
* The platform though ioctrl interface, Implement interaction with the NVMe chip, and tester easy to develop test cases.(通过操作系统驱动层的ioctrl接口，实现和NVMe 设备的交互，用户可以轻松开发自己需要的测试用例)

## Environmental requirements
Support system: Linux<br>
Develop language: Python<br>

## Architecture
Basically divided into three layers<br>
* NVMe ioctrl library, through ioctrl communicate with the driver layer of the system, in this layer, we can send Admin or IO command to driver
* Common library, include Admin, io and Buffer python library, this library develop on ioctrl library, provide NVMe interface to test case
* Test case and test suite, base on library, user develop related test case, verify ssd functionality

 ![Architecture](/images/Architecture.png)
 
 ## How to run test case
 Test case framework using nosetests, when you find your test case, run tests like below command:<br>
 More information about nosetests, please check with nose official documentation:https://nose.readthedocs.io/en/latest/man.html <br>
  * nosetests -s test_smart_health.py<br>
 
 ## Library
 Common library:<br>
 * Admin:<br>
 1. get log page<br>
    * Error Information<br>
    * SMART / Health Information<br>
    * Firmware Slot Information<br>
    * Changed Namespace List<br>
    * Commands Supported and Effects<br>
    * Self-test<br>
    * Controller Telemetry Host-Initiated<br>
    * Controller Telemetry Controller-Initiated <br>
 2. Identify<br>
    * Identify Namespace data structure<br>
    * Identify Controller data structure<br>
    * Active Namespace ID list<br>
    * Namespace Identification Descriptor list for the specified NSID<br>
    * Allocated Namespace ID list.<br>
    * Identify Namespace data structure for the specified allocated NSID<br>
    * Controller identifier list of controllers attached to the spcified NSID<br>
    * Controller identifier list of controllers that exist in the NVM subsystem.<br>
    * Primary Controller Capabilities data structure for the specified primary controller.<br>
    * Secondary Controller list of controllers associated with the primary controller processing the command.<br>
 3. Namespace<br>
    * Create namespace<br>
    * Delete namespace<br>
    * Attach namespace<br>
    * Detach namespace<br>
 4. Firmware Commit and Download<br>
    * Commit<br>
    * Download<br>
    
    