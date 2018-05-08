#coding=gbk
#加密文件方法
def jiami():
    yuanName = input('请输入您要加密的文件名:')
    yuanFile = open(yuanName,'r')
    while True:
        try:
            password = int(input('请输入整型的秘钥:'))
            if password<256:
                break
            else:
                print("请输入一个在0和256之间的数字!")
        except:
            print("请输入的数据类型是数字!")
    num = yuanName.rfind('.')
    jiamiFileName = yuanName[0:num]+'[加密]'+yuanName[num:]
    content = yuanFile.read(1)
    jiamiFile = open(jiamiFileName, 'w')
    while len(content)>0:
        # 将读取到的字母转化为ascall码
        position = ord(content)
        # 加密
        position = position+password
        # 将ascall码转化为字母写入
        contents = chr(position)
        jiamiFile.write(contents)
        content = yuanFile.read(1)
    print('加密完成')
    jiamiFile.close()
    yuanFile.close()
def jiemi():
    yuanName = input('请输入您要解密的文件名:')
    yuanFile = open(yuanName, 'r')
    while True:
        try:
            password = int(input('请输入解密的秘钥:'))
            break
        except:
            print("请输入的数据类型是数字!")
    num = yuanName.rfind('.')
    num1 = yuanName.rfind('[')
    jiamiFileName = yuanName[0:num1] + '[解密]' + yuanName[num:]
    content = yuanFile.read(1)
    jiamiFile = open(jiamiFileName, 'w')
    while len(content) > 0:
        #将读取到的字母转化为ascall码
        position = ord(content)
        #解密
        position = position - password
        #将ascall码转化为字母写入
        contents = chr(position)
        jiamiFile.write(contents)
        content = yuanFile.read(1)
    print('解密完成')
    jiamiFile.close()
    yuanFile.close()
def main():
    while True:
        try:
            num = int(input("请选择您要进行的操作（1--加密  2--解密  3--退出）："))
        except:
            print("输入有误，请重新输入!!!")
            continue;
        if num ==1:
            jiami()
        elif num==2:
            jiemi()
        elif num==3:
            break
        else:
            pass
if __name__ == '__main__':
    main()
