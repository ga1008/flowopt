python GUI 流程操作工具
====

## 介绍：  

<ul>  
    <li>    <h5>让你的双手从重复的敲键盘点鼠标中解放！</h5></li>    
    <li>    <h5>基于 pyautogui 开发，加入了图像匹配和颜色匹配功能，构造了使用鼠标键盘和屏幕进行自动流程操作的微平台</h5></li>    
    <li>    <h5>用 json 文件进行任务安排，文件具体格式见下方</h5></li>    
    <li>    <h5>在 linux 上功能更丰富</h5></li>    
</ul>  

---

### 简要使用说明：

#### &nbsp;&nbsp; 安装：  

```
$ pip install flowoperate  
```

#### &nbsp;&nbsp; 终端命令：    

```  
$ flowopt /path_to_your/mission1.json [-l --loop] [-s --start_time] [-e --end_time]
  
# 显示帮助：  
$ flowopt -h  
```    

<ul style="font-size:30">  
    <li>     <h5>参数解释：</h5>   
        <ul style="none">  
<li><b>-l --loop</b> 是否循环执行</li>  
<li><b>-s --start_time</b> 循环执行的开始时间</li>  
<li><b>-e --end_time</b> 循环执行的结束时间</li>  
        </ul></li>  
</ul>  
  

#### &nbsp;&nbsp; 代码中调用：    
  
```  
from flow_operate.flow_operation import FlowTool  
  
# 参数 operate_list 即为上面 json 文件 loads 后的列表
ft = FlowTool(operate_list=mission_list)  
ft.start()  
```

#### &nbsp;&nbsp; json文件（任务文件）格式：  
```  
[  
  {  
    "name": "step1: search image and click",  
    "method": "SearchClick",  
    "(other_args)": "......",  
  },
  {  
    "name": "step2: search image and drag",  
    "method": "SearchDrag",  
    "(other_args)": "......",  
  },
  {......}
]
```  

