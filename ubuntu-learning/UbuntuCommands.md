[Linux 命令大全](http://www.runoob.com/linux/linux-command-manual.html)

## 1. 创建.txt文件：
打开终端并输入 vim xxx.txt → 按Esc，然后输入:wq即可

## 3. 查看Ubuntu的内核版本号
>uname -a  #注意i686

查看Ubuntu的版本号

>cat /etc/issue

## 4. Ubuntu C++环境搭建
编译C程序使用gcc编译器，编译C++使用g++编译器
>sudo apt-get install g++

## 5. 使用g++编译C++文件
>g++ filename   #自动开始编译连接的过程，默认输出a.out<br>
>g++ filename -o output_filename    # 指定编译之后的文件名

## 6. Ubuntu下使用VS Code
编辑launch.json，配置调试环境；编辑tasks.json，配置编译环境。tasks.json推荐配置为：

    {
        "version": "0.1.0",
        "command": "g++",
        "isShellCommand": true,
        "args": ["-g","${workspaceRoot}/你的源码文件名.cpp"],
        "showOutput": "always"
    }
详细配置信息可以参考：https://blog.csdn.net/q932104843/article/details/51924900
(推荐两个插件：Bracket Pair Colorizer，对括号对进行着色；VSCode Great Icons，一套Icons主题)

编译快捷键：Ctrl+Shift+B；运行快捷键：Ctrl+F5（不调试直接运行，跟VS里的快捷键相同）。注意必须要先编译，再运行，修改代码才生效。

## 7. Ubuntu下安装Zsh和oh-my-zsh
参考网页：https://www.cnblogs.com/EasonJim/p/7863099.html

## 8. Ubuntu修改系统环境变量
>sudo gedit ~/.profile  # 用户目录下的环境变量

修改：`export PATH="$PATH:your path1:your path2..."`
>sudo gedit /etc/profile  #系统目录下的环境变量

## 9. Ubuntu锁屏快捷键
>Ctrl+Alt+L

## 10. With工具的使用
正常的`/with`目录包含：`bb/root`, `bb/conf`, `bb/common`, `bb/scripts`, `common`等目录。编译开发一般只使用`/with/bb/root`目录，通过使用`with -a bb/root=<开发包地址>`即可以快速设置编译使用的开发包。

hconsole：http://202.101.23.226:81/xwiki/bin/view/Main/FAQ/hconsole/

## 11. Ubuntu下搜索文件的命令
- `which 可执行文件名`，在PATH变量指定的路径中，搜索某个系统命令的位置，并且返回第一个搜索结果
- `locate 文件名`，linux会把系统内所有的文件都记录在一个数据库文件中，使用`locate+文件名`的方法会在linux系统维护的这个数据库中去查找目标，相比find命令去遍历磁盘查找的方式，效率会高很多；问题是数据库文件不是实时更新的，一般会每周更新一次，所以使用locate命令查找到的结果不一定是准确的。当然可以在使用locate之前通过`updatedb`命令更新一次数据库。
- `find / -name 文件名`，find是在指定的目录下遍历查找，如果目录使用`/`则表示在所有目录下查找，find方式查找文件消耗资源比较大，速度也慢一点。
- `whereis 文件名`，用于程序名的搜索，搜索结果只限于二进制文件（参数`-b`）、man说明文件（参数`-m`）和源代码文件（参数`-s`），**如果省略参数，则返回所有信息**。

## 12. 根据网络端口查看进程号
>sudo netstat -lnp|grep 80

这个时候，如果有进程在占用端口80，命令行便会显示该进程的详细信息。

假如占用80端口的进程pid是 846：
>sudo kill -9 846

## 13. 根据程序名找到进程号
>ps aux|grep 程序名 | grep -v grep

USER PID 注意第二个是pid；-v是避免匹配到grep进程

## 14. 使用sudo停止与启动服务
>sudo service cron stop <br>
>sudo service cron start

把定时任务写在root用户的cron里
>sudo crontab -u root -e

若在crontab中写了如下的一个任务：
>0 6 * * * echo "Good morning"

注意单纯echo，从屏幕上看不到任何输出，因为cron把任何输出都email到root的信箱了

## 15. crontab的使用
crontab启动：
>crontab -e 编辑模式启动crontab，按"i"键开启编辑模式

注意crontab执行定时任务时，不会加载任何环境变量。因此我们自己在Terminal里测试运行好的脚本可能在crontab里不能正常运行，所以我们需要先在自己写的shell脚本头部加上如下两句话使环境变量生效：
>source /home/xluo/.profile<br>
>source /etc/profile

为何crontab执行与脚本直接执行结果不同？(https://www.soosmart.com/topic/533.html)

`Python脚本在crontab中执行的几个坑`:

http://flyer0126.iteye.com/blog/2388142

## 16. 配置ls命令的颜色
如果您的终端或控制台输出的内容没有颜色，可以自己来定义。
`vim ~/.bashrc`，然后搜索  `# some more ls aliases`。然后加入下面的一行；
- `alias ls=’ls –-color=auto’`
- 执行 `source ~/.bashrc`，使你的`.bashrc`文件立即生效方法。

如果使用的是`zsh`，可以修改zsh的配置文件：`vim ~/.zshrc`，最下面加入上面的语句即可。

## 17. Linux中ctrl-c, ctrl-z, ctrl-d 区别
命令|描述
----|----
ctrl-c | kill foreground process
ctrl-z | suspend foreground process
ctrl-d | Terminate input, or exit shell

## 18. Ubuntu安装testplan模块
1. 把库文件夹放到这个文件夹下 linux(ubuntu)：
 
        /usr/local/lib/python2.7/dist-packages
2. 把库文件夹放到与py main文件相同目录下

#### 安装testplan依赖包：
- skip heavy dependencies but miss some functionality

        pip install -r requirements-basic.txt
        python setup.py develop --no-deps
- make a full setup

        pip install -r requirements.txt
        python setup.py develop

#### 安装数据库驱动
    pip install mysql-connector

 ## 19. Testplan学习笔记
    if __name__ == "__main__":
        exit (main())
调用函数`main()`并且当`main`结束时, it will exit giving the system the return code that is the result of `main`。如果main中没有明确指定返回值，则默认返回`None`，这与`return 0`语句产生的系统返回代码相同。

#### 生成详细的PDF报告文档：
>python testplanMyTest.py --pdf-style detailed --pdf report.pdf

- A `MultiTest` instance can be constructed from the following parameters:
    - **Name**: The name is internal to Testplan, and is used as a handle on the test
    - **Description**: The description will be printed in the report, below the test status.
    - **Suites**: MultiTest suites are simply objects (one or more can be passed) that must:
        - be decorated with `@testsuite`.
        - have one or more methods decorated with `@testcase`. 
    - **Environment**: The environment is a list of **drivers**. Drivers are typically implementations of messaging, protocols or external executables.

In addition suites can have setup() and teardown() methods. The `setup` method will be executed on suite entry, prior to any testcase if present. The `teardown` method will be executed on suite exit.

The `@testcase` decorated methods will execute `in the order` in which they are defined. If more than one suite is passed, the `suites` will be executed `in the order` in which they are placed in the list that is used to pass them to the constructor. 

`Testsuites` are normally identified in the `report` by their `class name`.

##### Multitest
https://testplan.readthedocs.io/en/latest/introduction.html

Multitest accepts a list of testsuites. This may be very useful in case different suites share the same environment. The **lifetime** of the drivers in respect to multiple suites is the following:
1. Start each driver in the environment in sequence
2. Run Suite1
3. Run Suite2 and any others
4. Stop each driver in reverse order


##### Ordering Tests
By default Testplan runs the tests in the following order:
- Test instances (e.g. `MultiTests`) are being executed in the order they are added to the plan object with plan.add() method.
- `Test suites` are run in the order they are added to the test instance via suites list.
- `Testcase` methods are run in their declaration order in the testsuite class.

This logic can be changed by use of custom or built-in test sorters. Currently Testplan supports only `shuffle` ordering via command line options. These can be used to randomise the order in which tests are run:

    $ test_plan.py --shuffle testcases

## 20. TestPlan Drivers
`Dependencies` between drivers are expressed very simply: any driver in the environment list passed to MultiTest is allowed to depend on any other driver appearing earlier than itself in the list.

`Dependent values` can be created either through the `context()` call, or using pairs of `double curly brackets` in configuration files (MultiTest is using the Tempita templating library).

    # Example environment of three dynamically connecting drivers.
    #  Client   Application    Service       

    environment=[
        Service(name='service'),
        Application(name='app',
                    host=context('service', '{{host}}')
                    port=context('service', '{{port}}'))
        Client(name='client',
            host=context('app', '{{host}}')
            port=context('app', '{{port}}'))
    ]


In practice the `context` is often used to communicate *hostnames*, *port* values, *file paths*, and other such values dynamically generated at runtime to avoid collisions between setups that must be shared between the various drivers to communicate meaningfully.

Any context value from any process can be accessed by the `context()` call, taking a driver name and a tempita expression that must be valid on that driver name. 

#### Built-in drivers
- **Driver** baseclass which provides the most common functionality features and all other drivers inherit .
- **App** that handles application binaries. 
- **TCPServer** and **TCPClient** to create TCP connections on the Multitest local environment and can often used to mock services.  
- **ZMQServer** and **ZMQClient** to create ZMQ connections on the Multitest local environment. 
- **FixServer** and **FixClient** to enable FIX protocol communication i.e between trading applications and exchanges.  
- **HTTPServer** and **HTTPClient** to enable HTTP communication.  
- **Sqlite3** to connect to a database and perform sql queries etc.  

#### Basic Assertions
命令 |	说明
----|-----
result.true | Checks if the value is truthy.
result.false | Checks if the value is falsy.
result.fail | Creates an explicit failure, a common use case is to use it with conditions.
result.equal / result.eq | Equality assertion, checks if reference is equal to the value.
result.not_equal / result.ne | Inequality assertion, checks if reference is not equal to the value.
result.less / result.lt | Comparison assertion, checks if reference is less than the value.
result.less_equal / result.le | Comparison assertion, checks if reference is less than or equal to the value.
result.greater / result.gt | Comparison assertion, checks if reference is greater than the value.
result.greater_equal / result.ge | Comparison assertion, checks if reference is greater than or equal the value.
result.isclose | Checks if first is close to second without requiring them to be exactly equal.
result.contain | Membership assertion, checks if member is in the container.
result.not_contain | Membership assertion, checks if member is not in the container.
result.log | Add a log entry in the console output and the report to make the output more human readable.
result.matplot | Displays a Matplotlib plot in the report.
result.regex.match | Checks if the given regexp (string pattern or compiled re object) matches (re.match) the value.
result.regex.search | Checks if re.search operation on the given text returns a match.


## 22. shell获取程序pid
获取自身pid：
- python获取pid：`os.getpid()`。
- Shell中获取pid:
  
        ps -ef | grep "name" | grep -v grep | awk '{print $2}'

## 23. Terminator中防止复制粘贴时出现"0~....1~"的情况
临时方案，终端输入：

    printf "\e[?2004l"

## 24. tee
In computing, tee is a command in command-line interpreters (shells) using standard streams which reads standard input and writes it to both standard output and one or more files, effectively duplicating its input. It is primarily used in conjunction with pipes and filters. 
> hconsole localhost ORDTEST1 --no-auth | tee a.txt

## 25. 关掉shell里的流buf
>stdbuf -i0 -o0 -e0 command

This turns off buffering completely for input, output and error. 

## 26. Terminator快捷键
命令 |	说明
----|-----
Ctrl+Shift+O | **Split** terminals **Horizontally**
Ctrl+Shift+E | **Split** terminals **Vertically**
Ctrl+Shift+Right | Move parent dragbar Right.
Ctrl+Shift+Left | Move parent dragbar Left
Ctrl+Shift+C | **Copy** selected text to clipboard
Ctrl+Shift+V |**Paste** clipboard text
Alt+Left | Move to the left terminal in the splitted terminators
Ctrl+Shift+W | Close the current terminal (关闭当前窗口)
Ctrl+Shift+Q | Quits Terminator (打开的终端全部关闭)


## 27. 清除Terminal的输出
命令 | 描述
----|----
clear | 将历史输出上滚，并不删除历史输出
reset | 清除历史输出，清空Terminal的buffer区域



## 28. 线程独占CPU
- lscpu <br>
显示CPU基础信息，CPU(s):8，Thread(s) per core:2，则物理内核共8/2=4个。
- lscpu -p <br>
  显示每一个CPU的详细信息，其中`L1d`表示一级数据缓存位于哪个核心；`L1I`表示一级指令缓存位于哪个核心；`L2`和`L3`分别表示二级和三级缓存位于哪个核心。一般4核心8线程的CPU编号为0-7。

线程运行时独占CPU核心，可以不用切换缓存数据，获得更快的性能。

需要首先在`/proc/cmdline`文件中末尾加上：`isolcpus=6-7`，表示编号为6和7的CPU可以被线程独占。此文件不可直接修改，修改方案见搜索引擎。
修改之后，程序能不能独占CPU以及独占的命令行指令，视具体的程序而定。

## 29. Ubuntu下修改MySQL用户名和密码
>sudo vim /etc/mysql/debian.cnf

查看默认生成的用户名和密码

在MySQL的Shell里敲入如下命令：

    mysql>CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser4667';

注意，此时newuser没有权限对数据库进行任何操作因此，我们需要给予此用户权限，以下命令给予root权限：

    mysql>GRANT ALL PRIVILEGES ON * . * TO 'testuser'@'localhost';

最后，还需要使新用户的权限生效，reload privileges：

    mysql>FLUSH PRIVILEGES;

Shell中查看用户和密码table：

    mysql>use mysql;
    mysql>select host,user,password from user;
    mysql>show databases;
    mysql>use someDB;
    mysql>show tables;

## 30. Linux中彻底删除文件
Linux中删除文件一般使用`rm`, 但是rm命令并不会真的清空保存该文件的数据块的内容，而只是释放了该文件所占用的索引节点和数据块。因此用rm删除的文件是可以通过一些方法恢复的(比如可以用debugfs恢复)。有些时候我们要彻底删除一些文件，可以使用`shred`命令来实现:

- shred会用一些随机内容覆盖文件所在的节点和数据块，并删除文件(-u参数)。
  
      $ shred -u file
- 如果想清除的更彻底一点可以加-z 参数，意思是先用随机数据填充，最后再用0填充。

      $ shred -u -z file

## 31. Ubuntu下pip3的安装、升级、卸载
- 安装
  
        sudo apt-get install python3-pip
- 升级
  
        sudo pip3 install --upgrade pip

- 卸载
  
        sudo apt-get remove python3-pip

## 32. Mysql workbench安装与使用
- Update repositories and upgrade if necessary:

      sudo apt update && sudo apt upgrade
- Install MySQL Workbench using the APT package manager:

      sudo apt install mysql-workbench
- Launch MySQL Workbench from the terminal:

      mysql-workbench

## 33. Tmux教程
https://www.hamvocke.com/blog/a-quick-and-easy-guide-to-tmux/

动作 | 命令
----|----
左右分屏|同时按住`Ctrl+b`，释放之后，按`Shift+%`即可分屏
上下分屏|同时按住`Ctrl+b`，释放之后，按`Shift+"`即可分屏
切换pane|同时按住`Ctrl+b`，释放之后，按方向键切换
关掉pane|输入`exit`回车，或者`Ctrl+d`
创建新窗口（覆盖原来的window)|同时按住`Ctrl+b`，释放之后，按`c`
切换到之前的窗口|同时按住`Ctrl+b`，释放之后，按`p`
切换到之后的窗口|同时按住`Ctrl+b`，释放之后，按`n`
切换窗口|`C-b <number>`，窗口号在状态栏左下方可见
detach tmux|`C-b d`
显示正在运行的tmux Sessions|`tmux ls`
attach tmux|`tmux attach -t 0`，其中`0`是`tmux ls`时最前面的数字。
创建新Session并命名|`tmux new -s newname`
重命名现有的session|`tmux rname-session -t 0 newname`
attach重命名的Session|`tmux attach -t newname`
显示帮助命令|`C-b ?`
调整窗口大小|`C-b C-<arrow>`
往上翻页|`C-b [`，退出时按`Esc`
关闭demo会话 | `tmux kill-session -t demo`
关闭服务器，关闭所有会话 | `tmux kill-server`

#### 复制粘贴命令
命令 | 含义
----- | ------
`Ctrl-b, [` | 进入copy模式
 `arrow`    | 移动光标到需要复制的文本起点
`C-space`   | 启动高亮文本功能
`arrow`     | 移动到需要复制的文本末尾
`Alt+w`     | 复制选中的文本到tmux剪贴板
`C-b, ]`    | 粘贴复制过的文本


## 34. SSH远程登录
- 登录ssh之后，修改密码的命令：

      passwd username
- 登录SSH之前，传送文件
    - 从服务器下载文件
    
          scp <用户名>@<ssh服务器地址>:<文件路径> <本地文件名> 
    - 上传文件到服务器

          scp <本地文件名> <用户名>@<ssh服务器地址>:<上传保存路径即文件名>

        - 只能将文件上传至用户目录下。如需上传至其它目录，可先上传至用户目录，然后移动文件至指定位置
    - 文件夹操作
        - 与文件操作类似，只需加入参数`-r`即可
     
## 35. Vim教程
#### vim使用方法
- vim (启动vim)
- i (进入插入模式)
- <输入文本>
- <Esc> (回到编辑模式)
- :w filename (保存文件为'filename')
- :q (退出vim)
- vim filename (打开您刚才在vim中保存的文件)

#### 设置vim 永久显示行号
https://blog.csdn.net/electrocrazy/article/details/79035216
输入：

    vim ~/.vimrc

在最后一行输入：

    set number
保存退出即可。

#### 简单命令
http://www.runoob.com/linux/linux-vim.html

命令 | 说明
---- | ----
`G` | 移动到最后一行
`gg` | 移动到第一行
`n<Enter>` | n为数字，光标向下移动n行
`H` |	光标移动到`这个屏幕`的最上方那一行的第一个字符
`L` |	光标移动到`这个屏幕`的最下方那一行的第一个字符
`/word` |	向光标之下寻找一个名称为 word 的字符串
`?word` |	向光标之上寻找一个字符串名称为 word 的字符串
`n` |	这个 n 是英文按键。代表重复前一个搜寻的动作。举例来说， 如果刚刚我们执行 /vbird 去向下搜寻 vbird 这个字符串，则按下 n 后，会向下继续搜寻下一个名称为 vbird 的字符串。
`N` |	这个 N 是英文按键。与 n 刚好相反，为『反向』进行前一个搜寻动作。 例如 /vbird 后，按下 N 则表示『向上』搜寻 vbird 。
h (←)  |	光标向左移动一个字符
j (↓)  |	光标向下移动一个字符
k (↑)  |	光标向上移动一个字符
l (→)  |	光标向右移动一个字符
`yy`     |	**复制**游标所在的那一行（常用）
`nyy`	| n 为数字。复制光标所在的向下 n 行
`y0`    |	复制光标所在的那个字符到该行行首的所有数据
`y$`    |	复制光标所在的那个字符到该行行尾的所有数据
`p`, `P`    |	p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！ 举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？ 那么原本的第 20 行会被推到变成 30 行。 （常用）
`u`       | **撤销**上一个动作
`ctrl+r`  | 恢复上一个撤销的动作
`dd`      | 删除游标所在的那一整行（常用）
`ndd`     |	n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行（常用）

09 11 * * * export LC_ALL=en_US.UTF-8 && with -b /local/sc/builds/v20180914-sc -a bb/scripts=/local/sc/dist/scripts/ -a bb/conf=/local/sc/dist/conf/ /with/bb/scripts/auto_test/crontab-UAT.sh > /with/bb/scripts/auto_test/crontablog/`date +\%Y\%m\%d`.log 

## 36. 配置环境

ftd和db运行命令都加上`--no-auth`

(hconsole)with中加上`export LC_ALL=en_US.UTF-8`

bailong上跑脚本：

    with -a common/conf=/local/sc/dist/common/conf -a bb/risk_limits=/local/sc/dist/risk_limits -a bb/conf=/local/sc/dist/conf -a bb/scripts=/local/sc/dist/scripts -b /local/sc/builds/v20180910-sc

bailong上的数据库连接：
`mysql -u bb -p -h chimp0.sc_jysx.in.athenacr.com`

bailong上的数据库连接：

    mysql -u bb -p -h chimp0.sc_jysx.in.athenacr.com

python脚本运行路径：`/home/xluo/ftdrundir`

## 37. Linux查找含有某字符串的所有文件
如果你想在当前目录下 查找"hello,world!"字符串,可以这样:

    grep -rn "hello,world!" *

指令 | 解释
-----|------
* | 表示当前目录所有文件，也可以是某个文件名
-r | 是递归查找
-n | 是显示行号
-R | 查找所有文件包含子目录
-i | 忽略大小写
-w | 匹配整个单词，而不是字符串的一部分
-C number | 匹配的上下文分别显示[number]行

## 38. Google开源项目风格指南
https://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments

## 39. gdb指南
#### 简单教程
https://www.cs.cmu.edu/~gilpin/tutorial/

#### 官方文档
https://ftp.gnu.org/old-gnu/Manuals/gdb-5.1.1/html_mono/gdb.html#SEC53

命令    |   说明
----    |----
gdb main | 启动debugger，并且debug可执行文件main
run     | 执行程序
backtrace | 查看调用栈
break function | 在函数入口处设置断点（只写`类名：：函数名`即可）
break linenum   | 在现在的源文件的第linenum行处设置断点，现在的源文件是只source text被打印的最后一个文件
break filename:linenum | 在源文件filename的第linenum行处设置断点
break filename:function | 在源文件filename的函数function入口处设置断点
condition 1 item_to_remove==1 | 对断点1设置条件，当条件满足时暂停执行
step    |    从断点处开始单步执行，会进入被调用的函数中 （注意设置断点后还需要重新run一次）
next    | 从断点处开始单步执行，不会进入被调用的函数中
回车   |  如果不敲入命令，直接点回车，gdb默认执行上一条命令
quit    | 退出gdb
p *pstData  |  查看变量的值，以及指针内容等
display variable | 单步执行时自动显示变量variable的值
info sources  | 列出所有用于编译的源文件








