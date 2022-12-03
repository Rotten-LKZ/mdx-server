## MDX Server

MDX Server is a service used to read MDX/MDD dictionary data and provide a standard HTTP interface to external tools.

It is just a combination of [mdict-query](https://github.com/mmjang/mdict-query) and [PythonDictionaryOnline](https://github.com/amazon200code/PythonDictionaryOnline).

And this project is originally from [ninja33/mdx-server](https://github.com/ninja33/mdx-server) and I forked and am about to improve code and add features.

Usage:

1. Open `config` and edit it according to the original example.
2. Run `mdx_server.py` under Python 3.5 environment. After it displayed `Serving HTTP on port 8000...` in console, the service is running at background. 
3. Open your browser and input <http://localhost:8000/{word}> (the `{word}` is the word you want to query.), then the definition of that word will be displayed according to which dictionary(mdx file) you selected in above step 1.

*(The number '8000' depends on the port you set)*

Please check with the [manual](manual/mdx-server%20manual.pdf) for more detail and screenshot



## MDX Server 使用说明

目前流行的 MDX 词典文件只能在 Mdict, GoldenDict, 欧路，深蓝等词典软件中使用，而不能将内容对外输出。MDX Server 通过读取 MDX、MDD 格式的词典文件，对外部提供一个标准的 HTTP 服务接口。使得一些需要词典服务的软件，比如 Kindlemate，Anki 划词助手以及其他工具可以利用这个本地服务，灵活选取所需的 MDX 词典，批量或者单独获取单词的解释。

1. 打开 `config` 并根据原有示例对其进行编辑。
1. 在 Python 3.5 环境下运行 `mdx_server.py`，控制台内输出 `Serving HTTP on port 8000...` 表明服务运行成功。
2. 在浏览器地址栏输入 <http://localhost:8000/{word}>，其中 `{word}` 部分为待查的单词，比如 <http://localhost:8000/test>，通过 mdx-server 查询，浏览器内将显示该单词在第 1 步所选词典内的解释。

*（数字 `8000` 真实情况是多少取决于你设置的端口）*

MDX Server 核心功能由 [mdict-query](https://github.com/mmjang/mdict-query) 和 [PythonDictionaryOnline](https://github.com/amazon200code/PythonDictionaryOnline) 整合而成。

这个项目最初来自 [ninja33/mdx-server](https://github.com/ninja33/mdx-server) 我 fork 后并打算改进代码、增加功能。

更多内容和屏幕截图，请查阅[手册](manual/mdx-server%20manual.pdf)
