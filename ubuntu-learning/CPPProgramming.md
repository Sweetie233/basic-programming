## 1. 一个空类应该占用多少字节？
C++的空类是指这个类不带任何数据，即类中没有非静态(non-static)数据成员变量，没有虚函数(virtual function)，也没有虚基类(virtual base class)。
C++标准指出，不允许一个对象（当然包括类对象）的大小为0，不同的对象不能具有相同的地址。这是由于：
- new需要分配不同的内存地址，不能分配内存大小为0的空间
- 避免除以 sizeof(T)时得到除以0错误

故使用一个字节来区分空类。
如果空类包含成员函数，则大小仍然是１字节；如果包含一个int型数据，则大小是４字节，空类原来的１字节舍去。如果包含虚函数，则有一个指针指向虚函数列表，该指针占用４字节大小。

C++中全局变量和静态变量的存储放在一块，都在全局区（又叫静态static区)；注意与堆区，栈区，文字常量区和程序代码区进行区分。

## 2. 虚函数与纯虚函数
- 定义一个函数为`虚函数`，不代表函数没有实现。定义他为虚函数是为了允许用基类的指针来调用子类的这个函数。
    - 虚函数只能借助于指针或者引用来达到多态的效果。
- 定义一个函数为`纯虚函数`，才代表函数没有被实现。

纯虚函数是在基类中声明的虚函数，它在基类中没有定义，但要求任何派生类都要定义自己的实现方法。在基类中实现纯虚函数的方法是在函数原型后加`=0`。同时含有纯虚拟函数的类称为`抽象类`，它不能生成对象。

    virtual void funtion1()=0

如果派生类中没有重新定义纯虚函数，而只是继承基类的纯虚函数，则这个派生类仍然还是一个抽象类。如果派生类中给出了基类纯虚函数的实现，则该派生类就不再是抽象类了，它是一个可以建立对象的具体的类。

抽象类的主要作用是将有关的操作作为结果接口组织在一个继承层次结构中，由它来为派生类提供一个公共的根，派生类将具体实现在其基类中作为接口的操作。

## 3. 虚拟内存
现在的操作系统基本都使用逻辑地址和物理地址这两个概念。简单来说，`逻辑地址`就可以理解为虚拟地址，这个地址是让用户看的，是虚拟的，并不真实存在，但是经过硬件和软件的配合，将逻辑地址映射到硬件中实实在在的`物理地址`上，实现了逻辑地址和物理地址的分离。

虚拟内存技术允许执行进程不必完全放在内存中，这样我们就可以运行比物理内存大的程序，使得程序员不受内存存储的限制。

## 4. 虚析构函数

当用一个基类的指针删除一个派生类的对象时，派生类的析构函数会被调用。
当然，并不是要把所有类的析构函数都写成虚函数。因为当类里面有虚函数的时候，编译器会给类添加一个虚函数表，里面来存放虚函数指针，这样就会增加类的存储空间。所以，只有当一个类被用来作为基类的时候，才把析构函数写成虚函数。

虚析构函数是为了解决基类的指针指向派生类对象，并用基类的指针删除派生类对象。

抽象类是准备被用做基类的，`基类必须要有一个虚析构函数`。
## 5. 内存泄漏如何避免
- **内存溢出(out of memory)**：程序在申请内存时，没有足够的内存空间供其使用。一般发生内存溢出时，程序讲无法进行，强制终止。
- **内些泄露(memory leak)**：程序在申请内存后，无法释放已经申请的内存空间，内存泄露的积累将导致内存溢出。

一般我们常说的`内存泄漏`是指`堆内存`的泄漏。堆内存是指程序从堆中分配的，大小任意的（内存块的大小可以在程序运行期决定），使用完后必须显示释放的内存。C内存分配采用malloc和free, C++采用new和delete, 调用方式要分别匹配。也就是用 malloc/alloc/realloc 方式申请的内存，用 free 释放；用 new 方式申请的内存用 delete 释放。

注意：堆内存如果程序员没有释放掉，那么在`程序`结束后，操作系统会自动回收。

比较常见的情况：
1. `函数`在入口处分配内存，在出口处释放内存，但是C函数可以在任何地方退出（return)，所以一旦有某个出口处(return)没有释放应该释放的内存，就会发生内存泄漏。
2. 基类的析构函数不是虚函数，则用基类指针调用子类对象时，子类析构函数不会运行。
3. vector中容纳的是指针时，最后只将vector.clear()不会释放指针指向的内存；由于vector的内存占用空间只增不减，所有内存空间是在vector析构时候才能被系统回收，clear()可以清空所有元素。但是即使clear()，vector所占用的内存空间依然如故，无法保证内存的回收。可以用`swap()`来帮助你释放内存。swap()是交换函数，使vector离开其自身的作用域，从而强制释放vector所占的内存空间
   
        vector<type> v;
        //.... 这里添加许多元素给v
        //.... 这里删除v中的许多元素
        vector<type>(v).swap(v);  //应该是构造一个新的vector
        //此时v的容量已经尽可能的符合其当前包含的元素数量
        //对于string则可能像下面这样
        string(s).swap(s);
