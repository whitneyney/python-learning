# python数据分析

jupyter快捷键：

D,D（快速按俩个D）：删除单元格

shift+enter：执行当前单元格，并把光标移到下一单元格

ctrl+enter：执行当前单元格，但光标不会移到下一单元格

Esc：从编辑模式变成命令模式

回车：从命令模式变成编辑模式

【按N+H可以看到全部快捷键】

# 入门

## 1.python基础语法

### 1.1常用数据类型

1. 字符串

   - 字符串使用引号来定义，且单引号与双引号是等价的

   - 三引号用来输入包含多行文字的字符串

   - 字符串的加法：即字符串的拼接

   - 字符串索引：从0开始

   - 字符串的分隔：`字符串.split(分隔符)` 【把字符串分隔成多个子字符串，并存入到列表中返回】 

     （如果不写入分隔符，则默认以空格来对字符串进行分隔）

   - 查看字符串的长度：`len(字符串)`

2. 整数

3. 浮点数

4. 布尔值

5. 空值：None

### 1.2运算符

1. 算术运算符（+  -  *  /  //  %    **  ）
2. 比较运算符[==   !=   <>(不等于，与!=类似)    >   <   >=   <=]
3. 赋值运算符（=   +=  -=   *=    /=     %=    **=     //=）
4. 逻辑运算符[  and，or，not（取反）]
5. 成员资格运算符（in, not in）

### 1.3数据结构

- 列表、元组、字典、集合

### 1.4可变对象和不可变对象

可变对象：可以对其进行插入、删除等操作

不可变对象：不可以对其进行有改变的操作

[列表、字典、集合都是可变的，元组、字符串、整型都是不可变的]

### 1.5类型转换

`int()`    `float()`   `list()`    ........

### 1.6判断和循环

### 1.7列表生成式

## 2.python函数

### 2.1内置函数

`min()`  `max()`    `sum()`  等等

### 2.2自定义函数

使用def关键字

return返回特定的值（如果省略，则返回None）

如果传入参数的数目与实际不相符，会报错：所以也可以在函数定义时给参数设定默认值。

一个参数可以返回多个返回值（）



# Numpy

> NumPy(Numeric Python)是Python的一种开源的数值计算扩展，是python的一个第三方库。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表结构要高效的多。NumPy提供了许多高级的数值编程工具。Numpy的一个重要特性是它的数组计算，是我们做数据分析必不可少的一个包。

导入python库使用关键字**import**，后面可以自定义库的简称，但是一般都将Numpy命名为np，pandas命名为pd。

使用前一定要先导入Numpy包，导入的方法有以下几种：

```python
import numpy
import numpy as np   # 推荐写法
from numpy import *  # 不是很建议这种写法，因为使用函数时不用加前缀的话有可能会与其他函数名称起冲突，可能会导致报错
```



## 1.Numpy的数组对象

### 1.1数组上的数学操作

引入：


```python
# 假设我们想将列表中的每个元素增加1，但列表不支持这样的操作：
a = [1,2,3,4]
# 想让每个元素都加一：a+1 #报错
# 要用列表生成式
[x+1 for x in a]  # [2, 3, 4, 5]

b = [2,3,4,5]
# 想要与另一个数组相加，得到对应元素相加的结果：
a+b #并不是我们想要的结果，只是列表的拼接：[1, 2, 3, 4, 2, 3, 4, 5]
# 需要利用到列表生成式：
[x+y for(x,y) in zip(a,b)]  # [3, 5, 7, 9]
```

这样的操作比较麻烦，而且在数据量特别大的时候会非常耗时间。如果使用Numpy，就会变得特别简单：


```python
import numpy as np   # 导入numpy包
a = np.array([1,2,3,4])
a # [1 2 3 4]
a+1 # [2 3 4 5]
a*2 # [2, 4, 6 8]

b = np.array([2,3,4,5])
a + b # [3 5 7 9]
```



### 1.2生成数组的方法

- 从列表产生数组：（最基本的方法）
  ```python
  l = [0,1,2,3]
  a = np.array(l)
  a  # [0 1 2 3]
  ```

- 从列表传入：
  ```python
  a = np.array([1,2,3,4])
  a # [1 2 3 4]
  ```

- 生成全0数组：
  ```python
  np.zeros(n) #括号内传的n为要生成的数组元素的个数，默认为浮点数
  ```
  ```python
  # eg：
  np.zeros(5)  # [0. 0. 0. 0. 0.]
  ```

- 生成全1的数组：
  ```python
  np.ones(n) #括号内传的n为要生成的数组元素的个数，默认浮点数
  ```
  ```python
  # eg：
  np.ones(5)  # [1. 1. 1. 1. 1.]
  ```


- 可以用`dtype = 想要的类型`来自己指定数据类型（int, bool...）

  ```python
  # eg:
  np.ones(5, dtype=bool) # 结果：[ True  True  True  True  True]
  np.zeros(5, dtype=int) # 结果：[0 0 0 0 0]
  ```

- 可以使用 fill 方法将数组设为指定值（让数组中的每一个元素都为指定值）

  语法：`数组.fill(要设置的指定值)`

  注意：

  - 数组中要求**所有元素的dtype(数据类型)都必须要是一样的**【与列表不同】
  - 如果传入参数的类型与数组类型不一样，会自动按照已有的类型进行转换。【如果就是想要将数组中的元素换成与原来的数组元素的类型不同时，可以用stype方法进行强制类型转换】

- stype强制将数组元素类型转换

  语法：`数组 = 数组.stype(要转换成的数据类型)`


```python
# eg：
import numpy as np   # 导入numpy包
a = np.array([1, 2, 3, 4])
print(a)  # [1 2 3 4]
a.fill(5)  # 让数组中的每一个元素都为5
print(a)  # [5 5 5 5]
a.fill(2.5)
print(a)  # [2 2 2 2]  # 会自动进行取整
a = a.astype('float')
a.fill(2)
print(a)  # [2. 2. 2. 2.]
a.fill(2.5)
print(a)  # [2.5 2.5 2.5 2.5]
```
- 还可以使用一些特定的方法生成特殊的数组

  - 用arange生成从某个数开始的序列：

    语法：`np.arange([起始数，]终点数[,步长])` 

    [与range的使用方法类似，但range的步长不支持小数]
  
    - 一个参数时，参数值为终点，起点取默认值0，步长取默认值1
  
    - 两个参数时，第一个参数为起点，第二个参数为终点，步长取默认值1。包前不包后【实际上是左闭右开(在终点数处结束但不包含它本身)】
    - 三个参数时，第一个参数为起点，第二个参数为终点，第三个参数为步长；步长支持小数。
  
    ```python
    a = np.arange(1,10) # 生成从1-9的一个整数序列
    print(a) # [1 2 3 4 5 6 7 8 9]
    b = np.arrang(1,10,2) # 步长为2
    print(b) # [1 3 5 7 9]
    c = np.arange(1.3, 10)
    print(c)  # [1.3 2.3 3.3 4.3 5.3 6.3 7.3 8.3 9.3]
    d = np.arange(1, 5, 1.5)
    print(d)  # [1.  2.5 4. ]
    ```
  
  - 生成等差数列：
  
    `linspace(起点，终点，元素个数)`  【<u>终点数是包括在内的</u>（左闭**右闭**）】
  
    ```python
    # eg:
    a = np.linspace(1, 5, 11)
    print(a)  # [1.  1.4 1.8 2.2 2.6 3.  3.4 3.8 4.2 4.6 5. ]
    ```
  
  - 生成随机数
  
    - 返回在0-1范围内的n个随机浮点数
  
      语法：`np.random.rand(需要的随机数的个数n)`   
  
    - 返回n个服从标准正态分布的随机浮点数
  
      [ 标准正态分布又称为u分布，是以0为均值、以1为标准差的正态分布，记为N（0，1）]
  
      语法：`np.random.randn(需要的随机数的个数n)`   
  
    - 返回n个从起点到终点的随机整数
  
      语法：`np.random.randint(起点，终点，需要的随机数的个数n)`  【<u>终点数是不包括在内的</u>（左闭右开）】
  
      > - 在python中：random.randint(a,b)：用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n：a<=n<=b,即[a,b]。
      >
      >   如：m=random.randint(0,3)它只会在0、1、2、3中随机返回一个整数
      >
      > - 在numpy中：np.random.randint(a,b)：用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限，生成的随机数n：a<=n<b,即[a,b)。
      >
      >   如：numpy.random.randint(0,3)会在0、1、2中随机返回一个整数，但是其中不会包括3。
  
    ```python
    np.random.rand(5)  # [0.75380372 0.44891155 0.43189469 0.633356   0.01367505] 
    np.random.randn(5) #标准正态分布# [ 0.31446483 -1.02828074  0.35086322  0.18106916 -0.07317298]
    np.random.randint(1,10,5) #生成随机整数，从1-19中随机10个# [5 9 9 8 4]
    ```
  
    - 创建多维随机数组
    
      语法：`np.random.random((第一维元素个数，第二维元素个数，...))`
    
      注意：`np.random.random()`中的"( )"里面要用( )把每一维的元素个数包括到一个元组中。否则报错
    
      ```python
      # eg:
      # 会报错：a = np.random.random(3, 4)
      a = np.random.random((3, 4))
      print(a)
      # [[0.31314274 0.27400047 0.26432628 0.98058422] [0.23238729 0.26398298 0.09495022 0.31992298] [0.84497553 0.02284272 0.26811946 0.97573487]]
      b = np.random.random((3, 4, 2))
      print(b)
      ```
    
    - 创建指定范围的整数元素的多维随机数组
    
      语法：`np.random.randint(起点，终点，(第一维的元素数目，第二维的元素数目，...))`
    
      【左闭右开，终点不包括在内】
    
    - 创建元素是服从标准正态分布的随机浮点数的多维随机数组
    
      语法：`np.random.randn((第一维的元素数目，第二维的元素数目，...))`
    
    - 返回一个n*n的随机项的矩阵
    
      `np.random.randn(n)`
    
    - 返回一个m*n的随机项矩阵(m是行的数目，n是列的数目)
    
      `np.random.randn(m,n)`或`np.random.randn([m n]) `
    
      

### 1.3数组的属性

- 用type查看变量类型

  语法：`type(变量名称)`

- 用dtype查看数组中的元素的数据类型

  语法：`数组名.dtype`

- 用shape查看数组的形状（会返回一个元组，每个元素代表每一维的元素数目）

  - 方法一：`数组名.shape`
  - 方法二：`np.shape(数组名)`

- 用size来查看数组里面总的元素的个数

  语法：`数组名.size`

- 用ndim查看数组的维度

  语法：`数组名.ndim`


```python
import numpy as np   # 导入numpy包
a = np.array([1, 2, 3, 4, 5])
print(type(a))  # <class 'numpy.ndarray'>(a的类型是numpy的n维数组)
print(a.dtype)  # int32
print(a.shape)  # (5,)
print(np.shape(a))  # (5,)
print(a.size)  # 5
print(a.ndim)  # 1
```

（多维的在后面）



### 1.4索引和切片

索引某个元素：`数组名[下标]`  【下标从0开始】

修改某个元素的值：`数组名[下标] = 要修改到的值`

切片操作：`数组名[起点：终点：步长]` 【左闭右开】 (支持负索引)（参数可省）


```python
a = np.array([0,1,2,3])
a[0]  # 0 #索引
a[0] = 10  # 修改元素值
print(a)  # [10 1 2 3]

# 切片
b = np.array([11,12,13,14,15])
b[1:3] #左闭右开，从0开始算
b[1:-2] #等价于a[1:3]
b[-4:3] #等价与a[1:3]
# 上面3个的结果都是：[12 13]
b[1:4:2] # 结果：[12 14]
b[-2:] #从倒数第2个取到最后。结果：[14 15]
b[::2] #从头取到尾，间隔2，结果：[11 13 15]
```



### 1.5多维数组及其属性

array还可以用来生成多维数组:

（如果传入的是一个以列表为元素的列表，最终得到一个二维数组。）

（查看其属性的方法与一维数组类似）


```python
b = np.array([[1, 2, 3], [3, 4, 5]])
# 查看b的类型：
print(type(b))  # <class 'numpy.ndarray'>  （numpy的n维数组)
# 查看数组中的元素的数据类型：
print(b.dtype)  # int32
# 查看形状：
print(b.shape)  # (2, 3)
print(np.shape(b))  # (2, 3)
# 查看总的元素个数：
print(b.size)  # 6
# 查看维数：
print(b.ndim)  # 2
```



### 1.6多维数组索引

- 对于二维数组，可以传入两个数字来索引：`数组名[在第一维的下标（行索引），在第二维的下标（列索引）]`

- 还可利用索引修改某个元素的值：`数组名[在第一维的下标（行索引），在第二维的下标（列索引）] = 要修改到的值`

- 还可以使用单个索引来索引一整行内容：`数组名[在第一维的下标(行索引)]` 

- 索引一整列内容:`数组名[: , 列索引]`


```python
# 索引
a = np.array([[0,  1,  2,  3], [10, 11, 12, 13]])
print(a[1, 2])  #12 # 其中，1是行索引，2是列索引。事实上，Python会将它们看成一个元组（1,2），然后按照顺序进行对应。
# 利用索引修改元素的值
a[1,2] = -1 
print(a)  # [[ 0  1  2  3] [10 11 -1 13]]
# 使用单个索引来索引一整行内容:
print(a[1])  # [10 11 -1 13]
# 索引一整列内容：
print(a[:,1])  # 1是指第二列，冒号左右两边都省略  # 结果：[1 11]
```



【“不完全”索引 ：只给定行索引的时候，而不给定列索引时返回整行】：


```python
a = np.array([[0, 1, 2, 3, 4, 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]])
# 返回一条次对角线上的5个值:
print(a[:3])  # [[ 0  1  2  3  4  5] [10 11 12 13 14 15] [20 21 22 23 24 25]]
# 也可以使用布尔数组来花式索引取出第2,3,5行：
con = np.array([0, 1, 1, 0, 1, 0], dtype=bool)
print(a[con])  # [[10 11 12 13 14 15] [20 21 22 23 24 25] [40 41 42 43 44 45]]
```



### 1.7多维数组切片操作

每一维都支持切片的规则，支持负索引，lower、upper、step都可省略。

`[lower:upper:step]`


```python
# eg：
a = np.array([[0, 1, 2, 3, 4, 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]])
# 想得到第一行的第4和第5两个元素：
print(a[0, 3:5])  # [3 4]
# 得到最后两行的最后两列：
print(a[4:, 4:])  # [[44 45] [54 55]]
print(a[-2:, -2:])  # # [[44 45] [54 55]]
# 得到第三列：
print(a[:, 2])  # [ 2 12 22 32 42 52]
# 取出3,5行的奇数列：
a[2::2,::2] # [[20 22 24] [40 42 44]]
```

-----

注意：**切片**在内存中使用的是**引用**机制，也就是说：python不会给切片操作后得到的子数组来分配一个新的存储空间，而是让得到的数组与原来的数组指向了同一个空间（原来数组本来所在的内存空间）。因此，改变其中一个数组的值时，另一个数组的值也会跟着发生同样的改变。


```python
# eg：
a = np.array([0,1,2,3,4])
b = a[2:4]
print(b) # [2 3]
# 引用机制意味着，Python并没有为b分配新的空间来存储它的值，而是让b指向了a所分配的内存空间，因此，改变b时会改变a的值：
b[0] = 10
print(a)  # [0 1 10 3 4]
```

> 而这种现象在列表中并不会出现：
>
>
> ```python
> # eg：
> a = [1,2,3,4,5]
> b = a[2:4]
> b[0] = 10
> print(a)  # [1, 2, 3, 4, 5]
> ```

- 切片在内存中使用引用机制: 


  优点：对于很大的数组，不用大量复制多余的值，节约了空间。

  缺点：可能出现改变一个值改变另一个值的情况。

—>>解决方法：使用`copy()`方法来进行复制，复制就会申请新的内存，那对它进行值的改动就不会影响到原来的数组：


```python
# eg：
a = np.array([0,1,2,3,4])
b = a[2:4].copy()
b[0] = 10
print(a)  # [0 1 2 3 4]  （没有改变）
```



### 1.8花式索引 

切片只能支持连续或者等间隔的切片操作，要想实现任意位置的操作，就需要使用花式索引。

**注意**：与切片不同，花式索引返回的是原对象的一个**复制**而不是引用。



#### 1.8.1一维花式索引 


```python
# eg:
a = np.arange(0,100,10) # 可以使用arange函数来产生等差数组
print(a)  # [1 10 20 30 40 50 60 70 80 90]
```

花式索引需要指定索引位置：


```python
index = [1,2,-3]
y = a[index]
print(y) # [10 20 70]
```


还可以使用布尔数组来花式索引：


```python
mask = np.array([0, 2, 2, 0, 0, 1, 0, 0, 1, 0], dtype = bool)
print(mask) # [False  True  True False False  True False False  True False]
```

必须要是**布尔数组**，且布尔数组（在这里是mask）的长度**必须**与要操作的数组（在这里是a）**长度相等**，才能使用布尔数组来进行花式索引，取出为true的位置上的元素。


```python
print(a[mask])  # [10 20 50 80]
```



#### 1.8.2二维花式索引 


```python
a = np.array([[0, 1, 2, 3, 4, 5],
              [10, 11, 12, 13, 14, 15],
              [20, 21, 22, 23, 24, 25],
              [30, 31, 32, 33, 34, 35],
              [40, 41, 42, 43, 44, 45],
              [50, 51, 52, 53, 54, 55]])
# 给定行和列的值：
# 返回一条次对角线上的5个值:
print(a[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)])  # [ 1 12 23 34 45]
# 返回最后3行第1、3、5列的数据：(方法有多种)
print(a[-3:, ::2])  # [[30 32 34] [40 42 44] [50 52 54]]
print(a[3:, (0, 2, 4)])  # [[30 32 34] [40 42 44] [50 52 54]]
print(a[3:, [0, 2, 4]])  # [[30 32 34] [40 42 44] [50 52 54]]

# 也可以利用布尔数组进行花式索引：
mask = np.array([0, 0, 0, 1, 1, 1], dtype=bool)
print(a[mask, ::2])  # [[30 32 34] [40 42 44] [50 52 54]]
```



### 1.9where语句

`np.where(数组)`：where函数会返回数组中所有非零（"真"的）元素的**索引**

`np.where(要返回的索引位置处的数组元素要满足的条件)`：where函数返回的是，满足where函数条件的数组元素的具体**索引**位置。

（where的返回值是一个元组）


```python
# eg：
a = np.array([0, 12, 5, 20])
# 判断数组中的元素是不是大于10：
print(a > 10)  # [False  True False  True]
# 数组中所有大于10的元素的索引位置：
print(np.where(a > 10))  # (array([1, 3], dtype=int64),)
# 注意到where的返回值是一个元组，返回的是索引位置
```

------

- 也可以直接用数组操作：

  语法：`数组名[要返回的数组元素要满足的条件]`


```python
a = np.array([0, 12, 5, 20])
print(a[np.where(a > 10)])  # [12 20]
print(a[a > 10])  # [12 20]
```



## 2.数组类型 

| **基本类型** | **可用的Numpy类型**                      | **备注**                                         |
| :----------- | :--------------------------------------- | :----------------------------------------------- |
| 布尔型       | bool                                     | 占一个字节                                       |
| 整型         | int8,int16,int32,int64,int128,int        | int跟C语言中long一样大                           |
| 无符号整型   | uint8,uint16,uint32,uint64,uint128,uint  | uint跟C语言中的unsigned long一样大               |
| 浮点数       | float16,float32,float                    | 默认为双精度float64，longfloat精度大小与系统有关 |
| 复数         | complex64,complex128,complex,longcomplex | 默认为complex128,即实部虚部都为双精度            |
| 字符串       | string,unicode                           | 可以使用dtype=S4表示一个4字节字符串的数组        |
| 对象         | object                                   | 数组中可以使用任意值                             |
| 时间         | datetime64,timedelta64                   |                                                  |

### 转换元素的类型的方法

- dtype


```python
a = np.array([1.5,-3],dtype = float)
print(a)  # [1.5 -3.]
```



- asarray 函数 

可以通过asarray函数来对数组元素的类型来做调整


```python
a = np.array([1, 2, 3])
print(np.asarray(a, dtype=float))  # [1. 2. 3.]
```



- astype方法

astype 方法返回一个**新数组**，而不是使用引用地址。所以，对返回的这个新数组做任何的改动都不会影响到原来的数组：


```python
a = np.array([1, 2, 3])
b = a.astype(float)
print(b) # [1. 2. 3.]
b[0] = 0.5
print(b)  # [0.5 2. 3.]
print(a)  # [1 2 3]
# a本身并没有发生任何变化--拷贝
```



## 3.数组操作 

以豆瓣10部高分电影为例 


```python
# 电影名称
mv_name = ["肖申克的救赎","控方证人","美丽人生","阿甘正传","霸王别姬","泰坦尼克号","辛德勒的名单","这个杀手不太冷","疯狂动物城","海豚湾"]
# 评分人数
mv_num = np.array([692795,42995,327855,580897,478523,157074,306904,662552,284652,159302])
# 评分
mv_score = np.array([9.6,9.5,9.5,9.4,9.4,9.4,9.4,9.3,9.3,9.3])
# 电影时长（分钟）
mv_length = np.array([142,116,116,142,171,194,195,133,109,92])
```

