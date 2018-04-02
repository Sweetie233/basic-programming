安装**pycharm**时把时间调到2038年即可自动激活

## 代码开头
    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-
    ' a test module '
    __author__ = 'Michael Liao'
第1行和第2行是标准注释:
1. `第1行`注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行;
2. `第2行`注释表示.py文件本身使用标准UTF-8编码；
3. `第3行`是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
4. `第4行`使用__author__变量把作者写进去。

`print()`遇到逗号输出空格

## 输入输出模块
    input()
返回数据类型是str，转换成int:

    s = input('birth: ')
    birth = int(s)
当语句以冒号`:`结尾时，缩进的语句视为代码块

    # print absolute value of an integer:
    a = 100
    if a >= 0:
        print(a)
    else:
        print(-a)
## 数据类型
整数，浮点数，字符串（单双引号均可，推荐双引号），布尔值（`True`，`False`，用`and`、`or`和`not`运算），空值（`None`），变量（类似于指针形式），常量（全部大写变量名，只是习惯用法，仅此而已）
浮点除法`/`，整数除法`//`

## 字符串和编码
`ASCII`编码是1个字节；而`Unicode`编码通常是2个字节；本着节约的精神，又出现了把Unicode编码转化为“可变长编码”的`UTF-8`编码，把一个Unicode字符根据不同的数字大小编码成1-6个字节
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码.

 `bytes`类型的数据用带b前缀的单引号或双引号表示：`x=b'ABC'`
 
 `encode（）`方法：

    >>> 'ABC'.encode('ascii')
    b'ABC'
    >>> '中文'.encode('utf-8')
    b'\xe4\xb8\xad\xe6\x96\x87'

`decode（）`方法：

    >>> b'ABC'.decode('ascii')
    'ABC'
    >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
    '中文'

`len(str)`计算字节数bytes;

让Python解释器按照UTF-8编码读取：

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

格式化输出（与C语言一致，`%`实现）:

    >>> '%2d-%02d' % (3, 1)
    ' 3-01'
    >>> '%.2f' % 3.1415926
    '3.14'

`%s`永远起作用:

    >>> 'Age: %s. Gender: %s' % (25, True)
    'Age: 25. Gender: True'

`%%`转义`%`;

修改str：

    >>> a = 'abc'
    >>> a.replace('a', 'A')
## list和tuple
1. `list`是一种有序的集合，`classmates = ['Michael', 'Bob', 'Tracy']`
2. `len(classmates)`获取个数
3. 索引访问，下标从0开始，`classmates[0]`
4. `-1`索引最后一个元素，以此类堆，倒数第X个
5. 末尾追加：`classmates.append('Adam')`
6. 插入指定位置：`classmates.insert(1, 'Jack')`
7. 末尾删除：`classmates.pop()`；要删除指定位置的元素，用`pop(i)`方法
8. 替换元素：直接赋值，`classmates[1] = 'Sarah'`
9. 数据类型可以不同：`L = ['Apple', 123, True]`
10. 可以嵌套定义，用二维索引访问

排序：

    >>> a = ['c', 'b', 'a']
    >>> a.sort()

**tuple**

有序列表，一旦初始化就不能修改，`classmates = ('Michael', 'Bob', 'Tracy')`
下标访问，空的tuple，可以写成`t=( )`
防止歧义，只有1个元素的tuple定义时必须加一个逗号，`t = (1,)`

## 条件判断（注意冒号）
    age = 3
    if age >= 18:
        print('adult')
    elif age >= 6:
        print('teenager')
    else:
        print('kid')

非布尔表达式（非零数值、非空字符串、非空list等，就判断为True）：

    if x:
        print('True')

## 循环
for...in循环

    names = ['Michael', 'Bob', 'Tracy']
    for name in names:
        print(name)
range（）生成一个整数序列，再通过list()函数可以转换为list：

    >>> list(range(5))
    [0, 1, 2, 3, 4]
while循环：

    sum = 0
    n = 99while n > 0:
        sum = sum + n
        n = n - 2print(sum)

`break`会提前退出循环;
`continue`跳过当前循环。

 ## dict和set
 `dict`（无序字典）相当于C中的`map`，定义与访问：
 
    >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
    >>> d['Michael']