4. shared_ptr环形引用，特别是涉及到有环图这样的结构时，如果用shared_ptr就会造成环形引用，然后就会内存泄露
5. delete一个对象数组时，未添加[]

        int* p=new int[5];
        delete [] p;
   
##### 如何防止内存泄漏
- 静态检测 <br>
所谓静态检测，就是不运行程序，在程序的编译阶段进行检测，主要原理就是对new与 delete，malloc与free进行匹配检测。常用的静态检测的工具有splint，PC-LINT，BEAM等。但是静态检测不能判定跨线程的内存申请与释放。
- 动态检测<br>
所谓动态检测，就是运行程序的过程中，对程序的内存分配情况进行记录并判定。常用的工具有valgrind，Rational purify等。对于动态检测来说，最大的弊端就是会加重程序的负担，对于一些大型工程，涉及到多个动态库，带来的负担太重，这时候就需要自己根据需求写一套了。

## 6. 智能指针
用来解决申请内存忘记释放，或者抛出异常导致不能正常释放内存之内的内存泄漏情况。

智能指针和普通指针的区别在于智能指针实际上是对普通指针加了一层封装机制，这样的一层封装机制的目的是为了使得智能指针可以方便的管理一个对象的生命期。一个对象什么时候和在什么条件下要被析构或者是删除是受智能指针本身决定的，用户并不需要管理。

智能指针是在 `<memory>` 标头文件中的 `std` 命名空间中定义的。

    std::unique_ptr<LargeObject> pLarge(new LargeObject());

智能指针具有通过使用“点”表示法访问的成员函数。 例如，一些 STL 智能指针具有释放指针所有权的reset成员函数。智能指针通常提供直接访问其原始指针的方法。 STL 智能指针拥有一个用于此目的的`get`成员函数:

    // Pass raw pointer to a legacy API
    LegacyLargeObjectFunction(pLarge.get());  

#### C++标准库智能指针
##### unique_ptr 
明确禁止对其封装的原始指针raw pointer进行拷贝操作。使用std::move可以将封装的原始指针所有权转移给另一个unique_ptr。unique_ptr不能被拷贝的原因是它的拷贝构造器和赋值操作符被显式的删除了。除非你确信需要用到shared_ptr，否则请将unique_ptr用作默认选项。替换已弃用的 auto_ptr，与 boost::scoped_ptr比较：unique_ptr 小巧高效；大小等同于一个指针且支持 rvalue 引用，从而可实现快速插入和对STL集合的检索。 C++11引入，头文件：`<memory>`。 

    std::unique_ptr<int> p1(new int(5));
    std::unique_ptr<int> p2 = p1; //Compile error.
    std::unique_ptr<int> p3 = std::move(p1); //Transfers ownership. p3 now owns the memory and p1 is set to nullptr.
    // Free the memory before we exit function block.
    p3.reset();
##### shared_ptr
采用引用计数的智能指针。 如果你想要将一个原始指针分配给多个所有者，请使用该指针。只有当所有的shared_ptr的拷贝被删除，才会删除原始指针。 大小为两个指针；一个用于对象，另一个用于包含引用计数的共享控制块。 头文件：`<memory>`。  

    std::shared_ptr<int> p0(new int(5));        // valid, allocates 1 integer and initialize it with value 5
    std::shared_ptr<int[]> p1(new int[5]);      // valid, allocates 5 integers
    std::shared_ptr<int[]> p2 = p1; //Both now own the memory.

    p1.reset(); //Memory still exists, due to p2.
    p2.reset(); //Deletes the memory, since no one else owns the memory.

需要特别指出的是，如果shared_ptr所表征的引用关系中出现一个环，那么环上所述对象的引用次数都肯定不可能减为0那么也就不会被删除，为了解决这个问题引入了weak_ptr。
##### weak_ptr 
配合shared_ptr使用的特殊智能指针。 weak_ptr的存在对shared_ptr及其拷贝的存在没有影响。当所有shared_ptr的拷贝被删除后，weak_ptr内容为空。头文件：`<memory>`。  

    std::shared_ptr<int> p1(new int(5));
    std::weak_ptr<int> wp1 = p1; //p1 owns the memory.