### 数组排序

#### sort函数

语法: `np.sort(要排序的数组对象)`

注意：排序后<u>原来数组里面元素的顺序不会变</u>，只是会返回一个原数组排序后得到的**新数组**


```python
print(np.sort(mv_num))  # [ 42995 157074 159302 284652 306904 327855 478523 580897 662552 692795]
# sort不改变原来数组元素的顺序:
print(mv_num)  # [692795  42995 327855 580897 478523 157074 306904 662552 284652 159302]
```

tips：将数组逆序可用：`数组[::-1]`



#### argsort函数 

返回在原来数组中从小到大的排列的数组元素的**索引位置**。【常常会用于索引其他数组的元素】

语法: `np.argsort(要排序的数组对象)`


```python
order = np.argsort(mv_num)
print(order)  # [1 5 9 8 6 2 4 3 7 0]
# 评分人数最少的电影名称
print(mv_name[order[0]])  # 控方证人
# 评分人数最多的电影名称
print(mv_name[order[-1]]) # 肖申克的救赎
```



### 求和 

方法1：`np.sum(要求和的数组对象)`

方法2：`要求和的数组对象.sum()`


```python
np.sum(mv_num)  # 3693549
mv_num.sum()  # 3693549
```



### 最大值 

方法1：`np.max(要最大值的数组对象)`

方法2：`要求最大值的数组对象.max()`


```python
np.max(mv_length)  # 195
mv_length.max() # 195
```



### 最小值 

方法1：`np.mim(要最小值的数组对象)`

方法2：`要求最小值的数组对象.mim()`


```python
np.min(mv_score)
mv_score.min()  # 9.3
```



### 均值 

方法1：`np.mean(要求均值的数组对象)`

方法2：`要求均值的数组对象.mean()`


```python
np.mean(mv_length)
mv_length.mean() # 141.0
```



### 标准差 

方法1：`np.std(要求标准差的数组对象)`

方法2：`要求标准差的数组对象.std()`


```python
np.std(mv_length)
mv_length.std() # 33.713498780162226
```



### 相关系数矩阵 

看两个数组的相关系数矩阵

语法：`np.cov(数组1，数组2)`


```python
np.cov(mv_score,mv_length) # [[9.88888889e-03 4.55555556e-01] [4.55555556e-01 1.26288889e+03]]
```



## 4.多维数组操作 

### 4.1数组形状 

- shape方法
  - 访问数组形状：`数组.shape`
  - 修改数组形状：`数组.shape = (第一维的元素数目，第二维的元素数目，...)`  


```python
a = np.arange(6)
print(a)  # [0 1 2 3 4 5]
# 修改数组的形状
a.shape=(2,3)
print(a)  # [[0 1 2] [3 4 5]] # 数组本身的形状发生了改变
print(a.shape)  # (2, 3)
```

- reshape方法

  【与shape的不同：reshape不会修改原来的数组，而是返回一个**新数组**】

  语法1：`需要reshape的数组.reshape(newshape)`

  语法2：`numpy.reshape(需要reshape的数组, newshape)`

  [newshape即为：(第一维的元素数目，第二维的元素数目，...)]


```python
a = np.arange(6)
print(a)  # [0 1 2 3 4 5]
print(a.reshape(2, 3))  # [[0 1 2] [3 4 5]]
print(a)  # [0 1 2 3 4 5] # 数组本身没有发生改变
```

注意：形状变化是基于数组元素不能改变的，变成的新形状中所包含的元素个数必须符合原来元素个数。如果数组元素发生了变化，就会报错。



### 4.2转置数组

方法1：`数组.T`

方法2：`数组.transpose()`

tips: 只要没有把转置后的新数组赋给原数组，那么原数组就不会发生变化


```python
a = np.array([[0, 1, 2], [3, 4, 5]])
print(a.T)  # [[0 3] [1 4] [2 5]]
print(a.transpose())  # [[0 3] [1 4] [2 5]]
#只要没赋值给数组本身，a的数值不会变化:
print(a)  # [[0 1 2] [3 4 5]]
a = a.T  # 或：a = a.transpose()  （都是一样的）
print(a)  # [[0 3] [1 4] [2 5]]
```



### 4.3数组连接 

将不同的数组按照一定的顺序连接起来： 

语法：`np.concatenate((数组1，数组2，...，数组n)[,axis=0])`

> asix写的是要进行数组拼接的方向:
>
> - 默认情况下，沿着第一维进行连接, axis=0，可以不写。
>
> - 如果要横沿着第二维进行连接，就可以把asix改为1

注意：

- 这些数组要用( )包括到一个元组中【即使没有写默认参数axis=0】
- 除了给定的轴外，这些数组其他轴的长度必须是一样的。


```python
x = np.array([[0,1,2],[10,11,12]])
y = np.array([[50,51,52],[60,61,62]])
print(x.shape)  # (2, 3)
print(y.shape)  # (2, 3) # 轴的长度一样-->可进行拼接

# 默认沿着第一维进行连接：(对于一维数组拼接，axis的值不影响最后的结果)
print(np.concatenate((x,y)))  # [[ 0  1  2] [10 11 12] [50 51 52] [60 61 62]]

# 沿着第二维进行连接：[把asix改为1]
print(np.concatenate((x, y), axis=1))# [[ 0  1  2 50 51 52] [10 11 12 60 61 62]]
```

------

还可以将它们连接成三维的数组，但不用concatenate，不过可以直接通过array来进行：


```python
print(np.array((x,y)))
# 结果：[[[ 0  1  2]  [10 11 12]] [[50 51 52]  [60 61 62]]]
```

----

Numpy也提供了分别对应这三种情况的函数：

* 沿着第一维进行连接：vstack
* 沿着第二维进行连接：hstack
* 连接成三维数组：dstack【注意：与直接用array连接成三维数组的方式不同】


```python
# 沿着第一维进行连接：
print(np.vstack((x,y)))# [[ 0  1  2] [10 11 12] [50 51 52] [60 61 62]]

# 沿着第二维进行连接：
print(np.hstack((x,y))) # [[ 0  1  2 50 51 52] [10 11 12 60 61 62]]

# 变成三维数组:
print(np.dstack((x,y))) # [[[ 0 50]  [ 1 51]  [ 2 52]] [[10 60]  [11 61]  [12 62]]]
```



## 5.Numpy内置函数

- 对数组的元素求绝对值：`np.abs(数组名)`
- 计算各元素的e的x次方：`np.exp(数组名)`
- 计算数组 a 中元素的中位数（中值）：`np.median(数组名)`
- 求累积和：`np.cumsum(数组名)`
- 求百分位数：`np.percentile(百分位数提取的对象，要计算的一个百分位数/多个百分位数组成的列表)`

numpy的内置函数 :  https://blog.csdn.net/nihaoxiaocui/article/details/51992860?locationNum=5&fps=1



## 6.数组属性方法总结 

| **调用方法**            | **作用**                                         |
| :---------------------- | :----------------------------------------------- |
| **1**                   | **基本属性**                                     |
| a.dtype                 | 数组元素类型float32,uint8,...                    |
| a.shape                 | 数组形状(m,n,o,...)                              |
| a.size                  | 数组元素数                                       |
| a.itemsize              | 每个元素占字节数                                 |
| a.nbytes                | 所有元素占的字节                                 |
| a.ndim                  | 数组维度                                         |
| -                       | -                                                |
| **2**                   | **形状相关**                                     |
| a.flat                  | 所有元素的迭代器                                 |
| a.flatten()             | 返回一个1维数组的复制                            |
| a.ravel()               | 返回一个一维数组，高效                           |
| a.resize(new_size)      | 改变形状                                         |
| a.swapaxes(axis1,axis2) | 交换两个维度的位置                               |
| a.transpose(* axex)     | 交换所有维度的位置                               |
| a.T                     | 转置，a.transpose()                              |
| a.squeeze()             | 去除所有长度为1的维度                            |
| -                       | -                                                |
| **3**                   | **填充复制**                                     |
| a.copy()                | 返回数组的一个复制                               |
| a.fill(value)           | 将数组的元组设置为特定值                         |
| -                       | -                                                |
| **4**                   | **转化**                                         |
| a.tolist()              | 将数组转化为列表                                 |
| a.tostring()            | 转换为字符串                                     |
| a.astype(dtype)         | 转换为指定类型                                   |
| a.byteswap(False)       | 转换大小字节序                                   |
| a.view(type_or_dtype)   | 生成一个使用相同内存，但使用不同的表示方法的数组 |
| -                       | -                                                |
| **5**                   | **查找排序**                                     |
| a.nonzero()             | 返回所有非零元素的索引                           |
| a.sort(axis=-1)         | 沿某个轴排序                                     |
| a.argsort(axis=-1)      | 沿某个轴，返回按排序的索引                       |
| a.searchsorted(b)       | 返回将b中元素插入a后能保持有序的索引值           |
| -                       | -                                                |
| **6**                   | **元素数学操作**                                 |
| a.clip(low,high)        | 将数值限制在一定范围内                           |
| a.round(decimals=0)     | 近似到指定精度                                   |
| a.cumsum(axis=None)     | 累加和                                           |
| a.cumprod(axis=None)    | 累乘积                                           |
| -                       | -                                                |
| **7**                   | **约简操作**                                     |
| a.sum(axis=None)        | 求和                                             |
| a.prod(axis=None)       | 求积                                             |
| a.min(axis=None)        | 最小值                                           |
| a.max(axis=None)        | 最大值                                           |
| a.argmin(axis=None)     | 最小值索引                                       |
| a.argmax(axis=None)     | 最大值索引                                       |
| a.ptp(axis=None)        | 最大值减最小值                                   |
| a.mean(axis=None)       | 平均值                                           |
| a.std(axis=None)        | 标准差                                           |
| a.var(axis=None)        | 方差                                             |
| a.any(axis=None)        | 只要有一个不为0，返回真，逻辑或                  |
| a.all(axis=None)        | 所有都不为0，返回真，逻辑与                      |



# Panads-1

## 1.1 Panads基本介绍 

> Python Data Analysis Library 或 Pandas是基于Numpy的一种工具，该工具是为了解决数据分析任务而创建的。Pandas纳入了大量库和一些标准的数据模型，提供了高效地操作大型数据集所需的工具。pandas提供了大量能使我们快速便捷地处理数据的函数和方法。

导入python库使用关键字**import**，后面可以自定义库的简称，但是一般都将pandas命名为pd。

使用前一定要先导入Pandas包，导入的方法有以下几种：

```python
import pandas
import pandas as pd   # 推荐写法
from pandas import *  # 不是很建议这种写法，因为使用函数时不用加前缀的话有可能会与其他函数名称起冲突，可能会导致报错
```

### Pandas 基本数据结构 

`pandas`有两种常用的基本结构：

+ `Series`（一维数组）
  + 与Numpy中的一维array类似。二者与Python基本的数据结构List也很接近。Series<u>能保存不同种数据类型</u>，字符串、boolean值、数字等都能保存在Series中。
+ `DataFrame`（二维的表格型数据结构）
  + 很多功能与R中的data.frame类似。可以将DataFrame理解为Series的容器。



## 1.2 Pandas库的series类型 

>  Series相比ndarray多了一个索引，相当于一位数组+索引

### 1.Series的初始化

一维`Series`初始化：

- 直接通过数据来创建：`pd.Series(data, index, dtype, name, copy)`  【Series中要大写S】

  > - data：一组数据(ndarray 类型)。
  > - index：数据索引标签，如果不指定，默认从 0 开始。
  > - dtype：数据类型，默认会自己判断。
  > - name：设置名称。
  > - copy：拷贝数据，默认为 False。


  ```python
  # eg：
  s = pd.Series([1,3,5,np.nan,6,8]) # np.nan [nan(NAN,Nan)：not a number表示不是一个数字（空值）]
  print(s)
  """
  结果：
  0    1.0
  1    3.0
  2    5.0
  3    NaN
  4    6.0
  5    8.0
  dtype: float64"""
  # （左边的这列是下标索引）
  ```

  

- 通过字典创建

  tips：也可以<u>用字典来传入数据</u>到series当中，其中字典中的key为series中的索引，value为索引对应的数据

```python
# eg:
# 先定义一个series，用字典传入数据：
dit = {"名字":"复仇者联盟3","投票人数":123456,"类型":"剧情/科幻","产地":"美国","上映时间":"2018-05-04 00:00:00","时长":142,"年代":2018,"评分":np.nan,"首映地点":"美国"}
# 字典数据的传入：
s = pd.Series(dit) 
# 给它一个具体的名称（索引号）:
s.name = 38738
print(s)
"""结果：
名字                   复仇者联盟3
投票人数                 123456
类型                    剧情/科幻
产地                       美国
上映时间    2018-05-04 00:00:00
时长                      142
年代                     2018
评分                      NaN
首映地点                     美国
Name: 38738, dtype: object
"""

# 注意s.name和s.index.name的区别：
s.index.name = 38738
print(s)
"""结果：
38738
名字                   复仇者联盟3
投票人数                 123456
类型                    剧情/科幻
产地                       美国
上映时间    2018-05-04 00:00:00
时长                      142
年代                     2018
评分                      NaN
首映地点                     美国
Name: 38738, dtype: object
"""

"""tips：如果前面没有先写了s.name，而是只写了s.index.name，则结果会是：

38738
名字                   复仇者联盟3
投票人数                 123456
类型                    剧情/科幻
产地                       美国
上映时间    2018-05-04 00:00:00
时长                      142
年代                     2018
评分                      NaN
首映地点                     美国
dtype: object
"""
```





### 2.自定义下标索引

默认情况下，`Series`的下标索引都是从0开始的数字，类型是统一的。也可以使用额外参数指定下标索引。

自定义下标索引语法：

1. 在series初始化时定义下标索引：`数组名=pd.Series(列表，index=要定义的下标索引组成的列表)`
2. 初始化后：`数组名.index=要定义的下标索引组成的列表`


```python
# eg：
# 方式1：
s = pd.Series([1,3,5,np.nan,6,8],index = ['a','b','c','d','e','f'])#设置索引,修改索引
# 或： s = pd.Series([1, 3, 5, np.nan, 6, 8], index=list('abcdef'))  # 设置索引,修改索引

# 方式2：
s = pd.Series([1,3,5,np.nan,6,8])
s.index = list('abcdef')

print(s)
"""
结果：
a    1.0
b    3.0
c    5.0
d    NaN
e    6.0
f    8.0
dtype: float64"""
```



### 3.查看索引

语法：`Series名称. index`


```python
# eg：
s = pd.Series([1,3,5,np.nan,6,8])
print(s.index) #从0到6（不含），1为步长 # RangeIndex(start=0, stop=6, step=1)
s = pd.Series([1,3,5,np.nan,6,8],index = ['a','b','c','d','x','y'])
print(s.index )# Index(['a', 'b', 'c', 'd', 'x', 'y'], dtype='object')
```



### 4.查看元素的值

- 查看所有元素的值：`Series名称. values`   【注意values有s】
- 根据下标查看单个元素的值：`Series名称[下标索引]`


```python
s.values  # [ 1.  3.  5. nan  6.  8.]
s[3]  # nan
```



### 5.切片操作

语法：`Series名称[start:stop:step]`【左闭右开】


```python
s[2:5] #左闭右开
"""
结果：
2    5.0
3    NaN
4    6.0
dtype: float64
"""

s[::2]
"""
结果：
0    1.0
2    5.0
4    6.0
dtype: float64
"""
```

-----

tips：可以根据自定义的索引来进行切片

**注意**：依据自己定义的数据类型进行切片时，就不是左闭右开了，而是**左闭右闭**

```python
# eg:
s = pd.Series([1,3,5,np.nan,6,8])
s.index = list('abcdef')
print(s['a':'c':2])
"""结果：
a    1.0
c    5.0
dtype: float64"""
```



### 6.给所有索引赋值

语法：`Series名称.index.name = '要赋得的值'`


```python
s.index.name = '索引'
print(s)
"""结果：
索引
0    1.0
1    3.0
2    5.0
3    NaN
4    6.0
5    8.0
dtype: float64"""
```



## 1.3 Pandas库的DataFrame类型

### 1.DataFrame结构的创建

- `date_range` 产生的是等差时间序列

  使用语法：`pd.date_range('日期起点',periods=要生成的日期个数)`

- 创建``DataFrame``结构（二维的表格型数据结构）：【`DataFrame`要求每一列数据的类型相同】

  - 方法1：直接传入一个二维数组：`pd.DataFrame(一个二维数组[,index=序列][，columns=序列])`

    > 可自定义索引、列标。
    >
    > 默认情况下，如果不指定``index``参数和``columns``，那么它们的值将从用0开始的整数序列替代。

    ```python
    # DataFrame是个二维结构，这里首先构造一组时间序列，作为第一维的下标（index）：
    date = pd.date_range("20180101", periods = 6)
    print(date)
    """结果:
    DatetimeIndex(['2018-01-01', '2018-01-02', '2018-01-03', '2018-01-04',
                   '2018-01-05', '2018-01-06'],
                  dtype='datetime64[ns]', freq='D')"""
    
    # 然后创建一个DataFrame结构（二维的表格型数据结构）：
    df = pd.DataFrame(np.random.randn(6,4), index = date, columns = list("ABCD"))
    print(df)
    """
                       A         B         C         D
    2018-01-01 -0.348959 -0.311461 -0.399123 -0.325182
    2018-01-02  0.238729  1.925845 -1.222850 -0.199705
    2018-01-03  0.961151 -0.215719 -0.555677 -1.298533
    2018-01-04 -0.301778 -1.473886  1.043568 -0.811393
    2018-01-05  0.628038  1.118145 -1.571545 -0.629766
    2018-01-06  2.207462  2.356775  2.103667  0.501393
    """
    ```

  - 方法2：使用字典传入数据

    [字典的每个``key``代表一列，其``value``可以是各种能够转化为``Series``的对象]

    ```python
    df2 = pd.DataFrame({'A':1.,'B':pd.Timestamp("20181001"),'C':pd.Series(1,index = list(range(4)),dtype = float),'D':np.array([3]*4, dtype = int),'E':pd.Categorical(["test","train","test","train"]),'F':"abc"}) 
    #B:时间戳,E分类类型
    
    """结果：
         A          B    C  D      E    F
    0  1.0 2018-10-01  1.0  3   test  abc
    1  1.0 2018-10-01  1.0  3  train  abc
    2  1.0 2018-10-01  1.0  3   test  abc
    3  1.0 2018-10-01  1.0  3  train  abc
    """
    ```

    

### 2.查看数据 

- 查看头尾行的数据：（n可以不写，不写时默认为5）

  - 看前n行的数据：`DataFrame的名称.head(n)`

  - 看后n行的数据：`DataFrame的名称.tail(n)`
- 查看各个列的数据类型：`DataFrame的名称.dtypes` 【dtypes有s】
- 查看下标：`DataFrame的名称.index`
- 查看列标：`DataFrame的名称.columns`  
- 查看具体数据值：`DataFrame的名称.values`  【values有s】


```python
# 示例：
df = pd.DataFrame({'A':1.,'B':pd.Timestamp("20181001"),'C':pd.Series(1,index = list(range(4)),dtype = float),'D':np.array([3]*4, dtype = int),'E':pd.Categorical(["test","train","test","train"]),'F':"abc"}) 
print(df)
"""
     A          B    C  D      E    F
0  1.0 2018-10-01  1.0  3   test  abc
1  1.0 2018-10-01  1.0  3     12  abc
2  1.0 2018-10-01  1.0  3   test  abc
3  1.0 2018-10-01  1.0  3  train  abc"""

# 查看头3行的数据：
df.head(3)
# 查看各个列的数据类型：
df.dtypes
# 查看下标索引：
df.index
# 查看列标：
df.columns
# 查看具体数据值：
df.values
```



## 1.4 pandas读取数据及数据操作 

读取excel表格：`pd.read_excel(路径)`  【tips：可在路径前面写上r来告诉编译器不需要转义】

读取csv文件：`pd.read_csv()`


```python
# eg:
df = pd.read_excel(r"D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业3\豆瓣电影数据.xlsx")  # r告诉编译器不需要转义
df.head()
```



### 1.4.1行操作 

#### 1.读取单行数据

- `DataFrame的名称.iloc[下标索引]`
- `DataFrame的名称.loc[下标索引]`



#### 2.读取多行数据(用切片)

- `DataFrame的名称.iloc[start:stop:step]`  【左闭右开】
- `DataFrame的名称.loc[start:stop:step]`  【**左闭右闭。注意：不是左闭右开**】


```python
df.iloc[0]
df.iloc[0:5] #左闭右开
df.loc[0:5] #不是左闭右开
```



####  3.添加一行

- 在 Pandas DataFrame 的末尾添加一行：`DataFrame名称 = DataFrame名称.append(一个Series)`

