WIP

## It seems Appium doesn't support deeplink on real iOS devices

### Goal
Test deeplink on real iOS devices

### First try
* Result
SafariLauncher seems cannot open specified URL with safariInitialUrl

* desired capabilities
```
  "platformName": "iOS",
  "platformVersion": "12.0",
  "udid": "YOUR_DEVICE_ID",
  "bundleId": "foo.SafariLauncher",
  "automationName": "XCUITest",
  "deviceName": "YOUR_DEVICE_NAME",
  "safariInitialUrl": "YOUR_DEEP_LINK"
```

* Step
1.  Install SafariLauncher, WebDriverAgent
1.  Launch Appium
1.  Launch SafariLauncher

* Result screenshot
![Img](https://github.com/liangcodebase/sdetnote/blob/master/ci/images/safarilauncher_does_not_open_specific_url.png)

* Reference
http://appium.io/docs/en/drivers/ios-uiautomation-safari-launcher/
https://github.com/appium/appium/issues/8389


### Second try
* Result
SafariLauncher seems cannot modify the URL in Appium

* desired capabilities
```
  "platformName": "iOS",
  "platformVersion": "12.0",
  "udid": "YOUR_DEVICE_ID",
  "bundleId": "foo.SafariLauncher",
  "automationName": "XCUITest",
  "deviceName": "YOUR_DEVICE_NAME",
  "browserName": "Safari"
```

* Step
1.  Install SafariLauncher, WebDriverAgent
1.  Launch Appium
1.  Launch SafariLauncher
1.  Tap and Send keys in Appium element inspector on SafariLauncher URL 


* Result screenshot
![Img](https://github.com/liangcodebase/sdetnote/blob/master/ci/images/appium_ios_real_device_deeplink_open.png)


### Thrid try
* Result
Appium seems cannot find the Open button to open the app

* desired capabilities
```
  "platformName": "iOS",
  "platformVersion": "12.0",
  "udid": "YOUR_DEVICE_ID",
  "deviceName": "YOUR_DEVICE_NAME",
  "automationName": "XCUITest",
  
  "autoWebview": True,
  "autoAcceptAlerts": True,
  "app": '/Users/foo/bar.ipa',
  "browserName": "Safari"
  "safariInitialUrl": "YOUR_DEEPLINK_URL"
```


* Step
1.  Launch Appium
1.  Click Open
```
driver.find_element_by_accessibility_id('Open').click()
```
* Result screenshot
![Img](https://github.com/liangcodebase/sdetnote/blob/master/ci/images/appium_ios_real_device_deeplink_open.png)
