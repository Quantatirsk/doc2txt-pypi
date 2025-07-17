import os
import sys
import tempfile
import requests

# Add parent directory to path to import doc2txt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc2txt import extract_text

response = requests.get("https://share.teea.cn/api/files/demo.doc")
tmp = tempfile.NamedTemporaryFile(suffix=".doc", delete=False)
tmp.write(response.content)
tmp.close()
text = extract_text(tmp.name, optimize_format=True)
os.unlink(tmp.name)
open("output.txt", "w", encoding="utf-8").write(text)
print("文本已保存到 output.txt")