- tips：把某一个系列传入到dataframe中作为一行时，如果设置它的行索引，则在添加到dataframe中之前，先给它一个具体的名称(索引号):`series名称.name = 要取的名称`

  【注意：当dataframe的索引是自定义了的话，那么要给dataframe传入一个series来新增一行时，一定要给它一个具体的名称；如果dataframe本来使用的就是默认的索引而没有再重新定义的话，那就不需要再给它一个具体的名称】


```python
# eg：
# 先定义一个series，用字典传入数据：
dit = {"名字":"复仇者联盟3","投票人数":123456,"类型":"剧情/科幻","产地":"美国","上映时间":"2018-05-04 00:00:00","时长":142,"年代":2018,"评分":np.nan,"首映地点":"美国"}
# 字典数据的传入：
s = pd.Series(dit) 
# 给它一个具体的名称（索引号）
s.name = 38738

df = pd.read_excel(r"D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业3\豆瓣电影数据.xlsx")
# 在文件后面增加一行数据s,并用增加后的数据覆盖掉原来的数据：
df = df.append(s)      #覆盖掉原来的数据，对原来的数据重新进行赋值
```



#### 4.删除一行 

在 Pandas DataFrame 中删除一行

- `DataFrame名称 = DataFrame名称.drop([要删除的行的索引])`  
- 或直接对原始数据进行修改：`DataFrame名称.drop([要删除的行的索引],inplace=True)`

注意：要删除的行索引要用中括号包起来


```python
# eg：
df = df.drop([38738])
```



### 1.4.2列操作 

#### 1.查看列名称/列标

语法：`DataFrame名称.columns`

#### 2.查看某(些)列

查看某列/某些列：`dataFrame名称[某列的名称/要查看的列的名称组成的列表]`

> tips: 查看行时要用 .loc 或 .iloc ，查看列则不需要

查看某些行的某些列的内容：`DataFrame名称[要查看的列的名称1，要查看的列的名称2，...][要查看的行的索引（可用切片操作来查看多行数据）]`

【注意：查看多列时，要查看的列的名称一定要组成一个列表，即要用中括号包起来】


```python
# eg：
df["名字"][:5] #后面中括号表示只想看到的行数，下同
df[["名字","类型"]][:5]
```



#### 3.增加一列 

语法：`DataFrame名称[要增加的列名称] = ...`  

(对新增的列直接赋值)


```python
# eg：
df["序号"] = range(1,len(df)+1) #生成序号的基本方式
```



#### 4.删除一列

语法：`DataFrame名称 = DataFrame名称.drop(要删除的列的名称，axis = 1)`

(注意与删除一行区分)  【用axis指定方向，0为行，1为列，axis默认为0】


```python
# eg:
df = df.drop("序号",axis = 1) 
```



### 1.4.3选择

#### 1.通过标签选择数据

语法：`DataFrame名称.loc[[index],[colunm]]`


```python
# eg:
# 一个数据：
df.loc[1,"名字"]  
#多行跳行多列跳列选择多个数据：（用列表）
df.loc[[1,3,5,7,9],["名字","评分"]] 
```

tips：可通过 `DataFrame名称.loc[[index],[colunm]] = 要赋得的值` 来修改某个位置上的值



#### 2.条件选择  

- `DataFrame名称[条件判断]`可根据条件挑选出满足条件的数据，还可以对它们进行操作。【就把挑出的数据再当作一个新的dataframe来正常处理即可】

  例如：可以用切片操作得到其中的多行数据；查看它(们)的行索引: `DataFrame名称[条件判断].index`

- 判断时如果要引用某一列(两种方式)：

  - `DataFrame名称[列的名称]`
  - `DataFrame名称.列的名称`  （更简洁，即使列的名称是字符串也不需要加引号）


```python
# eg：
# 选取产地为美国的所有电影
df[df["产地"] == "美国"] #内部为bool类型的数据，把为true的数据取出  # 更简洁的写法：df[df.产地 == "美国"]
# 取前五个产地为美国的电影
df[df["产地"] == "美国"][:5]  
# 选取产地为美国的所有电影，并且评分大于9分的电影：
#df.标签:更简洁的写法
df[(df.产地 == "美国") & (df.评分 > 9)][:5]   
# 选取前五个产地为美国或中国大陆的所有电影，并且评分大于9分：
df[((df.产地 == "美国") | (df.产地 == "中国大陆")) & (df.评分 > 9)][:5]
```



## 1.5 缺失值及异常值处理 

### 缺失值处理的方法

| **方法**    | **说明**                                                     |
| :---------- | :----------------------------------------------------------- |
| **isnull**  | 判断缺失值，返回一个布尔值对象。如果是缺失值，则返回True；如果不是，则返回False |
| **notnull** | isnull的否定                                                 |
| **dropna**  | 根据标签中的缺失值进行过滤，并删除缺失值                     |
| **fillna**  | 对缺失值进行填充                                             |



#### 判断缺失值

- 判断整个DataFrame的缺失值：

  - 返回布尔值：`DataFrame名称.isnull()`
  - 把所有缺失值都列出来：`DataFrame名称[DataFrame名称.isnull()]`

- 判断某一列的DataFrame的缺失值：

  - 返回布尔值：`DataFrame名称[列名称].isnull()`
  - 把这一列的所有缺失值都列出来：`DataFrame名称[DataFrame名称[列名称].isnull()]`

- 判断某一列的某几行的DataFrame的缺失值

  - 返回布尔值：`DataFrame名称[列名称].isnull()[行的索引（可用切片操作来查看多行数据）]`

  - 把这一列的某几行的缺失值都列出来：`DataFrame名称[DataFrame名称[列名称].isnull()][行的索引（可用切片操作来查看多行数据）]`  

    【注意：行的索引起始在`DataFrame名称[DataFrame名称[列名称].isnull()]`的时候就已经发生了改变，行索引的操作是对发生了改变之后的dataframe来进行操作】

tips：notnull方法与isnull方法类似，可找出非缺失的数据。但一般都是希望找出缺失值，所以一般用isnull方法。


```python
# eg:
df[df["名字"].isnull()][:10]  # 找到名字这一列的前10个缺失值
df[df["名字"].notnull()][:5]  # 找到名字这一列的前5个非缺失值
```



#### 填充缺失值 

- 填充某列的缺失值：`DataFrame名称[列名称] = DataFrame名称[列名称].fillna(要填充的值/数据/东西)`

- 如果加上`inplace=True`，就可以直接修改原始数据

  即也可直接：`DataFrame名称[列名称].fillna(要填充的值/数据/东西,inplace=True)`

> 常见填充数据的方法：
>
> 1. 用固定值填充
>    eg: `data['分数'] = data['分数'].fillna('-1')`
>
> 2. 用均值填充
>
>    > 对于数值型的特征，其缺失值也可以用未缺失数据的均值填充。
>
>    eg：`data['分数'] = data['分数'].fillna(data['分数'].mean()))`
>
> 3. 用众数填充
>
>    > 与均值类似，可以用未缺失 数据的众数来填充缺失值。
>
>    eg: `data['分数'] = data['分数'].fillna(data['分数'].mode()))`
>
> 4. 用上下数据进行填充
>
>    - 用前一个数据进行填充:  eg:`data['分数'] = data['分数'].fillna(method='pad')`
>
>    - 用后一个数据进行填充: eg: `data['分数'] = data['分数'].fillna(method='bfill')`
>
> 5. 用插值法填充
>
>    > 采用`interpolate()`函数使用线性方法填充缺失值
>
>    eg: `data['分数'] = data['分数'].interpolate()`
>
> 6. 用KNN进行填充
>    from fancyimpute import BiScaler, KNN, NuclearNormMinimization, SoftImpute
>    dataset = KNN(k=3).complete(dataset)
>
>    来自链接：https://blog.csdn.net/qq_23860475/article/details/89554848的改编


```python
# eg：
df["评分"].fillna(np.mean(df["评分"]), inplace=True) #在这里可以使用均值来进行替代要填充的内容，当然也可以用其他的数
# inplace=True意为直接对原始数据进行修改，并保存填充后的数据
# 如果没有写“inplace=True”，则原始数据不会发生改变，只是会返回一个修改后的dataframe
```



- 填充所有的缺失值：`DataFrame名称 = DataFrame名称.fillna(要填充的值/数据/东西)`
  - 注意：起始如果只是`DataFrame名称.fillna(要填充的值/数据/东西)`，那原始数据其实是没有发生改变的，只是会返回一个新的数据。要让原来的dataframe发生改变，则需要再让`DataFrame名称 = DataFrame名称.fillna(要填充的值/数据/东西)`，让新的数据覆盖掉原来的数据，对原来的数据重新进行赋值。


```python
df1 = df.fillna("未知电影") 
# 注意：这种写法没有指定列，它会对所有数据（只要是空值）来用“未知电影”进行填充
#要谨慎使用，除非确定所有的空值都是在一列中，否则所有的空值都会填成这个
# 没有用“inplace=True”，没有修改原始数据，在这里用一个新的dataframe（df1）来接收
#不可采用df["名字"].fillna("未知电影")的形式，因为填写后数据格式就变了，变成Series了
```



#### 删除缺失值

`dropna() `的主要参数：

- how = 'all' :  删除全为空值的行或列
- inplace = True :  覆盖之前的数据（直接对原始数据进行修改，原始数据发生改变）
- axis = 0: 选择行或列，默认是行(常用的也是行)


```python
print(len(df)) # 38739

# 删除缺失值，把删除了缺失值之后的数据返回（原始数据不变）：
df2 = df.dropna()  
print(len(df2)) # 38176
print(len(df)) # 38739【原始数据不变】

# 删除缺失值时传入inplace = True，会直接对原始数据进行修改（inplace = True会覆盖掉原来的数据）
df.dropna(inplace = True) 
print(len(df)) # 38176  【原始数据发生改变】  
```



### 处理异常值

> 异常值，即是在数据集中存在不合理的值，又称离群点。
>
> （比如年龄为-1，笔记本电脑重量为1吨等，都属于异常值）


```python
# 为负数的异常值
df[df["投票人数"] < 0] #可以直接删除，或者找原始数据来修正
# 或：df[df.投票人数 < 0]

# 为小数的异常值：
df[df["投票人数"] % 1 != 0] 
```



tips:

- 异常值一般数量都会很少，在不影响整体数据分布的情况下，就可以直接删除

  ```python
  # 只保存了没有负数、小数异常的数据
  df = df[df.投票人数 > 0]
  df = df[df["投票人数"] % 1 == 0]
  ```

- 其他属性的异常值处理，可以用数据格式转换的方法发现（如果有异常值，在转换格式时就会报错，从而被发现）

- 还可以通过描述性统计，来发现一些异常值



## 1.6 数据保存 

数据处理之后，用`DataFrame名称.to_excel(文件名)`可以将数据保存（默认保存的路径为现在文件夹所在的路径）


```python
df.to_excel("movie_data.xlsx") # 数据处理之后，然后将数据重新保存到movie_data.xlsx 
```



# Pandas-2

## 2.1 数据格式

在做数据分析时，原始数据常常会因为各种各样的原因产生各种数据格式的问题。数据格式是非常需要注意的，数据格式错误往往会造成很严重的后果。很多异常值也是我们经过格式转换后才会发现，数据格式转换对规整数据、清洗数据有着重要的作用。

```python
import pandas as pd
import numpy as np
# 首先读入保存的数据文件movie_data.xlsx 
df = pd.read_excel(r"D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业3\movie_data.xlsx.xlsx",index_col = 0) # index_col=0：设置第一列为index值
```



#### 查看格式 (数据类型)

语法：`DataFrame的名称[要查看格式的列的名称].dtype`



#### 转换格式

语法：`DataFrame的名称[要转换格式的列的名称] = DataFrame的名称[要转换格式的列的名称].astype(目标格式)`


```python
# eg:
# 查看格式：
print(df["投票人数"].dtype) # dtype('float64')
print(df["产地"].dtype) # dtype('O')
# 转换格式：
df["投票人数"] = df["投票人数"].astype("int")
df["产地"] = df["产地"].astype("str")
```

- 如果转化格式的时候报错，那就说明存在异常值

  - 可根据报错信息先查看存在异常值的那行数据

  - 再通过`DataFrame名称.loc[[index],[colunm]] = 要赋得的值` 来修改异常值，

    或者用`DataFrame名称.drop([要删除的行的索引],inplace=True)`直接将有异常值的行删除

  【如果删除或修改了异常值以后，再重新转化格式时，还是报错，那就说明还有异常值，即原来的数据有多个异常值】

  

----

例1：将年份转化为整数格式 

```python
df["年代"] = df["年代"].astype("int") #有异常值会报错,看报错的信息找出异常值
```


```python
# 查看有异常值的这行数据:
print(df[df.年代 == "2008\u200e"])  #看起来没问题，实际上是带着格式控制字符的
# 查看异常值的具体取值:
print(df[df.年代 == "2008\u200e"]["年代"].values )
# 修改异常值：
df.loc[14934,"年代"] = 2008 
#查看这一列修改后的样子
df.loc[14934]
# 重新转化格式：
df["年代"] = df["年代"].astype("int")
```

例2：将时长转化为整数格式 


```python
df["时长"] = df["时长"].astype("int") #有异常值会报错,看报错的信息找出异常值
# 错误信息：ValueError: invalid literal for int() with base 10: '8U'
```

```python
# 查看有异常值的这行数据:
df[df["时长"] == "8U"] #寻找异常值
# 不知道怎么改的话可以删除：
df.drop([31644], inplace = True)
```

```python
# 重新转化格式：
df["时长"] = df["时长"].astype("int")
# 错误信息：ValueError: invalid literal for int() with base 10: '12J'
```

```python
# 看报错的信息找出异常值,查看有异常值的这行数据
df[df["时长"] == "12J"]
#删数据：
df.drop([32949], inplace = True) 
# 再重新转化格式：
df["时长"] = df["时长"].astype("int")
```



## 2.2 排序 

- 默认排序 ：根据index进行排序

- 根据某一列的具体值values来排序

  - 升序排列：`DataFrame的名称.sort_values(by=要根据来取值的列的名称)`  （默认ascending=True）
  - 降序排列：`DataFrame的名称.sort_values(by=要根据来取值的列的名称,ascending=False)`

- 有先后顺序地根据多个值来排序(当前面的那个值相同时，根据下一个值来进行排列)

  - 升序排列：`DataFrame的名称.sort_values(by=[要根据排序的列名1，要根据排序的列名2，...])`
  - 降序排列：`DataFrame的名称.sort_values(by=[要根据排序的列名1，要根据排序的列名2，...]，ascending=False)`
  - 对多列数据排列且排序规则不同时：`DataFrame的名称.sort_values(by=[要根据排序的列名1，要根据排序的列名2，...]，ascending=(规则1，规则2，...))`  【规则为True(升序)或False(降序)，与要根据排序的列名一一对应。类型为**元组**，所以要用小括号包起来】
  
  【列表中的顺序决定先后顺序】
  
  [tips：以上的“`by=`”是可省略的]


```python
# 查看前10行按默认排序得到的数据:
df[:10]
# 查看前5行按照投票人数来降序排列得到的数据:
df.sort_values(by = "投票人数", ascending = False)[:5] 
# 按照年代进行排序:
df.sort_values(by = "年代")
# 多个值排序，先按照评分，再按照投票人数 :
df.sort_values(by = ["评分","投票人数"], ascending = False) 

# 按照评分降序排序，评分相同时按价格升序排序：
df.sort_values(['评分','价格'],ascending=(False,True))
```



## 2.3 基本统计分析 

#### 描述性统计

`DataFrame名称.describe()`：对DataFrame中的<u>**数值**型数据</u>进行描述性统计

eg：`df.describe()`

---

- 通过描述性统计，可以发现一些异常值 


```python
# eg:
#挑出有异常值的行：
df[df["年代"] > 2018] 
df[df["时长"] > 1000]

#删除异常数据:
df.drop(df[df["年代"] > 2018].index, inplace = True)
df.drop(df[df["时长"] > 1000].index, inplace = True) 
# 删除时会连带索引一起删除，所以删除后的索引就已经不是连续的了

# 为了解决删除后索引不连续的问题：重新对index进行设置:
df.index = range(len(df)) # 生成从0-len(df)但不包含len(df)的整数序列
```



#### 求最值

- `DataFrame名称[要求最大值的列名称].max()`
- `DataFrame名称[要求最小值的列名称].min()`

#### 求均值和中值

- 均值：`DataFrame名称[要求均值的列名称].mean()`
- 中值：`DataFrame名称[要求中值的列名称].median()`

#### 求方差和标准差

- 方差：`DataFrame名称[要求方差的列名称].var()`
- 标准差：`DataFrame名称[要求标准差的列名称].std()`

#### 求和

`DataFrame名称[要求和的列名称].sum()`

#### 求相关系数和协方差

- 相关系数：`DataFrame名称[[要求相关系数的列名称组成的列表]].corr()`【结果得到一个表】

- 协方差：`DataFrame名称[[要求协方差的列名称组成的列表]].cov()`【结果得到一个表】

注意：涉及2个或多个变量时，中括号里面是一个列表，还带有一个中括号

> tips：
>
> - 也可用`DataFrame名称.corr()`或`DataFrame名称.cov()`对dataframe中<u>所有</u>的数值型数据求得到一个相关系数表或协方差表
> - 涉及2个变量时，还可以：`DataFrame名称[要求相关系数的列名称1].corr(DataFrame名称[要求相关系数的列名称2])`或`DataFrame名称[要求协方差的列名称1].corr(DataFrame名称[要求协方差的列名称2])`【结果得到一个数】

```python
# eg：
df[["投票人数", "评分"]].corr()
df[["投票人数", "评分"]].cov()
```



#### 计数

- 计算dataframe的总行数（有多少份数据）：`len(DataFrame的名称)`
- 查看某一列的唯一值（得到由这一列唯一值组成的数组）：`DataFrame的名称[列名称].unique()`
- 计算某一列的唯一值组成的数组的长度/某一列的取值有多少种/某一列唯一值的个数：`len(DataFrame名称[列名称].unique())`

```python
# 查看总行数/某一列（例如产地这一列）有多少个取值：
len(df) 

# 查看产地这一列的取值/唯一值：
print(df["产地"].unique())  # 得到一个由这一列的唯一值组成的数组
"""结果：
['美国' '意大利' '中国大陆' '日本' '法国' '英国' '韩国' '中国香港' '阿根廷' '德国' '印度' '其他' '加拿大'
 '波兰' '泰国' '澳大利亚' '西班牙' '俄罗斯' '中国台湾' '荷兰' '丹麦' '比利时' 'USA' '苏联' '巴西' '瑞典'
 '西德' '墨西哥']
"""

#计算产地这一列的唯一值组成的数组的长度（计算产地这一列的取值有多少种/统计唯一值的个数）：
print(len(df['产地'].unique()))  # 28
```

-----

#### 数据替换

tips：产地中包含了一些重复的数据，比如美国和USA，德国和西德，俄罗斯和苏联，可以通过**数据替换**的方法将相同的国家的电影数据合并。

数据替换方法：`DataFrame的名称[列名称].replace(要被替换掉的值，替换后要得到的新值，inplace=True)`

【也可以使用列表来进行数据替换，注意要一一对应】

```python
df["产地"].replace("USA","美国",inplace=True) #第一个参数是要替换的值，第二个参数是替换后的值
# 使用列表进行数据替换【注意一一对应】
df["产地"].replace(["西德","苏联"],["德国","俄罗斯"], inplace=True) 

print(df['产地'].unique())
"""结果：
['美国' '意大利' '中国大陆' '日本' '法国' '英国' '韩国' '中国香港' '阿根廷' '德国' '印度' '其他' '加拿大'
 '波兰' '泰国' '澳大利亚' '西班牙' '俄罗斯' '中国台湾' '荷兰' '丹麦' '比利时' '巴西' '瑞典' '墨西哥']
"""
print(len(df['产地'].unique())) # 25
```

----

#### 统计唯一值相关数据

对某一列的<u>各个唯一值出现的次数</u>进行统计：（返回一个Series）

- 默认按**从大到小**的顺序进行排序【降序排列】：`DataFrame名称[列名称].value_counts()`
- 升序排列：`DataFrame名称[列名称].value_counts(ascending=True)`


```python
# 计算每一年电影的数量：
df["年代"].value_counts(ascending = True)[:10] #默认从大到小
# 电影产出前5的国家或地区：
df["产地"].value_counts()[:5]
```


```python
# 最后要保存数据：
df.to_excel("movie_data2.xlsx")
```



## 2.4 数据透视 

> Excel中数据透视表的使用非常广泛，Pandas也提供了一个类似的功能，为pivot_table，它只是一个函数，但是它能够快速地对数据进行强大的分析。
>
> 使用pandas中的pivot_table的挑战：你需要确保你理解你的数据，并清楚地知道你想通过透视表解决什么问题。



#### 数据透视的形式

1. 基础形式

   最基础的样式：`pd.pivot_table(需要做数据透视的DataFrame文件，index=[要作为索引的一列])`

   结果得到：根据作为索引的一列数据的唯一值来分类，再对那个类别里面的各个数值型数据计算出均值


