# 🎵 AI Music

AI音乐工具，支持作曲、编曲、歌词生成。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 🎼 旋律创作
- 📝 歌词生成
- 🎹 编曲建议
- 🔍 歌曲分析
- 🎧 播放列表生成

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_music import create_tools

tools = create_tools()

# 旋律创作
melody = tools.compose_melody("快乐", "流行", "3分钟")

# 歌词生成
lyrics = tools.generate_lyrics("爱情", "流行", "浪漫")

# 编曲建议
arrangement = tools.suggest_arrangement("摇滚", ["吉他", "贝斯", "鼓"])

# 歌曲分析
analysis = tools.analyze_song(song_description)

# 播放列表
playlist = tools.generate_playlist("放松", "阅读", 60)
```

## 📁 项目结构

```
ai-music/
├── tools.py       # 音乐工具核心
└── README.md
```

## 📄 许可证

MIT License
