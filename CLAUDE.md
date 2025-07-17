# CLAUDE.md - 项目开发指南

这个文件为Claude Code提供项目的开发和维护指南。

## 项目概述

**doc2txt** 是一个Python包，用于从Microsoft Word (.doc) 文档中提取纯文本。它基于antiword工具构建，内置了跨平台的二进制文件和配置数据。

### 主要组件

1. **antiword_wrapper.py** - antiword工具的Python封装器
2. **text_optimizer.py** - 文本格式优化工具
3. **bin/** - 跨平台antiword二进制文件
4. **antiword_share/** - antiword运行所需的数据文件

## 开发环境设置

### 测试命令

```bash
# 目前项目中没有找到标准的测试框架配置
# 建议手动测试主要功能
python -c "from doc2txt import extract_text; print('Import successful')"
```

### 构建和发布

```bash
# 构建包
python setup.py sdist bdist_wheel

# 发布到PyPI (需要先配置凭据)
twine upload dist/*
```

## 代码架构说明

### 核心功能流程

1. **extract_text()** 函数调用链：
   - `extract_text()` → `get_antiword_binary()` → 执行antiword
   - 可选：`optimize_text()` 进行文本格式优化

2. **平台检测逻辑** (`antiword_wrapper.py:9-40`):
   - 使用 `platform.system()` 和 `platform.machine()` 检测平台
   - 根据平台选择对应的二进制文件
   - 目前支持: Windows AMD64, Linux AMD64, macOS ARM64

3. **文本优化算法** (`text_optimizer.py:9-56`):
   - 识别表格行（包含 `|` 分隔符）
   - 合并无缩进的连续行
   - 移除行首空格但保留表格格式

## 文件结构详解

```
doc2txt/
├── __init__.py              # 包入口，导出主要函数
├── antiword_wrapper.py      # antiword二进制文件的Python包装器
├── text_optimizer.py       # 文本格式优化算法
├── bin/                     # 平台特定的antiword二进制文件
│   ├── darwin-arm64/antiword    # macOS Apple Silicon
│   ├── linux-amd64/antiword    # Linux AMD64
│   └── win-amd64/antiword.exe  # Windows AMD64
└── antiword_share/          # antiword运行时数据文件
    ├── fontnames            # 字体名称映射
    └── *.txt               # 各种字符编码映射文件
```

## 开发注意事项

### 添加新平台支持

要添加新平台支持，需要：

1. 在 `antiword_wrapper.py:15-31` 中添加平台检测逻辑
2. 在 `bin/` 目录下添加对应平台的antiword二进制文件
3. 更新 `setup.py` 中的 `package_data` 配置
4. 更新README.md中的支持平台列表

### 文本优化改进

文本优化逻辑位于 `text_optimizer.py`。如需改进：

1. `is_table_row()` - 修改表格行识别逻辑
2. `optimize_text()` - 调整行合并和格式化规则

### 错误处理

当前错误处理策略：
- 平台不支持 → `RuntimeError`
- 二进制文件缺失 → `RuntimeError`  
- antiword执行失败 → `subprocess.CalledProcessError`

## 维护清单

### 定期检查

- [ ] 验证所有平台的二进制文件是否可用
- [ ] 测试不同类型的Word文档
- [ ] 检查字符编码支持是否完整
- [ ] 更新antiword二进制文件到最新版本

### 发布前检查

- [ ] 运行基本功能测试
- [ ] 检查包的元数据信息
- [ ] 验证README.md和文档的准确性
- [ ] 确认所有平台的二进制文件都已包含

## 已知限制

1. **仅支持.doc格式**，不支持.docx
2. **macOS Intel (x86_64) 暂不支持**
3. **依赖antiword工具**，功能受限于antiword的能力
4. **文本提取质量**取决于原始文档的复杂程度

## 扩展建议

1. **添加.docx支持** - 可考虑集成python-docx
2. **改进文本格式化** - 增强表格和列表的处理
3. **添加更多平台** - 支持更多操作系统和架构
4. **性能优化** - 对大文件的处理优化
5. **错误恢复** - 更好的错误处理和恢复机制