```python
pd.set_option("max_columns",100) #可以设置可展示的最多的列，来让数据进行完整展示
pd.set_option("max_rows",500)  # 设置可展示的最多的行
# 如果没有写这些，如果当数据量大时，数据不会完全展示，而是在中间会带有省略号
```


```python
pd.pivot_table(df, index = ["年代"]) #统计各个年代中所有数值型数据的均值（默认）
```



2. 可以有多个索引，就会有多次分类。实际上，大多数的pivot_table参数可以通过列表获取多个值。

   样式：`pd.pivot_table(需要做数据透视的DataFrame文件，index=要作为索引的列组成的列表)`


```python
# eg：
pd.pivot_table(df, index = ["年代", "产地"]) #双索引
```



3. 可以指定需要统计汇总的数据

   样式：`pd.pivot_table(需要做数据透视的DataFrame文件，index=要作为索引的列组成的列表，values=要汇总的数据组成的列表)`


```python
pd.pivot_table(df, index = ["年代", "产地"], values = ["评分"])
```



4. 可以用`aggfunc=某函数`来指定函数，计算出不同的统计值

   样式：`pd.pivot_table(需要做数据透视的DataFrame文件，index=要作为索引的列组成的列表，values=要汇总的数据组成的列表，aggfunc=某函数或多个函数组成的列表)` 

   tips:  当未设置aggfunc时，它默认`aggfunc=np.mean`计算均值。所以当统计均值的时候，可以不写`aggfunc=np.mean`


```python
# eg：
pd.pivot_table(df, index = ["年代", "产地"], values = ["投票人数"], aggfunc = [np.sum])# 对按年代和产地分类的投票人数的数据进行汇总并求和

# 通过将“投票人数”列和“评分”列进行对应分组，对“产地”实现数据聚合和总结：
pd.pivot_table(df, index = ["产地"], values = ["投票人数", "评分"], aggfunc = [np.sum, np.mean])

# 注意：在这里当函数列表中有多个函数时，里面的函数并不是只对与它相同位置上的要汇总的数据values的值一一对应，而是每个函数都会对要汇总的数据分别进行统计计算（每一个数据都会照顾到，对按产地分类的投票人数和评分的数值 都会求和以及平均值）
```



5. 非数值（NaN）难以处理。如果想移除它们，可以加上参数“`fill_value=0`”将其设置为0


```python
pd.pivot_table(df, index = ["产地"], aggfunc = [np.sum, np.mean], fill_value = 0)
```



6. 可以加入`margins = True`，在所有数据的下方多显示一行总的数据ALL（这一行是对所有的分类进行的操作）


```python
pd.pivot_table(df, index = ["产地"], aggfunc = [np.sum, np.mean], fill_value = 0, margins = True)
# all对所有的产地的影片进行操作
```



7. 可以向aggfunc传递一个**字典**，实现对不同值执行不同的函数。不过有一个副作用：必须将标签做的更加整洁才行。


```python
# 对各个地区的投票人数求和，对评分求均值：
pd.pivot_table(df, index = ["产地"], values = ["投票人数", "评分"], aggfunc = {"投票人数":np.sum, "评分":np.mean}, fill_value = 0)
# 上面的操作可以对不同的数据用不同的函数进行不同的操作：对以产地进行分类(作为索引)的投票人数进行求和，对评分求平均值

# 对各个年份的投票人数求和，对评分求均值，并求出总的数据：
pd.pivot_table(df, index = ["年代"], values = ["投票人数", "评分"], aggfunc = {"投票人数":np.sum, "评分":np.mean}, fill_value = 0, margins = True)
```



8. 同样的，也可以按照多个索引来进行汇总——得到一个层次化的索引结构

   ```python
   pd.pivot_table(df, index = ["产地", "年代"], values = ["投票人数", "评分"], aggfunc = {"投票人数":np.sum, "评分":np.mean}, fill_value = 0)
   ```

   

####  透视表过滤 


```python
table = pd.pivot_table(df, index = ["年代"], values = ["投票人数", "评分"], aggfunc = {"投票人数":np.sum, "评分":np.mean}, fill_value = 0)
print(type(table))# pandas.core.frame.DataFrame
```

上面结果说明透视表过滤出来的结果本身就是一个dataframe，所以要对它进行操作时的方法和一般的dataframe都是相同的


```python
# 例如：
# 读取前5行透视后的数据：
table[:5]
```


```python
# 查看1994年的透视后的数据：
table[table.index == 1994]
```


```python
# 对评分这一列数据进行降序排列
table.sort_values("评分", ascending = False) # 降序方式
```



# Pandas-3


```python
import pandas as pd
import numpy as np
# 读入数据
df = pd.read_excel(r'D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业4\movie_data2.xlsx', index_col = 0)  
```

> tips:
>
> - index_col=0：设置第一列为index值
> - index_col默认为None：需要重新设置一列成为index值
> - index_col=False：需要重新设置一列成为index值



## 3.1 数据重塑和轴向旋转 

### 3.1.1层次化索引 

层次化索引是pandas的一项重要功能，能使在一个轴上有多个索引

#### 1.Series的层次化索引 

##### 1.1设置层次化索引

语法：`index=[[最外层索引名称组成的列表],...,[最内层索引名称组成的列表]]`


```python
# eg：
# 多层索引：
s = pd.Series(np.arange(1,10), index = [['a','a','a','b','b','c','c','d','d'], [1,2,3,1,2,3,1,2,3]])
#类似于excel中的合并单元格
print(s)
"""结果：
a  1    1
   2    2
   3    3
b  1    4
   2    5
c  3    6
   1    7
d  2    8
   3    9
dtype: int32"""
```



##### 1.2查看所有索引

语法：`Series名称.index`


```python
# 查看索引：
s.index
# 结果：
"""
MultiIndex([('a', 1),
            ('a', 2),
            ('a', 3),
            ('b', 1),
            ('b', 2),
            ('c', 3),
            ('c', 1),
            ('d', 2),
            ('d', 3)],
           )"""
```



##### 1.3用外层索引索引对应的数据

语法：`Series名称[某个外层索引名]`


```python
#外层索引，取外层索引为'a'的数据：
s['a'] 
```

```python
# 结果：
1    1
2    2
3    3
dtype: int32
```



##### 1.4用内层索引索引对应的数据

(以两层的为例)：`Series名称[:,某个索引名]`  【逗号前面的冒号两边都要省略】

> 类比得：
>
> 对三层索引的series要根据它的第二层索引取值：`Series名称[:,第二层的某个索引名]`
>
> 对三层索引的series要根据它的第三层索引取值：`Series名称[:,:,第二层的某个索引名]`


```python
# 取出内层索引为1的数据：
s[:,1] #内层索引，逗号前面的冒号两边都省略
# 结果：
a    1
b    4
c    7
dtype: int32
```



##### 1.5切片操作取索引对应的数据

【注意：对用自定义的索引来取值时，是左闭右闭】


```python
#切片，取出外层索引从a-c的数据：
s['a':'c'] 
# 结果：
a  1    1
   2    2
   3    3
b  1    4
   2    5
c  3    6
   1    7
dtype: int32
```



##### 1.6提取具体的某个值

语法：`Series名称[最外层索引名，...，对内层索引名]`


```python
#提取具体的值
s['c',3] # 提取外层索引为c、内层索引为3的数据  
# 结果：6
```






#### 2.Series与DataFrame的相互转化

（stack：堆叠      unstack：不堆叠）

![](D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业5\d5eff56ef6b2701728fee6e8927ec62.jpg)

> stack和unstack默认操作为**最内层**，可以用level参数指定操作层.
> stack和unstack默认旋转轴的级别将会成果结果中的最低级别（最内层）



##### 2.1将Series转变成DataFrame

通过unstack方法可以得到将Series转变成一个DataFrame的结果

语法：`Series名称.unstack()`

tips：

- 原来的series并没有发生改变，只不过得到一个将原来的Series转变成一个DataFrame的结果
- 如果想要将原来的Series转变成一个DataFrame，可以：`Series名称=Series名称.unstack()`，此时这个Series类型的数据已经被DataFrame类型的数据覆盖了


```python
s.unstack()  # 会返回一个将s转化为dataframe形式的结果，但是s本身并没有发生变化
type(s) #pandas.core.series.Series

s=s.unstack()  # 此时s发生改变，这个Series类型的数据已经被DataFrame类型的数据覆盖了
type(s) #pandas.core.frame.DataFrame
```



##### 2.2unstack与stack之间有形式上的转换：

- 对于Series类型的数据：作用效果相反，unstack和stack在一起时相当于作用可以相互抵消

  ```python
  s.unstack().stack() #形式上的相互转换
  # unstack和stack在一起时相当于作用可以相互抵消，得到的结果为s这个Series本身(但是莫名其妙地都变成了浮点数，烦！！)
  
  """结果：
  a  1    1.0
     2    2.0
     3    3.0
  b  1    4.0
     2    5.0
  c  1    7.0
     3    6.0
  d  2    8.0
     3    9.0
  dtype: float64
  """
  ```

- 对于DataFrame类型的数据并不是作用可以相互抵消的【对于单层的dataframe，unstack和stack在一起作用时，会变回原样】

  ```python
  data = pd.DataFrame(np.arange(12).reshape(4,3), index = [['a','a','b','b'],[1,2,1,2]], columns = [['A','A','B'],['Z','X','C']])
  print(data)
  """结果：
       A       B
       Z   X   C
  a 1  0   1   2
    2  3   4   5
  b 1  6   7   8
    2  9  10  11
  """
  
  print(data.stack())
  """结果：
            A     B
  a 1 C   NaN   2.0
      X   1.0   NaN
      Z   0.0   NaN
    2 C   NaN   5.0
      X   4.0   NaN
      Z   3.0   NaN
  b 1 C   NaN   8.0
      X   7.0   NaN
      Z   6.0   NaN
    2 C   NaN  11.0
      X  10.0   NaN
      Z   9.0   NaN
  """
  
  print(data.stack().unstack())
  """结果：
        A                B        
        C     X    Z     C   X   Z
  a 1 NaN   1.0  0.0   2.0 NaN NaN
    2 NaN   4.0  3.0   5.0 NaN NaN
  b 1 NaN   7.0  6.0   8.0 NaN NaN
    2 NaN  10.0  9.0  11.0 NaN NaN
  """
  ```




##### 2.3将单层DataFrame转变成Series

对**单层**(只有一层行索引和列索引)的DataFrame进行stack操作之后，会变成Series型数据

```python
data = pd.DataFrame(np.arange(4).reshape(2,2), index = ['a','b'], columns = ['A','B'])
print(data)
"""
   A  B
a  0  1
b  2  3"""

print(data.stack())
"""
a  A    0
   B    1
b  A    2
   B    3
dtype: int32"""

print(type(data.stack())) #<class 'pandas.core.series.Series'>

print(data.stack().unstack())
"""
   A  B
a  0  1
b  2  3"""
# 对于单层的dataframe，unstack和stack在一起作用时，会变回原样
```



#### 3.Dataframe的层次化索引

对于DataFrame来说，行和列都能进行层次化索引（多层索引，每层索引都是一个列表，用中括号包起来）

##### 3.1设置行列索引

- 设置层次化行索引：`index=[[最外层行索引名称组成的列表],...,[最内层行索引名称组成的列表]]`
- 设置层次化列索引：`columns=[[最外层列索引名称组成的列表],...,[最内层列索引名称组成的列表]]`


```python
# eg：
data = pd.DataFrame(np.arange(12).reshape(4,3), index = [['a','a','b','b'],[1,2,1,2]], columns = [['A','A','B'],['Z','X','C']])#有类似于excel中的合并单元格
print(data)
```

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th></th>
      <th colspan="2" halign="left">A</th>
      <th>B</th>
    </tr>
    <tr>
      <th></th>
      <th></th>
      <th>Z</th>
      <th>X</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
----



##### 3.2选取某一列：

【只能依次从外到内索引选取】


```python
# 选取A为列标的列  【注意：最外层只能选取A或B】
data['A']  
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>Z</th>
      <th>X</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
    </tr>
  </tbody>
</table>
```python
# 选取A为外层列标、X为内层列标的列：
data['A']['X']
```

```
结果：
a  1     1
   2     4
b  1     7
   2    10
Name: X, dtype: int32
```

-----



##### 3.3对各个级别(内外)的索引设置名称：

- 设置行索引的名称：`DataFrame名称.index.names=要起的行索引的名称组成的列表`
- 设置列索引的名称：`DataFrame名称.index.names=要起的列索引的名称组成的列表`

【tips：因为有几个名字，所以要记得是names！！后面有"s"】


```python
data.index.names = ["row1","row2"]
data.columns.names = ["col1", "col2"]
data
```

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>col1</th>
      <th colspan="2" halign="left">A</th>
      <th>B</th>
    </tr>
    <tr>
      <th></th>
      <th>col2</th>
      <th>Z</th>
      <th>X</th>
      <th>C</th>
    </tr>
    <tr>
      <th>row1</th>
      <th>row2</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">a</th>
      <th>1</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">b</th>
      <th>1</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>


##### 3.4调整行索引的顺序

交换两个维度的位置：`dataFrame名称.swaplevel(axis1,axis2)`  


```python
data.swaplevel("row1","row2") #位置调整
```

<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th>col1</th>
      <th colspan="2" halign="left">A</th>
      <th>B</th>
    </tr>
    <tr>
      <th></th>
      <th>col2</th>
      <th>Z</th>
      <th>X</th>
      <th>C</th>
    </tr>
    <tr>
      <th>row2</th>
      <th>row1</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <th>a</th>
      <td>0</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <th>a</th>
      <td>3</td>
      <td>4</td>
      <td>5</td>
    </tr>
    <tr>
      <th>1</th>
      <th>b</th>
      <td>6</td>
      <td>7</td>
      <td>8</td>
    </tr>
    <tr>
      <th>2</th>
      <th>b</th>
      <td>9</td>
      <td>10</td>
      <td>11</td>
    </tr>
  </tbody>
</table>


##### 3.5查看dataframe的所有索引

语法：`DataFrame名称.index`


```python
df.index #查看索引
```


    Int64Index([    0,     1,     2,     3,     4,     5,     6,     7,     8,
                    9,
                ...
                38153, 38154, 38155, 38156, 38157, 38158, 38159, 38160, 38161,
                38162],
               dtype='int64', length=38163)



##### 3.6把列变成索引

语法：`DataFrame名称=DataFrame名称.set_index(列名组成的列表)`

(当要把多个列变成行索引时，这些列名要用列表包装起来，第一个列名为最外层的索引，最后一个为最内层的索引)


```python
# 把产地和年代同时设成索引，产地是外层索引，年代为内层索引：
df = df.set_index(["产地", "年代"])
print(df)
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
    <tr>
      <th>产地</th>
      <th>年代</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="2" valign="top">美国</th>
      <th>1994</th>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.600000</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1957</th>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.500000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>意大利</th>
      <th>1997</th>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.500000</td>
      <td>意大利</td>
    </tr>
    <tr>
      <th>美国</th>
      <th>1994</th>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.400000</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>中国大陆</th>
      <th>1993</th>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.400000</td>
      <td>香港</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>美国</th>
      <th>1935</th>
      <td>1935年</td>
      <td>57</td>
      <td>喜剧/歌舞</td>
      <td>1935-03-15 00:00:00</td>
      <td>98</td>
      <td>7.600000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">中国大陆</th>
      <th>1986</th>
      <td>血溅画屏</td>
      <td>95</td>
      <td>剧情/悬疑/犯罪/武侠/古装</td>
      <td>1905-06-08 00:00:00</td>
      <td>91</td>
      <td>7.100000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1986</th>
      <td>魔窟中的幻想</td>
      <td>51</td>
      <td>惊悚/恐怖/儿童</td>
      <td>1905-06-08 00:00:00</td>
      <td>78</td>
      <td>8.000000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>俄罗斯</th>
      <th>1977</th>
      <td>列宁格勒围困之星火战役 Блокада: Фильм 2: Ленинградский ме...</td>
      <td>32</td>
      <td>剧情/战争</td>
      <td>1905-05-30 00:00:00</td>
      <td>97</td>
      <td>6.600000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>美国</th>
      <th>2018</th>
      <td>复仇者联盟3</td>
      <td>123456</td>
      <td>剧情/科幻</td>
      <td>2018-05-04 00:00:00</td>
      <td>142</td>
      <td>6.935704</td>
      <td>美国</td>
    </tr>
  </tbody>
</table>
<p>38163 rows × 7 columns</p>



##### 3.7每一个索引都是一个元组

查看dataframe的某一行的索引（查看第n行）：`DataFrame名称.index[n-1]`  

<u>对于**层次化的索引**，每一个索引都是一个元组</u> 


```python
# 查看第一行的索引：
print(df.index[0])  # ('美国', 1994)
print(type(df.index[0]))  # tuple
```

----

tips：当行索引不是层次化的索引时，不是元组类型

```python
#eg:如果上面没有df = df.set_index(["产地", "年代"]),而是：
df = df.set_index(["产地"])
print(df)
# 那么结果是：（只有一层行索引，并非层次化索引）
```

|     名字 |                                                     投票人数 |   类型 |                 上映时间 |                时长 | 年代 | 评分 | 首映地点 |              |
| -------: | -----------------------------------------------------------: | -----: | -----------------------: | ------------------: | ---: | ---: | -------: | -----------: |
|     产地 |                                                              |        |                          |                     |      |      |          |              |
|     美国 |                                                 肖申克的救赎 | 692795 |                剧情/犯罪 | 1994-09-10 00:00:00 |  142 | 1994 | 9.600000 | 多伦多电影节 |
|     美国 |                                                     控方证人 |  42995 |           剧情/悬疑/犯罪 | 1957-12-17 00:00:00 |  116 | 1957 | 9.500000 |         美国 |
|   意大利 |                                                     美丽人生 | 327855 |           剧情/喜剧/爱情 | 1997-12-20 00:00:00 |  116 | 1997 | 9.500000 |       意大利 |
|     美国 |                                                     阿甘正传 | 580897 |                剧情/爱情 | 1994-06-23 00:00:00 |  142 | 1994 | 9.400000 |   洛杉矶首映 |
| 中国大陆 |                                                     霸王别姬 | 478523 |           剧情/爱情/同性 | 1993-01-01 00:00:00 |  171 | 1993 | 9.400000 |         香港 |
|      ... |                                                          ... |    ... |                      ... |                 ... |  ... |  ... |      ... |          ... |
|     美国 |                                                       1935年 |     57 |                喜剧/歌舞 | 1935-03-15 00:00:00 |   98 | 1935 | 7.600000 |         美国 |
| 中国大陆 |                                                     血溅画屏 |     95 | 剧情/悬疑/犯罪/武侠/古装 | 1905-06-08 00:00:00 |   91 | 1986 | 7.100000 |         美国 |
| 中国大陆 |                                                 魔窟中的幻想 |     51 |           惊悚/恐怖/儿童 | 1905-06-08 00:00:00 |   78 | 1986 | 8.000000 |         美国 |
|   俄罗斯 | 列宁格勒围困之星火战役 Блокада: Фильм 2: Ленинградский ме... |     32 |                剧情/战争 | 1905-05-30 00:00:00 |   97 | 1977 | 6.600000 |         美国 |
|     美国 |                                                  复仇者联盟3 | 123456 |                剧情/科幻 | 2018-05-04 00:00:00 |  142 | 2018 | 6.935704 |         美国 |

38163 rows × 8 columns

```python
print(df.index[0])  # '美国'
print(type(df.index[0])) # str  #不是元组
```



##### 3.8通过行标签索引行数据

可通过行标签索引行数据：`DataFrame名称.loc[行索引]`

tips：对于层次化索引的dataframe，用这个方法索引的是某(些)外层索引包含的数据，得到的结果dataframe的行索引改变，最外层行索引变为原来的第二层索引

优点：可以简化很多的筛选环节


