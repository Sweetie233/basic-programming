2:55:05

1. java.io包中:

- File类表示磁盘上的文件和目录，具有平台无关性
- 结合JDK文档进行讲解
- 经常需要抛出异常，可以在main后面写throws Exception

- 平台无关代码，路径分隔符，常量`File.separator`
- 路径字符串可写成`dir+File.separator+Dir+……`
- Windows下单个分隔符表示程序所在磁盘分区的根目录，例如C:\

2. 创建临时文件和退出时删除：


        File f=File.createTempFile("","")
        f.deleteOnExit()
  
File类没有对文件进行读写的方法

3. 流的分类：
- 节点流，从特定地方读写，如InputStream
- 过滤流，使用节点流进行输入输出，如FilterInputStream

4. 抽象基类：
- InputStream<-FilterInputStream<-(DataInputStream,BufferedInputStream)
- OutputStream<-FilterOutputStream<-（DataOutputStream，BufferedOutputStream，PrintStream）

5. 从屏幕读取和写入数据：

        data=System.in.read()
        System.out.write(data)

- `FileInputStream(FileOutputStream)`节点流，完成对文件的读写操作，字节流
- `BufferedInputStream(BufferedOutputStream)`过滤流，提供带缓冲的读写，提高效率 
- `DataInputStream(DataOutputStream)`过滤流，读写Java中的基本数据类型，如int，char，float 
- `PipedInputStream(PipedOutputStream)`管道流，用来进行进程间通信，必须成对构造

1:20:00

- 关闭连接流时只需要关闭尾端的流即可

6. Java的I/O库提供了流管道的连接机制，也成为`Decorator`（装饰）设计模式的应用。

流的连接可以动态增加流的功能（虽然说不太容易掌握，但是实现上非常灵活）

7. I/O流的链接

- 输入流链：文件->FileInputStream->BufferedInputStream->DataInputStream->数据
- 输出流链：数据->DataOutputStream->BufferedOutputStream->FileOutputStream->文件

- `InputStream(OutputStream)`主要操作字节流
- `Reader(Writer)`主要操作字符流

- InputStreamReader(OutputStreamWriter)提供字符流和字节流转换的功能
- BufferedReader(BufferedWriter)提供带缓冲的高效读写操作
- 输入流链：文件->FileInputStream->InputStreamReader->BufferedReader->数据
- 输出流链：数据->BufferedWriter->OutputStreamWriter->FileOutputStream->文件
- 从屏幕读取数据：

    new BufferedReader(new InputStreamReader(System.in))

8. 字符集编码：1:43:00

- `ASCII`(American Standard Code for Information Interchange)，8位
- `GB2312`，汉字交换码，一个中文字符用2个字节表示，中文字符每个字节最高位置一
- `GBK`，K表示扩展，兼容GB2312，还对繁体，不常用汉字以及其他符号进行编码
- `Unicode`，每字符用2字节表示
- `UTF-8`，表示ASCII用1个字节，表示0x0080-0x007f和0x0000用2个字节，表示0x0800-0xffff用3个字节（中文即3个字节）

- 获取字符或字符串是解码`decode()`
- 获取字节流属于编码`encode()`

-从屏幕上读取汉字时，Java存储为字节数组，即GBK编码对应的码值； 当从字节数组构造字符串时，按照系统默认的字符集（如UTF-8）解码为对应的字符（按照Unicode编码存放），用System.out打印时，out如果用GBK字符集构造，则会把字符转换为GBK编码显示出来。编解码不一致自然会出现乱码。

-RandomAccessFile可对文件随机存取2:12:54

9. 对象序列化：不保存方法和静态成员变量

把对象转换为字节流保存起来；必须实现Serializable或Externalizable接口。

`Serializable`空接口，没有任何函数和数据，Externalizable继承自Serializable 

- 输入流链：文件->FileInputStream->ObjectInputStream->数据
- 输出流链：数据->ObjectOutputStream->FileOutputStream->文件

`writeObject(readObject )`

反序列化对象时不会调用对象的构造方法，仅仅是根据内存状态对对象进行重建

控制对象的读写顺序，重载private void readObject(writeObject)，会被自动调用

10. 经验：

写对象时会出现StackOverFlow的现象，因为对象进行了递归定义，自己引用自己，递归层次过多，栈很容易就不够用。
测试了一下，默认的栈大小是50M。在Eclipse里增大：

    Window->Preferences->Java->Installed JREs->select a JRE->Edit->Default VM arguments->"-Xss128m"

注意这个值如果太大，那么就会出现堆溢出的错误，一般情况下128M已经够用了，如果还不够用就需要重新审视一下程序代码的正确性了。




