* no sleep  
  ```
  pmset noidle
  ```
 
* restart smtp service
  ```
  sudo postconf compatibility_level=2
  sudo postfix reload
  sudo postfix start
  ```
* java home setting
  ```
  export JAVA_HOME="$(/usr/libexec/java_home -v 10.0.1)"
  ```
  Ref. [Stack overflow](https://stackoverflow.com/questions/6588390/where-is-java-home-on-macos-sierra-10-12-el-capitan-10-11-yosemite-10-10)