```python
#获取所有的美国电影，由于产地信息已经变成了索引，因此要是用.loc方法：
df.loc["美国"] #行标签索引行数据
# 得到的结果为所有美国电影的数据，是以年代为索引的一个dataframe：
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
    <tr>
      <th>年代</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1994</th>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.600000</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1957</th>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.500000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1994</th>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.400000</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>2012</th>
      <td>泰坦尼克号</td>
      <td>157074</td>
      <td>剧情/爱情/灾难</td>
      <td>2012-04-10 00:00:00</td>
      <td>194</td>
      <td>9.400000</td>
      <td>中国大陆</td>
    </tr>
    <tr>
      <th>1993</th>
      <td>辛德勒的名单</td>
      <td>306904</td>
      <td>剧情/历史/战争</td>
      <td>1993-11-30 00:00:00</td>
      <td>195</td>
      <td>9.400000</td>
      <td>华盛顿首映</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1987</th>
      <td>零下的激情</td>
      <td>199</td>
      <td>剧情/爱情/犯罪</td>
      <td>1987-11-06 00:00:00</td>
      <td>98</td>
      <td>7.400000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1986</th>
      <td>离别秋波</td>
      <td>240</td>
      <td>剧情/爱情/音乐</td>
      <td>1986-02-19 00:00:00</td>
      <td>90</td>
      <td>8.200000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1986</th>
      <td>极乐森林</td>
      <td>45</td>
      <td>纪录片</td>
      <td>1986-09-14 00:00:00</td>
      <td>90</td>
      <td>8.100000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1935</th>
      <td>1935年</td>
      <td>57</td>
      <td>喜剧/歌舞</td>
      <td>1935-03-15 00:00:00</td>
      <td>98</td>
      <td>7.600000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>复仇者联盟3</td>
      <td>123456</td>
      <td>剧情/科幻</td>
      <td>2018-05-04 00:00:00</td>
      <td>142</td>
      <td>6.935704</td>
      <td>美国</td>
    </tr>
  </tbody>
</table>
<p>11714 rows × 7 columns</p>




```python
#调换行索引的顺序：
df = df.swaplevel("产地", "年代") 
df
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
    <tr>
      <th>年代</th>
      <th>产地</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1994</th>
      <th>美国</th>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.600000</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1957</th>
      <th>美国</th>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.500000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1997</th>
      <th>意大利</th>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.500000</td>
      <td>意大利</td>
    </tr>
    <tr>
      <th>1994</th>
      <th>美国</th>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.400000</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>1993</th>
      <th>中国大陆</th>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.400000</td>
      <td>香港</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1935</th>
      <th>美国</th>
      <td>1935年</td>
      <td>57</td>
      <td>喜剧/歌舞</td>
      <td>1935-03-15 00:00:00</td>
      <td>98</td>
      <td>7.600000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">1986</th>
      <th>中国大陆</th>
      <td>血溅画屏</td>
      <td>95</td>
      <td>剧情/悬疑/犯罪/武侠/古装</td>
      <td>1905-06-08 00:00:00</td>
      <td>91</td>
      <td>7.100000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>中国大陆</th>
      <td>魔窟中的幻想</td>
      <td>51</td>
      <td>惊悚/恐怖/儿童</td>
      <td>1905-06-08 00:00:00</td>
      <td>78</td>
      <td>8.000000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>1977</th>
      <th>俄罗斯</th>
      <td>列宁格勒围困之星火战役 Блокада: Фильм 2: Ленинградский ме...</td>
      <td>32</td>
      <td>剧情/战争</td>
      <td>1905-05-30 00:00:00</td>
      <td>97</td>
      <td>6.600000</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>2018</th>
      <th>美国</th>
      <td>复仇者联盟3</td>
      <td>123456</td>
      <td>剧情/科幻</td>
      <td>2018-05-04 00:00:00</td>
      <td>142</td>
      <td>6.935704</td>
      <td>美国</td>
    </tr>
  </tbody>
</table>
<p>38163 rows × 7 columns</p>




```python
df.loc[1994]  # 得到的结果为所有1994年电影的数据，是以产地为索引的一个dataframe：
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
    <tr>
      <th>产地</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>美国</th>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>美国</th>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>法国</th>
      <td>这个杀手不太冷</td>
      <td>662552</td>
      <td>剧情/动作/犯罪</td>
      <td>1994-09-14 00:00:00</td>
      <td>133</td>
      <td>9.4</td>
      <td>法国</td>
    </tr>
    <tr>
      <th>美国</th>
      <td>34街的</td>
      <td>768</td>
      <td>剧情/家庭/奇幻</td>
      <td>1994-12-23 00:00:00</td>
      <td>114</td>
      <td>7.9</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>中国大陆</th>
      <td>活着</td>
      <td>202794</td>
      <td>剧情/家庭</td>
      <td>1994-05-18 00:00:00</td>
      <td>132</td>
      <td>9.0</td>
      <td>法国</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>美国</th>
      <td>鬼精灵2： 恐怖</td>
      <td>60</td>
      <td>喜剧/恐怖/奇幻</td>
      <td>1994-04-08 00:00:00</td>
      <td>85</td>
      <td>5.8</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>英国</th>
      <td>黑色第16</td>
      <td>44</td>
      <td>剧情/惊悚</td>
      <td>1996-02-01 00:00:00</td>
      <td>106</td>
      <td>6.8</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>日本</th>
      <td>蜡笔小新之布里布里王国的秘密宝藏 クレヨンしんちゃん ブリブリ王国の</td>
      <td>2142</td>
      <td>动画</td>
      <td>1994-04-23 00:00:00</td>
      <td>94</td>
      <td>7.7</td>
      <td>日本</td>
    </tr>
    <tr>
      <th>日本</th>
      <td>龙珠Z剧场版10：两人面临危机! 超战士难以成眠 ドラゴンボール Z 劇場版：危険なふたり！</td>
      <td>579</td>
      <td>动画</td>
      <td>1994-03-12 00:00:00</td>
      <td>53</td>
      <td>7.2</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>中国香港</th>
      <td>重案实录之惊天械劫案 重案實錄之驚天械劫</td>
      <td>90</td>
      <td>动作/犯罪</td>
      <td>1905-06-16 00:00:00</td>
      <td>114</td>
      <td>7.3</td>
      <td>美国</td>
    </tr>
  </tbody>
</table>
<p>489 rows × 7 columns</p>



#### 4.取消层次化索引 

即把索引变成列 ：`处理对象=处理对象.reset_index()`


```python
df = df.reset_index()
df[:5]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
    </tr>
  </tbody>
</table>


### 3.1.2数据旋转 

- `.T`：可以直接让数据的行列进行交换

  注意：如果只是“`DataFrame名称.T`”，而没有将它再赋值给原来的dataframe本身的话，那么原来的dataframe并不会发生改变


```python
#行列转化：以前5部电影为例
data = df[:5]
data
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
    </tr>
  </tbody>
</table>



```python
data.T
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>年代</th>
      <td>1994</td>
      <td>1957</td>
      <td>1997</td>
      <td>1994</td>
      <td>1993</td>
    </tr>
    <tr>
      <th>产地</th>
      <td>美国</td>
      <td>美国</td>
      <td>意大利</td>
      <td>美国</td>
      <td>中国大陆</td>
    </tr>
    <tr>
      <th>名字</th>
      <td>肖申克的救赎</td>
      <td>控方证人</td>
      <td>美丽人生</td>
      <td>阿甘正传</td>
      <td>霸王别姬</td>
    </tr>
    <tr>
      <th>投票人数</th>
      <td>692795</td>
      <td>42995</td>
      <td>327855</td>
      <td>580897</td>
      <td>478523</td>
    </tr>
    <tr>
      <th>类型</th>
      <td>剧情/犯罪</td>
      <td>剧情/悬疑/犯罪</td>
      <td>剧情/喜剧/爱情</td>
      <td>剧情/爱情</td>
      <td>剧情/爱情/同性</td>
    </tr>
    <tr>
      <th>上映时间</th>
      <td>1994-09-10 00:00:00</td>
      <td>1957-12-17 00:00:00</td>
      <td>1997-12-20 00:00:00</td>
      <td>1994-06-23 00:00:00</td>
      <td>1993-01-01 00:00:00</td>
    </tr>
    <tr>
      <th>时长</th>
      <td>142</td>
      <td>116</td>
      <td>116</td>
      <td>142</td>
      <td>171</td>
    </tr>
    <tr>
      <th>评分</th>
      <td>9.6</td>
      <td>9.5</td>
      <td>9.5</td>
      <td>9.4</td>
      <td>9.4</td>
    </tr>
    <tr>
      <th>首映地点</th>
      <td>多伦多电影节</td>
      <td>美国</td>
      <td>意大利</td>
      <td>洛杉矶首映</td>
      <td>香港</td>
    </tr>
  </tbody>
</table>
-----------

对dataframe使用stack和unstack实现与series之间的相互转换：


```python
data.stack()  # 将dataframe转化为层次化索引的Series
```


    0  年代                     1994
       产地                       美国
       名字                   肖申克的救赎
       投票人数                 692795
       类型                    剧情/犯罪
       上映时间    1994-09-10 00:00:00
       时长                      142
       评分                      9.6
       首映地点                 多伦多电影节
    1  年代                     1957
       产地                       美国
       名字                     控方证人
       投票人数                  42995
       类型                 剧情/悬疑/犯罪
       上映时间    1957-12-17 00:00:00
       时长                      116
       评分                      9.5
       首映地点                     美国
    2  年代                     1997
       产地                      意大利
       名字                    美丽人生 
       投票人数                 327855
       类型                 剧情/喜剧/爱情
       上映时间    1997-12-20 00:00:00
       时长                      116
       评分                      9.5
       首映地点                    意大利
    3  年代                     1994
       产地                       美国
       名字                     阿甘正传
       投票人数                 580897
       类型                    剧情/爱情
       上映时间    1994-06-23 00:00:00
       时长                      142
       评分                      9.4
       首映地点                  洛杉矶首映
    4  年代                     1993
       产地                     中国大陆
       名字                     霸王别姬
       投票人数                 478523
       类型                 剧情/爱情/同性
       上映时间    1993-01-01 00:00:00
       时长                      171
       评分                      9.4
       首映地点                     香港
    dtype: object


```python
data.stack().unstack()  #再转回到dataframe
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
    </tr>
  </tbody>
</table>





## 3.2 数据分组，分组运算

### GroupBy技术 

实现数据的分组，和分组运算，作用类似于数据透视表

作用比数据透视表还要方便一些

![45f3e7f7e15bdc7e5ef4d01267073a4](D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业5\45f3e7f7e15bdc7e5ef4d01267073a4.jpg)

每一类都是得到求和之后的一个结果



- 按照电影的产地进行分组 

`DataFrame名称.groupby(分组依据)`




```python
# 先定义一个分组变量group ：
group = df.groupby(df["产地"])
```


```python
type(group)
```


    pandas.core.groupby.generic.DataFrameGroupBy



### 可以对分组后的整个dataframe进行操作


```python
# 计算分组后各个数值型数据的统计量 
group.mean() # 计算分组后各个数值型数据的平均值
group.sum()  # 计算分组后各个数值型数据的总和
```



也可以对具体的某一列进行操作

计算每年的平均评分 ：只想要操作评分这一列数据，以年代为分组依据


```python
df["评分"].groupby(df["年代"]).mean()
```




    年代
    1888    7.950000
    1890    4.800000
    1892    7.500000
    1894    6.633333
    1895    7.575000
              ...   
    2013    6.375974
    2014    6.249384
    2015    6.121925
    2016    5.834524
    2018    6.935704
    Name: 评分, Length: 127, dtype: float64



### 注意：只会对数值变量进行分组运算 


```python
# 将年代这一列的数据类型转化为字符串（因为对年份进行数据操作没有什么意义）
df["年代"] = df["年代"].astype("str")
df.groupby(df["产地"]).median() #不会再对年代进行求取均值（因为已经把年代转化成字符串格式）
df.groupby(df["产地"]).sum() #不会再对年代进行求取总和（因为已经把年代转化成字符串格式）
```



</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>投票人数</th>
      <th>时长</th>
      <th>评分</th>
    </tr>
    <tr>
      <th>产地</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>中国台湾</th>
      <td>487.0</td>
      <td>92.0</td>
      <td>7.1</td>
    </tr>
    <tr>
      <th>中国大陆</th>
      <td>502.0</td>
      <td>90.0</td>
      <td>6.4</td>
    </tr>
    <tr>
      <th>中国香港</th>
      <td>637.0</td>
      <td>92.0</td>
      <td>6.5</td>
    </tr>
    <tr>
      <th>丹麦</th>
      <td>182.0</td>
      <td>94.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>俄罗斯</th>
      <td>132.5</td>
      <td>93.0</td>
      <td>7.7</td>
    </tr>
    <tr>
      <th>其他</th>
      <td>158.0</td>
      <td>90.0</td>
      <td>7.4</td>
    </tr>
    <tr>
      <th>加拿大</th>
      <td>258.0</td>
      <td>89.0</td>
      <td>6.8</td>
    </tr>
    <tr>
      <th>印度</th>
      <td>139.0</td>
      <td>131.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>墨西哥</th>
      <td>183.0</td>
      <td>94.0</td>
      <td>7.2</td>
    </tr>
    <tr>
      <th>巴西</th>
      <td>131.0</td>
      <td>96.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>德国</th>
      <td>212.0</td>
      <td>94.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>意大利</th>
      <td>187.0</td>
      <td>101.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>日本</th>
      <td>359.0</td>
      <td>89.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>比利时</th>
      <td>226.0</td>
      <td>90.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>法国</th>
      <td>244.0</td>
      <td>95.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>波兰</th>
      <td>174.0</td>
      <td>87.0</td>
      <td>7.5</td>
    </tr>
    <tr>
      <th>泰国</th>
      <td>542.5</td>
      <td>92.5</td>
      <td>6.2</td>
    </tr>
    <tr>
      <th>澳大利亚</th>
      <td>323.0</td>
      <td>95.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>瑞典</th>
      <td>191.0</td>
      <td>96.0</td>
      <td>7.6</td>
    </tr>
    <tr>
      <th>美国</th>
      <td>415.0</td>
      <td>93.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>英国</th>
      <td>345.0</td>
      <td>92.0</td>
      <td>7.6</td>
    </tr>
    <tr>
      <th>荷兰</th>
      <td>180.0</td>
      <td>85.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>西班牙</th>
      <td>267.0</td>
      <td>97.0</td>
      <td>7.1</td>
    </tr>
    <tr>
      <th>阿根廷</th>
      <td>146.0</td>
      <td>97.0</td>
      <td>7.3</td>
    </tr>
    <tr>
      <th>韩国</th>
      <td>1007.0</td>
      <td>104.0</td>
      <td>6.5</td>
    </tr>
  </tbody>
</table>

</div>



### 也可传入多个分组变量 

`DataFrame名称.groupby(多个分组依据组成的列表)`


```python
#根据两个变量进行分组，并对所有数据进行求平均值操作
df.groupby([df["产地"],df["年代"]]).mean() 
```



</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>投票人数</th>
      <th>时长</th>
      <th>评分</th>
    </tr>
    <tr>
      <th>产地</th>
      <th>年代</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">中国台湾</th>
      <th>1963</th>
      <td>121.000000</td>
      <td>113.000000</td>
      <td>6.400000</td>
    </tr>
    <tr>
      <th>1965</th>
      <td>153.666667</td>
      <td>105.000000</td>
      <td>6.800000</td>
    </tr>
    <tr>
      <th>1966</th>
      <td>51.000000</td>
      <td>60.000000</td>
      <td>7.900000</td>
    </tr>
    <tr>
      <th>1967</th>
      <td>4444.000000</td>
      <td>112.000000</td>
      <td>8.000000</td>
    </tr>
    <tr>
      <th>1968</th>
      <td>89.000000</td>
      <td>83.000000</td>
      <td>7.400000</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">韩国</th>
      <th>2012</th>
      <td>5812.542857</td>
      <td>100.771429</td>
      <td>6.035238</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>10470.370370</td>
      <td>97.731481</td>
      <td>6.062037</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>3776.266667</td>
      <td>98.666667</td>
      <td>5.650833</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>3209.247706</td>
      <td>100.266055</td>
      <td>5.423853</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>1739.850000</td>
      <td>106.100000</td>
      <td>5.730000</td>
    </tr>
  </tbody>
</table>
<p>1578 rows × 3 columns</p>

</div>



**获得每个地区，每一年的电影的评分的均值** 


```python
#根据两个变量进行分组，并对评分这一列数据进行求平均值操作
group = df["评分"].groupby([df["产地"], df["年代"]])
means = group.mean()
means
# 也可以直接：df["评分"].groupby([df["产地"], df["年代"]]).mean()
```




    产地    年代  
    中国台湾  1963    6.400000
          1965    6.800000
          1966    7.900000
          1967    8.000000
          1968    7.400000
                    ...   
    韩国    2012    6.035238
          2013    6.062037
          2014    5.650833
          2015    5.423853
          2016    5.730000
    Name: 评分, Length: 1578, dtype: float64



Series可通过unstack方法转化为dataframe

**会产生缺失值**


```python
type(means) #pandas.core.series.Series  
# means为series类型，可以通过unstack()转化为dataframe。还可以对转化后的这个dataframe里面数据的行列进行交换
means.unstack().T
```

如果没有数据，会用NaN来填充

</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th>产地</th>
      <th>中国台湾</th>
      <th>中国大陆</th>
      <th>中国香港</th>
      <th>丹麦</th>
      <th>俄罗斯</th>
      <th>其他</th>
      <th>加拿大</th>
      <th>印度</th>
      <th>墨西哥</th>
      <th>巴西</th>
      <th>...</th>
      <th>波兰</th>
      <th>泰国</th>
      <th>澳大利亚</th>
      <th>瑞典</th>
      <th>美国</th>
      <th>英国</th>
      <th>荷兰</th>
      <th>西班牙</th>
      <th>阿根廷</th>
      <th>韩国</th>
    </tr>
    <tr>
      <th>年代</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1888</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>7.950000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1890</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.800000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1892</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1894</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.450000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1895</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2013</th>
      <td>7.076471</td>
      <td>5.306500</td>
      <td>6.105714</td>
      <td>6.555556</td>
      <td>6.875000</td>
      <td>6.853571</td>
      <td>6.018182</td>
      <td>6.400000</td>
      <td>6.983333</td>
      <td>8.00</td>
      <td>...</td>
      <td>6.966667</td>
      <td>5.568000</td>
      <td>6.76000</td>
      <td>7.100</td>
      <td>6.308255</td>
      <td>7.460140</td>
      <td>6.33</td>
      <td>6.358333</td>
      <td>6.616667</td>
      <td>6.062037</td>
    </tr>
    <tr>
      <th>2014</th>
      <td>6.522222</td>
      <td>4.963830</td>
      <td>5.616667</td>
      <td>7.120000</td>
      <td>7.175000</td>
      <td>6.596250</td>
      <td>5.921739</td>
      <td>6.374194</td>
      <td>7.250000</td>
      <td>6.86</td>
      <td>...</td>
      <td>7.060000</td>
      <td>5.653571</td>
      <td>6.56875</td>
      <td>6.960</td>
      <td>6.393056</td>
      <td>7.253398</td>
      <td>7.30</td>
      <td>6.868750</td>
      <td>7.150000</td>
      <td>5.650833</td>
    </tr>
    <tr>
      <th>2015</th>
      <td>6.576000</td>
      <td>4.969189</td>
      <td>5.589189</td>
      <td>7.166667</td>
      <td>7.342857</td>
      <td>6.732727</td>
      <td>6.018750</td>
      <td>6.736364</td>
      <td>6.500000</td>
      <td>6.76</td>
      <td>...</td>
      <td>6.300000</td>
      <td>5.846667</td>
      <td>6.88000</td>
      <td>7.625</td>
      <td>6.231486</td>
      <td>7.123256</td>
      <td>6.70</td>
      <td>6.514286</td>
      <td>7.233333</td>
      <td>5.423853</td>
    </tr>
    <tr>
      <th>2016</th>
      <td>NaN</td>
      <td>4.712000</td>
      <td>5.390909</td>
      <td>7.000000</td>
      <td>NaN</td>
      <td>6.833333</td>
      <td>6.200000</td>
      <td>6.900000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.522581</td>
      <td>7.200000</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>5.730000</td>
    </tr>
    <tr>
      <th>2018</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>...</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>6.935704</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>127 rows × 25 columns</p>

</div>



## 3.3 离散化处理 

> 在实际的数据分析项目中，对有的数据属性，我们往往并不怎么关注数据的绝对取值，而是只关心它所处的区间或者等级。
>
> 此时就会进行离散化操作。离散化也可称为分组、区间化。



Pandas为我们提供了方便的函数cut():  可实现分组、区间化的操作

函数原型：`pd.cut(x,bins,right = True,labels = None, retbins = False,precision = 3,include_lowest = False) `

> 参数解释：
>
> - x：需要离散化的数组、Series、DataFrame对象
>
> - bins：分组的依据（如果它是数字：把x划成bins个等间距的区间；如果它是一个序列：把x划分再指定的序列当中）
>
> - 设置对bins的分组的端点状态：【默认**左开右闭**，可以自己调整】
>
>   - right ：是否包括右端点 【默认right = True  (包括右端点)】
>
>   - include_lowest ：是否包括左端点 【默认include_lowest  = False  (不包括左端点)]】
>
> - labels：是否要用标记来替换返回出来的bins(分组)
>
>   【默认labels = None，就会根据bins中划分的区间来进行分组(如果没有设置，就是**左开右闭**)】
>
>   【注意：labels里面的顺序要注意，要和bins中的区间划分一一对应】
>
> - retbins：返回x当中每一个值对应的bins的列表
>
> - precision：设置精度




```python
# 把评分9分及以上的电影定义为A，7到9分定义为B，5到7分定义为C，3到5分定义为D，小于3分定义为E。
# 并新增“评分等级”这一列:
df["评分等级"] = pd.cut(df["评分"], [0,3,5,7,9,10], labels = ['E','D','C','B','A']) 
# 把投票人数分成五等份来确定它的热门程度
bins = np.percentile(df["投票人数"], [0,20,40,60,80,100]) #获取分位数