### &nbsp;&nbsp; 目前支持的 step 方法：  
#### &nbsp;&nbsp; &nbsp;&nbsp; 目前集成的所有方法：
|method|说明|
|--|--|
|[SearchClick](#SearchClick)| 搜寻目标并点击 |
|[SearchDrag](#SearchDrag)| 搜寻目标并拖动 |
|[MulSearchClick](#MulSearchClick)| SearchClick 的批量 "或" 搜索匹配方法 |
|[MulSearchDrag](#MulSearchDrag)| SearchDrag 的批量 "或" 搜索匹配方法 |
|[EnterUrl](#EnterUrl)| linux 专用，打开 chrome 浏览器，输入指定的 url 并访问 |
|[WaitIcon](#WaitIcon)| 等待屏幕出现某个图标 |
|[WaitIconGone](#WaitIconGone)| 等待屏幕的某个图标消失 |
|[SaveWithVim](#SaveWithVim)| linux 专用，打开终端，使用 vim 打开指定的文件，写入剪贴板内容 |
|[TermCommand](#TermCommand)| linux 专用，打开终端执行命令 |
|[Click](#Click)| 模拟鼠标点击 |
|[Drag](#Drag)| 模拟鼠标拖动 |
|[HotKey](#HotKey)| 按下快捷键 |
|[InputABC](#InputABC)| 输入字符（仅限英文） |

 - <span id="SearchClick">SearchClick</span></br>
  <span>搜寻目标并点击</span></br>
  <span>标准配置(json Object)，使用时请去掉后面的注释以防出错：</span></br>

```  
{
  "name": "step1: ......",    //[缺省] 自定义的步骤名
  "method": "SearchClick",    //[必须] 此步骤的方法，注意不要拼写错误
  "take_method": "random",    //[缺省] 参数列表取出方式: only, order, all, random, pop_all, pop_order 和 pop_random
                                //order: 按序循环使用参数列表的元素，每次运行到此步骤则自动取下一个
                                //all: 每次都全部取出使用
                                //[默认] random: 每次都是随机取出使用
                                //only: 每次只取第一个
                                //pop_all: 一次性不放回取出全部，下次运行到此步骤自动跳出
                                //pop_order: 按序不放回取出一个，直至用完跳出
                                //pop_random: 随机不放回取出一个，直至用完跳出
  "data_list": [              //[必须] 本步骤需要使用的参数资源列表，放入直接的图片文件路径列表
    "/path/to/icon1.png",          
    "/path/to/resoures_file.txt", // 但如果文件太多，可以放在一个或多个txt文件内，一行一个，然后将txt文件名放入列表
    "resource_redis_key1",        // 也可以将资源文件名放入 redis 数据库内,在此处填入对应的 key，注意只能是其中一种方式,取决于下面 "data_list_type" 的值
    "......"
  ],
  "data_list_type": "array",//[缺省] 上面资源列表的类型，默认 "array", 同时也支持文件路径"file"和数据库"redis"
                               // 当 data_list_type 为 "array" 的时候, data_list 为直接的资源列表;
                               // 当值为 "file" 时, data_list 内放入存放资源的文件全路径的列表;
                               // 当值为 "redis" 时, data_list 内放入存放资源的 redis key
  "search_method": "shape", //[缺省] 搜寻方式，"shape" 或者 "color"
                                //[默认] shape: 按资源列表的图像形状搜寻
                                // color: 按图像颜色搜寻
  "match_options": {        //[缺省] 图像匹配的选项
  
    //如果是 search_method 是 shape 的方式：
    "threshold_value": 90,            //[缺省] 匹配的阈值，默认 90
    "as_gray": true,                //[缺省] 以灰度方式匹配（影响速度大，准确度有所下降）默认 true
    "as_binary": false,                //[缺省] 以二值化方式匹配（影响速度大，准确度下降大）默认 false
    "img_shape_times": 1.0,            //[缺省] 缩放率，0-n，以缩放n倍的方式匹配（影响速度较大，准确度下降大），默认 1.0 即不缩放
    "check_region": [0,0,1920,1080] //[缺省] 指定搜索范围，[屏幕左距离, 屏幕上距离, 宽度, 高度]，默认整个屏幕搜索（影响速度大，准确度看查找范围对不对）

    //如果是 search_method 是 color 的方式：
    "color_tolerance": 0,            //[缺省] 色彩容差，1-128，容差越大包含的颜色范围越广
    "color_purity": 1,                //[缺省] 色彩纯净度，大于1的整数，根据图像大小和复杂性调整，推荐一般图片设置为 1-50 之间
    "choice_method": "random",        //[缺省] 匹配中多个点时的取点方式，默认随机取点，填其他字符则取第一个匹配到的点
    "check_region": [0,0,1920,1080] //[缺省] 同上
  },
  "deviation": [0, 0]        //[缺省] 搜寻到目标后，点击时的偏移位置，[往上偏移量(负数往下), 往右偏移量(负数往左)]
  "speed": 0.5,              //[缺省] 搜寻到目标后点击的速度，默认0.5s
  "click_times": 1,            //[缺省] 点击次数，默认 1 次
  "click_sep": 0.2,            //[缺省] 多次点击的间隔时间，默认 0.2s
  "pre_delay": 0,              //[缺省] 本步骤开始前的等待时间，默认 0
  "sub_delay": 0.2,          //[缺省] 本步骤开始前的等待时间，默认 0
  "search_only": false,      //[缺省] 只搜寻，不点击，将搜寻坐标传入下一步骤，默认 false
  "not_locate": "exit"      //[缺省] 若无法匹配时的方法，默认 "exit"(退出)，其他选项：jumpN，backN，nextN
                                //[默认] exit，匹配不中则退出整个流程
                                //jumpN，N 为整数，跳到第 N 步
                                //backN，N 为整数，以当前步骤为基数，回退 N 步
                                //nextN，N 为整数，以当前步骤为基数，往下 N 步
}
```
 - <span id="SearchDrag">SearchDrag</span>  
```  
{
  "name": "step1: ......",    //[缺省] 同 SearchClick
  "method": "SearchDrag",    //[必须] 此步骤的方法，注意不要拼写错误
  "take_method": "random",    //[缺省] 同 SearchClick
  "data_list": [            //[必须] 同 SearchClick
    "/path/to/icon1.png",
    "/path/to/resoures_file.txt",
    "......"
  ],
  "data_list_type": "array",//[缺省] 同 SearchClick
  "search_method": "shape", //[缺省] 同 SearchClick
  "match_options": {        //[缺省] 同 SearchClick
    //如果是 search_method 是 shape 的方式：
    "threshold_value": 90,
    "as_gray": true,
    "as_binary": false,
    "img_shape_times": 1.0,
    "check_region": [0,0,1920,1080]
    
    //如果是 search_method 是 color 的方式：
    "color_tolerance": 0,
    "color_purity": 1,
    "choice_method": "random",
    "check_region": [0,0,1920,1080]
  },
  "deviation": [0, 0]        //[缺省] 同 SearchClick
  "speed": 0.5,              //[缺省] 同 SearchClick
  "start_position": [0,0],    //[缺省] 拖动的开始位置，默认本步骤搜索到的位置，可以是 [X, Y] 的形式，X、Y可以是整数坐标，或者 "pre_step"
                                //["pre_step", Y] 的形式：x坐标由上一步骤传递下来的，y坐标由本步骤定位
                                //["pre_step", "pre_step"] 的形式：x、y坐标均由上一步传递
  "end_position": [0,0],    //[缺省] 拖动的结束位置，默认本步骤搜索到的位置，格式同 start_position
  "pre_delay": 0,              //[缺省] 同 SearchClick
  "sub_delay": 0.2,          //[缺省] 同 SearchClick
  "search_only": false,      //[缺省] 同 SearchClick
  "not_locate": "exit"      //[缺省] 同 SearchClick
}
```
 - <span id="MulSearchClick">MulSearchClick</span></br>
  <span>SearchClick 的批量 "或" 搜索匹配方法，即取出全部的 data_list 参数资源进行批量搜索，直到搜索中其中一个，或者全部都不中；</span></br>
  <span>除了 "take_method" 默认为 "all" 以外，其他参数与 SearchClick 一样；</span></br>
  <span>MulSearchClick 方法比使用 SearchClick 时设置 "take_method" 为 "all" 要快，在批量"或"搜索时建议使用前者</span></br>
```
{
  "name": "step1: ......",        //[缺省] 同 SearchClick
  "method": "MulSearchClick",
  "......": "......."            //其他同 SearchClick
}
```
 - <span id="MulSearchDrag">MulSearchDrag</span></br>
  <span>SearchDrag 的批量 "或" 搜索匹配方法，即取出全部的 data_list 参数资源进行批量搜索，直到搜索中其中一个，或者全部都不中；  </span></br>
  <span>除了 "take_method" 默认为 "all" 以外，其他参数与 SearchDrag 一样；  </span></br>
  <span>MulSearchDrag 方法比使用 SearchDrag 时设置 "take_method" 为 "all" 要快，在批量"或"搜索时建议使用前者  </span></br>
```
{
  "name": "step1: ......",
  "method": "MulSearchDrag",
  "......": "......."            //其他同 SearchDrag
}
```  
 - <span id="EnterUrl">EnterUrl</span></br>
  <span>打开 chrome 浏览器，输入指定的 url 并访问  </span></br>
```
{
  "name": "step1: ......",
  "method": "EnterUrl",
  "chrome_icon": "/path/to/chrome_icon.png",    //[缺省] chrome 浏览器的截图图标，默认使用内置的图片模板
  "data_list": [                                //[必须] url 列表，或放 url 的txt文件，注意每行一个
        "http://meesee.top",
        "http://meesee.top/ip",
        "/path/to/url_file.txt"
    ],
  "data_list_type": "array",                    //[缺省] 同上
  "take_method": "order",                        //[缺省] 同上
  "pre_delay": 0,                                  //[缺省] 同上
  "sub_delay": 0,                                  //[缺省] 同上
  "search_only": false,                          //[缺省] 同上
  "not_locate": "exit"                          //[缺省] 同上
}
```
 - <span id="WaitIcon">WaitIcon</span></br>
<span>等待屏幕出现某个图标</span></br>
```
{
  "name": "step1: ......",
  "method": "WaitIcon",
  "match_options": {            //[缺省] 搜索匹配选项，解释同上
        "threshold_value": 90,
        "as_gray": true,
        "as_binary": false,
        "img_shape_times": 1.0,
        "check_region": [0,0,1920,1080]
    },
  "data_list": [                //[必须] 图标文件列表，或放图标路径的txt文件，注意每行一个
        "/path/to/icon1.png",
        "/path/to/icons_file.txt"
    ],
  "data_list_type": "array",    //[缺省] 同上
  "take_method": "order",        //[缺省] 同上
  "interval": 1.0,                //[缺省] 搜索间隔，默认 1.0s
  "after_showed": "next1"        //[缺省] 若匹配到了则往下多少步，默认 1 步
  "time_out": 120,                //[缺省] 超时时间，超过此时间没有匹配到则进入超时逻辑（if_timeout），默认 120s
  "if_timeout": "exit",            //[缺省] 若超时则退出或者跳转到哪一步（jumpN，backN，nextN），同 SearchClick 的 not_locate，默认 exit
  "pre_delay": 0,                  //[缺省] 同上
  "sub_delay": 0,                  //[缺省] 同上
  "search_only": false,          //[缺省] 同上
  "not_locate": "exit"          //[缺省] 同上
}
```
 - <span id="WaitIconGone">WaitIconGone</span></br>
<span>等待屏幕的某个图标消失</span></br>
```
{
  "name": "step1: ......",
  "method": "WaitIconGone",
  "match_options": {            //[缺省] 搜索匹配选项，解释同上
        "threshold_value": 90,
        "as_gray": true,
        "as_binary": false,
        "img_shape_times": 1.0,
        "check_region": [0,0,1920,1080]
    },
  "data_list": [                //[必须] 图标文件列表，或放图标路径的txt文件，注意每行一个
        "/path/to/icon1.png",
        "/path/to/icons_file.txt"
    ],
  "data_list_type": "array",    //[缺省] 同上
  "take_method": "order",        //[缺省] 同上
  "interval": 1.0,                //[缺省] 搜索间隔，默认 1.0s
  "after_gone": "next1"            //[缺省] 若图标消失了则往下多少步，默认 1 步
  "time_out": 120,                //[缺省] 超时时间，超过此时间没有消失则进入超时逻辑（if_timeout），默认 120s
  "if_timeout": "exit",            //[缺省] 若超时则退出或者跳转到哪一步（jumpN，backN，nextN），同 SearchClick 的 not_locate，默认 exit
  "pre_delay": 0,                  //[缺省] 同上
  "sub_delay": 0,                  //[缺省] 同上
  "search_only": false,          //[缺省] 同上
  "not_locate": "exit"          //[缺省] 同上
}
```
 - <span id="SaveWithVim">SaveWithVim</span></br>
<span>linux 系统专用方法，打开终端，使用 vim 打开指定的文件，写入剪贴板内容</span></br>
```
{
  "name": "step1: ......",
  "method": "WaitIconGone",
  "file_full_path": "/path/to/save/test.file",    //[必须] 保存的文件名
                                                    //若文件名需要携带上一步的结果，则在需要携带的地方加上 "[NAME]"，系统会自动替换
                                                    //例如 "/home/my_file_[NAME].txt"，而上一步传递下来的结果有{"flow_name": "001"}，则此文件名会替换为 "/home/my_file_001.txt"
  "pre_delay": 0,                  //[缺省] 同上
  "sub_delay": 0,                  //[缺省] 同上
  "after": "next1"              //[缺省] 保存结束后跳转到下面的第几步，还有 jumpN，backN，nextN，与上面解释一致
}
```
 - <span id="TermCommand">TermCommand</span></br>
<span>linux 专用方法，打开终端执行命令</span></br>
```
{
  "name": "step1: ......",
  "method": "TermCommand",
  "root_password": "xxxxxx",    //[缺省] root用户密码，如果执行的指令需要用到超级用户的话，则此项必须
  "data_list": [                //[必须] cmd 列表，或者放 cmd 命令的txt文件名
        "systemctl restart redis",
        "systemctl stop redis",
        "/path/to/cmd_list_file.txt",
    ],
  "take_method": "order",        //[缺省] cmd列表取出方式，默认 order，其他的 only, all, random, pop_all, pop_order 和 pop_random，解释同上
  "data_list_type": "array",    //[缺省] data_list 的元素的类型，file 或者 array，默认 array
  "after": "next1",                //[缺省] 完成命令后跳到第几步，其他的 jumpN，backN，nextN，与上面解释一致
  "pre_delay": 0,                  //[缺省] 同上
  "sub_delay": 0,                  //[缺省] 同上
}
```
 - <span id="Click">Click</span></br>
<span>模拟鼠标点击</span></br>
```
{
  "name": "step1: ......",
  "method": "Click",
  "data_list": [            //[必须] 点击位置的列表，可以是直接的x，y坐标，也可以是关键字
                                //x可以是：left/center/right/pre_step或者整数 N(不超过屏幕宽度)
                                //y可以是：top/center/bottom/pre_step或者整数 M(不超过屏幕高度)
                                //设置为 pre_step 时，将使用从上一步流转下来的坐标，如果上步没有，则使用当前鼠标坐标
        ["right", "bottom"],
        ["pre_step", "center"],
        [1000, 500]
  ],
  "take_method": "only",    //[缺省] 坐标列表取出方式，默认为 only，其他的 order, all, random, pop_all, pop_order 和 pop_random，解释同上
  "data_list_type": "array",    //[缺省] data_list 的元素的类型，file 或者 array，默认 array
  "click_side": "left",        //[缺省] 点击鼠标的左键 left 或者右键 right，或者中键 middle，默认左键
  "click_times": 1,            //[缺省] 点击多少次，默认1次
  "click_sep": 0.2,            //[缺省] 点击间隔，默认 0.2s
  "after": "next1",            //[缺省] 完成命令后跳到第几步，其他的 jumpN，backN，nextN，与上面解释一致
  "pre_delay": 0,              //[缺省] 同上
  "sub_delay": 0,              //[缺省] 同上
}
```
 - <span id="Drag">Drag</span></br>
<span>模拟鼠标拖动</span></br>
```
{
  "name": "step1: ......",
  "method": "Click",
  "data_list": [            //[必须] 拖动开始位置到结束位置的列表，可以是直接的x，y坐标，也可以是关键字
                                //x可以是：left/center/right/pre_step或者整数 N(不超过屏幕宽度)
                                //y可以是：top/center/bottom/pre_step或者整数 M(不超过屏幕高度)
                                //设置为 pre_step 时，将使用从上一步流转下来的坐标，如果上步没有，则使用当前鼠标坐标
        [["right", "bottom"], ["right", "top"]],
        [["center", "center"], ["pre_step", "center"]],
        [[1000, 500], ["pre_step", "pre_step"]]
  ],
  "take_method": "only",    //[缺省] 坐标列表取出方式，默认为 only，其他的 order, all, random, pop_all, pop_order 和 pop_random，解释同上
  "data_list_type": "array",//[缺省] data_list 的元素的类型，file 或者 array，默认 array
  "drag_speed": 0.5,        //[缺省] 拖动速度，默认0.5s
  "after": "next1",            //[缺省] 完成命令后跳到第几步，其他的 jumpN，backN，nextN，与上面解释一致
  "pre_delay": 0,              //[缺省] 同上
  "sub_delay": 0,              //[缺省] 同上
}
```
 - <span id="HotKey">HotKey</span></br>
<span>按下快捷键</span></br>
```
{
  "name": "step1: ......",
  "method": "HotKey",
  "data_list": [            //[必须] 快捷键名称列表，注意每个元素为一个快捷键名（对应键盘上的名称）
        ["ctrl", "c"],            //复制
        ["ctrl", "atl", "t"],    //打开终端（linux）
        ["A"]                    //按下键盘的A键
  ],
  "take_method": "order",    //[缺省] 坐标列表取出方式，默认为 order，其他的 only, all, random, pop_all, pop_order 和 pop_random，解释同上
  "data_list_type": "array",//[缺省] data_list 的元素的类型，file 或者 array，默认 array
  "after": "next1",            //[缺省] 完成命令后跳到第几步，其他的 jumpN，backN，nextN，与上面解释一致
  "pre_delay": 0,              //[缺省] 同上
  "sub_delay": 0,              //[缺省] 同上
}
```
 - <span id="InputABC">InputABC</span></br>
<span>输入字符（仅限英文）</span></br>
```
{
  "name": "step1: ......",
  "method": "InputABC",
  "data_list": [            //[必须] 需要输入的字符的列表，支持使用上一步的 flow_name 进行关键字替换
        "This is the test txt",
        "can be any English words, sentences",
        "LiMing's class number is [NAME]"    //关键字替换
  ],
  "take_method": "order",    //[缺省] 坐标列表取出方式，默认为 order，其他的 only, all, random, pop_all, pop_order 和 pop_random，解释同上
  "data_list_type": "array",//[缺省] data_list 的元素的类型，file 或者 array，默认 array
  "after": "next1",            //[缺省] 完成命令后跳到第几步，其他的 jumpN，backN，nextN，与上面解释一致
  "pre_delay": 0,              //[缺省] 同上
  "sub_delay": 0,              //[缺省] 同上
}
```

### 其他集成方法有待开发
  

***  
  
### 集成的测试小工具  
flowopt 安装后附带两个终端工具  
 - ilocate  （形状定位工具）
 - clocate  （颜色定位工具）

#### 1. 形状定位工具  
```shell  
$ ilocate template_img_path.jpg [-h] [-tr TEMPLATE_RESIZE] [-th THRESHOLD_VALUE] [-ag] [-ab] [-ip IMAGE_PATH] [-ir IMAGE_RESIZE] [-ssr SCREENSHOT_REGION] [-d DELAY]
```  
一个必要位置参数：
 - template_img_path  样本图片存放位置

其他可选参数：
 - --help  -h：显示可用参数
 - --template_resize  -tr： 样本图片放大多少倍（大于零），小于1时缩小，大于1放大
 - --threshold_value  -th： 定位阈值（0-100）
 - --as_gray  -ag： 以灰度图像处理，速度会加快，准确率会稍微降低
 - --as_binary  -ab： 以二极图像处理，速度非常快，准确率比较低，适用于对比鲜明的图像
 - --image_path  -ip： 待匹配图片的路径，默认不需要传入，程序会截取当前屏幕作为输入
 - --image_resize  -ir： 待匹配图片放大多少倍，与 -tr 参数一样
 - --screenshot_region  -ssr： 待匹配图片的搜索范围，传入四组数字，'屏幕左距离,屏幕上距离,宽度,高度'，以英文逗号分隔
 - --delay  -d：延时多少秒开始
 
 例如：
```shell  
$ ilocate 昵图网.png -ag -ssr 1920,100,1920,980
searching ...
delay [ 0.0 ] seconds ...
[ 2021-11-12 16:03:47 ]
     matching image: [ ScreenShot ]
     using template: [ 昵图网.png ]
     >>> locate success! score: 100.0
```  
<img src="https://guardian-angel.oss-cn-shenzhen.aliyuncs.com/flowopt/Figure_1.png" alt="ilocate 样例">

#### 2. 颜色定位工具  
```shell  
$ clocate template_color_img_path.jpg [-h] [-ct COLOR_TOLERANCE] [-cp COLOR_PURITY] [-ip IMAGE_PATH] [-ir IMAGE_RESIZE] [-ssr SCREENSHOT_REGION] [-d DELAY]
```  
一个必要位置参数：
 - template_color_img_path  颜色样本图片存放位置，最好是纯色

其他可选参数：
 - --help  -h：显示可用参数
 - --color_tolerance  -ct： 颜色容差（0-127）越大匹配范围越宽，越小越精细
 - --color_purity  -cp： 色彩纯净度，大于1的整数，根据图像大小和复杂性调整，推荐一般图片设置为 1-50 之间
 - --image_path  -ip： 待匹配图片的路径，默认不需要传入，程序会截取当前屏幕作为输入
 - --image_resize  -ir： 待匹配图片放大多少倍，与 -tr 参数一样
 - --screenshot_region  -ssr： 待匹配图片的搜索范围，传入四组数字，'屏幕左距离,屏幕上距离,宽度,高度'，以英文逗号分隔
 - --delay  -d：延时多少秒开始

 
 例如：
```shell  
$ clocate 蓝色.png -ct 50 -cp 6 -ssr 2020,100,1820,880
searching ...
delay [ 0.0 ] seconds ...
positions:
    [904, 227]
```  
其中 positions 为匹配图像的中心点（可能有多个），即下图的黄色加号 + 的位置点

<img src="https://guardian-angel.oss-cn-shenzhen.aliyuncs.com/flowopt/Figure_2.png" alt="clocate 样例">