实际上，通常shared_ptr内部实现的时候维护的是两个引用计数，一个表示strong reference，也就是用shared_ptr进行复制的时候进行的计数，一个是weak reference，也就是用weak_ptr进行复制的时候的计数。weak_ptr本身并不会增加strong reference的值，而strong reference降低到0，对象被自动析构。在一个环上只要把原来的某一个shared_ptr改成weak_ptr，实质上这个环就可以被打破了，原有的环状引用带来的无法析构的问题也就随之得到了解决。

 

## 7. 设计模式
#### 单例（Singleton）
- 关键代码：构造函数是私有的。
- 应用实例： 1、一个党只能有一个书记。 2、Windows 是多进程多线程的，在操作一个文件的时候，就不可避免地出现多个进程或线程同时操作一个文件的现象，所以所有文件的处理必须通过唯一的实例来进行。 3、一些设备管理器常常设计为单例模式，比如一个电脑有两台打印机，在输出的时候就要处理不能两台打印机打印同一个文件。
- 优点： 1、在内存里只有一个实例，减少了内存的开销，尤其是频繁的创建和销毁实例（比如管理学院首页页面缓存）。 2、避免对资源的多重占用（比如写文件操作）。

#### 简单工厂（Simple Factory）
**目的**：在创建一个对象时不向客户暴露内部细节，并提供一个创建对象的通用接口。

**实现细节**：简单工厂把实例化的操作单独放到一个类中，这个类就成为简单工厂类，让简单工厂类来决定应该用哪个具体子类来实例化。

这样做能把客户类和具体子类的实现解耦，客户类不再需要知道有哪些子类以及应当实例化哪个子类。如果不使用简单工厂，那么所有的客户类都要知道所有子类的细节。而且一旦子类发生改变，例如增加子类，那么所有的客户类都要进行修改。

    public interface Product {}
    public class ConcreteProduct0 implements Product {}
    public class ConcreteProduct1 implements Product {}
    public class ConcreteProduct2 implements Product {}
以下的 Client 类包含了实例化的代码，这是一种**错误的实现**。如果在客户类中存在这种实例化代码，就需要考虑将代码放到简单工厂中。

    public class Client {
        public static void main(String[] args) {
            int type = 1;
            Product product;
            if (type == 1) {
                product = new ConcreteProduct1();
            } else if (type == 2) {
                product = new ConcreteProduct2();
            } else {
                product = new ConcreteProduct0();
            }
            // do something with the product
        }
    }

以下的 SimpleFactory 是简单工厂实现，它被所有需要进行实例化的客户类调用。

    public class SimpleFactory {
        public Product createProduct(int type) {
            if (type == 1) {
                return new ConcreteProduct1();
            } else if (type == 2) {
                return new ConcreteProduct2();
            }
            return new ConcreteProduct0();
        }
    }

    public class Client {
        public static void main(String[] args) {
            SimpleFactory simpleFactory = new SimpleFactory();
            Product product = simpleFactory.createProduct(1);
            // do something with the product
        }
    }

#### 工厂方法（Factory Method）
##### 目的
定义了一个创建对象的接口，但由子类决定要实例化哪个类。工厂方法把**实例化**操作**推迟到子类**。
##### 实现细节
在`简单工厂`中，创建对象的是另一个类，而在`工厂方法`中，是由子类来创建对象。

下面示例中，`Factory` 有一个 `doSomething()` 方法，这个方法需要用到一个产品对象，这个产品对象由 `factoryMethod()` 方法创建。该方法是抽象的，需要由子类去实现。

    //工厂方法类
    public abstract class Factory {  
        abstract public Product factoryMethod();
        public void doSomething() {
            Product product = factoryMethod();
            // do something with the product（产品接口或抽象类）
        }
    }
    //实现的工厂类0
    public class ConcreteFactory0 extends Factory {    
        public Product factoryMethod() {
            return new ConcreteProduct0();
        }
    }
    //实现的工厂类1
    public class ConcreteFactory1 extends Factory {    
        public Product factoryMethod() {
            return new ConcreteProduct1();
        }
    }
    //实现的工厂类2
    public class ConcreteFactory2 extends Factory {     
        public Product factoryMethod() {
            return new ConcreteProduct2();
        }
    }

#### 抽象工厂（Abstract Factory）
##### 目的
提供一个接口，用于创建相关的**对象家族**。
##### 实现细节
`抽象工厂`模式创建的是对象家族，也就是很多对象而不是一个对象，并且这些对象是相关的。而`工厂方法`模式只是用于创建一个对象，这和抽象工厂模式有很大不同。

抽象工厂模式用到了工厂方法模式来创建单一对象，`AbstractFactory` 中的 `createProductA()` 和 `createProductB()` 方法都是让子类来实现，这两个方法单独来看就是在创建一个对象，这符合工厂方法模式的定义。