通过`in`判断`key`是否存在：

    >>> 'Thomas' in d
    False
    
`get`方法，如果key不存在，返回`None`，或者自己指定的value：

    >>> d.get('Thomas')
    >>> d.get('Thomas', -1)
    -1
    
删除：

    >>> d.pop('Bob')
    
`set`（无序集合）

一组`key`的集合，不能重复。
创建，需要提供一个`list`作为输入集合（重复元素自动过滤）：

    >>> s = set([1, 2, 3])
添加`add(key)`：

    >>> s.add(4)
删除`remove(key)`同理。

数学操作交并补：

    >>> s1 = set([1, 2, 3])
    >>> s2 = set([2, 3, 4])
    >>> s1 & s2
    {2, 3}
    >>> s1 | s2
    {1, 2, 3, 4}
    
## 函数
标准函数在文档中的位置：`The Python Standard Library->Built-in Functions`;

`abs`求绝对值:

    >>> abs(-20)
    20
`max`求最大:
    >>> max(2, 3, 1, -5)
    3

类型转换：

    >>> int('123')
    123
    >>> int(12.34)
    12
    >>> float('12.34')
    12.34
    >>> str(1.23)
    '1.23'
    >>> str(100)
    '100'
    >>> bool(1)
    True
    >>> bool('')
    False
函数重命名：

    >>> a = abs # 变量a指向abs函数
    >>> a(-1) # 所以也可以通过a调用abs函数
    1
## 定义函数
def语句，函数名、括号中的参数和冒号；在缩进块中编写函数体，返回值return语句。

    def my_abs(x):
        if x >= 0:
            return x
        else:
            return -x

`return None`可以简写为`return`。

空函数：

  def nop():
      pass

类型检查：

只允许整数和浮点数类型的参数，`bool y=isinstance(x, (int, float))`

返回多个值，`return nx, ny`,实际上返回值是一个tuple:

    >>> x, y = move(100, 100, 60, math.pi / 6)
    
默认参数（必须指向不变对象）：

    def enroll(name, gender, age=6, city='Beijing'):
        print('name:', name)
        
可变参数（参数前面加一个*号）：

    def calc(*numbers):
        sum = 0
        for n in numbers:
            sum = sum + n * n
        return sum
        
允许在list或tuple前面加一个*号，变成可变参数传进去。

关键字参数,
命名关键字参数,
参数组合,
略。

# 高级特性

## 切片
list取元素（L[start : _end]，注意不包括 _end ）。
第一个索引是0，还可以省略：

    >>> L[:3]
    ['Michael', 'Sarah', 'Tracy']
倒数切片（注意 _end省略时为取后面所有元素）：

    >>> L[-2:]
    ['Bob', 'Jack']
    >>> L[-2:-1]
    ['Bob']
跳位切片，前10个数，每两个取一个：

    >>> L[:10:2]
    [0, 2, 4, 6, 8]
所有数，每5个取一个：`L[ : : 5]`。

只写`[ : ]`就可以原样复制一个list

    >>> L[:]
    [0, 1, 2, 3, ..., 99]
1. tuple也可以切片，结果仍是tuple；
2. 字符串‘XXX’也可以切片，结果仍是字符串
3. Python中没有对字符串的截取函数，只需要切片操作即可

## 迭代
只要是可迭代对象，都可以迭代，比如dict：

    >>> d = {'a': 1, 'b': 2, 'c': 3}
    >>> for key in d:
            print(key)

默认情况下，迭代的是key；迭代value，可以用`for value in d.values()`，如果要同时迭代key和value，可以用`for k, v in d.items()`。
字符串str也可以迭代:

    >>> for x, y in [(1, 1), (2, 4), (3, 9)]:
    ...     print(x, y)
通过`collections`模块的`Iterable`类型判断可迭代对象：

    >>> from collections import Iterable
    >>> isinstance('abc', Iterable) # str是否可迭代
    True
    
## 列表生成式

