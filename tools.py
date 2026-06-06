"""
AI Music - AI音乐工具
支持作曲、编曲、歌词生成
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIMusicTools:
    """
    AI音乐工具
    支持：作曲、编曲、歌词
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def compose_melody(self, mood: str, genre: str, duration: str) -> Dict:
        """创作旋律"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请创作一段{mood}情绪的{genre}旋律：

时长：{duration}

请返回JSON格式：
{{
    "title": "曲名",
    "key": "调性",
    "tempo": "速度",
    "time_signature": "拍号",
    "chord_progression": ["和弦进行"],
    "melody_notes": ["音符序列"],
    "structure": ["结构"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"melody": content}

    def generate_lyrics(self, theme: str, genre: str, mood: str) -> Dict:
        """生成歌词"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{genre}歌曲生成歌词：

主题：{theme}
情绪：{mood}

请返回JSON格式：
{{
    "title": "歌名",
    "verses": ["第一段", "第二段"],
    "chorus": "副歌",
    "bridge": "桥段",
    "theme": "主题"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"lyrics": content}

    def suggest_arrangement(self, genre: str, instruments: List[str]) -> Dict:
        """建议编曲"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        instruments_text = ", ".join(instruments)

        prompt = f"""请为{genre}歌曲建议编曲：

乐器：{instruments_text}

请返回JSON格式：
{{
    "arrangement": [
        {{"section": "段落", "instruments": ["乐器"], "dynamics": "力度", "notes": "说明"}}
    ],
    "mixing_tips": ["混音建议"],
    "effects": ["效果建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"arrangement": content}

    def analyze_song(self, song_description: str) -> Dict:
        """分析歌曲"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析以下歌曲：

{song_description}

请返回JSON格式：
{{
    "structure": "结构分析",
    "key_elements": ["关键元素"],
    "emotional_arc": "情感曲线",
    "strengths": ["优点"],
    "improvements": ["改进建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"analysis": content}

    def generate_playlist(self, mood: str, activity: str, duration: int) -> Dict:
        """生成播放列表"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请生成{mood}情绪的{activity}播放列表：

时长：{duration}分钟

请返回JSON格式：
{{
    "playlist_name": "播放列表名",
    "songs": [
        {{"title": "歌名", "artist": "艺术家", "reason": "推荐原因"}}
    ],
    "total_duration": "总时长"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"playlist": content}


def create_tools(**kwargs) -> AIMusicTools:
    """创建音乐工具"""
    return AIMusicTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Music Tools")
    print()

    # 测试
    lyrics = tools.generate_lyrics("爱情", "流行", "浪漫")
    print(json.dumps(lyrics, ensure_ascii=False, indent=2))