至于**创建对象的家族**这一概念是在 Client 体现，Client 要通过 AbstractFactory 同时调用两个方法来创建出两个对象，在这里这两个对象就有很大的相关性，Client 需要同时创建出这两个对象。

    public class AbstractProductA {}
    public class AbstractProductB {}
    public class ProductA1 extends AbstractProductA {}
    public class ProductA2 extends AbstractProductA {}
    public class ProductB1 extends AbstractProductB {}
    public class ProductB2 extends AbstractProductB {}
    //抽象工厂类
    public abstract class AbstractFactory {    
        abstract AbstractProductA createProductA();
        abstract AbstractProductB createProductB();
    }
    //实现的工厂类1，实现类似于工厂方法，不过创建了对象家族
    public class ConcreteFactory1 extends AbstractFactory {
        AbstractProductA createProductA() {
            return new ProductA1();
        }
        AbstractProductB createProductB() {
            return new ProductB1();
        }
    }
    //实现的工厂类2，实现类似于工厂方法，不过创建了对象家族
    public class ConcreteFactory2 extends AbstractFactory {
        AbstractProductA createProductA() {
            return new ProductA2();
        }
        AbstractProductB createProductB() {
            return new ProductB2();
        }
    }

    public class Client {
        public static void main(String[] args) {
            AbstractFactory abstractFactory = new ConcreteFactory1();
            AbstractProductA productA = abstractFactory.createProductA();
            AbstractProductB productB = abstractFactory.createProductB();
            // do something with productA and productB
        }
    }


## 8. 构造函数，析构函数和赋值函数
- 深拷贝和浅拷贝：有时候需要自己定义拷贝构造函数，以避免浅拷贝（位拷贝）问题。
- 在什么情况下需要用户自己定义拷贝构造函数：一般情况下，当类中成员有指针变量、类中有动态内存分配时常常需要用户自己定义拷贝构造函数。
- 在什么情况下系统会调用拷贝构造函数：
    1. 用类的一个对象去初始化另一个对象时
    2. 当函数的形参是类的对象时（也就是值传递时），如果是引用传递则不会调用
    3. 当函数的返回值是类的对象或引用时

#### 对于任意一个类A，如果不想编写上述函数，C++编译器将自动为A产生四个缺省的函数，如：

    A(void);  // 缺省的无参数构造函数
    A(const A &a); // 缺省的拷贝构造函数
    ~A(void);  // 缺省的析构函数
    A & operate =(const A &a); // 缺省的赋值函数
#### 构造函数的初始化表，如果类存在继承关系，派生类必须在其初始化表里调用基类的构造函数：

    class B : public A 
    {
        B(int x, int y);// B的构造函数
    }; 
    B::B(int x, int y) : A(x) // 在初始化表里调用A的构造函数
    {  } 
- 类的数据成员的初始化可以采用`初始化表`或`函数体内赋值`两种方式，这两种方式的效率不完全相同。
    - 非内部数据类型（即自定义的类）的成员对象应当采用初始化列表进行初始化，以获取更高的效率。
    - 对于内部数据类型（例如int）的数据成员而言，两种初始化方式的效率几乎没有区别，但函数体内赋值的程序版式似乎更清晰些。
#### 构造和析构的次序
- 构造从类层次的最根处开始，在每一层中，首先调用基类的构造函数，然后调用成员对象的构造函数。析构则严格按照与构造相反的次序执行，该次序是唯一的，否则编译器将无法自动执行析构过程。
- `成员对象初始化`的次序完全不受它们在初始化表中次序的影响，`只由成员对象在类中声明的次序决定`。这是因为类的声明是唯一的，而类的构造函数可以有多个，因此会有多个不同次序的初始化表。如果成员对象按照初始化表的次序进行构造，这将导致析构函数无法得到唯一的逆序。

        // String的普通构造函数
        String::String(const char *str) 
        { 
            if(str==NULL){ 
                m_data = new char[1]; 
                *m_data = ‘\0’; 
            } 
            else{ 
                int length = strlen(str); 
                m_data = new char[length+1]; 
                strcpy(m_data, str); 
            }
        } 
#### 拷贝构造函数和赋值函数
- 如果不主动编写拷贝构造函数和赋值函数，编译器将以`位拷贝`而不是`值拷贝`的方式自动生成缺省的函数。倘若类中含有指针变量，那么这两个缺省的函数就隐含了错误。以类String的两个对象为例，假设a.m_data的内容为“hello”，b.m_data的内容为“world”。现将a赋给b，缺省赋值函数的“位拷贝”意味着执行b.m_data=a.m_data。这将造成三个错误：
    1. b.m_data 原有的内存没被释放，造成内存泄露
    2. b.m_data和a.m_data指向同一块内存，a或b任何一方变动都会影响另一方
    3. 在对象被析构时，m_data被释放了两次。