Python内置用来创建list的生成式:

    >>> list(range(1, 11))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> [x * x for x in range(1, 11)]
    [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来。

for循环中的判断：

    >>> [x * x for x in range(1, 11) if x % 2 == 0]
    [4, 16, 36, 64, 100]
双重循环：

    >>> [m + n for m in 'ABC' for n in 'XYZ']
    ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
多个变量：

    >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
    >>> [k + '=' + v for k, v in d.items()]
    ['y=B', 'x=A', 'z=C']
## 生成器
与列表生成式直接生成整个列表不同，生成器可以在循环过程中不断推算后续的元素。
详细略。

## 迭代器
1. 可直接作用于for循环的有一类是集合数据类型，如list、tuple、dict、set、str等；一类是`generator`，包括生成器和带`yield`的`generator function`。
2. 可以直接作用于for循环的对象统称为可迭代对象：`Iterable`；
3. 可以被`next()`函数调用并不断返回下一个值的对象称为迭代器：`Iterator`。

    >>>from collections import Iterator
    >>>isinstance((x for x in range(10)), Iterator)
    True
    
生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

## Sorted
Python内置的sorted()函数就可以对list进行排序：

    >>> sorted([36, 5, -12, 9, -21])
    [-21, -12, 5, 9, 36]

sorted()接受函数作为参数，例如按绝对值排序：

    >>> sorted([36, 5, -12, 9, -21], key=abs)
    [5, 9, -12, -21, 36]
忽略大小写排序：

    >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
    ['about', 'bob', 'Credit', 'Zoo']
反向排序：

    >>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
    ['Zoo', 'Credit', 'bob', 'about']

## 匿名函数

    >>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
    [1, 4, 9, 16, 25, 36, 49, 64, 81]
    
匿名函数`lambda x: x * x`实际上就是：

    def f(x):
        return x * x
        
- 关键字`lambda`表示匿名函数，冒号前面的`x`表示函数参数；
- 只能有一个表达式，不用写`return`，返回值就是该表达式的结果。

# 模块
1. 在Python中，一个.py文件就称之为一个`模块（Module）`。
2. 模块可以避免函数名和变量名冲突。
3. 为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为`包（Package）`。
4. 举个例子，一个abc.py的文件就是一个名字叫abc的模块，假设abc与其他模块冲突了，可以通过包来组织模块，方法是选择一个顶层包名，比如mycompany；
5. 现在，abc.py模块的名字就变成了`mycompany.abc`
6. 请注意，每一个包目录下面都会有一个`__init__.py`的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
7. 自己创建模块时要注意命名，不能和Python自带的模块`名称冲突`。
8. 可以有多级目录，组成`多级层次的包结构`。

## 使用模块

    #!/usr/bin/env python3
    # -*- coding: utf-8 -*-

    ' a test module '

    __author__ = 'Michael Liao'

    import sys

    def test():
        args = sys.argv
        if len(args)==1:
            print('Hello, world!')
        elif len(args)==2:
            print('Hello, %s!' % args[1])
        else:
            print('Too many arguments!')

    if __name__=='__main__':
        test()

- `第1行`和`第2行`是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身使用标准UTF-8编码；
- `第4行`是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
- `第6行`使用__author__变量把作者写进去。
- 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，后面开始就是真正的代码部分。

导入`sys`模块后，我们就有了变量sys指向该模块。
`argv`变量用list存储了命令行的所有参数，第一个参数是.py文件的名称。

函数对象有一个`__name__`属性，可以拿到函数的名字：

    >>> def now():
    ...     print('2015-3-25')
    
    >>> now.__name__
    'now'
    
    if __name__=='__main__':
        test()

当在命令行运行文件时，Python解释器把`__name__`置为`__main__`，而如果在其他地方导入该hello模块时，if判断将失败。

## 安装第三方模块
在Python中，安装第三方模块，是通过包管理工具`pip`完成的。
一般来说，第三方库都会在Python官方的pypi.python.org网站注册，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：

    pip install Pillow

使用Pillow处理图片：

    >>> from PIL import Image
    >>> im = Image.open('test.png')
    >>> print(im.format, im.size, im.mode)
    PNG (400, 300) RGB
    >>> im.thumbnail((200, 100))
    >>> im.save('thumb.jpg', 'JPEG')
    
## 模块搜索路径
加载模块时，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：

  >>> import sys
  >>> sys.path
  ['', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python34.zip', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/plat-darwin', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages']

添加搜索目录：

- 一是直接修改sys.path（运行结束即失效）

  >>> import sys
  >>> sys.path.append('/Users/michael/my_py_scripts')
  
- 二是设置环境变量PYTHONPATH，该环境变量的内容会被自动添加到模块搜索路径中。设置方式与设置Path环境变量类似。注意只需要添加你自己的搜索路径，Python自己本身的搜索路径不受影响。

# I/O编程   
## 读文件
打开文件（默认读取文本文件，UTF-8编码）

    >>> f = open('/Users/michael/test.txt', 'r')
    
读取文件（返回str对象）

    >>> f.read()
    'Hello, world!'
    >>> f.close()
`with`语句自动调用`close()`方法

    with open('/path/to/file', 'r') as f:
        print(f.read())
`read(size)`读取指定大小内容，`readline()`读取一行，`readlines()`读取所有内容返回list：

    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉

二进制文件

    >>> f = open('/Users/michael/test.jpg', 'rb')
    >>> f.read()
    b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
指定字符编码格式

    >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
    >>> f.read()
    '测试'
`UnicodeDecodeError`，文件中夹杂非法编码的字符:

    >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

## 写文件

    >>> f = open('/Users/michael/test.txt', 'w')
    >>> f.write('Hello, world!')
    >>> f.close()
with语句自动调用close()，同时刷新缓冲区

    with open('/Users/michael/test.txt', 'w') as f:
        f.write('Hello, world!')

## 操作文件和目录
    >>> import os
    >>> os.name # 操作系统类型
    'posix'

如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。

环境变量

    >>> os.environ
    environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})

