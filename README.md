# 饶辅天的个人主页

欢迎访问我的个人主页仓库！这里展示我的项目经历、获奖荣誉、技术博客和业余生活。

## 个人介绍

北京工业大学信息科学技术学院 · 电子科学与技术专业本科在读，专注于数字芯片设计与计算机体系结构，具备从 RTL 设计到 FPGA 实现的完整开发经验。

## 项目经历

### AES 协处理器 FPGA 实现与架构升级（集创赛国家级二等奖）

2025 第九届全国大学生集成电路创新创业大赛 Robei 杯 · 队长 & 主要设计者

- 完成全部 RTL 设计与 FPGA 硬件实现，主导从算法验证到硬件部署的全流程
- 支持 ECB / CBC / CTR 模式与 128 / 192 / 256 位可变密钥长度，兼容 APB 总线接口
- 自主设计 UART 控制的下位机，验证 APB 总线时序与算核功能正确性
- 通过拆分流水线解决 FPGA 综合中的建立时间违例，完成时序收敛

### "一生一芯"计划：RISC-V 处理器设计（进行中）

2026.01 至今 · 已通过预学习答辩，完成 D、C1 阶段，正在 C2 阶段

- 模块化实现迷你 RISC-V 单周期 NPC（IFU / IDU / EXU / LSU / WBU），Verilator + DPI-C 实现访存与仿真终止
- 实现 MMIO 地址解码、串口与 RTC 时钟，跑通 am-kernels cpu-tests、riscv-tests 与 Hello World
- NEMU 扩展至 RV32IM，实现 itrace / mtrace / ftrace 全套追踪 + iringbuf，搭建 NEMU↔Spike 逐条 DiffTest
- 将 NEMU 的表达式求值 / 监视点 / sdb 移植到 NPC，仅重接 4 个后端原语即复用全部前端逻辑

## 获奖与荣誉

- 国家级二等奖 · 第九届全国大学生集成电路创新创业大赛 Robei 杯（队长，2025）
- 校级学习优秀奖（2023-2024 / 2024-2025 连续两年）
- 校级创新创业奖（2024-2025）
- 校级三好学生（2024-2025）

## 技术博客

- [状态机怎么设计](https://blog.csdn.net/darkaluminum/article/details/151216103?spm=1001.2014.3001.5501)
- [基于uart的APB协议片上测试下位机](https://blog.csdn.net/darkaluminum/article/details/151070612?spm=1001.2014.3001.5501)

## 业余生活

骑行、滑雪，和一些值得记录的瞬间（见主页"业余生活"板块，照片与视频位于 `assets/`）。

## 仓库结构

```
PROFILE/
├── README.md
├── index.html          # 个人主页
├── style.css           # 页面样式
└── assets/
    ├── images/         # 照片
    └── videos/         # 视频
```

## 如何访问

直接用浏览器打开 `index.html`，或通过 GitHub Pages 等服务部署。

---

© 2026 饶辅天. 保留所有权利。
