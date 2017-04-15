## 使用tensorflow对目标图像进行分类并使用机械臂抓取


#### images_classify: 图像识别文件
#### robot_control: 控制小车移动以及机械臂动作，部署到树莓派上运行


### 系统需求：
#### 树莓派3 b型

#### Windows：
- Python 3.5.*
- OpenCV 3.2.*
- Numpy 1.12.1
- Tensorflow 1.0.1

#### Linux:
##### 推荐使用Ubuntu 14.04/16.04 LTS
- Python 2.7.*
- OpenCV 2.4.*
- Numpy 1.12.1
- Tensorflow 1.0.1

### 使用方法：
- 在根目录下打开终端(cmd, powershell or terminal)
- 在终端中输入
    ```
    python classify.py [<video source>]
    ```
- 拍照之后将图像分割成六个部分分别识别
- 识别结果存放在
    ```
    images_classify/results/results.json
    ```