- 拷贝构造函数是在对象被创建时调用的，而赋值函数只能被已经存在了的对象调用：

        String a(“hello”); 
        String b(“world”); 
        String c = a; // 调用了拷贝构造函数，最好写成c(a); 
        c = b; // 调用了赋值函数
    本例中第三个语句的风格较差，宜改写成String c(a) 以区别于第四个语句。

        // 拷贝构造函数
        String::String(const String &other){ 
            // 允许操作other的私有成员m_data 
            int length = strlen(other.m_data); 
            m_data = new char[length+1]; 
            strcpy(m_data, other.m_data); 
        } 
        // 赋值函数
        String & String::operate =(const String &other){ 
            // (1) 检查自赋值
            if(this == &other)  //比较地址 
                return *this; 
            // (2) 释放原有的内存资源
            delete [] m_data;  // char *m_data = new char[X]; 
            // （3）分配新的内存资源，并复制内容
            int length = strlen(other.m_data); 
            m_data = new char[length+1]; 
            strcpy(m_data, other.m_data); 
            // （4）返回本对象的引用
            return *this;  //返回对象
        } 
    - 注意不要将检查自赋值的if语句错写成`if(*this == other) `。
    - 注意不要将`return *this`错写成`return this`。
    - `this`表示的是对象指针，`*this`表示的是对象。
    - 类String拷贝构造函数与普通构造函数的区别是：在函数入口处无需与NULL进行比较，这是因为`引用`不可能是NULL，而`指针`可以为NULL。



## 9. 内联函数
C++`内联函数`是通常与类一起使用。如果一个函数是内联的，那么在编译时，编译器会把该函数的代码副本放置在每个调用该函数的地方，省去了*参数压栈，生成汇编语言的CALL调用，返回参数，执行return等过*程。对内联函数进行任何修改，都需要重新编译函数的所有客户端，因为编译器需要重新更换一次所有的代码，否则将会继续使用旧的函数。引入内联函数的`目的`是为了解决程序中函数调用的效率问题，这么说吧，程序在编译器编译的时候，编译器将程序中出现的内联函数的调用表达式用内联函数的函数体进行替换，而对于其他的函数，都是在运行时候才被替代。这其实就是个空间代价换时间的节省。所以内联函数一般都是1-10行的小函数。

    inline int max(int a, int b)
    {
        return a > b ? a : b;
    }
如果想把一个函数定义为内联函数，则需要在函数名前面放置关键字`inline`。
- 在内联函数内不允许使用循环语句和其他复杂的结构；
- 内联函数的定义必须出现在内联函数第一次调用之前；
- 函数体在类声明中的函数都是内联函数，即使没有使用inline说明符。
- 关键字 inline 必须与函数定义体放在一起才能使函数成为内联，仅仅放在函数声明前面不起任何作用。
- C++中的函数内联机制既具备宏代码的效率，又增加了安全性，还可以自由操作类的数据成员。
- 宏的缺点是不可调试，但是内联函数在Debug版本中可以像正常函数一样调试；只有在程序的release版本里，编译器才对函数进行真正的内联。



## 10. Session和Cookie的区别
- Session是在服务端保存的一个数据结构，用来跟踪用户的状态，这个数据可以保存在集群、数据库、文件中；
    - 典型的场景比如购物车，当你点击下单按钮时，由于HTTP协议无状态，所以并不知道是哪个用户操作的，所以服务端要为特定的用户创建了特定的Session，用用于标识这个用户，并且跟踪用户，这样才知道购物车里面有几本书。
- Cookie是客户端保存用户信息的一种机制，用来记录用户的一些信息，也是实现Session的一种方式。
    - 每次HTTP请求的时候，客户端都会发送相应的Cookie信息到服务端。实际上大多数的应用都是用 Cookie 来实现Session跟踪的，第一次创建Session的时候，服务端会在HTTP协议中告诉客户端，需要在 Cookie 里面记录一个Session ID，以后每次请求把这个会话ID发送到服务器，我就知道你是谁了。

cookie保存在客户端，session保存在服务器端；
cookie目的可以跟踪会话，也可以保存用户喜好或者保存用户名密码；
session用来跟踪会话。