获取某个环境变量

    >>> os.environ.get('PATH')
    '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
    >>> os.environ.get('x', 'default')
    'default'

操作文件和目录

函数一部分放在os模块中，一部分放在os.path模块中。

    # 查看当前目录的绝对路径:>>> os.path.abspath('.')
    '/Users/michael'# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
    >>> os.path.join('/Users/michael', 'testdir')
    '/Users/michael/testdir'# 然后创建一个目录:
    >>> os.mkdir('/Users/michael/testdir')
    # 删掉一个目录:
    >>> os.rmdir('/Users/michael/testdir')

拆分路径

    >>> os.path.split('/Users/michael/testdir/file.txt')
    ('/Users/michael/testdir', 'file.txt')
获取扩展名

    >>> os.path.splitext('/path/to/file.txt')
    ('/path/to/file', '.txt')
    
重命名和删除

    # 对文件重命名:
    >>> os.rename('test.txt', 'test.py')
    # 删掉文件:
    >>> os.remove('test.py')

`shutil`模块提供了`copyfile()`函数，可以在shutil模块中找到很多实用函数，是os模块的补充。

- 列出所有目录：

    >>> [x for x in os.listdir('.') if os.path.isdir(x)]
    ['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
    
- 列出所有.py文件：

    >>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
    ['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
    

## 正则表达式
- 规则
`\d`可以匹配一个数字，`\w`可以匹配一个字母或数字，`.`可以匹配任意字符，`\s`可以匹配一个空格（也包括Tab等空白符），
`*`表示任意个字符，`+`表示至少一个字符，`?`表示0个或1个字符，`{n}`表示n个字符，`{n,m}`表示n-m个字符

- 进阶
用`[]`表示范围，比如：
`[0-9a-zA-Z\_]`可以匹配一个数字、字母或者下划线；

re模块

    s = 'ABC\\-001' # Python的字符串
    # 对应的正则表达式字符串变成：
    # 'ABC\-001'
    
因此我们强烈建议使用Python的r前缀，就不用考虑转义的问题了：

    s = r'ABC\-001' # Python的字符串
    # 对应的正则表达式字符串不变：
    # 'ABC\-001'

例如：
match()如果匹配成功，返回一个Match对象，否则返回None：

    import re
    test = '用户输入的字符串'
    if re.match(r'正则表达式', test):
        print('ok')
    else:
        print('failed')

- 切分字符串：

用正则表达式切分字符串比用固定的字符更灵活:

    >>>re.split(r'\s+', 'a b   c')
    ['a', 'b', 'c']

- 分组
提取子串，用`()`表示的就是要提取的分组（Group）；
例如：^(\d{3})-(\d{3,8})$分别定义了两个组

    >>>m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
    >>>m
    <_sre.SRE_Match object; span=(0, 9), match='010-12345'>
    >>> m.group(0)
    '010-12345'>>> m.group(1)
    '010'>>> m.group(2)
    '12345'
    
注意到`group(0)`永远是原始字符串。

- 贪婪匹配
正则匹配默认是贪婪匹配

    >>>re.match(r'^(\d+)(0*)$', '102300').groups()
    ('102300', '')
由于\d+采用贪婪匹配，结果0*只能匹配空字符串。
d+采用非贪婪匹配，加个?即可：

    >>>re.match(r'^(\d+?)(0*)$', '102300').groups()
    ('1023', '00')

- 编译
当使用正则表达式时，re模块内部：
1. 编译正则表达式，如果正则表达式的字符串本身不合法，会报错；
2. 用编译后的正则表达式去匹配字符串。
出于效率的考虑，我们可以预编译该正则表达式，接下来重复使用时就不需要编译这个步骤了，直接匹配：

    >>>import re
    #编译:
    >>>re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
    #使用：
    >>>re_telephone.match('010-12345').groups()
    ('010', '12345')
    >>> re_telephone.match('010-8086').groups()
    ('010', '8086')

编译后生成Regular Expression对象，由于该对象自己包含了正则表达式，所以调用对应的方法时不用给出正则字符串。

## 使用MySQL
- 在Windows上，安装时请选择UTF-8编码，以便正确地处理中文。
- 在Mac或Linux上，需要编辑MySQL的配置文件，把数据库默认的编码全部改为UTF-8。MySQL的配置文件默认存放在`/etc/my.cnf`或者`/etc/mysql/my.cnf`：

    [client]default-character-set = utf8

    [mysqld]default-storage-engine = INNODB
    character-set-server = utf8
    collation-server = utf8_general_ci

- 安装MySQL驱动

需要支持Python的MySQL驱动来连接到MySQL服务器

    $pip install mysql-connector-python --allow-external mysql-connector-python

如果上面的命令安装失败，可以试试另一个驱动：

    $pip install mysql-connector

- 连接数据库：

    #导入MySQL驱动:
    >>>import mysql.connector
    #注意把password设为你的root口令:
    >>>conn = mysql.connector.connect(user='root', password='password', database='test')
    >>>cursor = conn.cursor()
    #创建user表:
    >>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    #插入一行记录，注意MySQL的占位符是%s:
    >>> cursor.execute('insert into user (id, name) values (%s, %s)', ['1', 'Michael'])
    >>> cursor.rowcount
    1
    #提交事务:
    >>> conn.commit()
    >>> cursor.close()
    #运行查询:
    >>> cursor = conn.cursor()
    >>> cursor.execute('select * from user where id = %s', ('1',))
    >>> values = cursor.fetchall()
    >>> values
    [('1', 'Michael')]
    #关闭Cursor和Connection:
    >>> cursor.close()
    True>>> conn.close()
    
- 执行INSERT等操作后要调用`commit()`提交事务；
- MySQL的SQL占位符是`%s`。

## HTMLParser

如果我们要编写一个搜索引擎，第一步用爬虫抓取页面，第二步解析HTML页面；利用HTMLParser，可以把网页中的文本、图像等解析出来。

    from html.parser import HTMLParser
    from html.entities import name2codepoint

### urllib
Get

    from urllib import request

    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', data.decode('utf-8'))

    Status: 200 OK
    Server: nginx
    Date: Tue, 26 May 2015 10:02:27 GMT
    Content-Type: application/json; charset=utf-8
    Content-Length: 2049Connection: close
    Expires: Sun, 1 Jan 2006 01:00:00 GMT
    Pragma: no-cache
    Cache-Control: must-revalidate, no-cache, private
    X-DAE-Node: pidl1
    Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6","tags":[{"count":20,"name":"spring","title":"spring"}...}

    from urllib import request

    req = request.Request('http://www.douban.com/')
    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
    with request.urlopen(req) as f:
        print('Status:', f.status, f.reason)
        for k, v in f.getheaders():
            print('%s: %s' % (k, v))
        print('Data:', f.read().decode('utf-8'))

    ...
        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
        <meta name="format-detection" content="telephone=no">
        <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
    ...
