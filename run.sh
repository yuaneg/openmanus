#!/bin/bash

# 获取脚本所在目录的绝对路径
SCRIPT_DIR=~/openmanus

# 检查脚本所在目录是否存在
if [ ! -d "$SCRIPT_DIR" ]; then
    echo "错误：脚本所在目录不存在 - $SCRIPT_DIR"
    exit 1
fi

# 在脚本所在目录执行git命令（不切换当前目录）
echo "在目录 $SCRIPT_DIR 执行git操作..."
git -C "$SCRIPT_DIR" reset --hard HEAD
git -C "$SCRIPT_DIR" pull

# 在脚本所在目录执行python命令（不切换当前目录）
echo "在目录 $SCRIPT_DIR 执行python脚本..."
python "$SCRIPT_DIR/main.py"
