import yaml
import os

def read_yml(yamlpath):
    """读取yaml文件内容
    参数path：相对路径，起始路径：项目的根目录
    realpath：文件的真实路径，绝对路径地址
    """
    if not os.path.isfile(yamlpath):
        raise FileNotFoundError("文件路径不存在，请检查路径是否正确：%s"%yamlpath)

    #open方法打开直接读出来
    f=open(yamlpath,'r',encoding='utf-8')
    cfg=f.read()
    d=yaml.safe_load(cfg)    #用load方法转字典
    print("读取的测试文件数据：%s"%d)
    return d

if __name__ == '__main__':
    #yamlpath=
    r=read_yml("E:\\pyproject\\test_data\\data.yaml")
    print(r['login'])