#根据投票人数来刻画电影的热门，投票越多的热门程度越高。新增“热门程度”这一列:
df["热门程度"] = pd.cut(df["投票人数"],bins,labels = ['E','D','C','B','A'])
#大烂片集合(投票人数很多，评分很低):
df[(df.热门程度 == 'A') & (df.评分等级 == 'E')]
#冷门高分电影：
df[(df.热门程度 == 'E') & (df.评分等级 == 'A')]
```


```python
#将处理后的数据保存到movie_data3.xlsx
df.to_excel("movie_data3.xlsx")
```



## 3.4 合并数据集 

因为经常需要对几个数据集一起进行操作

### （ 1 ）append 

纵向拼接，一般数据集当中中的列标相同时会用

语法：`数据集1.append(数据集2)`


```python
#由于没有什么数据，所以先把数据集拆分为多个，再进行合并
df_usa = df[df.产地 == "美国"]
df_china = df[df.产地 == "中国大陆"]

# 将这两个数据集进行合并
df_china.append(df_usa) #直接追加到后面，最好是变量相同的
```



### （ 2 ）merge 

常用于做横向合并，两个数据集之间有相同的变量或index

```python
pd.merge(left, right, how = 'inner', on = None, left_on = None, right_on = None,
    left_index = False, right_index = False, sort = True,
    suffixes = ('_x', '_y'), copy = True, indicator = False, validate=None) 
```

left：参与合并的左侧DataFrame对象

right：参与合并的右侧DataFrame对象

how：用来指定数据的保留、连接方式。有inner、left、right、outer（默认方式为内连接“inner”——取左边数据和右边数据的交集）

how='left'：左连接——以左边的数据为基准(左边的数据不动)，如果右边的数据文件与左边的数据文件有交集，那么右边数据就会保留交集部分；如果右边的数据文件与左边的数据文件没有交集，就不会保留右边的数据。

how='right'：右连接（与左连接同理）





- **on：**指的是用于连接的列索引名称，必须存在于左右两个DataFrame中，如果没有指定且其他参数也没有指定，则以两个DataFrame列名交集作为连接键（如果两个数据文件的列名称相同的话，可以直接用on来指定；如果不同的话，左边和右边用来连接的键分别用left_on 和 right_on 进行设定）
- **left_on：**左侧DataFrame中用于连接键的列名，这个参数左右列名不同但代表的含义相同时非常的有用；
- **right_on：**右侧DataFrame中用于连接键的列名；
- **left_index：**使用左侧DataFrame中的行索引作为连接键；
- **right_index：**使用右侧DataFrame中的行索引作为连接键；
- **sort：**综合通过连结键按字典顺序对结果进行排序，(将合并的数据排序)，默认为True，设置为False可以提高性能
- **suffixes：**字符串值组成的元组，用于指定当左右DataFrame存在相同列名时在列名后面附加的后缀名称，默认为(' _ x', ' _ y')。tips：字符串后缀不适用于重叠列的元组
- **copy：**默认为True，总是将数据复制到数据结构中，设置为False可以提高性能；
- **indicator：**显示合并数据中数据的来源情况。






```python
#选取6部热门电影
df1 = df.loc[:5]  #注意：loc是左闭右闭
```



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
      <th>评分等级</th>
      <th>热门程度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2012</td>
      <td>美国</td>
      <td>泰坦尼克号</td>
      <td>157074</td>
      <td>剧情/爱情/灾难</td>
      <td>2012-04-10 00:00:00</td>
      <td>194</td>
      <td>9.4</td>
      <td>中国大陆</td>
      <td>A</td>
      <td>A</td>
    </tr>
  </tbody>
</table>




```python
#取前六部电影的名字和产地这两列：
df2 = df.loc[:5][["名字","产地"]]
#再新增票房这一列：
df2["票房"] = [123344,23454,55556,333,6666,444]
```




```python
df2 = df2.sample(frac = 1) #打乱数据（索引也会一起跟着改变，变得无序）
```


```python
# 重新设置行索引
df2.index = range(len(df2))
df2
```



<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名字</th>
      <th>产地</th>
      <th>票房</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>泰坦尼克号</td>
      <td>美国</td>
      <td>444</td>
    </tr>
    <tr>
      <th>1</th>
      <td>阿甘正传</td>
      <td>美国</td>
      <td>333</td>
    </tr>
    <tr>
      <th>2</th>
      <td>控方证人</td>
      <td>美国</td>
      <td>23454</td>
    </tr>
    <tr>
      <th>3</th>
      <td>美丽人生</td>
      <td>意大利</td>
      <td>55556</td>
    </tr>
    <tr>
      <th>4</th>
      <td>霸王别姬</td>
      <td>中国大陆</td>
      <td>6666</td>
    </tr>
    <tr>
      <th>5</th>
      <td>肖申克的救赎</td>
      <td>美国</td>
      <td>123344</td>
    </tr>
  </tbody>
</table>

</div>



现在，我们需要把df1和df2合并

我们发现，df2有票房数据，df1有评分等其他信息  
由于样本的顺序不一致，因此不能直接采取直接复制的方法


```python
pd.merge(df1, df2, how = "inner", on = "名字")
```



</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地_x</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
      <th>评分等级</th>
      <th>热门程度</th>
      <th>产地_y</th>
      <th>票房</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
      <td>A</td>
      <td>A</td>
      <td>美国</td>
      <td>123344</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
      <td>A</td>
      <td>A</td>
      <td>美国</td>
      <td>23454</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
      <td>A</td>
      <td>A</td>
      <td>意大利</td>
      <td>55556</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
      <td>A</td>
      <td>A</td>
      <td>美国</td>
      <td>333</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
      <td>A</td>
      <td>A</td>
      <td>中国大陆</td>
      <td>6666</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2012</td>
      <td>美国</td>
      <td>泰坦尼克号</td>
      <td>157074</td>
      <td>剧情/爱情/灾难</td>
      <td>2012-04-10 00:00:00</td>
      <td>194</td>
      <td>9.4</td>
      <td>中国大陆</td>
      <td>A</td>
      <td>A</td>
      <td>美国</td>
      <td>444</td>
    </tr>
  </tbody>
</table>

</div>

由于两个数据集都存在产地，因此合并后会有两个产地信息



### （ 3 ）concat

将多个数据集进行批量合并


```python
df1 = df[:10]
df2 = df[100:110]
df3 = df[200:210]
dff = pd.concat([df1,df2,df3]) #还有参数axis，默认axis = 0（增加行），列拼接需要修改为1
dff
```



</style>

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
      <th>评分等级</th>
      <th>热门程度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2012</td>
      <td>美国</td>
      <td>泰坦尼克号</td>
      <td>157074</td>
      <td>剧情/爱情/灾难</td>
      <td>2012-04-10 00:00:00</td>
      <td>194</td>
      <td>9.4</td>
      <td>中国大陆</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1993</td>
      <td>美国</td>
      <td>辛德勒的名单</td>
      <td>306904</td>
      <td>剧情/历史/战争</td>
      <td>1993-11-30 00:00:00</td>
      <td>195</td>
      <td>9.4</td>
      <td>华盛顿首映</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1997</td>
      <td>日本</td>
      <td>新世纪福音战士剧场版：Air/真心为你 新世紀エヴァンゲリオン劇場版 Ai</td>
      <td>24355</td>
      <td>剧情/动作/科幻/动画/奇幻</td>
      <td>1997-07-19 00:00:00</td>
      <td>87</td>
      <td>9.4</td>
      <td>日本</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>8</th>
      <td>2013</td>
      <td>日本</td>
      <td>银魂完结篇：直到永远的万事屋 劇場版 銀魂 完結篇 万事屋よ</td>
      <td>21513</td>
      <td>剧情/动画</td>
      <td>2013-07-06 00:00:00</td>
      <td>110</td>
      <td>9.4</td>
      <td>日本</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1994</td>
      <td>法国</td>
      <td>这个杀手不太冷</td>
      <td>662552</td>
      <td>剧情/动作/犯罪</td>
      <td>1994-09-14 00:00:00</td>
      <td>133</td>
      <td>9.4</td>
      <td>法国</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>100</th>
      <td>1993</td>
      <td>韩国</td>
      <td>101</td>
      <td>146</td>
      <td>喜剧/爱情</td>
      <td>1993-06-19 00:00:00</td>
      <td>112</td>
      <td>7.4</td>
      <td>韩国</td>
      <td>B</td>
      <td>D</td>
    </tr>
    <tr>
      <th>101</th>
      <td>1995</td>
      <td>英国</td>
      <td>10</td>
      <td>186</td>
      <td>喜剧</td>
      <td>1995-01-25 00:00:00</td>
      <td>101</td>
      <td>7.4</td>
      <td>美国</td>
      <td>B</td>
      <td>D</td>
    </tr>
    <tr>
      <th>102</th>
      <td>2013</td>
      <td>韩国</td>
      <td>素媛</td>
      <td>114819</td>
      <td>剧情/家庭</td>
      <td>2013-10-02 00:00:00</td>
      <td>123</td>
      <td>9.1</td>
      <td>韩国</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>103</th>
      <td>2003</td>
      <td>美国</td>
      <td>101忠狗续集：伦敦</td>
      <td>924</td>
      <td>喜剧/动画/家庭</td>
      <td>2003-01-21 00:00:00</td>
      <td>70</td>
      <td>7.5</td>
      <td>美国</td>
      <td>B</td>
      <td>B</td>
    </tr>
    <tr>
      <th>104</th>
      <td>2000</td>
      <td>美国</td>
      <td>10</td>
      <td>9514</td>
      <td>喜剧/家庭</td>
      <td>2000-09-22 00:00:00</td>
      <td>100</td>
      <td>7.0</td>
      <td>美国</td>
      <td>C</td>
      <td>A</td>
    </tr>
    <tr>
      <th>105</th>
      <td>2013</td>
      <td>韩国</td>
      <td>10</td>
      <td>601</td>
      <td>剧情</td>
      <td>2014-04-24 00:00:00</td>
      <td>93</td>
      <td>7.2</td>
      <td>美国</td>
      <td>B</td>
      <td>C</td>
    </tr>
    <tr>
      <th>106</th>
      <td>2006</td>
      <td>美国</td>
      <td>10件或</td>
      <td>1770</td>
      <td>剧情/喜剧/爱情</td>
      <td>2006-12-01 00:00:00</td>
      <td>82</td>
      <td>7.7</td>
      <td>美国</td>
      <td>B</td>
      <td>B</td>
    </tr>
    <tr>
      <th>107</th>
      <td>2014</td>
      <td>美国</td>
      <td>10年</td>
      <td>1531</td>
      <td>喜剧/同性</td>
      <td>2015-06-02 00:00:00</td>
      <td>90</td>
      <td>6.9</td>
      <td>美国</td>
      <td>C</td>
      <td>B</td>
    </tr>
    <tr>
      <th>108</th>
      <td>2012</td>
      <td>日本</td>
      <td>11·25自决之日 三岛由纪夫与年轻人们 11・25自決の</td>
      <td>149</td>
      <td>剧情</td>
      <td>2012-06-02 00:00:00</td>
      <td>119</td>
      <td>5.6</td>
      <td>日本</td>
      <td>C</td>
      <td>D</td>
    </tr>
    <tr>
      <th>109</th>
      <td>1997</td>
      <td>美国</td>
      <td>泰坦尼克号</td>
      <td>535491</td>
      <td>剧情/爱情/灾难</td>
      <td>1998-04-03 00:00:00</td>
      <td>194</td>
      <td>9.1</td>
      <td>中国大陆</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>200</th>
      <td>2014</td>
      <td>日本</td>
      <td>最完美的离婚 2014特别篇</td>
      <td>18478</td>
      <td>剧情/喜剧/爱情</td>
      <td>2014-02-08 00:00:00</td>
      <td>120</td>
      <td>9.1</td>
      <td>日本</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>201</th>
      <td>2009</td>
      <td>日本</td>
      <td>2001夜物</td>
      <td>84</td>
      <td>剧情/动画</td>
      <td>2009-10-02 00:00:00</td>
      <td>80</td>
      <td>6.6</td>
      <td>美国</td>
      <td>C</td>
      <td>D</td>
    </tr>
    <tr>
      <th>202</th>
      <td>2009</td>
      <td>中国香港</td>
      <td>头七 頭</td>
      <td>7039</td>
      <td>恐怖</td>
      <td>2009-05-21 00:00:00</td>
      <td>60</td>
      <td>6.2</td>
      <td>美国</td>
      <td>C</td>
      <td>A</td>
    </tr>
    <tr>
      <th>203</th>
      <td>1896</td>
      <td>法国</td>
      <td>火车进站 L</td>
      <td>7001</td>
      <td>纪录片/短片</td>
      <td>1896-01-06</td>
      <td>60</td>
      <td>8.8</td>
      <td>法国</td>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>204</th>
      <td>2009</td>
      <td>美国</td>
      <td>银行舞蹈</td>
      <td>6944</td>
      <td>短片</td>
      <td>1905-07-01 00:00:00</td>
      <td>60</td>
      <td>7.8</td>
      <td>美国</td>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>205</th>
      <td>2003</td>
      <td>荷兰</td>
      <td>2003提雅</td>
      <td>48</td>
      <td>音乐</td>
      <td>2003-10-07 00:00:00</td>
      <td>200</td>
      <td>8.9</td>
      <td>美国</td>
      <td>B</td>
      <td>E</td>
    </tr>
    <tr>
      <th>206</th>
      <td>2012</td>
      <td>美国</td>
      <td>死亡飞车3：地狱烈</td>
      <td>6937</td>
      <td>动作</td>
      <td>2012-12-12 00:00:00</td>
      <td>60</td>
      <td>5.8</td>
      <td>美国</td>
      <td>C</td>
      <td>A</td>
    </tr>
    <tr>
      <th>207</th>
      <td>2012</td>
      <td>日本</td>
      <td>时光钟摆 振り</td>
      <td>6876</td>
      <td>剧情/动画/短片</td>
      <td>2012-03-20 00:00:00</td>
      <td>60</td>
      <td>8.7</td>
      <td>美国</td>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>208</th>
      <td>2011</td>
      <td>中国香港</td>
      <td>你还可爱么 你還可愛</td>
      <td>6805</td>
      <td>短片</td>
      <td>2011-04-22 00:00:00</td>
      <td>60</td>
      <td>8.3</td>
      <td>美国</td>
      <td>B</td>
      <td>A</td>
    </tr>
    <tr>
      <th>209</th>
      <td>2002</td>
      <td>中国香港</td>
      <td>一碌蔗</td>
      <td>6799</td>
      <td>剧情/喜剧/爱情</td>
      <td>2002-09-19 00:00:00</td>
      <td>60</td>
      <td>6.7</td>
      <td>美国</td>
      <td>C</td>
      <td>A</td>
    </tr>
  </tbody>
</table>

</div>





# Matplotlib可视化展示

## 1.Matplotlib基础 

**matplotlib**是一个Python的 2D 图形包。pyplot封装了很多画图的函数

导入Matplotlib包： （常常以`plt`作为``matplotlib.pyplot``的省略）

```python
import matplotlib.pyplot as plt
```

``matplotlib.pyplot``包含一系列类似**MATLAB**中绘图函数的相关函数。每个``matplotlib.pyplot``中的函数对当前的图像进行一些修改，例如：产生新的图像，在图像中产生新的绘图区域，在绘图区域中画线，给绘图加上标记，等等......``matplotlib.pyplot``会自动记住当前的图像和绘图区域，因此这些函数会直接作用在当前的图像上。



### plt.show()函数 

- 默认情况下，``matplotlib.pyplot``不会直接显示图像，只有调用``plt.show()``函数时，图像才会显示出来。（类比于print，不打印就不会显示出来）

- 在``ipython``命令行中，也可以不调用``plt.show()``，而是直接把图片插入到``notebook``中，也可以将图像显示出来。需要使用魔术命令——以百分号%开头：``%matplotlib notebook`` 或``%matplotlib inline``

- 但在实际写程序中，一般还是习惯调用``plt.show()``函数来把图像显示出来（类似print）



### plt.plot()函数 

``plt.plot()``函数：基本绘图函数，用来绘线型图。


#### 基本用法

``plot``函数基本的用法：

> y的值是必须要写的；x可以指定，也可以不指定。当没有指定写x时，会默认使用列表的索引（默认把列表的索引作为x值）

- 指定x和y（x和y都需要指定时：**先x后y**）：`plt.plot(x,y)`

- 不指定x：`plt.plot(y)`  

  【没有指定写x时，会默认使用列表的索引（默认把列表的索引作为x值）】

（x、y可以是列表/数组）



> 例子
>
> - 传入x和y：
>
>
>   ```python
>   plt.plot([1,2,3,4],[1,4,9,16])
>   plt.show() #相当于打印的功能，下面不会出现内存地址
>   ```
>
>   ![png](D:\网页下载文件\6\output_15_0.png)
>   ​
>
> - 只传入一个数组（只指定y，不指定x）：
>
>
>   ```python
>   plt.plot([1,2,3,4]) #默认以列表的索引作为x，输入的是y
>   # 其实[1，2，3，4]是在指定y，x会默认使用列表的索引，所以x的默认值是`[0,1,2,3]`
>   
>   # 给x轴、y轴设置名称：
>   plt.ylabel('y')
>   plt.xlabel("x轴") #有中文，因为前面也没有限定，所以展示时会出现乱码
>   
>   plt.show()
>   ```
>
>   
>
>
>   ![png](D:\网页下载文件\6\output_12_1.png)
>       





#### 字符参数

>  和**MATLAB**中类似，可以用字符来指定绘图的格式

表示颜色的字符参数有：

| 字符            | 颜色                         |
| :-------------- | :--------------------------- |
| ``'b'``（默认） | 蓝色，blue【注意：不是黑色】 |
| ``'g'``         | 绿色，green                  |
| ``'r'``         | 红色，red                    |
| ``'c'``         | 青色，cyan                   |
| ``'m'``         | 品红，magenta                |
| ``'y'``         | 黄色，yellow                 |
| ``'k'``         | 黑色，black【注意：k是黑色】 |
| ``'w'``         | 白色，white                  |



表示类型的字符参数有：

| 字符            | 类型       | 字符     | 类型      |
| :-------------- | :--------- | :------- | :-------- |
| ``'-'``（默认） | 实线       | ``'--'`` | 虚线      |
| ``'-'.``        | 虚点线     | ``':'``  | 点线      |
| ``'.'``         | 点         | ``','``  | 像素点    |
| ``'o'``         | 圆点       | ``'v'``  | 下三角点  |
| ``'^'``         | 上三角点   | ``'<'``  | 左三角点  |
| ``'>'``         | 右三角点   | ``'1'``  | 下三叉点  |
| ``'2'``         | 上三叉点   | ``'3'``  | 左三叉点  |
| ``'4'``         | 右三叉点   | ``'s'``  | 正方点    |
| ``'p'``         | 五角点     | ``'*'``  | 星形点    |
| ``'h'``         | 六边形点1  | ``'H'``  | 六边形点2 |
| ``'+'``         | 加号点     | ``'x'``  | 乘号点    |
| ``'D'``         | 实心菱形点 | ``'d'``  | 瘦菱形点  |
| ``'_'``         | 横线点     |          |           |






```python
# 例如画出红色圆点：
plt.plot([1,2,3,4],[1,4,9,16],"ro") #也可以是or，没顺序要求 # r——红色；o——原点  ——>>红色圆点
plt.show()
```


![png](D:\网页下载文件\6\output_18_0.png)
​    






#### 显示范围

可以使用``axis``函数指定坐标轴显示的范围：`plt.axis([xmin, xmax, ymin, ymax])`




```python
plt.plot([1,2,3,4],[1,4,9,16],"g*")# 绘制图像

# 在上图中有两个点在图像的边缘——可以改变轴的显示范围：
plt.axis([0,6,0,20])

plt.show()
```


​    
![png](D:\网页下载文件\6\output_22_0.png)
​    



#### 传入Numpy数组 

> 前面我们传给``plot``的参数都是列表，而向``plot``中传入``numpy``数组是更常用的做法。
>
> 事实上，如果传入的是列表，``matplotlib``会在内部将它转化成数组再进行处理。

传入的numpy数组会作为x、y的数据



#### 传入多组数据 

不需要使用多个``plot``函数来画多组数组，只需要可以将`(x,y,format_str)`这些组合放到一个``plot``函数中去即可。



---

例子：


```python
# 向``plot``函数传入数组，还传入了多组``(x,y,format_str)``参数，让它们在同一张图上显示：

t = np.arange(0.,5.,0.2)  #设置数组：左闭右开，从0到5但不包括5，步长为0.2
#在一个图里面画多条线：
plt.plot(t,t,"r--",      # 第一条线：x和y都是t数组，绘图格式为红色虚线
        t,t**2,"bs",     # 第二条线：x是t数组，y是t数组的平方，绘图格式为蓝色正方点
        t,t**3,"g^")     # 第一条线：x是t数组，y是t数组的立方，绘图格式为绿色三角形   # 传入`Numpy`数组 
