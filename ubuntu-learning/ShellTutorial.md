#### 1. `#!` 告诉系统其后路径所指定的程序即是解释此脚本文件的 Shell 程序
>#!/bin/bash <br>
>echo "Hello World !"

注意第一句非常重要，脚本文件必须加上！！！
#### 2. 运行 Shell 脚本有两种方法
##### * 作为可执行程序
>chmod +x ./test.sh  # 使脚本具有执行权限 <br>
>./test.sh  # 执行脚本

注意，一定要写成`./test.sh`，而不是`test.sh`，要用`./test.sh`告诉系统说，就在当前目录找。
##### * 作为解释器参数
直接运行解释器，其参数就是shell脚本的文件名
>/bin/bash test.sh

#### 3. Shell 变量
>your_name="runoob.com"

定义变量时，变量名不加美元符号；注意，变量名和等号之间**不能有空格**;

使用一个定义过的变量，只要在变量名前面加美元符号即可，如：
>echo $your_name <br>
>echo ${your_name}

变量名外面的花括号是可选的，加不加都行，加花括号是为了帮助解释器识别变量的边界，比如下面这种情况：
>echo "I am good at ${skill}Script"

推荐给所有变量加上花括号，这是个好的编程习惯

##### * 变量类型
- **局部变量**：局部变量在脚本或命令中定义，仅在当前shell实例中有效
- **环境变量**：所有的程序，包括shell启动的程序，都能访问环境变量
- **shell变量**：shell变量是由shell程序设置的特殊变量。shell变量中有一部分是环境变量，有一部分是局部变量

#### 4. Shell 字符串
字符串可以用单引号，也可以用双引号，也可以不用引号
- **单引号**：单引号里的任何字符都会原样输出，单引号字符串中的变量（`$`）是无效的；单引号字串中不能出现单独一个的单引号（对单引号使用转义符后也不行）
- **双引号**：双引号里可以有变量；双引号里可以出现转义字符
>str="Hello, I know you are \"$your_name\"! \n"<br>
>echo $str

>Hello, I know you are "runoob"! 

