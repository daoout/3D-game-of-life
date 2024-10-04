# 3D_Game_of_Life

## 介绍

本项目实现了一个 **三维生命游戏（3D Game of Life）** 的模拟与可视化。生命游戏最初由英国数学家约翰·康威（John Conway）在1970年提出，是一个零玩家的细胞自动机，通过简单的生存和繁衍规则模拟复杂的生命演化过程。相比传统的二维生命游戏，三维版本能够展示更为丰富和复杂的动态行为，提供更直观和深入的生命模式探索。

**主要特点：**
- **高效性能**：利用 NumPy 和 Numba 实现高效的数值计算，加速模拟过程。
- **多样的初始配置**：支持随机分布、球形、螺旋形、多个立方体和蜂窝结构等多种初始活细胞配置。
- **交互式可视化**：使用 Plotly 生成交互式三维动画，便于观察生命演化动态。
- **灵活的参数调整**：用户可根据需求调整网格大小、初始活细胞数量、演化代数及生存与诞生规则。

## 软件架构

本项目采用模块化设计，主要分为以下几个部分：

1. **初始配置生成模块**
   - **功能**：生成不同形状和分布的初始活细胞配置，包括随机分布、球形、螺旋形、多个立方体和蜂窝结构。
   - **实现**：通过一系列函数（如 `generate_random_active_cells`、`generate_spherical_active_cells` 等）实现多样化的初始配置生成。

2. **模拟演化模块**
   - **功能**：根据生命游戏的规则演化细胞状态，生成各代的网格状态。
   - **实现**：使用 Numba 的 `@njit` 装饰器和并行化技术（`prange`）加速关键计算部分，包括邻居计数和状态更新。

3. **可视化模块**
   - **功能**：将模拟历史记录生成三维动画，并提供交互式的可视化界面。
   - **实现**：利用 Plotly 的 `Scatter3d` 对象创建三维散点图，并通过帧动画展示生命演化过程。支持保存为 HTML 文件并自动在浏览器中打开。

4. **主控制模块**
   - **功能**：协调各模块的工作流程，包括初始化网格、运行模拟、生成可视化结果。
   - **实现**：通过 `main()` 函数实现整体流程控制，用户可在此处设置参数并启动模拟。

## 安装教程

### 1. 克隆仓库

首先，克隆本项目到本地：

```bash
git clone https://gitee.com/your_username/3D_Game_of_Life.git
cd 3D_Game_of_Life
2. 创建虚拟环境（可选）
建议在虚拟环境中安装依赖，以避免与其他项目的依赖冲突：

bash
复制代码
python -m venv venv
source venv/bin/activate  # 对于 Windows 用户使用 `venv\Scripts\activate`
3. 安装依赖库
在项目目录下运行以下命令安装所需的 Python 库：

bash
复制代码
pip install numpy numba plotly
依赖库说明：

NumPy：用于高效的数值计算和数组操作。
Numba：通过 JIT 编译加速关键计算部分，提升模拟性能。
Plotly：用于生成交互式的三维可视化图形。
使用说明
1. 配置初始参数
打开 3D_Game_of_Life.py 文件，找到 main() 函数，根据需要调整以下参数：

网格大小：
python
复制代码
size = (100, 100, 100)  # 将长宽高各扩大2倍，使体积扩大8倍
初始活细胞数量：
python
复制代码
num_random_cells = 25340  # 设置初始随机活细胞数量为25,340
演化代数：
python
复制代码
generations = 100  # 可以根据需要调整
2. 运行模拟
在终端或命令提示符中，导航到脚本所在目录并运行：

bash
复制代码
python 3D_Game_of_Life.py
运行过程：

初始化：脚本将生成指定数量的唯一活细胞，并初始化三维网格。
模拟演化：根据设定的代数，逐代演化细胞状态，并在每代打印活细胞数量。
生成可视化：模拟完成后，脚本会生成一个 HTML 文件并自动在默认浏览器中打开，展示三维生命游戏的动画。
示例输出：

plaintext
复制代码
初始化活细胞数量: 25340
Generation 1 completed. Live cells: 25000
Generation 2 completed. Live cells: 24500
...
Generation 100 completed. Live cells: 8000
Visualization saved to 3D_Game_of_Life_25340.html
模拟完成。按 Enter 键退出程序并关闭脚本。
3. 交互式可视化
在浏览器中打开的 HTML 文件中，您可以：

播放动画：点击“Play”按钮开始动画。
暂停动画：点击“Pause”按钮停止动画。
旋转视角：通过拖动鼠标旋转三维视图，观察不同角度的生命演化。
参与贡献
欢迎您为本项目贡献代码和想法！以下是贡献指南：

Fork 本仓库

在 Gitee 上点击 “Fork” 按钮，将本仓库克隆到您的账户下。

新建 Feat_xxx 分支

在本地仓库中，基于 main 分支新建一个功能分支：

bash
复制代码
git checkout -b feat_add_new_feature
提交代码

在功能分支上进行修改，添加新功能或修复问题，并提交更改：

bash
复制代码
git add .
git commit -m "添加新功能：描述"
推送分支

将功能分支推送到远程仓库：

bash
复制代码
git push origin feat_add_new_feature
新建 Pull Request

在 Gitee 上提交 Pull Request，描述您的更改和贡献内容。项目维护者将审核并合并您的贡献。

特别提示：

遵循代码规范：请确保代码风格统一，符合 PEP 8 规范。
编写清晰的提交信息：每次提交应有明确的说明，便于审查和回溯。
提供详细的文档：如果添加新功能，请相应更新文档和使用说明。
特技
本项目具有以下特色功能和支持：

多语言支持

使用不同的 README 文件来支持多种语言，例如 README_en.md（英文）、README_zh.md（中文）等，方便全球用户查阅。
Gitee 资源

Gitee 官方博客：blog.gitee.com
探索优秀开源项目：https://gitee.com/explore
GVP（Gitee 最有价值开源项目）：综合评定出的优秀开源项目，展示在 GVP 页面
使用手册：https://gitee.com/help
封面人物栏目：展示 Gitee 会员风采的栏目，Gitee Stars
如何参与 Gitee 生态：

浏览和学习优秀项目：通过 Gitee Explore 了解和学习其他优秀的开源项目。
提交和贡献代码：通过 Fork 仓库、新建分支、提交 Pull Request 等方式，为您感兴趣的项目贡献代码。
参与社区讨论：在项目的 Issues 和 Discussions 中参与讨论，提出问题或分享您的见解。