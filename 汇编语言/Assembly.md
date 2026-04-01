# 概
所有汇编指令运算都需区分**源操作数**和**目的操作数**，也可能是直接的操作数
Windows中靠近指令的第一个字段是目的操作数，第二个是源操作数。而Linux中则是相反的。
两个字段不能同时为寄存器，目的操作数不能是立即数

## CPU模型
中央处理单元**C**entral **P**rocessing **U**nit,核心部件
原型为**差分机**和**分析机**
进程向CPU中的指令寄存器发送指令，指令计数器向进程返回指令地址
**控制单元**向存储单元与运算单元发出**控制指**令，**存储单元**和**运算单元**之间互相交换数据。存储单元向数据段返回操作数地址，同时交换数据。

**时序产生器**：CPU会按一定的脉冲频率工作，操作控制器利用定时脉冲的顺序和间隔有条理和节奏的指挥、规定机器在脉冲到来时的工作，给计算机各部分提供工作所需的时间标志。为此，**需要采用多级时序体制**。

**指令译码器**：将指令按二进制编码转变为一个具体的电路开关通断动作的过程。

**缓冲寄存器**：为了解决CPU和内存之间的速度差而设置。

CPU的指令一般由操作数和操作数地址构成，所以**寻址**贯穿了整个汇编语言，运算所需要的数据都是从不同地址的内存或者存储单元中来。
## 寄存器

寄存器最初并不属于CPU，从8086开始才融入CPU中。由于64之争Intel输给AMD，所以64位和32位CPU寄存器差异巨大。

**数据寄存器**和**地址寄存器**属于**通用寄存器**
数据寄存器：累加器、基址寄存器、计数寄存器、数据寄存器。
地址寄存器：堆栈指针、基址指针、源变址寄存器、目的址寄存器

控制寄存器：指令指针、标志寄存器
段寄存器：代码段寄存器、数据段寄存器、堆栈段寄存器、附加段寄存器

x64CPU的寄存器中变化巨大，甚至有充当GPU功能的寄存器组（视/音频）
另外一种CPU架构为ARM，x64的通用寄存器不足，ARM更多。ARM减少了读写内存的次数，散热又更加优秀，所以整体上都更加优秀
64位和32位汇编有所**差距**，传统的x86传递参数通过**栈**来进行传递，而栈在内存，所以需要多次读取。ARM有16个寄存器，让4个参数以下的函数无需栈直接使用寄存器进行传递，这种函数也是大多数常见的函数。

寄存器与内存之间也有速度差，所以涉及到**现代计算机系统**的另一个创新：指令流水线。
使译码器在连续的指令过程中仅消耗一次取值和执行时间，第一条指令开始执行时，第二条指令进入译码环节。配合上多级缓存，内存的读写速度和CPU寄存器的读写速度就得到了缓和。

EIP(Extended Instruction Pointer)指令指针寄存器：指向CPU正在执行的**下一条指令的内存地址**，在64位架构中变成了RIP；只存在于CPU中，**不能直接修改**，通过**异常处理机制**可以实现修改EIP；VT技术**虚拟化的EIP寄存器可以被直接修改**
标志寄存器：
- CF  Carry Flag（进位标志）
- ZF  Zero Flag（零标志）
- SF  Sign Flag（符号标志）
- OF  Overflow Flag（溢出标志）
- PF  Parity Flag（偶校验标志）
- DF  Direction Flag（方向标志）
- AF  Auxiliary Carry Flag（辅助进位标志）
EFLAGS：由32个标志位组成，其中包含上面7个常见标志位
- IF  Interrupt Flag（中断标志）1关中断
- TF  Trap Flag（陷阱标志）1时CPU进入单步调试
- DF  Direction Flag（方向标志）控制字符串操作方向，1高到低
- NT  Nested Task Flag（嵌套任务标志）控制任务切换链（多任务）
- RF  Resume Flag（恢复标志）控制调试异常后的回复行为
- AC  Alignment Check Flag（对齐检查标志）1时检查内存访问对齐
- ID  Identification Flag（标识标志）表示CPU支持CPUID指令

逆向重要级：ZF>SF>CF>OF>PF
## 内存模型
内存的工作模型是为了帮助软件开发人员理解内存的运行机制，进而解决软件运行过程中遇到的各种实际问题。
理论上最好的内存就是CPU的缓存，读写速度快，速率高。但是cache结构复杂、成本高昂、容量小。无法大规模应用。
当前CPU的算法可以令缓存命中率达到90%，意味着大部分情况下都不需要去访问内存。