获取字符串长度
>string="abcd"<br>
>echo ${#string} # 输出 4

#### 5. Shell 数组
bash支持一维数组（不支持多维数组），并且没有限定数组的大小。类似与 C 语言，数组元素的下标由 0 开始编号。
>array_name=(value0 value1 value2 value3)

还可以单独定义数组的各个分量：
>array_name[0]=value0<br>
>array_name[1]=value1<br>
>array_name[n]=valuen

读取数组元素值的一般格式是：`${array_name[index]}`

#### 7. Shell 注释
以`#`开头的行就是注释，会被解释器忽略。sh里没有多行注释，只能每一行加一个`#`号。

#### 8. Shell 传递参数
在执行 Shell 脚本时，向脚本传递参数，脚本内获取参数的格式为：`$n`。`n`代表一个数字，`1`为执行脚本的第一个参数，`2`为执行脚本的第二个参数，以此类推；其中`$0`为执行的文件名。
*给shell脚本传递的参数中如果包含空格，应该使用单引号或者双引号将该参数括起来，以便于脚本将这个参数作为整体来接收。*

#### 9.Shell 基本运算符
参考网址为[runoob.com](http://www.runoob.com/linux/linux-shell-basic-operators.html)。原生bash不支持简单的数学运算，但是可以通过其他命令来实现，例如`awk`和`expr`；`expr`是一款表达式计算工具，使用它能完成表达式的求值操作。例如，两个数相加（注意使用的是反引号\` 而不是单引号`'`）：
>val=\`expr 2 + 2\` <br>
>echo "两数之和为 : $val"

>两数之和为 : 4

注意：
- 表达式和运算符之间要有空格，例如`2+2`是不对的，必须写成`2 + 2`
- 完整的表达式要被 \` \` 包含

##### * 算术运算符
- 取余`%`：\`expr $b % $a\` 结果为 0
- 赋值`=`：`a=$b` 将把变量 b 的值赋给 a
- 相等`==`（相同返回true):`[ $a == $b ]` 返回 false
- 不相等`！=`：`[ $a != $b ]` 返回 true
  
注意：条件表达式要放在方括号之间，并且要有空格，例如:`[$a==$b]`是错误的，必须写成`[ $a == $b ]`

##### * 关系运算符
关系运算符**只支持数字**，不支持字符串，除非字符串的值是数字。
>-eq =; -ne !=; -gt >; -lt <; -ge >=; -le <=;

例如：`[ $a -ge $b ]`返回 false。

##### * 布尔运算符
- `！` 非运算：`[ ! false ]`返回true。
- `-o` 或运算：`[ $a -lt 20 -o $b -gt 100 ]`返回true
- `-a` 与运算：`[ $a -lt 20 -a $b -gt 100 ]`返回false

##### * 字符串运算符
>=; !=; -z; -n; 

`str` → `[ $a ]`返回true（检测是否为空，不为空则返回true)

##### * 文件测试运算符
>-b -c -d -f -g -k -p -u -r -w -x -s -e

`[ -e $file ]`返回true，文件（目录）存在


#### 10.  Shell echo命令
Shell 的 `echo` 指令与 PHP 的 `echo` 指令类似，都是用于字符串的输出
- 显示普通字符串
>echo "It is a test" <br>
>echo It is a test  # 这里的双引号完全可以省略
- 显示变量：`read` 命令从标准输入中读取一行,并把输入行的每个字段的值指定给 shell 变量
>read name  <br>
>echo "$name It is a test"
- 显示换行（echo自动添加换行符）
>echo -e "OK! \n" # `-e` 开启转义，`\c` 不换行
- 显示结果定向至文件
>echo "It is a test" > myfile
- 原样输出字符串，不进行转义或取变量(用单引号)
>echo '$name\"'
- 显示命令执行结果
>echo `date`    #结果将显示当前日期

注意： 这里使用的是反引号 `, 而不是单引号 '。

#### 11. Shell test 命令
Shell中的 test 命令用于检查某个条件是否成立，它可以进行数值、字符和文件三个方面的测试。
>if test $[num1] -eq $[num2]<br>
>if test $num1 = $num2<br>
>if test -e ./bash   # 测试文件是否存在<br>
>if test -e ./notFile -o -e ./bash   # `-o` 或运算

代码中的 `[]` 执行基本的算数运算
>result=$[a+b] # 注意等号两边不能有空格<br>
>echo "result 为： $result"

#### 12. Shell 流程控制
if else语法格式：
  
    if condition1
    then
        command1
    elif condition2 
    then 
        command2
    else
        commandN
    fi

for 循环一般格式：

    for var in item1 item2 ... itemN
    do
        command1
        command2
        ...
        commandN
    done
例如：

    for loop in 1 2 3 4 5
    do
        echo "The value is: $loop"
    done

while 语句

    while condition
    do
        command
    done
例如：

    int=1
    while(( $int<=5 ))
    do
        echo $int
        let "int++"
    done
使用中使用了 Bash `let` 命令，它用于执行一个或多个表达式，变量计算中**不需要**加上 `$` 来表示变量


#### 13. Shell 函数
shell中函数的定义格式如下：

    [ function ] funname [()]
    {
        action;
        [return int;]
    }
说明：
- 可以带function fun() 定义，也可以直接fun() 定义,不带任何参数。
- 参数返回，可以显示加：return 返回，如果不加，将以最后一条命令运行结果，作为返回值。 return后跟数值n(0-255）
  
例如：

    funWithReturn(){
        echo "这个函数会对输入的两个数字进行相加运算..."
        echo "输入第一个数字: "
        read aNum
        echo "输入第二个数字: "
        read anotherNum
        echo "两个数字分别为 $aNum 和 $anotherNum !"
        return $(($aNum+$anotherNum))
    }
>funWithReturn <br>
>echo "输入的两个数字之和为 $? !"

**函数参数**：在函数体内部，通过 `$n` 的形式来获取参数的值，例如，`$1`表示第一个参数，`$2`表示第二个参数...
>funWithParam 1 2 3 4 5 6 7 8 9 34 73

#### 14. Shell 输入/输出重定向
大多数 UNIX 系统命令从你的终端接受输入并将所产生的输出发送回​​到您的终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下，这恰好是你的终端。同样，一个命令通常将其输出写入到标准输出，默认情况下，这也是你的终端。

重定向命令列表如下：

命令 |	说明
----|-----
command > file	| 将输出重定向到 file。
command < file	| 将输入重定向到 file。
command >> file	| 将输出以追加的方式重定向到 file。
n > file	| 将文件描述符为 n 的文件重定向到 file。
n >> file	| 将文件描述符为 n 的文件以追加的方式重定向到 file。
n >& m	| 将输出文件 m 和 n 合并。
n <& m	| 将输入文件 m 和 n 合并。
<< tag	| 将开始标记 tag 和结束标记 tag 之间的内容作为输入。

>$ command > file 2>&1 <br>
>$ command >> file 2>&1
这里的&没有固定的意思

放在`>`后面的`&`，表示重定向的目标不是一个文件，而是一个文件描述符，内置的文件描述符如下:
- 1 => stdout
- 2 => stderr
- 0 => stdin

换言之 2>1 代表将stderr重定向到当前路径下文件名为1的regular file中，而2>&1代表将stderr重定向到文件描述符为1的文件(即/dev/stdout)中，这个文件就是stdout在file system中的映射

而`&>`file是一种特殊的用法，也可以写成`>&`file，二者的意思完全相同，都等价于:
>file 2>&1

此处&>或者>&视作整体，分开没有单独的含义

File descriptors 0, 1 and 2 are for stdin, stdout and stderr respectively.

File descriptors 3, 4, .. 9 are for additional files. In order to use them, you need to open them first. For example:

>exec 3<> /tmp/foo  #open fd 3.    <br>
>echo "test" >&3    <br>
>exec 3>&- #close fd 3.

关于Bash的I/O重定向更高级的用法：
http://tldp.org/LDP/abs/html/io-redirection.html   

#### 15. Shell 文件包含
Shell 也可以包含外部脚本。这样可以很方便的封装一些公用的代码作为一个独立的文件。语法格式如下：
>. filename   # 注意点号`.`和文件名中间有一空格

或
>source filename

#### 16. 什么是shell?
Linux系统的shell相当于操作系统的“一层外壳”，它是命令语言解释器，它为用户提供了使用操作系统的接口，它不属于内核，而是在内核之外以用户态方式运行。它的基本功能是解释并执行用户打入的各种命令，实现用户与Linux内核的接口。 

在启动Linux系统后，内核会为每个终端用户建立一个进程去执行shell解释程序，它的执行过程遵循以下步骤：

1. 读取用户由键盘输入的命令； 
2. 对命令进行分析，以命令名为文件名，并将其他参数改造为系统调用execve()参数处理所要求的格式； 
3. 终端进程(shell)调用fork()或者vfork()建立一个子进程； 
4. 子进程根据文件名（命令名）到目录中查找有关文件，将他调入内存，并创建新的文本段，并根据写时拷贝的方式创建相应的数据段、堆栈段； 
5. 当子进程完成处理或者出现异常后，通过exit()或_exit()函数向父进程报告； 
6. 终端进程调用wait函数来等待子进程完成，并对子进程进行回收；

#### 17. shell对输入命令的分析?
在Linux中，有一些命令，例如`echo`，`pwd`，`cd`是包含在shell内部的命令，还有一些命令，例如`cp`，`mv`或`rm`是存在于文件系统中某个目录下的单独的程序。如何区分这些命令是否是内置，外部命令，可以利用`type`命令来辨别,例如：
>type cd 

`cd is a shell builtin`
>type rm

`rm is /bin/rm`

##### * 内部或者外部的命令有什么区别？
- 像`cd`，`pwd`这些内置命令是属于Shell的一部分，当Shell一运行起来就随Shell加载入内存，因此，当我们在命令行上输入这些命令就可以像调用函数一样直接使用，效率非常高。
- 而如`ls`，`cat`这些外部命令却不是如此，当我们在命令行输入`cat`，当前的Shell会fork一个子进程，然后调用`exec`载入这个命令的可执行文件，比如`bin/cat`，因此效率上稍微低了点。

## shell文件描述符最大限制
Limits on the number of file descriptors：https://unix.stackexchange.com/questions/84227/limits-on-the-number-of-file-descriptors

































