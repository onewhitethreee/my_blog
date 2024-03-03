# C++实现日期基本类，重载运算符，友元..【第一篇】

最近刚好写完了关于c++的日期类实现。特地来分享给大家

话不多说，直接上示例

首先我要实现三个构造函数，一个拷贝函数和另外一个析构函数来构成最基本的日期类。在此之前我需要在我的类中声明private变量。
## 声明private变量
`int dia //表示天数`
`int mes // 表示月份`, 
`int anyo // 表示年份`
和`char *mensaje // 表示一个字符串数组`
## 声明默认函数
它们分别是
`TCalendario(); // 默认构造函数，用来初始话日期为1/1/1900和mensaje为nullptr`

`TCalendario(int dia, int mes, int anyo, const char *mens); // 用来初始化日期为参数`

`TCalendario(const TCalendario &); // 深拷贝`

`~TCalendario(); //析构函数，用来释放内存`

哦对了，类名为Tcalendario，相信聪明的你一定已经看出来了。

## 声明重载运算符

`TCalendario &operator=(const TCalendario &); // 赋值运算符重载`

`TCalendario operator+(const int); // +号运算符重载`

`TCalendario operator-(const int); // -号运算符重载`
`TCalendario operator++(int); //后置++运算符重载`

`TCalendario &operator++(); // 前置++运算符重载`

`TCalendario operator--(int); // 后置--运算符重载`
`TCalendario &operator--(); // 前置--运算符重载`

`bool operator==(const TCalendario &) const; // 等号运算符重载`

`bool operator!=(const TCalendario &) const; //不等于号运算符重载`

`bool operator>(const TCalendario &) const; // 大于号运算符重载`

`bool operator<(const TCalendario &) const; //小于号运算符重载`

## 一些其他函数的实现

`bool ModFecha(int dia, int mes, int anyo); // 用来修改日期，True为修改成功，False为修改失败`

`bool EsVacio() const; // 用来判断当前对象是否具有初始化的值`

`int Dia() const; // 返回对象的当前天数`

`int Mes() const;// 返回对象的当前月份`

`int Anyo() const;// 返回对象的当前年份`

`char *Mensaje() const // 返回对象的当前数组字符`


另外我们可以再加两个函数来判断**日期是否正确**OR**闰年**
`int get_month_day(int month, int year) const;`

`bool check_days_correct(int day, int month, int year) const;`

---

目前为止，我们已经声明了所有需要的函数，现在要对它们一一进行实现。声明函数放在.h文件中，实现函数放在.cpp文件中。

---


## 实现默认构造析构函数

######  默认构造函数
`TCalendario::TCalendario() : dia(1), mes(1), anyo(1900), mensaje(nullptr) {} // 使用初始化列表来进行初始化`

###### 默认构造参数函数
```
TCalendario::TCalendario(int dia, int mes, int anyo, const char *mens) 
{
    if (check_days_correct(dia, mes, anyo)) // 首先需要判断日期是否正确，如为True，进行初始化
    {
        this->dia = dia;
        this->mes = mes;
        this->anyo = anyo;
        if (mens != nullptr) // 此处需要注意，我们正在使用一个指针来对char进行操作，需要先进行判断，然后动态分配char所需要的内存大小
        {
            // dynamic alloc memory to char
            size_t t_strlen = strlen(mens);
            this->mensaje = new char[t_strlen + 1];
            memset(this->mensaje, 0, t_strlen);
            strcpy(this->mensaje, mens);
        }
        else
        {
            this->mensaje = nullptr;
        }
    }

    else
    {
        // 日期错误，初始化为默认值
        this->dia = 1;
        this->mes = 1;
        this->anyo = 1900;
        this->mensaje = nullptr;
    }
}

```

##### 日期判断函数

这一部分相信大家都看得懂就不打注释了

```
bool TCalendario::check_days_correct(int day, int month, int year) const
{
    int dia_ = get_month_day(month, year);
    if (day > dia_ || month > 12 || year < 1900 || day < 1 || month < 1)
    {
        return false;
    }
    else
    {
        return true;
    }
}
int TCalendario::get_month_day(int month, int year) const
{
    static int day[] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) // check if year is bisiestor
    {
        if (month == 2)
        {
            return 29;
        }
    }
    return day[month];
}
```
##### 析构函数(释放内存)

```
TCalendario::~TCalendario()
{
    // 在这里进行释放内存操作，重新将变量设置为默认
    this->anyo = 1900;
    this->mes = 1;
    this->dia = 1;
    if (mensaje != nullptr) // 此处需要特别注意，如果不加上这个空指针判断会造成释放空指针错误，从而导致程序崩溃。因为是一个ptr，所以要用delete[]
    {
        delete[] mensaje;
        mensaje = nullptr;
    }
    else
    {
        mensaje = nullptr;
    }
}
```

