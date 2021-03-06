 # 基于卷积神经网络的学生人脸识别考勤系统  
 ## 上传前已经通过测试，希望各位认真查阅README，不要做伸手党，不熟悉TensorFlow和python的请提前学习。欢迎给小星星。    
 ## 测试环境：
 >**1.Windows 10**  
 >**2.TensorFlow1.14 GPU版本（没有GPU也可以，CPU版本会慢一些）**  
 >**3.PyQt**  
 >**4.Sqlite3**  

 ## 使用的模型：
 ### MTCNN->人脸检测  
 ### FaceNet->人脸识别  

 ## 程序目录如下：
>**20170512-11-547下为FaceNet数据 这个数据太大无法上传，请到百度云下载**   
>**链接:https://** 
>**pan.baidu.**
>**com/s/1nMwbahnZ0ZgeIOO6UrATdw(请去掉空格)**
>**提取码：w3it  **    
>**align文件夹下为MTCNN模型数据**  
>**src文件夹下为所有主程序文件 SetUpMainWindow.py为启动文件**  
>**DB文件夹下为sqlite3数据库**  
>**emb_img和src_img文件夹在程序运行时会自动创建（或者可以直接手动创建，两个都是空文件夹）**  
**文件中不包含UI文件，所有UI文件均转换成Python程序文件**  

![5](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/5.png)  

## 目录结构
![目录结构1](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/目录结构1.png)  
![目录结构2](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/目录结构2.png)  
![目录结构3](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/目录结构3.png)  


## DB目录讲解
>**StudentCheckWorkDB.db 为学生考勤数据表**  
>**StudentFaceDB.db 为学生人脸数据**  

![6](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/6.png)

## 操作步骤
1、创建班级人脸数据  
2、创建班级考勤表  
3、选择学生学号，与人脸表  
4、录入人脸  
5、提取特征  
5、开始检测  
  
## 软件界面细节  

![1](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/1.png) 

![2](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/2.png) 

![3](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/3.png) 

![4](https://github.com/omega-Lee/PyQt5_Face_Recognition/blob/master/image/4.png) 
