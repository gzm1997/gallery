# 自制简易图片云盘

标签（空格分隔）： 图片 python


----------


[github地址][1]

----------

## 需求 ##

因为我经常在**markdown**书写过程中需要获取我一些图片或者截图的在线url，但是有些图片云盘需要收费或者要自己手动上传不方便。自己上传github固然可以，但是还是不够方便，所以写了个小脚本。

----------


## demo ##

![demo][2]


----------

## 需要 ##

 1. python
 2. git
 3. python依赖PIL

----------


## 用法 ##

 1. 一开始需要把配图或者截图保存到本地(**本地的git仓库中的raw文件夹**)，不需要修改文件名。

![文件结构][3]


----------


 2. 点击运行 **run.cmd** 文件

![run.cmd][4] 

可以看见后面会输出这张图片的url，最后会提示你确认退出，其实这个确认退出只是为了**造成阻塞**，不然这个cmd文件运行完就自动关闭窗口不留时间给你复制url了。


----------
## 代码 ##

只用了一点点很简单的**py**

 1. 把保存在raw文件夹里面的图片复制到mature文件夹里面，并重命名(其实重命名不是必要的)，最后删除raw里面的原图片，最终返回这张图片的新名字
```
def deliver_image():
	raw = os.listdir("raw")
	if raw == []:
		return False
	f = open("num.txt", "rb")
	num_str = f.read().decode("utf-8")
	num = int(num_str)
	f.close()
	old_name = "raw/" + raw[0]
	image_to_add = Image.open(old_name)
	new_name = str(num + 1) + ".png"
	image_to_add.save("mature/" + new_name)
	f = open("num.txt", "wb")
	f.write(str(num + 1).encode("utf-8"))
	f.close()
	os.remove("raw/" + raw[0])
	return new_name
```
 2. 使用subprocess产生三个子进程去调用git命令，使这个本地仓库的修改被push到github上的仓库中，最后返回这张图片在github上的地址

```
def push_to_github():
	subprocess.call("git add .", shell = True)
	subprocess.call("git commit -m 新增一张图片", shell = True)
	subprocess.call("git push origin master", shell = True)
```

 3. 运行
## py中运行 ##
```
if __name__ == "__main__":
	pic_name = deliver_image()
	if pic_name != False:
		push_to_github()
		print("图片的url:")
		print("https://raw.githubusercontent.com/gzm1997/gallery/master/mature/" + pic_name)
		stop = input("确认退出:")
```
## cmd中 ##
```
python add.py
```


  [1]: https://github.com/gzm1997/gallery
  [2]: https://raw.githubusercontent.com/gzm1997/gallery/master/mature/demo.gif
  [3]: https://raw.githubusercontent.com/gzm1997/gallery/master/mature/18.png
  [4]: https://raw.githubusercontent.com/gzm1997/gallery/master/mature/20.png