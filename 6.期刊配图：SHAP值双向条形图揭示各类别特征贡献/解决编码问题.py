#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
解决 Jupyter Notebook 中的 Unicode 编码错误问题
"""

import sys
import os

# 检查当前系统默认编码
print("当前系统默认编码:", sys.getdefaultencoding())
print("文件系统编码:", sys.getfilesystemencoding())
print("标准输出编码:", sys.stdout.encoding)

# 设置环境变量确保使用 utf-8 编码
os.environ['PYTHONIOENCODING'] = 'utf-8'

# 如果在 Python 2 环境下运行，需要设置默认编码
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print("已设置 Python 2 默认编码为 utf-8")
else:
    print("Python 3 环境，默认使用 utf-8 编码")

# 解决读取文件时的编码问题示例：
# 正确的文件读取方式
def read_file_with_encoding(file_path):
    """
    尝试用不同编码读取文件
    """
    encodings = ['utf-8', 'gbk', 'gb2312', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
            print(f"成功使用 {encoding} 编码读取文件")
            return content
        except UnicodeDecodeError:
            print(f"使用 {encoding} 编码读取失败")
            continue
    
    raise Exception("无法使用常见编码读取文件")

# 如果你需要处理包含中文的数据框，确保正确设置
import pandas as pd

def read_csv_with_encoding(file_path):
    """
    尝试用不同编码读取 CSV 文件
    """
    encodings = ['utf-8', 'gbk', 'gb2312']
    
    for encoding in encodings:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"成功使用 {encoding} 编码读取 CSV 文件")
            return df
        except UnicodeDecodeError:
            print(f"使用 {encoding} 编码读取 CSV 文件失败")
            continue
    
    raise Exception("无法使用常见编码读取 CSV 文件")

# 示例：如何正确处理包含中文的字符串
chinese_text = "宇航员"
print("中文文本输出:", chinese_text)

print("\n编码问题解决建议:")
print("1. 在文件开头添加: # -*- coding: utf-8 -*-")
print("2. 读取文件时指定编码: open(file, encoding='utf-8')")
print("3. 读取CSV时指定编码: pd.read_csv(file, encoding='utf-8')")
print("4. 设置环境变量: export PYTHONIOENCODING=utf-8")