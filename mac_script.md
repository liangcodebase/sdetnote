* no sleep  
 `pmset noidle `
 
* restart smtp service
  ```
  sudo postconf compatibility_level=2
  sudo postfix reload
  sudo postfix start
  ```