内存的工作方式主要分为存取两种。计算机中的晶震部件会产生周期性的方波，通过修改这个电波可以在不同部件之间传输数据，频率越高，单位时间内速率越快。
实际工作的时候，内存频率会受到主板限制，会主动降频祛适配主板

## 指令
mov        传输数据
push        压入栈
pop         弹出栈中数据到目的位置
xchg        exchange      交换操作数
lea           Load effective address     取地址

### 数学运算
add  加  add eax,ebx
sub  减
mul  无符号乘  mul ecx   ECX:EAX，高32位在 `ECX`，低32位在 `EAX`
imul  有符号乘  imul eax,ecx
div   无符号除法  div ecx  ECX:EAX，高32位在 `ECX`，低32位在 `EAX`，运算完毕商存储在EAX，余数在ECX。需要保证ECX清零，否则结果可能出错
idiv  有符号除法  idiv ecx
inc   自增  inc eax
dec  自减 dec eax
cdq  **用在有符号除法之前，用于拓展符号位**

### 位操作
有符号填符号位，无符号填0
and eax, ebx与
or eax, ebx或
xor eax, ebx异或
not eax非
shl eax, n无符号左移n位
shr eax, n无符号右移n位
sal eax, n左移n位
sar eax, n右移n位
rol eax, n循环左移n位
ror eax, n循环右移n位

### 逻辑比较
用于对比操作数或设置标志
cmp eax, ebx  比较两个操作数
test eax, eax    测试，与操作，不存结果，仅设置标志
cmp(compare)会将两个操作数进行减法运算，不存结果，更新标志器ZF、CF等，常用于设置与条件跳转指令，和JE、JNE、JG、JL等配合使用，以决定程序执行流程。
CMP一般影响CF/ZF/SF/OF/PF/AF六个标志位
TEST用于按位与，不存结果，只更新标志器，可用来检查某些位是否被设置。

### 控制转移指令
***JCC指令，x86条件跳转指令的统称，CC指条件码***
jmp 0x001   无条件跳转
call  0x001   调用子程序
ret                返回调用点
je/jz  0x001  条件(ZF)相等跳转
jne/jnz 0x001  条件(ZF)不等跳转
jg  0x001   如果大于跳转
jl  0x001    如果小于跳转
jge 0x001   如果大于等于跳转
jle  0x001   如果小于等于跳转
loop  0x001      循环跳转
int  0x001         调用中断
iret  0x001        从中断返回

### 栈操作指令
push eax   压入栈
pop eax     弹出栈
pushad      按顺序将EAX、ECX、EDX、EBX、ESP、EBP、ESI、EDI的值压入栈
popad        按顺序从栈中弹出值恢复到寄存器EDI、ESI、EBP、ESP、EBX、EDX、ECX、EAX
pushfd       将32位标志寄存器（EFLAGS压入栈）
popfd         从栈中弹出值到32为标志寄存器EFLAGS
call [address]       调用子程序，将当前指令的返回地址压入至栈顶再跳转到目标地址
ret     从栈中弹出返回地址并跳转
**enter**       设置栈帧，将当前EBP压入栈，然后设置新的EBP并为局部变量分配空间
**leave**        恢复栈帧，将EBP的值恢复到ESP，然后弹出原EBP
int imm8    软中断，将标志寄存器、代码段CS和指令指针EIP压入栈，然后跳转到中断向量表中的处理程序地址
iret 中断返回，从栈中弹出标志寄存器、代码段CS、指令指针EIP，恢复中断前状态

### 字符串操作
00 一般代表字符串结尾
mov eax, offset str_hello   加载hello字符串的地址到eax
mov [edi], eax    把这个地址存入edi指向的位置
rep movsb  批量复制字符串数据，rep重复，movsb一次复制一个字节(move string byte)，因此也有movsw, movsd，movsq（四字quad word，8字节）
```
mov ecx, length    设置要复制的字节数
mov esi, source    源字符串地址
mov edi, destination   目标字符串地址
rep movsb   批量复制字符串
```
rep可以是有条件的，例如repe/repz 等价，当ZF为1且ECX不为0时，重复执行字符串操作指令
repne/repnz，ZF为0且ECX不为0时，重复执行字符串操作指令
例如repe cmpsb，反复对比直到**不**相等
scas 扫描字符串中特定的字符，扫描方向有DF(Direction flag)决定，cld清除DF，默认从低地址扫描，std设置DF从高地址扫描，**用于实现字符查找**
stos    向目标地址填充数据
lodsb   加载一个字节到AL，并将ESI自增1
lodsw  加载一个字到AL，并将ESI自增2
lodsd   加载双字到AL，并将ESI自增4