##### 深拷贝

这里没有什么好说的，需要注意的是深拷贝带有const关键字。其他的都上默认构造参数函数一样

```
TCalendario::TCalendario(const TCalendario &t)
{
    if (check_days_correct(t.dia, t.mes, t.anyo))
    {
        // deep copy all value
        // cout << "deep copy" << endl;
        this->dia = t.dia;
        this->mes = t.mes;
        this->anyo = t.anyo;
        // // deep copy char
        if (t.mensaje != nullptr)
        {
            size_t t_strlen = strlen(t.mensaje);
            this->mensaje = new char[t_strlen + 1];
            memset(this->mensaje, 0, t_strlen);
            strcpy(this->mensaje, t.mensaje);
        }
        else
        {
            this->mensaje = nullptr;
        }
    }
    else
    {
        this->dia = 1;
        this->mes = 1;
        this->anyo = 1900;
        this->mensaje = nullptr;
    }
}

```
## 实现重载运算符

###### = 重载
```
TCalendario &TCalendario::operator=(const TCalendario &t)
{

    if (this == &t)
    {
        /* 如果出现当对象1赋值给对象1的情况下直接返回对象1，无需继续进行后续操作因为为同一个对象*/
        return *this;
    }
    /*在进行赋值前，需要对左值进行内存释放，不然会造成segmentation fault。在这里使用了析构函数来进行释放*/
    (*this).~TCalendario();

    /*下面的没什么可以讲的，都是一样的步骤，赋值，分配内存，然后结束*/
    if (check_days_correct(t.dia, t.mes, t.anyo))
    {
        this->dia = t.dia;
        this->mes = t.mes;
        this->anyo = t.anyo;
        // // deep copy char
        if (t.mensaje != nullptr)
        {
            size_t t_strlen = strlen(t.mensaje);
            this->mensaje = new char[t_strlen + 1];
            memset(this->mensaje, 0, t_strlen);
            strcpy(this->mensaje, t.mensaje);
        }
        else
        {
            this->mensaje = nullptr;
        }
    }
    else
    {
        this->dia = 1;
        this->mes = 1;
        this->anyo = 1900;
        this->mensaje = nullptr;
    }
    return *this;
}
```

##### + 重载

这里需要特别注意，这里没有使用引用进行返回，而是创建了一个临时对象

```
TCalendario TCalendario::operator+(const int value)
{
    // 创建临时对象
    TCalendario temp(*this);
    if (value < 0) // 当传入的参数小于0无需进行任何操作
    {
        return temp;
    }
    // 这里进行了+操作，首先对临时对象的dia变量进行了相加，然后进入一个while循环。后面就是进行加月份或者年份操作当当前日期超出的时候
    temp.dia += value;
    while (temp.dia > get_month_day(temp.mes, temp.anyo))
    {
        temp.dia -= get_month_day(temp.mes, temp.anyo);
        ++temp.mes;
        if (temp.mes > 12)
        {
            temp.mes = 1;
            ++temp.anyo;
        }
    }
    return temp;
}
```
##### - 重载

和上面的+一样，不过逻辑需要变动一下，直接看代码吧

```
TCalendario TCalendario::operator-(const int value)
{
    TCalendario temp(*this);
    if (value < 0)
    {
        return temp;
    }
    temp.dia -= value;
    while (temp.dia <= 0)
    {
        --temp.mes;
        if (temp.anyo <= 1900) // when data is inferior than 1900 reinicialice to init value and break loop
        {
            temp.~TCalendario();
            break;
        }
        if (temp.mes == 0)
        {
            temp.mes = 12;
            --temp.anyo;
        }
        temp.dia += get_month_day(temp.mes, temp.anyo);
    }
    return temp;
}

```

##### ++ 后置重载

和上方的一样，不过这里是后置++，有一个占位符int来表示后置
```
TCalendario TCalendario::operator++(int)
{
    TCalendario temp = *this;

    ++dia;
    while (dia > get_month_day(mes, anyo))
    {
        dia -= get_month_day(mes, anyo);
        ++mes;
        if (mes > 12)
        {
            mes = 1;
            ++anyo;
        }
    }

    return temp;
}
```

##### ++ 前置重载

此处开始变了，返回的不再是临时对象而是引用。逻辑还是一样的，只不过返回对象变了
```

TCalendario &TCalendario::operator++()
{
    ++this->dia;
    while (this->dia > get_month_day(this->mes, this->anyo))
    {
        this->dia -= get_month_day(this->mes, this->anyo);
        ++this->mes;
        if (this->mes > 12)
        {
            this->mes = 1;
            ++this->anyo;
        }
    }
    return *this;
}
```
##### -- 后置重载