## 11. 进程线程间数据同步和通信（Linux)
#### 进程间通信
1. **管道（Pipe）及命名管道（named pipe）**：管道可用于具有亲缘关系进程间的通信，有名管道克服了管道没有名字的限制，因此，除具有管道所具有的功能外，它还允许无亲缘关系进程间的通信；    
2. **信号（Signal）**：信号是比较复杂的通信方式，用于通知接受进程有某种事件生，除了用于进程间通信外，进程还可以发送信号给进程本身。    
3. **消息（Message）队列**：消息队列是消息的链接表，有足够权限的进程可以向队列中添加消息，被赋予读权限的进程则可以读走队列中的消息。消息队列克服了信号承载信息量少，管道只能承载无格式字节流以及缓冲区大小受限等缺点。
4. **共享内存**：使得多个进程可以访问同一块内存空间，是最快的可用IPC形式。是针其他通信机制运行效率较低设计的。往往与其它通信机制，如信号量结合使用， 来达到进程间的同步及互斥。共享内存的通信方式是通过将共享的内存缓冲区直接附加到进程的虚拟地址空间中来实现的，因此，这些进程之间的读写操作的同步问题操作系统无法实现，必须由各进程利用其他同步工具解决。   
5. **信号量（semaphore）**：主要作为进程间以及同一进程不同线程之间的同步手段。             
6. **套接字（Socket）**：更为一般的进程间通信机制，可用于不同机器之间的进程间通信。

#### 进程和线程的区别
- 进程是资源分配的单位，线程是Cpu调度的基本单位。
- 线程运行时，暂用一些计数器，寄存器和栈。
- 一个线程只能属于一个进程；一个进程至少有一个线程（主线程）。
- 同一进程中的多个线程共享该进程的资源（如作为共享内存的全局变量）。Linux中所谓的“线程”只是在被创建时clone了父进程的资源，因此clone出来的进程表现为“线程”。
- 进程有独立的地址空间，一个进程崩溃后，在保护模式下不会对其它进程产生影响；线程有自己的堆栈和局部变量，但线程之间没有单独的地址空间，一个线程死掉就等于整个进程死掉，所以多进程的程序要比多线程的程序健壮。
- 在进程切换时，进程耗费资源较大，效率要差一些。


#### 线程间通信
线程间的通信有两种情况：
- 一个进程中的线程与另外一个进程中的线程通信，由于两个线程只能访问自己所属进程的地址空间和资源，故**等同于进程间的通信**。
- 同一个进程中的两个线程进行通信。
    - 因为同一进程的不同线程共享同一份全局内存区域，其中包括初始化数据段、未初始化数据段，以及堆内存段，程序代码，所以线程之间可以方便、快速地共享信息。只需要将数据复制到共享（全局或堆）变量中即可。不过，要避免出现多个线程试图同时修改同一份信息。

#### 线程安全
进程中有多个线程在同时运行，而这些线程可能会同时运行某一段代码。如果每次运行结果和单线程运行的结果是一样的，而且其他的变量的值也和预期的是一样的，就是线程安全的。线程安全就是说多线程访问同一段代码不会产生不确定的结果。编写线程安全的代码依靠`线程同步`。

如果变量时只读的，多个线程同时读取该变量不会有一致性问题，但是，当一个线程可以修改的变量，其他线程也可以读取或者修改的时候，我们就需要对这些线程进行同步，确保它们在访问变量的存储内容时不会访问到无效的值。
##### 线程同步
1. **互斥锁**：互斥量本质上说是一把锁，在访问共享资源前对互斥量进行加锁，在访问完成后释放互斥量。对互斥量进行枷锁以后，其他视图再次对互斥量加锁的线程都会被阻塞直到当前线程释放该互斥锁。
    - 死锁就是指多个线程/进程因竞争资源而造成的一种僵局（相互等待）。死锁的处理策略：
        - 预防死锁：破坏死锁产生的四个条件：互斥条件、不剥夺条件、请求和保持条件以及循环等待条件。
        - 避免死锁：在每次进行资源分配前，应该计算此次分配资源的安全性，如果此次资源分配不会导致系统进入不安全状态，那么将资源分配给进程，否则等待。算法：银行家算法。
        - 检测死锁：检测到死锁后通过资源剥夺、撤销进程、进程回退等方法解除死锁。