### 浮点运算
FPU是硬件模块，x87是它的指令集
SSE是独立于FPU的SIMD指令集
	使用独立的xmm寄存器，不依赖FPU，也不与x87共享堆栈资源

#### 指令
FLD  浮点加载指令Floating-Point Load
	FLD指令会将单精度浮点数转换为**80位扩展精度格式**（内部格式），所以会造成数据视图不相等
FST/FSTP 浮点存储指令，将浮点堆栈顶部st0的值存到指定位置(原来的值不变)；FSTP会**弹出**堆栈顶部的值并将堆栈**指针向下移动**

#### FPU(Floating Point Unit, 浮点运算单元)
FPU是处理器中的一个硬件模块，专门用于浮点运算
处理浮点数的加减乘除、平方根、三角函数等复杂操作
	在早期x86处理器中，FPU是一个独立的协处理器（如Intel 8087） 
	从80486开始，FPU集成进了CPU内核中
**8个80位宽的浮点寄存器ST(0~7)，以堆栈形式组织**
通过PUSH和POP模式操作寄存器
状态寄存器：用于保存堆栈状态（如深度）和计算标志（C0~C3）
控制寄存器：配置FPU的工作模式（如精度、舍入模式等）

#### x87指令集
定义：x87是专门为FPU设计的一套指令集，早期专用于处理浮点运算
特点：
	操作对象是FPU的堆栈寄存器st(0~7)
	指令风格通常是Fxxx开头，例如 加载浮点数FLD、浮点加法FADD
	**支持扩展精度**（80位），比SSE的单精度和双精度浮点数更高
代表指令：
- FLD/FST：加载/存储浮点数
- FADD/FSUB：浮点加法/减法
- FMUL/FDIV：浮点乘法/除法
- FCOM/FUCOM：比较浮点数
适用于高精度的计算（如科学计算）
需要80位扩展精度支持的场景

#### SSE(Streaming SIMD Extensions)
Intel在x86处理器上引入的一套SIMD（单指令多数据）**扩展指令集**
**采用xmm寄存器**（128位宽）
支持并行处理多个单精度或双精度浮点数
**指令风格是xxxPS（处理单精度矢量）或xxxSD（处理双精度标量）**
浮点运算更快（无需堆栈操作）
并行处理多个浮点数，提高性能
并行计算
性能要求较高但不需要扩展精度的场景

## 函数
代码逻辑的最小单元，封装可复用的代码；便于程序的模块化、流程化、分层嵌套
call xxx  函数入口，跳转到指定地址
	在**中断状态**下可使用F7或F8进行步入或布过操作
	在非中断状态下使用回车键进入call查看代码，-号键退出

### 栈结构
基址指针寄存器EBP（Extended Base Pointer） 和 栈指针寄存器ESP（Extended Stack Pointer）
call上方的push一般都作为call的参数使用，在call调用时
压入上一个函数的返回地址
push ebp压入上一个函数的栈帧
mov esp，ebp **将上一个函数的栈帧作为当前函数的栈基地址**
**返回地址 = 上一个函数“执行到哪儿”**  
**旧 ebp = 上一个函数“栈帧在哪儿”**

### 函数调用约定
在x86架构中，不同的调用约定(Calling Convention)决定了**函数参数如何传递、栈如何管理以及局部变量如何分配**
*就是call之间的差异，什么类型的call，不同call架构不同*
需观察：
	是否由寄存器传参
	参数压栈方向
	栈清理由谁来做
	this指针
	系统调用特征：寄存器传参+int 0x80 或 sysenter -> syscall
	
---

1. cdec1  (C调用，C Declaration)- **Windows 下都是外平栈**
	- **参数传递**：参数**从右到左**以此压栈
	- **栈清理**：由调用者（Caller）清理栈 add esp, X
	- **返回值**：eax寄存器
	- **常见场景**：C语言默认约定，可变参数函数（例printf）
	- **堆栈平衡**：由于平衡操作在call外，因此称作外平栈
```
	反编译为
	push 1
	push 2
	push 3
	call func_name
	add esp, 0xC   三个参数3*4字节=12
```

