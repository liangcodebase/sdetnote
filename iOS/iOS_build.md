#### Fix the iOS code signing issue when using Jenkins
https://stackoverflow.com/questions/21230696/no-code-sign-identities-found-setting-up-jenkins
http://code-dojo.blogspot.com/2012/09/fix-ios-code-signing-issue-when-using.html
```
1. "Code Sign error: There are no valid certificate/private key pairs in the default keychain"
Solution: Copy your iPhone developer certificate from "login" keychain to "System" keychain.
Detailed steps:
  open the "Keychain Access" application, click the login tab, right click the certificate like "iPhone Developer: your_name (XXXXXXX)", choose copy, then click the "System" tab, right click mouse, choose "Paste 2 items"; you might need to do the same thing with the certificate like "iPhone Distribution: your_name".

After doing this, you will get the second error.
2. "Code Sign error: Provisioning profile 'xxxxx-xxxx-xxxx-xxxxx' can't be found"
Solution: Copy the provision profile to Jenkins user folder.
The provision profile is under in the folder
/YourUserName/Library/MobileDevice/Provisioning Profiles,
for example in my machine, the provision profile files are under /Users/steve/Library/MobileDevice/Provisioning Profiles
In the mac, the Jenkins will be in /Users/Shared/Jenkins, create the following folder:
/Users/Shared/Jenkins/Library/MobileDevice/Provisioning Profile,  then copy the .mobileprovision file to this folder.
```

#### Unable to sign iOS builds with Jenkins
https://stackoverflow.com/questions/9626447/unable-to-sign-ios-builds-with-jenkins
```
 adding SessionCreate=true
 <?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
 <key>EnvironmentVariables</key>
 <dict>
   <key>JENKINS_HOME</key>
   <string>/Users/Shared/Jenkins/Home</string>
 </dict>
<key>GroupName</key>
<string>daemon</string>
<key>KeepAlive</key>
<true/>
<key>Label</key>
<string>org.jenkins-ci</string>
<key>ProgramArguments</key>
<array>
  <string>/bin/bash</string>
  <string>/Library/Application Support/Jenkins/jenkins-runner.sh</string>
</array>
<key>RunAtLoad</key>
<true/>
<key>UserName</key>
<string>jenkins</string>
<key>SessionCreate</key>
<true/>
</dict>
</plist>
```