2. **读写锁**：读写锁与互斥量类似，不过读写锁拥有更高的并行性。互斥量一次只有一个线程可以对其加锁。读写锁有3种状态：`读模式`下加锁状态，`写模式`下加锁状态，`不加锁`状态。一次只有一个线程可以占有`写`模式的读写锁，但是多个线程可以同时占有`读`模式的读写锁。当读写锁是`写`加锁状态时，在这个锁被解锁之前，所有视图对这个锁加锁的线程都会被阻塞。当读写锁在`读`加锁状态时，所有试图以读模式对它进行加锁的线程都可以得到访问权，但是任何希望以写模式对此锁进行加锁的线程都会阻塞。
3. **条件变量**：互斥量用于上锁，条件变量则用于等待，并且条件变量总是需要与互斥量一起使用。条件变量本身是由互斥量保护的，线程在改变条件变量之前必须首先锁住互斥量。其他线程在获得互斥量之前不会察觉到这种变化，因为互斥量必须在锁定之后才能计算条件。
4. **信号量**：线程的信号和进程的信号量类似，使用线程的信号量可以高效地完成基于线程的资源计数。信号量实际上是一个非负的整数计数器，用来实现对公共资源的控制。在公共资源增加/减少的时候，信号量就增加/减少。只有当信号量的值>0的时候，才能访问信号量所代表的公共资源。
5. **自旋锁**：自旋锁与互斥量类似，但它不是通过休眠使进程阻塞，而是在获取锁之前一直处于忙等（自旋）阻塞状态。自旋锁可以用于以下情况：锁被持有的时间短，而且线程并不希望在重新调度上花费太多的成本。
6. **屏障**：barrier(屏障)与互斥量，读写锁，自旋锁不同，它不是用来保护临界区的。相反，它跟条件变量一样，是用来协同多线程一起工作！条件变量是多线程间传递状态的改变来达到协同工作的效果。屏障是多线程各自做自己的工作，如果某一线程完成了工作，就等待在屏障那里，直到其他线程的工作都完成了，再一起做别的事。


## 12. Java new流程
1. 首先去JVM的方法区中区寻找类的class对象，如果能找到，则按照定义生成对象，找不到则转2；找到转3。
2. 加载类定义：类加载器（classLoader）寻找该类的`.class`文件，找到后对文件进行分析转换为class对象存入JVM方法区方便以后调用。其中jdk的class一般是在jvm启动时用启动类加载器完成加载，用户的class则是在用到的时候再加载。
3. 在jvm的堆中给对象开辟一个内存空间。
4. 对象初始化，顺序：
    - 父类静态对象，静态代码块
    - 子类静态对象，静态代码块
    - 父类非静态对象，非静态代码块
    - 父类构造函数
    - 子类非静态对象，非静态代码块
    - 子类构造函数

## 13. K路归并算法的分析与实现
#### 问题描述
将k个已经排序的数组归并成一个大的排序的结果数组。这些数组可能数量比较大，以至于不能直接装载到内存中。
#### 初步分析
参考归并排序的`merge`函数，将两个排好序的小数组合并成一个大数组：

    template<typename T>  //合并函数
    void merge_sort_recursive(T arr[], T reg[], int start, int end) {
        if (start >= end)
            return;
        int len = end - start, mid = (len >> 1) + start;
        int start1 = start, end1 = mid;
        int start2 = mid + 1, end2 = end;
        merge_sort_recursive(arr, reg, start1, end1);
        merge_sort_recursive(arr, reg, start2, end2);
        int k = start;
        while (start1 <= end1 && start2 <= end2)
            reg[k++] = arr[start1] < arr[start2] ? arr[start1++] : arr[start2++];
        while (start1 <= end1)
            reg[k++] = arr[start1++];
        while (start2 <= end2)
            reg[k++] = arr[start2++];
        for (k = start; k <= end; k++)  //从额外空间复制给原数组
            arr[k] = reg[k];
    }
    template<typename T> //主函数
    void merge_sort(T arr[], const int len) {
        T *reg = new T[len];  //reg为合并所需的额外空间
        merge_sort_recursive(arr, reg, 0, len - 1);
        delete[] reg;
    }
#### 思路1：循环遍历K个数组
思路就比较直接，首先，我们比较所有k个数组的头一个元素，找到最小的那一个，然后取出来。我们在该最小元素所在的数组取下一个元素，然后重复前面的过程去找最小的那个。这样依次循环直到找到所有的元素。

#### 思路2：最小堆K路归并排序
和前面那个方法比起来，它没有多少特殊的，主要是用建堆和调整的方式来比较元素。如果总剩余的元素小于K：
1. 假定在处理元素的过程中，某个序列的元素取光了。我们可以在开始的时候针对所有序列的最后都加一个表示无穷大的数值。这样如果取完这个序列之后可以保证它后续肯定不会被选择到。
2. 我们将该元素用堆最后的元素替换，然后调整堆的属性并将堆的大小减1。这样我们这个大小为k的堆慢慢会变成`k-1, k-2，...,1`这些个长度的堆。一直到我们把这些堆里序列的元素处理完。

## 14. Socket工作原理
此处应有流程图：https://www.jianshu.com/p/90348ef3f41e

在同一台计算机，进程之间可以这样通信。网络上不同的计算机，也可以通信，需要使用网络套接字（socket）。socket就是在不同计算机之间进行通信的一个抽象，是工作于TCP/IP协议中`应用层和传输层之间`的一个抽象概念。

- TCP客户端：

      socket() -> connect() -> write() -> read() -> close()
- TCP服务器端：
     
      socket() -> bind() -> listen() -> accept() -> read() -> write() -> read() ->close()
