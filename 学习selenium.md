## 

### Drivers
#### Firefox
1. 因为MacOS需要数字认证，火狐暂不可用
#### Chrome
1. https://chromedriver.chromium.org/downloads
    - If you are using Chrome version 104, please download ChromeDriver 104.0.5112.79
~~2. chrome浏览器——设置——关于Chrome，找到浏览器版本，下载对应driver~~
3. chrome browser和driver版本自动保持一致
    - 参考synchronize_browser_driver_ver.py
    - 脚本可以自动下载和browser版本一致的driver，运行后找到driver路径：
    - /Users/admin/.wdm/drivers/chromedriver/mac64/104.0.5112/chromedriver
4. driver环境变量设置
    - https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/#quick-reference
    - To see what directories are already on PATH, open a Terminal and execute:
    - `echo $PATH`
    - If the location to your driver is not already in a directory listed, you can add a new directory to PATH:
    - `echo 'export PATH=$PATH:/Users/admin/.wdm/drivers/chromedriver/mac64/104.0.5112/chromedriver' >> ~/.zshenv`
    - `source ~/.zshenv`
    - `echo $PATH` 再次查看系统路径，发现driver路径已经被写入到系统路径中
    - You can test if it has been added correctly by starting the driver:
    - `chromedriver`, 如果失败也不要紧，继续尝试：
    - https://stackoverflow.com/questions/39428042/use-selenium-with-chromedriver-on-mac
    - `brew install chromedriver`
    - `brew update chromedriver`， 注意chrome driver的版本号和chrome browser版本号要一致
    - 此时在bash界面直接输入chromedriver应该可以启动driver

### selenium免登录
1. 手动输入用户名、密码等，登陆上目标网页
2. 把chromedriver可执行文件所在目录设置为系统目录，使得在bash页面可以直接打开chromedriver程序，参考上一步
3. 在.py文件中设置，可以直接用selenium在已经登陆的网页上进行操作
4. 参考：
    - https://www.cnblogs.com/yoyoketang/p/15132889.html
    - https://www.cnblogs.com/songzhenhua/p/12842919.html
    - https://stackoverflow.com/questions/8344776/can-selenium-interact-with-an-existing-browser-session
    - https://cosmocode.io/how-to-connect-selenium-to-an-existing-browser-that-was-opened-manually/
    - https://www.csdn.net/tags/NtzaAg2sMDkzOS1ibG9n.html

### 用selenium操纵网页页面
#### 官网参考
+ https://www.selenium.dev/documentation/webdriver/getting_started/first_script/