#（分行是为了更清楚，也可以不分行）
plt.show()
```


![png](D:\网页下载文件\6\output_26_0.png)
​    

#### 修改线条属性的方式

总结：

1. ##### 用字符串

   - 样式：`plt.plot(x,y,format_str)`

   > ````python
   > # 例如画出红色圆点：
   > plt.plot([1,2,3,4],[1,4,9,16],"ro") #也可以是or，没顺序要求 # r——红色；o——原点  ——>>红色圆点
   > plt.show()
   > ````

2. ##### 在`plot()`函数中用关键字参数进行设置

   > 例如：
   >
   > 可以通过``linewidth``改变线条的宽度，通过``color``改变线条的颜色：（都是可以用也可以不用的）
   >
   >
   > ```python
   > x = np.linspace(-np.pi,np.pi)  # 设置x的范围：从-pi到pi
   > y = np.sin(x)  
   > plt.plot(x,y,linewidth = 4.0,color = 'r') #细节调整
   > plt.show()
   > ```
   >
   >
   > ![png](D:\网页下载文件\6\output_31_0.png)

3. ##### 使用plt.plot()的返回值来设置线条属性

   ``plot``函数返回一个``Line2D``对象组成的列表，每个对象代表输入的一对组合

   > 例如：
   >
   > * line1,line2 为两个 Line2D **对象**
   >
   > ```python
   > line1, line2 = plt.plot(x1, y1, x2, y2)#返回两个 Line2D 对象
   > #如果：
   > line = plt.plot(x1, y1, x2, y2) # 返回1个由2个Line2D对象组成的列表
   > 
   > #区别：做线条属性设置时，可以作用于Line2D对象，但不能对列表进行属性设置
   > ```
   >
   > * 返回3个 Line2D 对象组成的**列表**
   >
   > ```python
   > lines = plt.plot(x1, y1, x2, y2, x3, y3)
   > ```
   >
   > 
   >
   > 可以使用这个返回值来对线条属性进行设置：
   >
   >
   > ```python
   > line1,line2 = plt.plot(x,y,"r-",x,y+1,"g-")  #把两个Line2D对象分别赋值给line1和line2（因为line1和line2是Line2D对象，所以可以对它们进行格式的设定）.第一条线为line1，第二条线为line2
   > #对抗锯齿功能进行设定：
   > line1.set_antialiased(False)  #关闭抗锯齿设置（抗锯齿功能：让整个线条更加平滑）
   > plt.show()
   > ```
   >
   >
   > ![png](D:\网页下载文件\6\output_34_0.png)
   >     
   >
   > 
   >
   > ```python
   > line = plt.plot(x,y,"r-",x,y+1,"g-")
   > line[1].set_antialiased(False) #列表
   > plt.show()
   > ```
   >
   >
   > ![png](D:\网页下载文件\6\output_35_0.png)

4. ##### plt.setp() 修改线条性质(更方便的做法)

   > 使用``plt``的``setp``函数：
   >
   > `plt.setp(要进行处理的对象[,color=...][,linewidth=...][,...])`
   >
   > matlab风格：`plt.setp(要进行处理的对象[,color,...][,linewidth,...][,...,...])`
   >
   >
   > ```python
   > line = plt.plot(x,y)
   > #plt.setp(line, color = 'g',linewidth = 4)
   > plt.setp(line,"color",'r',"linewidth",4) #matlab风格
   > ```
   >
   > 
   >
   >
   >     [None, None]
   >
   > 
   >
   >
   > ![png](D:\网页下载文件\6\output_38_1.png)
   >
   > 



### plt.figure()函数

- 功能：创建图像函数。生成空白图像，并设置它的大小和纵横比

- 函数原型：

  ```python
  matplotlib.pyplot.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, clear=False, **kwargs)
  ```

- 常用参数：（该函数没有必须参数，所有参数都是可选的）

  - num：图形的唯一标识符。整数、字符串或Figure对象。默认值为None。图像编号或名称（数字为编号 ，字符串为名称）

    > ``figure()``函数会产生一个指定编号为``num``的图：
    >
    > ```python
    > plt.figure(num)
    > ```
    >
    > 这里，``figure(1)``其实是可以省略的，因为默认情况下``plt``会自动产生一幅图像。（当num是1的时候，可以省略）
    >
  
  - figsize : 指定figure的尺寸，即宽和高，单位为英寸。浮点数二元组。
  
    【饼图一般使用长和宽相同的尺寸（figsize），其他的图形不限定】
  
  - dpi : 指定绘图对象的分辨率，即每英寸多少个像素，缺省值为80
  
  - facecolor:背景颜色，默认='white'
  
  - edgecolor:图形边框颜色，默认='white'
  
  - frameon:是否显示边框。布尔值。默认值为`True`。

- 返回值为`Figure`对象



### plt.subplot()函数

- 功能：在一幅图中生成多个子图

- 函数常用样式：

  ```python
  plt.subplot(numrows, numcols, fignum)
  ```

- 函数常用参数说明：

  - numrows：行数

  - numcols：列数

  - fignum：指定是哪一张子图

- tips：当``numrows * numncols < 10``时（都是各位数），各个参数中间的逗号可以省略

  >  例如：``plt.subplot(211)``就相当于``plt.subplot(2,1,1)``。
  >
  > 意思是：生成2行1列，2*1=2（两幅子图），后面的“1”指定是第1张子图




```python
def f(t):
    return np.exp(-t)*np.cos(2*np.pi*t)  #返回(e的-t次方)*cos(2*t*pi)

t1 = np.arange(0.0,5.0,0.1)  #从0.0到5.0但不包含5.0,步长为0.1
t2 = np.arange(0.0,4.0,0.02)

plt.figure(figsize = (10,6))  #figsize指定图形的尺寸
#绘制第一张子图：
plt.subplot(211)  
plt.plot(t1,f(t1),"bo",t2,f(t2),'k') #子图1上有两条线
#绘制第二张子图：
plt.subplot(212)  
plt.plot(t2,np.cos(2*np.pi*t2),"r--")

plt.show() #显示图像
```

![png](D:\网页下载文件\6\output_41_0.png)
​    




## 2.绘图

可以对电影数据进行可视化分析


```python
# 导入第三方库：
import warnings  
warnings.filterwarnings("ignore")  #关闭“可能出现但对数据分析并无影响的一些警告”这个功能

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```



设置字体：`plt.rcParams["font.sans-serif"]=要设置的字体名称` （设置字体为"SimHei"显示中文，可以解决中文乱码问题）

设置正常显示符号：`plt.rcParams["axes.unicode_minus"]=False` （默认是使用Unicode符号）


```python
plt.rcParams["font.sans-serif"] = "SimHei" # 用来设置字体样式以正常显示中文标签（解决中文字符乱码的问题）
plt.rcParams["axes.unicode_minus"] = False #设置正常显示字符，如正常显示负号，解决负号的乱码问题
```


```python
df = pd.read_excel(r"D:\学习\python数据分析课程\python三剑客数据分析课程资料\作业5\movie_data3.xlsx", index_col = 0) #读入数据
```


```python
df[:5]
```

<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>年代</th>
      <th>产地</th>
      <th>名字</th>
      <th>投票人数</th>
      <th>类型</th>
      <th>上映时间</th>
      <th>时长</th>
      <th>评分</th>
      <th>首映地点</th>
      <th>评分等级</th>
      <th>热门程度</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1994</td>
      <td>美国</td>
      <td>肖申克的救赎</td>
      <td>692795</td>
      <td>剧情/犯罪</td>
      <td>1994-09-10 00:00:00</td>
      <td>142</td>
      <td>9.6</td>
      <td>多伦多电影节</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1957</td>
      <td>美国</td>
      <td>控方证人</td>
      <td>42995</td>
      <td>剧情/悬疑/犯罪</td>
      <td>1957-12-17 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>美国</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1997</td>
      <td>意大利</td>
      <td>美丽人生</td>
      <td>327855</td>
      <td>剧情/喜剧/爱情</td>
      <td>1997-12-20 00:00:00</td>
      <td>116</td>
      <td>9.5</td>
      <td>意大利</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1994</td>
      <td>美国</td>
      <td>阿甘正传</td>
      <td>580897</td>
      <td>剧情/爱情</td>
      <td>1994-06-23 00:00:00</td>
      <td>142</td>
      <td>9.4</td>
      <td>洛杉矶首映</td>
      <td>A</td>
      <td>A</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1993</td>
      <td>中国大陆</td>
      <td>霸王别姬</td>
      <td>478523</td>
      <td>剧情/爱情/同性</td>
      <td>1993-01-01 00:00:00</td>
      <td>171</td>
      <td>9.4</td>
      <td>香港</td>
      <td>A</td>
      <td>A</td>
    </tr>
  </tbody>
</table>

</div>



### 1)柱状图

绘制柱状图：`matplotlib.pyplot.bar(x, height, width=0.8, bottom=None, *, align='center', data=None, **kwargs)`

> 参数说明：
>
> - x：浮点型数组，柱子在x轴上的坐标。可以为字符串数组（横轴）
>
> - height(即y)：浮点型数组，柱形图的高度，即y轴上的坐标（纵轴）
>
> - width：浮点型数组，柱形图的宽度，默认值为0.8
>
> - bottom：浮点型数组，底座的 y 坐标（柱子的基准高度），默认值为 0
>
> - align：柱形图与 x 坐标的对齐方式。字符串，取值范围为{'center', 'edge'}，默认为'center'。
>
>   - 'center' 以 x 位置为中心，是默认值。 
>
>   - 'edge'：将柱形图的左边缘与 x 位置对齐。
>
>     [ 如果想让x位于柱子右侧，需要同时设置负的width 以及align='edge ]
>
> - **kwargs：其他参数。
>
> > 柱子的位置由x以及align确定 ，柱子的尺寸由height和 width 确定。垂直基准位置由bottom确定(默认值为0)。大部分参数即可以是单独的浮点值也可以是值序列，单独值对所有柱子生效，值序列一一对应每个柱子。



```python
#绘制每个国家或地区的电影数量的柱状图

data = df["产地"].value_counts() # data为Series类型的数据(index为产地(国家),对应的value为这个产地在这一列出现的次数)

x = data.index 
y = data.values

#生成空白图像
plt.figure(figsize = (10,6)) #设置figure的尺寸

#绘制柱状图：
plt.bar(x,y,color = "g") #表格给的数据是怎样就怎样，不会自动排序

#设置标题
plt.title("各国家或地区电影数量", fontsize = 20) #fontsize参数设置字体大小

#对横纵轴进行说明：
plt.xlabel("国家或地区",fontsize = 18) #设定x轴名称
plt.ylabel("电影数量") #设定y轴名称

#设定坐标轴上字体的大小:
plt.tick_params(labelsize = 14)

#让x轴的标签旋转90度
plt.xticks(rotation = 90) 

for a,b in zip(x,y): #数字直接显示在柱子上（添加文本）
    plt.text(a,b+10,b,ha = "center",va = "bottom",fontsize = 10) 
    #a:x的位置；b:y的位置，加上10是为了把数字展示的位置提高一点点，使它不与柱子重合，
    #第二个b:显示的文本的内容,ha,va:格式设定,center居中,top&bottom在上或者在下,fontsize:字体大小指定

#plt.grid() #还可以画网格线
plt.show()
```




​    
![png](D:\网页下载文件\6\output_52_0.png)
​    



设置标题: plt.title

对横纵轴进行说明：plt.xlabel    plt.ylabel

设定坐标轴上字体: plt.tick_params

让x轴的标签旋转90度   plt.xticks(rotation = 90) 

绘制网格线：`plt.grid()`



plt.text()函数用于设置文字说明(在图像上增加文本注释)
`plt.text(x,y,string,fontsize=15,verticalalignment="top",horizontalalignment="right")`

参数：

x,y: 表示坐标值上的值

string:表示说明文字（要显示在图像上的文本的内容）

fontsize:设置字体大小

verticalalignment（va）：垂直对齐方式 ，（ ‘center’ | ‘top’ | ‘bottom’ | ‘baseline’ ）

horizontalalignment（ha）：水平对齐方式 ，（‘center’ 居中、  ‘right’  右对齐 、 ‘left’ 左对齐）





### 2)曲线图/折线图

> 曲线图又称折线图，是利用曲线的升，降变化来表示被研究现象发展趋势的一种图形。它在分析研究社会经济现象的发展变化、依存关系等方面具有重要作用。
>
> 绘制曲线图时，如果是某一现象的时间指标，应将时间绘在坐标的横轴上，指标绘在坐标的纵轴上。如果是两个现象依存关系的显示，可以将表示原因的指标绘在横轴上，表示结果的指标绘在纵轴上，同时还应注意整个图形的长宽比例。


```python
#绘制每年上映的电影数量的曲线图

#取1888-2015年的数据 
data = df["年代"].value_counts()
data = data.sort_index()[:-2] #排除掉2016年以后的数据，共两条

x = data.index
y = data.values

plt.plot(x,y,color = 'b') #绘图
plt.title("每年电影数量",fontsize = 20)
plt.ylabel("电影数量",fontsize = 18)
plt.xlabel("年份",fontsize = 18)

# 让数字直接显示在曲线上（添加文本）：
for (a,b) in zip(x[::10],y[::10]): #每隔10年进行数量标记，防止过于密集
    plt.text(a,b+10,b,ha = "center", va = "bottom", fontsize = 10)
   
#标注极值点：
plt.annotate("2012年达到最大值", xy = (2012,data[2012]), xytext = (2025,2100), arrowprops = dict(facecolor = "black",edgecolor = "red"))
#xy设置箭头尖的坐标，xytext注释内容起始位置，arrowprops对箭头设置，传字典，facecolor填充颜色，edgecolor边框颜色

#纯文本注释内容，例如注释增长最快的地方：
plt.text(1980,1000,"电影数量开始快速增长")

plt.show()
```




![png](D:\网页下载文件\6\output_57_0.png)
    


对于这幅图形，我们使用``xlabel, ylabel, title, text``方法设置了文字，其中：

* ``xlabel``: x轴标注
* ``ylabel``: y轴标注
* ``title``: 图形标题
* ``text``: 在指定位置放入文字

输入特殊符号支持使用``Tex``语法，用``$<some Text code>$``隔开。

除了使用``text``在指定位置标上文字之外，还可以使用``annotate``进行注释，``annotate``主要有两个参数：

* ``xy``: 注释位置
* ``xytext``: 注释文字位置



标记特殊点（如极值点）：plt.annotate(要注释的内容，xy=箭头尖的坐标，xytext=注释内容显示的起始位置坐标，arrowprops=用字典传入来对箭头进行设置)



当数据较多时，可以设置一定的步长来防止过于密集





### 3)饼图 

> 饼图常用于统计学模块。2D饼图为圆形，手画时，常用圆规作图。适用于类别较少的数据。仅排列在工作表的一列或一行中的数据可以绘制到饼图中。饼图只显示一个数据系列中各项的大小与各项总和的比例。饼图中的数据点显示为整个饼图的百分比。



绘制饼图：

```python
matplotlib.pyplot.pie(x, explode=None, labels=None, colors=None, autopct=None, pctdistance=0.6, shadow=False, labeldistance=1.1, startangle=0, radius=1, counterclock=True, wedgeprops=None, textprops=None, center=0, 0, frame=False, rotatelabels=False, *, normalize=None, data=None)[source]
```

> - 参数说明：
>
>   **x**：浮点型数组，表示每个扇形的面积。
>
>   **explode**：数组，表示各个扇形之间的间隔，默认值为0。
>
>   **labels**：列表，各个扇形的标签，默认值为 None。
>
>   colors：数组，表示各个扇形的颜色，默认值为 None。
>
>   **autopct**：设置饼图内各个扇形百分比显示格式。（**%d%%** 整数百分比，**%0.1f** 一位小数， **%0.1f%%** 一位小数百分比， **%0.2f%%** 两位小数百分比。）
>
>   **labeldistance**：标签标记的绘制位置，相对于半径的比例，默认值为 1.1（默认在饼图的外侧），如 **<1**则绘制在饼图内侧。
>
>   pctdistance：：类似于 labeldistance，指定 autopct 的位置刻度，默认值为 0.6。
>
>   **shadow：**：布尔值 True 或 False，设置饼图的阴影，默认为 False，不设置阴影。
>
>   radius：：设置饼图的半径，默认为 1。
>
>   **startangle：**：起始绘制饼图的角度，默认为从 x 轴正方向逆时针画起，如设定 =90 则从 y 轴正方向画起。
>
>   counterclock：布尔值，设置指针方向，默认为 True，即逆时针，False 为顺时针。
>
>   wedgeprops ：字典类型，默认值 None。参数字典传递给 wedge 对象用来画一个饼图。例如：wedgeprops={'linewidth':5} 设置 wedge 线宽为5。
>
>   textprops ：字典类型，默认值为：None。传递给 text 对象的字典参数，用于设置标签（labels）和比例文字的格式。
>
>   center ：浮点类型的列表，默认值：(0,0)。用于设置图标中心位置。
>
>   frame ：布尔类型，默认值：False。如果是 True，绘制带有表的轴框架。
>
>   rotatelabels ：布尔类型，默认为 False。如果为 True，旋转每个 label 到指定的角度。
>
> - **返回值：**  
>   如果没有设置autopct，返回(patches,texts)  
>   如果设置autopct，返回(patches,texts,autotexts)




```python
#根据电影的长度绘制饼图

data = pd.cut(df["时长"], [0,60,90,110,1000]).value_counts() #数据离散化
data
```


    (90, 110]      13201
    (0, 60]         9884
    (60, 90]        7661
    (110, 1000]     7417
    Name: 时长, dtype: int64




```python
y = data.values
y = y/sum(y) #归一化(即使不进行，系统也会自动进行)  # 得到百分比

plt.figure(figsize = (7,7)) #饼图一般使用长和宽相同的尺寸，其他的图形不限定
plt.title("电影时长占比",fontsize = 15)
patches,l_text,p_text = plt.pie(y, labels = data.index, autopct = "%.1f %%", colors = "bygr", startangle = 90)  #'%.1f'：格式化操作—— 一位小数百分比

for i in p_text: #通过返回值设置饼图内部字体
    i.set_size(15)
    i.set_color('w')

for i in l_text: #通过返回值设置饼图外部字体
    i.set_size(15)
    i.set_color('r')
    
plt.legend() #显示图例
plt.show()
```


​    
![png](D:\网页下载文件\6\output_63_0.png)
​    







显示图例： plt.legend() 



### 4)频率直方图 

> 直方图(Histogram)又称质量分布图。是一种统计报告图。由一系列高度不等的纵向条纹或线段表示数据分布的情况。一般用横轴表示数据类型，纵轴表示分布情况。
>
> 直方图是数值数据分布的精确图形表示。这是一个连续变量（定量变量）的概率分布的估计，并且被卡尔·皮尔逊(Karl Pearson)首先引入。它是一种条形图。为了构建直方图，第一步是将值的范围分段，即将整个值的范围分成一系列间隔，然后计算每个间隔中有多少值。这些值通常被指定为连续的，不重叠的变量间隔。间隔必须相邻，并且通常是（但不是必须的）相等的大小。
>
> 直方图也可以被归一化以显示“相对频率”。然后，它显示了属于几个类别中每个案例的比例，其高度等于1。
>



绘制直方图：

`plt.hist(arr[,bins=10][, normed=None][, histtype='bar'][,...])`

> - （hist的参数非常多，但常用的就这六个，且只有第一个是必须的）:
>
>   **arr**: 需要计算直方图的**一维**数组  (必须的)
>
>   bins: 直方图的柱数，即要分的组数，可选项，默认为10
>
>   normed: 是否将得到的直方图向量归一化(True/False)。默认为0
>
>   facecolor: 直方图颜色
>
>   edgecolor: 直方图边框的颜色
>
>   alpha: 透明度（0到1之间）
>
>   histtype: 直方图类型，取值范围是{‘bar’, ‘barstacked’, ‘step’, ‘stepfilled’}，默认`histtype='bar'`。'bar’是传统的条形直方图；'barstacked’是堆叠的条形直方图；'step’是未填充的条形直方图，只有外边框；‘stepfilled’是有填充的直方图；当histtype取值为’step’或’stepfilled’，rwidth设置失效，即不能指定柱子之间的间隔，默认连接在一起
>
> - 返回值（用参数接收返回值，便于设置数据标签）：
>   n：直方图向量，即每个分组下的统计值，是否归一化由参数normed设定。当normed取默认值时，n即为直方图各组内元素的数量（各组频数）
>   bins: 各个bin的区间范围
>   patches：每个bin里面包含的数据，是一个list。




```python
# 根据电影的评分绘制频率直方图

plt.figure(figsize = (10,6))
plt.hist(df["评分"], bins = 20, edgecolor = 'k',alpha = 0.5)
plt.show()
```

![png](D:\网页下载文件\6\output_66_0.png)
​    

>  从上图可以发现，电影的评分是服从一个右偏的正态分布的。





### 5)双轴图

>  双轴图包含的信息可以比直方图更大

双轴图  (twin：孪生，双胞胎)：

- `twinx() `：添加 y 坐标轴

- `twiny() `：添加 x 坐标轴

```python
# eg:
ax2 = ax1.twinx() # 将ax1的x轴也分配给ax2使用（用同一个x轴，双y轴）
```

---

计算正态分布密度函数的具体命令：`norm.pdf(bins,mu,sigma)  `  [mu:均值；sigma：标准差]

tips：使用该函数前要先获取：`from scipy.stats import norm`




```python
#获取正态分布密度函数：
from scipy.stats import norm 