返回临时对象。当超出初始范围时重新赋值。其他逻辑不变

```
TCalendario TCalendario::operator--(int)
{
    if (this->dia == 1 && this->mes == 1 && this->anyo == 1900)
    {
        this->~TCalendario();
        return *this;
    }

    TCalendario temp(*this);
    --dia;
    while (dia <= 0)
    {
        --mes;
        if (anyo <= 1900) // when data is inferior than 1900 reinicialice to init value and break loop
        {
            this->~TCalendario();
            break;
        }
        if (mes == 0)
        {
            mes = 12;
            --anyo;
        }
        dia += get_month_day(mes, anyo);
    }
    return temp;
}
```
##### -- 前置重载

返回引用，逻辑不变

```
TCalendario &TCalendario::operator--()
{
    if (this->dia == 1 && this->mes == 1 && this->anyo == 1900)
    {
        this->~TCalendario();
        return *this;
    }

    --this->dia;
    while (this->dia <= 0)
    {
        --this->mes;
        if (this->anyo <= 1900) // when data is inferior than 1900 reinicialice to init value and break loop
        {
            this->~TCalendario();
            break;
        }
        if (this->mes == 0)
        {
            this->mes = 12;
            --this->anyo;
        }
        this->dia += get_month_day(this->mes, this->anyo);
    }
    return *this;
}
```

##### == 重载

返回为布尔值。此函数功能为用来比较两个对象是否是同一个值。

在这里有一个坑，当时写的时候花了有些时间才发现。

当对象中的mensaje为nullptr的时候，我一开始用的是strcmp来比较两个是否相等。那么大家肯定知道，我一个空指针和一个字符比较那么肯定会报错。所以这里我使用了一个string对象来初始化一个空的字符串然后去进行compare函数比较，这样子就没有什么问题了
```
bool TCalendario::operator==(const TCalendario &t) const
{
    string this_mensaje;
    string t_mensaje;
    if(this->mensaje == nullptr)
    {
        this_mensaje = "";
    }
    else
    {
        this_mensaje = this->mensaje;
    }

    if(t.mensaje == nullptr)
    {
        t_mensaje = "";
    }
    else
    {
        t_mensaje = t.mensaje;
    }
    return ((this->dia == t.dia) && (this->mes == t.mes) && (this->anyo == t.anyo) && (this_mensaje.compare(t_mensaje) == 0));
}
```

##### != 重载

和==一样，不过是相反的条件
```
bool TCalendario::operator!=(const TCalendario &t) const
{
    string this_mensaje;
    string t_mensaje;
    if(this->mensaje == nullptr)
    {
        this_mensaje = "";
    }
    else
    {
        this_mensaje = this->mensaje;
    }

    if(t.mensaje == nullptr)
    {
        t_mensaje = "";
    }
    else
    {
        t_mensaje = t.mensaje;
    }
    
    return ((this->dia != t.dia) || (this->mes != t.mes) || (this->anyo != t.anyo) || (this_mensaje.compare(this_mensaje) != 0));

}
```

##### > 重载
此处有两个条件来判断对象1是否大于对象2
    1. 日期大于
    2. 日期等于但是mensaje大于
```
bool TCalendario::operator>(const TCalendario &t) const
{
    // (Criterio 1) : la fecha de T1 es posterior a la de T2(independientemente del mensaje).
    // (Criterio 2) : la fecha de T1 es igual a la de T2, y el mensaje de T1 es mayor(en comparación de cadenas) al mensaje de T2.Si la fecha de T1 es igual a la de T2 y el mensaje de T1 e igual al de T2, entonces tanto operator> como operator<devuelven FALSE.
    string this_mensaje;
    string t_mensaje;
    if(this->mensaje == nullptr)
    {
        this_mensaje = "";
    }
    else if(t.mensaje == nullptr)
    {
        t_mensaje = "";
    }
    else
    {
        this_mensaje = this->mensaje;
        t_mensaje = t.mensaje;
    }
    bool crt_1 = (this->anyo > t.anyo) || (this->anyo == t.anyo && this->mes > t.mes) || (this->anyo == t.anyo && this->mes == t.mes && this->dia > t.dia);

    // crt_2 have more priority than crt_1
    bool crt_2 = ((this->anyo == t.anyo && this->mes == t.mes && this->dia == t.dia) && this_mensaje.compare(t_mensaje) > 0);

    return crt_1 || crt_2;
    
}
```

