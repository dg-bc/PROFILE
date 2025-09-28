#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gitee网络图自动截图工具

此脚本使用Selenium自动访问Gitee网络图页面并截图保存，
解决前端JavaScript由于跨域限制无法直接获取网络图的问题。

使用方法:
1. 安装依赖: pip install selenium webdriver-manager
2. 运行脚本: python gitee_screenshot.py
3. 截图将保存在assets/images目录下
"""

import os
import time
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def print_with_timestamp(message):
    """带时间戳的打印函数"""
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(f"[{timestamp}] {message}")


def main():
    """主函数：抓取Gitee网络图并保存"""
    print("="*50)
    print_with_timestamp("Gitee网络图自动抓取脚本启动")
    print("="*50)
    
    driver = None
    try:
        # 配置信息
        GITEE_NETWORK_URL = os.environ.get('GITEE_NETWORK_URL', 'https://gitee.com/DG_TG/my_notes/graph/master')
        OUTPUT_DIR = os.path.join(os.getcwd(), 'assets', 'images')
        OUTPUT_FILE = 'gitee_network_graph.png'
        save_path = os.path.join(OUTPUT_DIR, OUTPUT_FILE)
        
        # 设置浏览器选项
        print_with_timestamp("正在配置浏览器选项...")
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1200,800')
        options.add_argument('--no-sandbox')  # 解决权限问题
        options.add_argument('--disable-dev-shm-usage')  # 解决共享内存问题
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36')
        
        # 初始化浏览器
        print_with_timestamp("正在初始化浏览器...")
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )
        print_with_timestamp("浏览器初始化成功！")
        
        # 访问Gitee网络图页面
        print_with_timestamp(f"正在访问Gitee网络图页面: {GITEE_NETWORK_URL}")
        driver.get(GITEE_NETWORK_URL)
        
        # 等待页面加载完成
        print_with_timestamp("等待页面加载完成...")
        time.sleep(10)  # 增加等待时间以确保网络图完全加载
        
        # 尝试找到网络图元素并调整窗口大小以适应内容
        print_with_timestamp("尝试调整窗口大小以适应网络图内容...")
        try:
            # 尝试获取网络图容器的尺寸
            graph_container = driver.find_element(by='css selector', value='.graph-container')
            if graph_container:
                # 获取元素的大小
                size = graph_container.size
                width = max(size['width'], 1200)  # 最小宽度1200
                height = max(size['height'], 800)  # 最小高度800
                print_with_timestamp(f"检测到网络图尺寸: 宽{width}px, 高{height}px")
                # 设置窗口大小
                driver.set_window_size(width, height)
                # 再次等待页面调整布局
                time.sleep(2)
        except Exception as e:
            print_with_timestamp(f"调整窗口大小失败，使用默认尺寸: {str(e)}")
        
        # 创建保存目录
        if not os.path.exists(OUTPUT_DIR):
            print_with_timestamp(f"创建截图保存目录: {OUTPUT_DIR}")
            os.makedirs(OUTPUT_DIR)
        
        # 尝试找到网络图容器并截图
        try:
            network_graph_element = driver.find_element(by='css selector', value='.graph-container')
            print_with_timestamp("找到网络图容器，正在截取元素...")
            network_graph_element.screenshot(save_path)
        except Exception as e:
            print_with_timestamp(f"无法找到特定的网络图容器元素 ({e})，将截取整个页面...")
            driver.save_screenshot(save_path)
        
        # 验证文件是否保存成功
        if os.path.exists(save_path):
            file_size = os.path.getsize(save_path) / 1024 / 1024  # 转换为MB
            print_with_timestamp(f"✅ 截图保存成功！文件大小: {file_size:.2f} MB")
            print_with_timestamp(f"请在HTML文件中引用此截图: <img src=\"{OUTPUT_DIR.replace(os.getcwd() + os.sep, '')}/{OUTPUT_FILE}\" alt=\"Gitee网络图\">")
            print_with_timestamp("提示: 您可以将此脚本添加到定时任务中，实现网络图的定期自动更新。")
        else:
            print_with_timestamp("❌ 截图保存失败，文件不存在！")
            
    except Exception as e:
        print_with_timestamp(f"❌ 抓取过程中发生错误: {str(e)}")
        print_with_timestamp("详细错误信息:")
        traceback.print_exc()
    finally:
        # 关闭浏览器
        if driver:
            print_with_timestamp("正在关闭浏览器...")
            driver.quit()
            print_with_timestamp("浏览器已关闭")
    
    print("="*50)
    print_with_timestamp("脚本执行完成")
    print("="*50)


if __name__ == "__main__":
    main()