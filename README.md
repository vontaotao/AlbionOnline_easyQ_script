# AlbionOnline Easy Q Script

## 简介
AlbionOnline Easy Q Script 是一个简单的自动按键脚本，用于在游戏中自动持续按下 `Q` 键。该脚本提供了图形用户界面（GUI），用户可以自定义开始和停止按键的热键，并设置按键的时间间隔。

## 特性
- 支持持续按下 `Q` 键，适合在游戏中需要频繁按键的场景。
- 用户可自定义开始/停止按键和按键时间间隔。
- 图形化界面，易于使用。
- 设置程序图标，增加应用的可识别性。

## 安装
### 依赖项
在运行脚本之前，请确保已安装以下依赖库：

- `pyautogui`
- `keyboard`
- `tkinter`

你可以通过以下命令安装依赖：
```bash
pip install pyautogui keyboard
```
> 注意：`tkinter` 是 Python 标准库的一部分，通常无需手动安装。

## 使用方法
1. 克隆或下载本仓库：
   ```bash
   git clone https://github.com/vontaotao/AlbionOnline_easyQ_script.git
   ```
2. 在项目目录下运行脚本：
   ```bash
   python AutoKeyPress.py
   ```
3. 打开程序后，你将看到图形化界面，用户可以：
   - 输入自定义的开始/停止按键（默认为 `s` 键）。
   - 在下拉栏中选择 `Q` 键按下的时间间隔（默认为 `1` 秒）。
   - 点击“开始/停止”按钮或按下自定义按键开始/结束自动按键功能。

## 打包为 .exe 文件
如果你想将此脚本打包为 `.exe` 可执行文件，可以使用 `PyInstaller`：
```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=custom_icon.ico AutoKeyPress.py
```
打包完成后，`.exe` 文件会出现在 `dist` 文件夹中。

## 注意事项
- 请在不违反游戏规则的前提下使用该脚本，避免造成任何封号风险。
- 使用该脚本时，请确保选择的间隔时间合适，以免影响游戏的流畅性。

## 开源地址
你可以在 GitHub 上找到该项目的开源代码：
[AlbionOnline Easy Q Script](https://github.com/vontaotao/AlbionOnline_easyQ_script)

## 许可
该项目使用 MIT 许可协议。