fig = plt.figure(figsize = (10,8))  # 生成空白图像，并设置它的大小和纵横比
ax1 = fig.add_subplot(111) #画一个一行一列的第一个也是唯一一个子图
n,bins,patches = ax1.hist(df["评分"],bins = 100, color = 'm') #hist绘制直方图，有三个返回值   #(bins默认是10)

#设置横纵坐标和标题：
ax1.set_ylabel("电影数量",fontsize = 15)
ax1.set_xlabel("评分",fontsize = 15)
ax1.set_title("频率分布图",fontsize = 20)

#准备拟合
# 计算一个均值为评分的均值、方差是评分的方差的正态分布在区间的概率密度：
y = norm.pdf(bins,df["评分"].mean(),df["评分"].std()) # 在这里bins是直接用直方图hist函数操作后返回的bins

ax2 = ax1.twinx() #双轴 
ax2.plot(bins,y,"b--") #绘图
ax2.set_ylabel("概率分布",fontsize = 15)

plt.show()
```


![png](D:/学习/笔记/7/output_9_0.png)
​    



### 6)散点图 

> 用两组数据构成多个坐标点，看坐标点的分布，判断两变量之间是否存在某种关联或总结坐标点的分布模式。散点图将序列显示为一组点。值由点在图表中的位置表示。类别由图表中的不同标记表示。散点图通常用于比较跨类别的聚合数据。

#### 绘图

绘制散点图基本格式：`matplotlib.pyplot.scatter(x, y)`  ，即：`plt.scatter(x,y)`

函数原型：

```python
matplotlib.pyplot.scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, vmin=None, vmax=None, alpha=None, linewidths=None, *, edgecolors=None, plotnonfinite=False, data=None, **kwargs)
```

> 常用参数说明：
>
> x，y：长度相同的数组，也就是我们即将绘制散点图的数据点，输入数据。一个用于 x 轴的值，另一个用于 y 轴上的值。
>
> c：点的颜色，默认蓝色 'b'，也可以是个 RGB 或 RGBA 二维行数组。
>
> marker：点的样式，默认小圆圈 'o'
>
> alpha：：透明度设置，0-1 之间，默认 None，即不透明

----




```python
# 根据电影时长和电影评分绘制散点图 

x = df["时长"][::100]
y = df["评分"][::100] 
#由于数据量过大，所以画出来的图非常冗杂。所以可以选取原来数据的部分数据（原有数据的百分之一）来解决数据冗杂的问题

plt.figure(figsize = (10,6)) #生成空白图像
plt.scatter(x,y,color = 'c',marker = 'p',label = "评分") # 绘制散点图  （marker = 'p'：形状设置为五角）
plt.legend() #展示图例
#设置标题和横纵坐标：
plt.title("电影时长与评分散点图",fontsize = 20)
plt.xlabel("时长",fontsize = 18)
plt.ylabel("评分",fontsize = 18)
plt.show()
```


![png](D:/学习/笔记/7/output_12_0.png)
​    








#### marker属性

设置散点的形状

| **marker** | **description** | **描述**  |
| ---------- | --------------- | --------- |
| "."        | point           | 点        |
| ","        | pixel           | 像素      |
| "o"        | circle          | 圈        |
| "v"        | triangle_down   | 倒三角形  |
| "^"        | triangle_up     | 正三角形  |
| "<"        | triangle_left   | 左三角形  |
| ">"        | triangle_right  | 右三角形  |
| "1"        | tri_down        | tri_down  |
| "2"        | tri_up          | tri_up    |
| "3"        | tri_left        | tri_left  |
| "4"        | tri_right       | tri_right |
| "8"        | octagon         | 八角形    |
| "s"        | square          | 正方形    |
| "p"        | pentagon        | 五角      |
| "\*"       | star            | 星星      |
| "h"        | hexagon1        | 六角1     |
| "H"        | hexagon2        | 六角2     |
| "+"        | plus            | 加号      |
| "x"        | x               | x号       |
| "D"        | diamond         | 钻石      |
| "d"        | thin_diamon     | 细钻      |
| "\|"       | vline           | v线       |
| "\_"       | hline           | H线       |



### 7)箱型图

> 箱型图：主要能让我们直观地观测到数据集中的一些异常值，然后我们也可以判断数据集的数据离散程度和它的偏向。
>
> 箱型图（Box-plot）又称为盒须图，盒式图或箱型图，是一种用作显示一组数据分散情况资料的统计图，形如箱子。在各种领域中也经常被使用，常见于品质管理。它主要用于反映原始数据分布的特征，还可以进行多组数据分布特征的比较。
>
> 箱线图的绘制方法是：先找出一组数据的中位数，两个四分位数，上下边缘线；然后，连接两个四分位数画出箱子；再将上下边缘线与箱子相连接，中位数在箱子中间。
>
> > **一般计算过程**
> >
> > （ 1 ）计算上四分位数（ Q3 ），中位数，下四分位数（ Q1 ）
> >
> > （ 2 ）计算上四分位数和下四分位数之间的差值，即四分位数差（IQR, interquartile range）Q3-Q1
> >
> > （ 3 ）绘制箱线图的上下范围，上限为上四分位数，下限为下四分位数。在箱子内部中位数的位置绘制横线
> >
> > （ 4 ）大于上四分位数1.5倍四分位数差的值，或者小于下四分位数1.5倍四分位数差的值，划为异常值（outliers）
> >
> > （ 5 ）异常值之外，最靠近上边缘和下边缘的两个值处，画横线，作为箱线图的触须
> >
> > （ 6 ）极端异常值，即超出四分位数差3倍距离的异常值，用实心点表示；较为温和的异常值，即处于1.5倍-3倍四分位数差之间的异常值，用空心点表示
> >
> > （ 7 ）为箱线图添加名称，数轴等



![img](https://bkimg.cdn.bcebos.com/pic/0b55b319ebc4b74596c1a432cdfc1e178a8215b8?x-bce-process=image/watermark,image_d2F0ZXIvYmFpa2U4MA==,g_7,xp_5,yp_5)



绘制箱型图函数原型：

```python
plt.boxplot(x,notch=None,sym=None,vert=None,
    whis=None,positions=None,widths=None,
    patch_artist=None,meanline=None,showmeans=None,
    showcaps=None,showbox=None,showfliers=None,
    boxprops=None,labels=None,flierprops=None,
    medianprops=None,meanprops=None,
    capprops=None,whiskerprops=None,)
```

> 参数详解：
>
> **x**: 指定要绘制箱线图的数据；
>
> notch: 是否是凹口的形式展现箱线图，默认非凹口；
>
> **sym**: 指定异常点的形状，默认为+号显示；
>
> vert: 是否需要将箱线图垂直摆放，默认垂直摆放；
>
> **whis**: 指定上下须与上下四分位的距离，默认为为1.5倍的四分位差；（控制异常值和正常值的范围）
>
> positions: 指定箱线图的位置，默认为[0,1,2...]；
>
> widths: 指定箱线图的宽度，默认为0.5；
>
> patch_artist: 是否填充箱体的颜色（设为“=True”后就可以对箱体的颜色进行修改了，就可以用boxprops来设置箱体的颜色了）
>
> meanline:是否用线的形式表示均值，默认用点来表示；
>
> showmeans: 是否显示均值，默认不显示；
>
> showcaps: 是否显示箱线图顶端和末端的两条线，默认显示；
>
> showbox: 是否显示箱线图的箱体，默认显示；
>
> showfliers: 是否显示异常值，默认显示；
>
> boxprops: 设置箱体的属性，如边框色，填充色等；
>
> **labels**: 为箱线图添加标签，类似于图例的作用；
>
> filerprops: 设置异常值的属性，如异常点的形状、大小、填充色等；
>
> medainprops: 设置中位数的属性，如线的类型、粗细等
>
> meanprops: 设置均值的属性，如点的大小，颜色等；
>
> capprops: 设置箱线图顶端和末端线条的属性，如颜色、粗细等；
>
> whiskerprops: 设置须的属性，如颜色、粗细、线的类型等

----

#### 一组数据箱型图


```python
# 绘制美国电影评分的箱线图 

data = df[df.产地 == "美国"]["评分"]  #条件筛选，准备美国电影评分的数据

plt.figure(figsize = (10,6)) 

#绘制箱型图：
plt.boxplot(data,whis = 2,flierprops = {"marker":'o',"markerfacecolor":"r","color":'k'}
           ,patch_artist = True, boxprops = {"color":'k',"facecolor":"#66ccff"})
#用color设置外框颜色，facecolor设定填充颜色

plt.title("美国电影评分",fontsize = 20)# 设置标题
plt.show()
```


​    
![png](D:/学习/笔记/7/output_22_0.png)
​    


#### 多组数据箱型图 


```python
# 绘制各个地区的评分箱型图

data1 = df[df.产地 == "中国大陆"]["评分"]
data2 = df[df.产地 == "日本"]["评分"]
data3 = df[df.产地 == "中国香港"]["评分"]
data4 = df[df.产地 == "英国"]["评分"]
data5 = df[df.产地 == "法国"]["评分"]

plt.figure(figsize = (12,8))

#绘制箱型图：
plt.boxplot([data1,data2,data3,data4,data5],labels = ["中国大陆","日本","中国香港","英国","法国"],
           whis = 2,flierprops = {"marker":'o',"markerfacecolor":"r","color":'k'}
           ,patch_artist = True, boxprops = {"color":'k',"facecolor":"#66ccff"},
           vert = False)    #多组数据时，可通过labels来指定每一个箱线图的标签，一一对应
# 通过vert属性可以把图旋转过来.不设置时箱线图是竖着展示的，设置了 vert=False 之后，箱线图就会横着展示

ax = plt.gca() #获取当前的坐标系  
ax.patch.set_facecolor("gray") #设置坐标系背景颜色
ax.patch.set_alpha(0.3) #设置背景透明度

plt.title("电影评分箱线图",fontsize = 20) 
plt.show()
```

![png](D:/学习/笔记/7/output_24_0.png)
​    



ax = plt.gca() #获取当前的坐标系  #gca：get current axes 
ax.patch.set_facecolor("gray") #设置坐标系背景颜色
ax.patch.set_alpha(0.3) #设置背景透明度



通过vert属性可以把图旋转过来

不设置时箱线图是竖着展示的，设置了`vert=False`之后，箱线图就会横着展示



### 8)相关系数矩阵图/热力图

#### 用pandas本身封装的画图函数 

pandas本身也封装着画图函数

- 基本样式：`pd.plotting.scatter_matrix(要绘制相关系数矩阵图的dataframe)`

- 函数原型：

  ```python
  pandas.plotting.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwargs)
  ```

- 函数功能：画一个散点图矩阵

- 参数说明：

  frame : DataFrame

  alpha : 浮点型, 可选择，设置透明度

  figsize : (浮点型,浮点型), 可选择，以英寸为单位的元组(宽、高)，设置图像大小

  ax : Matplotlib轴对象，可选

  grid : 布尔型，可选，将其设置为True将显示网格

  diagonal :设置对角线上的图形，取值范围： {‘hist’, ‘kde’}

  - diagonal = hist:对角线上显示的是数据集各个特征的直方图
  - diagonal = kde:对角线上显示的是数据集各个特征的核密度估计

  marker : 字符串，可选，Matplotlib标记类型，默认是'.'

  hist_kwds : 其他标绘关键字参数，传递给hist函数

  density_kwds :其他标绘关键字参数，传递给核密度估计标绘

  range_padding : 浮点型，可选x和y轴范围相对于(x_max - x_min)或(y_max - y_min)的相对扩展，默认为0.05

  **kwargs : 其他标绘关键字参数，要传递到散点函数

- 返回：numpy.ndarray（一个矩阵的散点图。）

----




```python
# 画出各个属性之间的散点图，对角线是分布图 

%pylab inline 
#要在前面加上魔术命令，让图像直接展示在notebook里面[因为我们现在所使用的并不是matplotlib里面的pyplot，没有办法通过plt.show()的命令来让图像展示在jupyter notebook里面]

data = df[["投票人数","评分","时长"]]
result = pd.plotting.scatter_matrix(data[::100],diagonal = "kde",color = 'k',alpha = 0.3,figsize = (10,10)) 
#抽取data中的一部分数据（原有数据的百分之一）来进行散点图的绘制（解决数据冗杂的问题）
#diagonal设置对角线上的图形：只能在hist和kde中作出一个选择
```




![png](D:/学习/笔记/7/output_30_1.png)
    



#### 用matplotlib

- 绘制前先导入seaborn库

  > seaborn是一个精简的python库，可以创建具有统计意义的图表，能理解pandas的DataFrame类型。

- 热力图绘制函数：sns.heatmap()

- 函数原型：

  ```python
  seaborn.heatmap(data, vmin=None, vmax=None, cmap=None, center=None, robust=False, annot=None, fmt='.2g', 
  annot_kws=None,linewidths=0, linecolor='white', cbar=True, cbar_kws=None, cbar_ax=None, square=False, 
  xticklabels='auto', yticklabels='auto',mask=None, ax=None, **kwargs) 
  ```

- 参数详解:

  1. 热力图输入数据参数：对哪一个数据进行热力图的绘制，就把哪一个数据写到里面去
     - data:矩阵数据集，可以是numpy的数组（array），也可以是pandas的DataFrame。可以强制转换为ndarray格式数据的2维数据集。如果是DataFrame，则DataFrame的index和column信息会分别对应到heatmap的columns(列)和rows(行)，即pt.index是热力图的行标，pt.columns是热力图的列标。那么如果提供了关系矩阵就可以显示变量之间的相关性。
  2. 热力图矩阵块颜色参数：
     - vmax,vmin:分别是热力图的颜色取值最大和最小范围，默认是根据data数据表里的取值确定。（浮点型数据，可选参数）
     - cmap:从数字到色彩空间的映射，取值是matplotlib包里的colormap名称或颜色对象，或者表示颜色的列表（可选参数）。 如果没有提供，默认值将取决于是否设置了“center”
     - center:浮点数，可选参数。绘制有色数据时将色彩映射居中的值。 如果没有指定，则使用此参数将更改默认的`cmap`。
     - robust:默认取值False，如果是False，且没设定vmin和vmax的值。
  3. 热力图矩阵块注释参数：
     - annot(annotate的缩写):  布尔值或者矩形数据，可选参数。设置热力图矩阵块上是否要有注释参数。默认取值False；如果是True，在热力图每个方格写入数据；如果是矩阵，在热力图每个方格写入该矩阵对应位置数据。如果数组的形状与data相同，则使用它来代替原始数据注释热力图。
     - fmt:字符串格式代码，矩阵上标识数字的数据格式，比如保留小数点后几位数字。
     - annot_kws:（可以通过字典数据来进行具体的设置，通过字典数据来传入）默认取值False；如果是True，就可以设置热力图矩阵上数字的大小颜色字体粗细，matplotlib包text类下的字体设置
  4. 热力图矩阵块之间间隔及间隔线参数：
     - linewidth:定义热力图里“表示两两特征关系的矩阵小块”之间的间隔大小
     - linecolor:切分热力图上每个矩阵小块的线的颜色，默认值是"white"
  5. 热力图颜色刻度条参数：
     - cbar:是否在热力图侧边绘制颜色进度条，默认值是True
     - cbar_kws:热力图侧边绘制颜色刻度条时，相关字体设置，默认值是None
     - cbar_ax：热力图侧边绘制颜色刻度条时，刻度条位置设置，默认值是None
  6. 其他：
     - square:设置热力图矩阵小块形状，默认值是False
     - xticklabels,yticklabels:xticklabels控制每列标签名的输出；yticklabels控制每行标签名的输出。默认值是auto。如果是True，则以DataFrame的列名作为标签名。如果是False，则不添加行标签名。如果是列表，则标签名改为列表中给的内容。如果是整数K，则在图上每隔K个标签进行一次标注。

- 返回值类型：热力图对象

----




```python
# 画电影时长，投票人数，评分的一个相关系数矩阵图

import seaborn as sns  # 导入seaborn库

data = df[["投票人数","评分","时长"]]
corr = data.corr() # 获取相关系数   # 先通过pandas中corr()方法获得关系矩阵
corr = abs(corr) # 取绝对值（因为只是想考虑相关性，不需要是正相关还是负相关）

fig = plt.figure(figsize = (10,8))
ax = fig.add_subplot(111) # 定义一个也是唯一的一个子图

ax = sns.heatmap(corr,vmax = 1,vmin = 0,annot = True,annot_kws = {"size":13,"weight":"bold"},linewidths = 0.05)#热力图绘制 
#annot=True 设置热力图矩阵块上可以有注释参数
#annot_kws:（可以通过字典数据来进行具体的设置，通过字典数据来传入）size设置字体大小，weight设置字体的粗细
#linewidths：设置热力图矩阵块之间的间隔大小

plt.xticks(fontsize = 15)  #设置x轴的字体
plt.yticks(fontsize = 15)  #设置y轴的字体

plt.show()
```


​    
![png](D:/学习/笔记/7/output_33_0.png)
​    





## 3.一些琐碎的点知识点总结

### 3.1导入的一些其他的第三方库/函数

#### 关闭警告

```python
import warnings  
warnings.filterwarnings("ignore")  #关闭“可能出现但对数据分析并无影响的一些警告”这个功能
```

#### 获取正态分布密度函数

计算正态分布密度函数的具体命令：`norm.pdf(bins,mu,sigma)  `  [mu:均值；sigma：标准差]

tips：使用该函数前要先获取：`from scipy.stats import norm`

#### 热力图绘制

- 用pandas库

- 用seaborn + matplotlib



### 3.2一些基本功能用法

#### 解决乱码问题

设置字体：`plt.rcParams["font.sans-serif"]=要设置的字体名称` （设置字体为"SimHei"显示中文，可以解决中文乱码问题）

设置正常显示符号：`plt.rcParams["axes.unicode_minus"]=False` （默认是使用Unicode符号）



#### 设置标注

tips：设置的标注如果要显示中文/符号，则还要加上其他具体的命令来限定，不然会显示乱码。

---

##### 对横纵轴设置说明

- 设置横轴：`plt.xlabel(xlabel, fontdict=None, labelpad=None)`
- 设置纵轴：`plt.ylabel(ylabel, fontdict=None, labelpad=None)`

> 参数：
> xlabel、ylabel: 标签名称(必须参数)
> fontdict:标签字体样式
> labelpad:设置标签和轴之间的间距



##### 设置标题文字

- 函数：`plt.title(str, fontdict=None, loc=’center’, pad=None, **kwargs)`

- 参数：

  - str：标题文本【必须参数】

  - fontdict：此参数使用<u>字典</u>控制文本的外观，例如文本大小，文本对齐方式等。

    > 默认：fontdict = {‘fontsize’：rcParams [‘axes.titlesize’]，‘fontweight’：rcParams [‘axes.titleweight’]，‘verticalalignment’：‘baseline’，‘horizontalalignment’：loc}

  - loc：标题的位置，采用字符串值（‘center’ 居中、  ‘right’  右对齐 、 ‘left’ 左对齐）

  - pad：标题距轴顶部的偏移量(以磅为单位)。其默认值为“无”。

  - *\*kwargs:此参数是指使用其他关键字参数作为文本属性，例如`color`，`fonstyle`，`linespacing`，`backgroundcolor`，`rotation`等等



##### 在图像上增加文本注释

> 用 plt.text()函数 可在指定位置放入文字

- 函数常用样式：`plt.text(x,y,string,fontsize=15,verticalalignment="top",horizontalalignment="right")`

- 参数：（还有很多其他的参数）

  x,y: 设置放置文本的位置。(x,y)为防止文本的坐标

  string: 说明文字（要显示在图像上的文本内容）

  fontsize : 设置字体大小

  verticalalignment（va）：垂直对齐方式 ，（ ‘center’ | ‘top’ | ‘bottom’ | ‘baseline’ ）

  horizontalalignment（ha）：水平对齐方式 ，（‘center’ 居中、  ‘right’  右对齐 、 ‘left’ 左对齐）



##### 用箭头标记特殊点（如极值点）

常用格式：

`plt.annotate(要注释的内容，xy=箭头尖的坐标，xytext=注释内容显示的起始位置坐标，arrowprops=用字典传入来对箭头进行设置)`



#### 其他设置

- 可以使用``axis``函数指定坐标轴显示的范围：`plt.axis([xmin, xmax, ymin, ymax])`

- x = np.linspace(-np.pi,np.pi)  # 设置x的范围：从-pi到pi

- 设定坐标轴上字体: plt.tick_params

- 让x轴的标签旋转90度   plt.xticks(rotation = 90) 

- 绘制网格线：`plt.grid()`

- 显示图例： plt.legend() 

- 当原来数据量过大时，可以用过步长来选取原来数据的部分数据，防止过于密集，从而解决数据冗杂的问题

- ax = plt.gca() #获取当前的坐标系  #gca：get current axes 
  ax.patch.set_facecolor("gray") #设置坐标系背景颜色
  ax.patch.set_alpha(0.3) #设置背景透明度

- 通过vert属性可以把图旋转过来

  不设置时箱线图是竖着展示的，设置了`vert=False`之后，箱线图就会横着展示