##### < 重载
相同的逻辑不同的条件
```
bool TCalendario::operator<(const TCalendario &t) const
{
    string this_mensaje;
    string t_mensaje;
    if (this->mensaje == nullptr)
    {
        this_mensaje = "";
    }
    else if (t.mensaje == nullptr)
    {
        t_mensaje = "";
    }
    else
    {
        this_mensaje = this->mensaje;
        t_mensaje = t.mensaje;
    }
    bool crt_1 = (this->anyo < t.anyo) || (this->anyo == t.anyo && this->mes < t.mes) || (this->anyo == t.anyo && this->mes == t.mes && this->dia < t.dia);

    // crt_2 have more priority than crt_1
    bool crt_2 = ((this->anyo == t.anyo && this->mes == t.mes && this->dia == t.dia) && this_mensaje.compare(t_mensaje) < 0);

    return crt_1 || crt_2;
}
```

那么到这里已经全部实现了个别运算符重载和默认函数的实现。接下来实现一些其他函数or方法也可以这么说

## 其他函数

##### 修改日期

返回True 修改成功。反之失败
```
bool TCalendario::ModFecha(int dia, int mes, int anyo)
{
    /*Check de Numero de días correcto, número de mes correct y Control de años bisiestos*/

    if (dia > 31 || dia < 1 || mes < 1 || mes > 12 || anyo < 1900)
    {
        return false;
    }

    int dia_ = get_month_day(mes, anyo);
    if (dia <= dia_)
    {
        this->dia = dia;
        this->mes = mes;
        this->anyo = anyo;
        return true;
    }
    return false;
}
```

##### 修改mensaje

返回True 修改成功。反之失败
```
bool TCalendario::ModMensaje(const char *c)
{
    /*mensaje is null we need to allocated memory to it*/
    if (c == nullptr)
    {
        this->mensaje = nullptr;
        return true;
    }

    if (this->mensaje == nullptr)
    {
        // alloc new memory
        size_t t_strlen = strlen(c);
        this->mensaje = new char[t_strlen + 1];
        memset(this->mensaje, 0, t_strlen);
        strcpy(this->mensaje, c);
        return true;
    }
    /*delete old char memory and alloc new memory*/
    else
    {
        delete[] this->mensaje;
        size_t t_strlen = strlen(c);
        this->mensaje = new char[t_strlen + 1];
        memset(this->mensaje, 0, t_strlen);
        strcpy(this->mensaje, c);
        return true;
    }
    /*unusual condicional return*/
    return false;
}
```
##### 判断当前对象日期是否为默认值

根据声明的函数来实现。很简单的逻辑

```
bool TCalendario::EsVacio() const 
{
    /* devuelve TRUE si el calendario tiene fecha 1/1/1900 y el mensaje es NULL */
    if ((this->anyo == 1900 && this->dia == 1 && this->mes == 1) && (this->mensaje == nullptr))
    {
        return true;
    }
    return false;
}
```

接下来是几个返回天数，月份，年份，信息的函数

##### 天数
```
int TCalendario::Dia() const
{
    return this->dia;
}
```
##### 月份
```
int TCalendario::Mes() const
{
    return this->mes;
}
```
##### 年份
```
int TCalendario::Anyo() const
{
    return this->anyo;
}
```
##### 信息
唯一需要注意的就是这个了，不好好判断会有空指针错误。然后程序就崩了
```
char *TCalendario::Mensaje() const
{
    
    if (this->mensaje == nullptr)
    {
        return nullptr;
    }
    else
    {
        return this->mensaje;
    }
}

```

## 友元 【<<重载】
终于到最后了，友元还是蛮简单的实现方法，和cout输出一样，只是它换位另外一种输出方式了。

##### 声明
一般我放在类的最上方，要求为public，不能为private
```
friend std::ostream &operator<<(std::ostream &, const TCalendario &);

```

##### 实现
跟cout差不多，不过要带两个参数，一个为输出流对象，另外一个为const对象。内部实现就是进行了一些格式化的输出，没什么可以讲的
```
ostream &operator<<(ostream &cout, const TCalendario &t)
{
    if (t.dia < 10)
    {
        cout << "0";
    }
    cout << t.dia << "/";
    if (t.mes < 10)
    {
        cout << "0";
    }
    cout << t.mes << "/" << t.anyo << " ";

    if (t.mensaje == nullptr)
    {
        cout << "\"\"";
    }
    else
    {
        cout << "\""<< t.mensaje << "\"";
    }

    return cout;
}
```

## 结束

到这里第一部分就写完了，这个作业在写的过程中还是花费了一些时间的。不过好在最后还是完成了。难度为c++初学者中等。

后面我将实现日期类的Vector类，自己手搓一个仿vector的方法出来，实现了resize()。

那么大家下次再见！

github 仓库: https://github.com/onewhitethreee/PED-P1。内有完整的实现和声明和测试.cpp文件