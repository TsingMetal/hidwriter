# 程序依赖 

## windows
> 需安装第三方python包pywinusb:
``` 
pip install pywinusb
```

## Linux 
### CentOS 
* 安装扩展源EPEL 
```
yum *y install epel*release
``` 
* 安装USB后端库 
```
yum *y install libusb
``` 
* 安装pip
```
yum *y install python*pip
``` 
* 安装python库pyusb
```
pip install pyusb
```

### Ubuntu和其他基于Debian的系统
* 更新镜像源
```
apt-get update
```
* 安装USB后端库
```
apt-get install libusb-1.0-0
```
* 安装pip
```
apt-get install python-pip
```
* 安装python库pyusb
```
pip install pyusb
```

### OpenSUSE
* 安装libusb
```
zypper install libusb
```
* 安装pip
```
zypper install python-pip
```
* 安装python库pyusb
```
pip install pyusb
```