2. stdcall  (标准调用约定，Standard Call) - **Windows 下都是内平栈**
	- **参数传递**：参数**从右到左**压栈
	- **栈清理**：由被调用者（Callee）清理栈（retn X）
	- **返回值**：eax寄存器
	- **常见场景**：Windows API（如MessageBoxA）
	- **堆栈平衡**：在Call内，通过`retn 参数大小`进行清理栈

3. fastcall - **Windows 下都是内平栈**
	- **参数传递**：前两个参数通过寄存器（ecx和edx），其余参数**从右到左**压栈
	- **栈清理**：由被调用者callee清理栈，类似stdcall
	- **返回值**：eax寄存器
	- **常见场景**：性能敏感的函数
```
反编译为
	mov ecx,1
	mov edx,2
	push 3
	call func_name
		...
		retn 0xC
```

4. thiscall (C++成员函数调用) - 可内可外
	 - **参数传递**：this**指针**通过ecx传递，其余参数**从右到左**压栈
	 - **栈清理**：由调用者或者编译器决定（类似stdcall或cdecl）
	 - **返回值**：eax寄存器
	 - **常见场景**：C++类成员函数
```
反编译为
	mov ecx,obj_ptr  this指针存入ecx
	push 2   第二个参数
	push 1   第一个参数
	call obj.method  调用成员函数
	add esp, 8   调用者清理栈
	
	obj.method:
		...
		retn 或 retn 8,取决于编译器
```
## ?
TEB(Thread Environment Block)：存储与当前**线程相关**的信息，FS寄存器**指向当前线程的TEB**，每个线程都有独立的TEB用于存储多种信息。包括线程的本地存储、异常处理、TLS（线程局部存储）、栈指针等。每个线程都通过fs:[0] 获取指向其TEB的指针
PEB(Process Enviroment Block):存储与**进程相关**的信息，64位系统中可以通过FS寄存器访问
SEH(Structured Exception Handling):存储**线程的异常处理信息**，保存在TEB中，FS寄存器可访问
VEH(Vectored Exception Handling)：**全局的异常处理机制**，虽然不直接依赖FS，但处理线程相关异常时，仍然涉及TEB和FS寄存器

FS和GS(General Purpose Segment)扩展段寄存器，用于操作系统和多任务管理
在现代64位x86架构中，段寄存器使用较少，通常由操作系统 1管理，很多现代操作系统采用平摊地址空间模型，即不再使用段寄存器进行内存管理，而直接使用线性地址。

在Windows中，段寄存器fs用于**指向线程的线程环境块TEB**，fs寄存器主要用于访问**当前线程的局部存储区域**而**非全局数据**，这使得线程能够高效地存储和访问其专有的信息，而不需要锁定整个进程的数据。

## TEB、PEB与反调试
现在的进程一般由多个线程组成，可以认为进程是封装好的线程。
TEB线程环境块中主要字段为：
1. NtTib：线程信息块，时TEB的出事部分，主要包含栈的信息，TIB是用于维护线程的堆栈和异常处理的基本结构
	- NtTib.StackBase: 线程栈的基地址
	- NtTib.StackLimit：线程栈的限制地址
2. EnvironmentPointer：指向线程的环境块，这个指针通常为空，在某些情况下会用到
3. **ClientId**(+20)：客户端标识符，包含**线程的唯一标识符**与**所属进程ID**(+24)
4. ThreadLocalStoragePointer：指向线程局部存储（TLS）的指针。PEB存储了与当前进程相关的信息，例如进程的启动参数、模块信息、进程内存布局等
5. **ProcessEnvironment**(+30)：指向进程环境块（PEB）的指针。PEB存储了与当前进程相关的信息，例如进程的**启动参数、模块信息、进程内存布局**等
6. LastErrorValue：最近错误值，通常是Windows系统调用或API函数的错误代码
7. CountOfOwnedCriticalSections：线程拥有的临界区（Critical Section）数量临界区用于线程间同步，防止同时访问共享资源

PEB是进程环境块，内含进程相关重要信息
重要字段（偏移形式）：
**BeingDebugged**(+0x002)   是否正在调试  0->0x1
**NtGlobalFlag**(0x068)           附加调试不影响，拖入调试时->0x70
InheretAddressSpace和beingDebugged等标志字段控制进程状态
Ldr指向进程加载器数据，记录进程已加载模块的列表DLL、EXE等
ProcessParameters指向进程的启动参数，包含命令行、环境变量、启动路径等信息

附加调试对进程的影响最小，也可以通过特定手段隐藏对PEB进程环境块的影响。如果检测到**调试字段**数据变化，可能会触发**反调试**