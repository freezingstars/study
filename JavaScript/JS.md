# JavaScript
JavaScript是一种轻量级的面向对象解释型脚本语言。主要被用于在网页上实现动态效果，增加用户与网页的交互性
可以直接嵌入HTML并执行，实现动态页面
主要适用于客户端脚本、网页开发和后端

## 使用

``` html
<script>
	console.log('Hello user');   
</script> <!--内联-->
<script src="..."></script> <!--外联-->
```

## 变量与数据类型
'var' 声明一个变量
'let' 声明一个有值的变量
'const' 声明一个常量

## 条件控制语句
### if else
``` javascript
if (condition1) {
	event1;
} else if (condithon2) {
	event2;
} else {
	event3;
}
```

### for
``` javascript
for (初始化表达式;循环条件;迭代器) {
	event;
}
```

### while
``` javascript
switch (condithon) {
	event; //if condithon is true
}
```

### break&continue
和其他语言一样，不举例

## 函数
一段可复用的代码块，接收输入参数，执行特定任务并返回输出
``` javascript
function function_name(var1,var2,var3,...) {
	body;
	return 返回值;
}
```

如果只是想要一个不复用的函数，可以写为匿名函数'事件名.操作 = funcion(){}'，例如：
``` javascript
button_element.onclick = function (){
	alert("事件触发")
}
```

## 事件

|事件|描述|
|:--:|:--:|
|onClick|点击事件|
|onMouseOver|鼠标经过|
|onMouseOut|鼠标移出|
|onChange|文本内容改变事件|
|onSelect|文本框选中|
|onFocus|光标聚集|
|onBlur|光标移出|

JavaScript绑定事件的方法有三种：

1. HTML属性
2. DOM属性
3. addEventListener方法  

```html
<botton onclick="click_event()"></botton>
<input type="text" onfocus="focus_event()" onblur="blur_event()"></input>
<script>
	function click_event() {
        alert("触发点击事件");
    }
    function focus_event() {
        console.log("聚焦");
    }
    function blur_event() {
        console.log("失焦");
    }
</script> <!--上述为html属性-->
```

``` html
<!DOCTYPE html> <!--DOM属性-->
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="box1">ID</div>
<div class="box2">类</div>
<div>普通</div>
<button>点击弹窗</button>
<script>
    var element_id = document.getElementById('box1');
    console.log(element_id);
    var element_class = document.getElementsByClassName('box2');
    console.log(element_class);
    var element_tag = document.getElementsByTagName('div');
    console.log(element_tag);
    element_id.innerHTML = '被修改的内容';  <!--id不可复用，所以无需下标-->
    element_class[0].innerText = '修改后的类选择文本';
    element_tag[0].style.color = 'red';
    element_tag[0].style.fontSize = '10px';

    var button_element = document.getElementsByTagName('button')[0]
    console.log(button_element)

    // button_element.onclick = function () {  <!--点击触发-->
    //     alert("触发")
    // }
    /* tagName和className实际上返回的都是一个数组 */

    /*button_element.addEventListener('click',function() { <!--监听点击事件，触发-->
        alert("触发");
    })*/

    button_element.addEventListener('click',click_event); <!--监听点击事件，执行功能函数-->

    function click_event() {
        alert("触发")
    }
</script>
</body>
</html>
```

**EventTarget.addEventListener()** 方法将指定的监听器注册到 [`EventTarget`](https://developer.mozilla.org/zh-CN/docs/Web/API/EventTarget) 上，当该对象触发指定的事件时，指定的回调函数就会被执行。事件目标可以是一个文档上的元素 [`Element`](https://developer.mozilla.org/zh-CN/docs/Web/API/Element)、[`Document`](https://developer.mozilla.org/zh-CN/docs/Web/API/Document) 和 [`Window`](https://developer.mozilla.org/zh-CN/docs/Web/API/Window)，也可以是任何支持事件的对象（比如 [`XMLHttpRequest`](https://developer.mozilla.org/zh-CN/docs/Web/API/XMLHttpRequest)）。

### 关键字

this(指向当前对象),例如onclick="deleteThis(this)",点击后会指向该节点  
parentNode 指向父节点，同时还有个parentChild
``` javascript
if (node.parentNode)  {
	node.parentNode.removeChild(node) 
} 
/*node.parentNode
检查当前节点（node）是否有父节点。
如果 node 还在 DOM（网页结构）中，它就会有一个 parentNode。
如果它已经被删除，则没有父节点。
node.parentNode.removeChild(node)
从父节点中移除这个子节点node。
相当于把这个元素从网页上删除*/
```

prompt("提示语") 弹窗，接收输入的字符串