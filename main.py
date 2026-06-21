import akshare as ak
import pandas as pd
import requests
from datetime import datetime

# === 把下面引号里的内容，换成第一步你保存的钥匙 ===
MY_KEY = "SCT366996TAG692aIvDJKoUdhPJPsnF9FK"
# ============================================

def send_wechat(title, content):
    url = f'https://sctapi.ftqq.com/{MY_KEY}.send'
    requests.post(url, data={'title': title, 'desp': content})

print("机器人开始干活...")
send_wechan("选股机器人启动", "你的缠论选股机器人已成功部署！每天下午4点会给你发消息。")
print("测试消息已发送到微信，请检查。")
