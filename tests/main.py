import os
import sys
import tempfile
import requests

# Add parent directory to path to import doc2txt
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from doc2txt import extract_text


# English file download and extraction
response = requests.get("https://share.teea.cn/api/files/eng.doc")
tmp = tempfile.NamedTemporaryFile(suffix=".doc", delete=False)
tmp.write(response.content)
tmp.close()
text = extract_text(tmp.name, optimize_format=True)
os.unlink(tmp.name)
open("output.txt", "w", encoding="utf-8").write(text)
print("文本已保存到 output.txt")


# Chinese file download and extraction
response = requests.get("https://share.teea.cn/api/files/chi.doc")
tmp = tempfile.NamedTemporaryFile(suffix=".doc", delete=False)
tmp.write(response.content)
tmp.close()
text = extract_text(tmp.name, optimize_format=True)
os.unlink(tmp.name)
open("output_chi.txt", "w", encoding="utf-8").write(text)
print("中文文本已保存到 output_chi.txt")
print("所有操作完成")