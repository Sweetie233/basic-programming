## 1. Python文件指针
https://www.cnblogs.com/blogCblog/p/5597973.html

## 2. 面向对象编程
参考网址：https://bop.mol.uno/14.oop.html
#### 普通变量
对象可以使用属于它的普通变量来存储数据。这种从属于对象或类的变量叫作`字段`（Field）。
字段有两种类型：它们属于某一类的各个实例或对象，`实例变量`（Instance Variables）；或是从属于某一类本身，称作与`类变量`（Class Variables）。

#### self
类方法与普通函数只有一种特定的区别：类方法必须多加一个参数(`self`)在参数列表开头，但是你不用在调用函数时为其赋值，Python会为它提供。这种特定的变量引用的是对象本身。Python中的 self相当于C++中的`this`指针。

- Python如何给self赋值?
    - 假设你有一个 `MyClass` 的类，这个类下有一个实例 `myobject`。当你调用一个这个对象的方法，如 `myobject.method(arg1, arg2)` 时，Python 将会自动将其转换成 `MyClass.method(myobject, arg1, arg2)`。这就是 self 的全部特殊之处所在。

#### `__init__`方法
该方法会在类的对象被实例化（Instantiated）时立即运行。这一方法可以对任何你想进行操作的目标对象进行初始化（Initialization）操作，类似于C++中对象的构造函数。这里你要注意在 init 前后加上的双下划线。

    class Person:
        def __init__(self, name):
            self.name = name

        def say_hi(self):
            print('Hello, my name is', self.name)
当我们在 Person 类下创建新的实例 p 时，我们采用的方法是先写下类的名称，后跟括在括号中的参数，形如：`p = Person('Swaroop')`。

#### 类变量与对象变量
- 类变量（Class Variable）是共享的（Shared）：它们可以被属于该类的所有实例访问。该类变量只拥有一个副本，当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现。
- 对象变量（Object variable）由类的每一个独立的对象或实例所拥有：在这种情况下，每个对象都拥有属于它自己的字段的副本。


        class Robot:
            """表示有一个带有名字的机器人。"""

            # 一个类变量，用来计数机器人的数量
            population = 0

            def __init__(self, name):
                """初始化数据"""
                self.name = name
                print("(Initializing {})".format(self.name))

            def say_hi(self):
                print("Greetings, my masters call me {}.".format(self.name))

            @classmethod
            def how_many(cls):
                """打印出当前的人口数量"""
                print("We have {:d} robots.".format(cls.population))
- 它是如何工作的？
  - `population`属于Robot类，因此它是一个类变量。`name`变量属于一个对象（通过使用self分配），因此它是一个对象变量。我们通过 `Robot.population` 而非 `self.population` 引用 population 类变量。
  - 当一个对象变量与一个类变量名称相同时，类变量将会被隐藏。
  - `how_many` 实际上是一个属于类而非对象的方法。我们使用`装饰器（Decorator）`将 how_many 方法标记为类方法。启用 @classmethod 装饰器等价于调用：`how_many = classmethod(how_many)`。
  - 所有的类成员都是公开的。但有如果你使用`双下划线`作为数据成员的前缀，形成诸如 __privatevar 这样的形式，Python 会使用名称调整（Name-mangling）来使其有效地成为一个私有变量。
  - 针对 C++/Java程序员的提示：所有类成员（包括数据成员）都是公开的，并且 Python 中所有的方法都是虚拟的（Virtual）。
#### 继承
    class SchoolMember:
        '''代表任何学校里的成员。'''
        def __init__(self, name, age):
            self.name = name
            self.age = age
            print('(Initialized SchoolMember: {})'.format(self.name))

        def tell(self):
            '''告诉我有关我的细节。'''
            print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")


    class Teacher(SchoolMember):
        '''代表一位老师。'''
        def __init__(self, name, age, salary):
            SchoolMember.__init__(self, name, age)
            self.salary = salary
            print('(Initialized Teacher: {})'.format(self.name))

        def tell(self):
            SchoolMember.tell(self)
            print('Salary: "{:d}"'.format(self.salary))
- 它是如何工作的？
    - 要想使用继承，在定义类时我们需要在类后面跟一个包含基类名称的元组。然后，我们会注意到基类的`__init__`方法是通过 self 变量被显式调用的，因此我们可以初始化对象的基类部分。
    - 需要牢记的一点是：因为我们在 Teacher 和 Student 子类中定义了`__init__`方法，Python 不会自动调用基类 SchoolMember 的构造函数，你必须自己显式地调用它。相反，如果我们没有在一个子类中定义一个 `__init__` 方法，Python 将会自动调用基类的构造函数。
    - 观察到，我们可以通过在方法名前面加上基类名作为前缀，再传入 self 和其余变量，来调用基类的方法。
    - Python 总会从当前的实际类型中开始寻找方法。如果它找不到对应的方法，它就会在该类所属的基类中依顺序逐个寻找基类的方法，这个基类是在定义子类时后跟的元组指定的。
    - 如果继承元组（Inheritance Tuple）中有超过一个类，这种情况就会被称作`多重继承`（Multiple Inheritance）。通过多重继承，一个子类就可以同时获得多个父类的所有功能。
    - `end`参数用在超类的`tell()`方法的`print`函数中，目的是打印一行并允许下一次打印在同一行继续。这是一个让 print 能够不在打印的末尾打印出`\n`（新行换行符）符号的小窍门。
    - 子类的的方法如果和父类的方法重名，子类会覆盖掉父类。

#### 关于Python面向对象编程更高级的用法参见：http://yangcongchufang.com/%E9%AB%98%E7%BA%A7python%E7%BC%96%E7%A8%8B%E5%9F%BA%E7%A1%80/python-object-class.html

## 3. python中的格式化字符串`format`
https://docs.python.org/2.7/library/string.html#formatspec

- 注意，如果字符串中有`{}`而不想转义，需要使用转义字符书写
    - `{{`表示`{`，`}}`表示`}`。

#### Accessing arguments by `position`:
    >>> '{0}, {1}, {2}'.format('a', 'b', 'c')
    'a, b, c'
    >>> '{}, {}, {}'.format('a', 'b', 'c')  # 2.7+ only
    'a, b, c'
    >>> '{2}, {1}, {0}'.format('a', 'b', 'c')
    'c, b, a'
    >>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
    'abracadabra'
#### Accessing arguments by `name`:
    >>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
    'Coordinates: 37.24N, -115.81W'
#### Accessing arguments’ `items`:
    >>> coord = (3, 5)
    >>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
    'X: 3;  Y: 5'
#### Replacing `%+f`, `%-f`, and `% f` and specifying a sign:
    >>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
    '+3.140000; -3.140000'
    >>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
    ' 3.140000; -3.140000'
    >>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
    '3.140000; -3.140000'
#### Replacing `%x` and `%o` and converting the value to different bases:
    >>> # format also supports binary numbers
    >>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
    'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
    >>> # with 0x, 0o, or 0b as prefix:
    >>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
    'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'




## 4. 三目运算符
    1 if 5>3 else 0
先输出结果，再判定条件：输出1，如果5大于3，否则输出0

## 5. Python assert Statement
如果assert条件为假，则终止程序，并且抛出AssertionError：

    assert <condition>
    assert <condition>,<error message>

## 6. range
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(1, 11)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    >>> range(0, 30, 5)
    [0, 5, 10, 15, 20, 25]
    >>> range(0, 10, 3)
    [0, 3, 6, 9]
    >>> range(0, -10, -1)
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    >>> range(0)
    []
    >>> range(1, 0)
    []
























