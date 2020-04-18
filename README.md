# alien
使用`pygame`开发一个2D游戏，参考《python编程：从入门到实践》

每个玩家消灭一行向下移动的外星人提升等级且游戏节奏会变快

具体描述
> 在游戏《外星人入侵》中，玩家控制一个在屏幕底部的飞船。玩家可以使用箭头键左右移动飞船，书用空格键射击。游戏开始时外星人从屏幕由上到下移动。玩家将这些外星人消灭后，出现新的外星人，移动速度变快。如果外星人撞到了飞船或到达屏幕底部，玩家损失一架飞船，损失三架后，游戏结束

## 安装pygame


依赖库
> brew install hg sdl sdl_image sdl_ttf

可以使游戏包含声音等的额外库
> brew install sdl_mixer portmidi

安装`pygame`
> pip install --user hg+http://bitbucket.org/pygame/pygame

注意：
 `pygame`会和macos出现不兼容的情况
 测试代码：


如果出现声音，但没有图像就是不兼容
使用`miniconda`创建`python 3.7`的环境就可以了