#### TCP三次握手
- 客户端向服务器发送一个`SYN seq=J`
- 服务器向客户端响应一个`SYN seq=K`，并对SYN J进行确认`ACK J+1`
- 客户端向服务器发一个确认`ACK K+1`和`seq=J+1`

##### 为什么需要三次握手？  
在这样一种情况下会产生`已失效的连接请求报文段`： 
- client发出的第一个连接请求报文段并没有丢失，而是在某个网络结点长时间的滞留了，以致延误到连接释放以后的某个时间才到达server。本来这是一个早已失效的报文段。但server收到此失效的连接请求报文段后，就误认为是client再次发出的一个新的连接请求。于是就向client发出确认报文段，同意建立连接。
- 假设不采用“三次握手”，那么只要server发出确认，新的连接就建立了。由于现在client并没有发出建立连接的请求，因此不会理睬server的确认，也不会向server发送数据。但server却以为新的运输连接已经建立，并一直等待client发来数据。这样，server的很多资源就白白浪费掉了。采用“三次握手”的办法可以防止上述现象发生。 

## 15. http状态码
2开头 （请求成功）表示成功处理了请求的状态代码。
    
    200   （成功）  服务器已成功处理了请求。 通常，这表示服务器提供了请求的网页。 

3开头 （请求被重定向）表示要完成请求，需要进一步操作。 通常，这些状态代码用来重定向。
    
    301   （永久移动）  请求的网页已永久移动到新位置。 服务器返回此响应（对 GET 或 HEAD 请求的响应）时，会自动将请求者转到新位置。

4开头 （请求错误）这些状态代码表示请求可能出错，妨碍了服务器的处理。

    403   （禁止） 服务器拒绝请求。
    404   （未找到） 服务器找不到请求的网页。

5开头（服务器错误）这些状态代码表示服务器在尝试处理请求时发生内部错误。 这些错误可能是服务器本身的错误，而不是请求出错。

    500   （服务器内部错误）  服务器遇到错误，无法完成请求。 
    503   （服务不可用） 服务器目前无法使用（由于超载或停机维护）。 通常，这只是暂时状态。 
    505   （HTTP 版本不受支持） 服务器不支持请求中所用的 HTTP 协议版本。

## 16. map VS unordered_map
    #include <map>
    #include <unordered_map>
#### 区别
1. 内部实现
   - map使用红黑树存储数据，元素是按照key被顺序存储的；unordered_map使用哈希表存储数据，数据key无序存储。
2. 内存使用
   - unordered_map的内存占用更大，因为需要额外空间存储哈希表。
3. 时间复杂度
   - map中搜索时间复杂度为O(logn)，因为是用平衡树结构存储数据的；unordered_map的最优情况是O(1)，最差O(n)。
4. 使用自定义对象作为key
   - map想要使用用户自定义对象作为key，必须重载`<`比较运算符，或者传入一个外部比较函数。
   - unordered_map使用自定义对象作为key，需要提供`std::hash<K>`的定义，`K`为key；并且需要重载`==`运算符。

#### 什么时候选择map
- 内存开销有限制时
- 需要元素保持有序时
    - map的迭代器从start到end输出，会发现元素按照key从小到大已经排好序。
- 当需要保证性能时
    - unordered_map的性能最好为O(1)，最差为O(n)；但是map的性能确保为O(logn)。

#### 什么时候选择unordered_map
- 哈希函数很优秀，并且没有内存限制时

## 17. 红黑树
红黑树（Red–black tree）是一种自平衡二叉查找树。它是复杂的，但它的操作有着良好的最坏情况运行时间，并且在实践中是高效的：它可以在O(logn)时间内做查找，插入和删除，这里的 n是树中元素的数目。

红黑树是每个节点都带有颜色属性的二叉查找树，颜色为红色或黑色。在二叉查找树强制一般要求以外，对于任何有效的红黑树我们增加了如下的额外要求：

- 节点是红色或黑色。
- 根是黑色。
- 所有叶子都是黑色（叶子是NIL节点）。
- 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
- 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。

## 18. 函数修饰关键字
函数关键字 | 解释
----|----
static | 表明该函数是属于类的，不属于对象；不能在该函数中访问或者处理类中的其他非static成员变量。
explicit | 禁止编译器进行隐式转换，避免不必要的bug；例如类`group`有构造函数`group(int num)`，同时有个函数以`group`类为参数`play(group biggroup)`，则在调用函数`play(3)`时，编译器会把数字3根据`group`的构造函数隐式转换成一个`group`对象。我们不想进行这样的转换，因此在`group`的构造函数前面加入该关键字`explicit`。








## Finally: Other Things
#### Liam means helmet of will.

https://www.babycenter.com/baby-names-liam-2820.htm
