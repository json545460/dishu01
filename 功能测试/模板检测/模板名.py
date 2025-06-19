import urllib.request
import urllib.error
import json
import time
import logging
import sys
import os
from typing import Dict, List, Optional

# 配置日志
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'template_check.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# dev接口地址
LIST_URL = "https://api.editorup.com/api/v1/resource/templates"

# 请求配置
TIMEOUT = 30  # 请求超时时间（秒）
MAX_RETRIES = 5  # 最大重试次数
RETRY_DELAY = 1  # 重试间隔（秒）

headers = {
    "Accept": "application/json, text/plain, */*",
    "Origin": "https://dev.editorup.com",
    "Referer": "https://dev.editorup.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def clean_template_name(name: str) -> str:
    """清理和标准化模板名称"""
    # 去除首尾空格
    name = name.strip()
    # 将多个空格替换为单个空格
    name = ' '.join(name.split())
    # 去除特殊字符（保留中文、英文、数字）
    name = ''.join(char for char in name if char.isalnum() or '\u4e00' <= char <= '\u9fff' or char.isspace())
    return name

def validate_template_name(name: str) -> bool:
    """验证模板名称是否合法"""
    if not name:
        return False
    # 检查长度
    if len(name) < 2 or len(name) > 50:
        return False
    # 检查是否包含非法字符
    if any(char in name for char in ['<', '>', '&', '"', "'"]):
        return False
    return True

def validate_template_data(template: Dict) -> bool:
    """验证模板数据的完整性"""
    required_fields = ['id', 'title']
    return all(field in template and template[field] for field in required_fields)

def safe_request(url: str, params: Dict, headers: Dict) -> Dict:
    """安全的请求处理"""
    # 构建完整URL
    query_string = '&'.join([f"{k}={urllib.parse.quote(str(v))}" for k, v in params.items()])
    full_url = f"{url}?{query_string}"
    
    # 创建请求对象
    req = urllib.request.Request(
        full_url,
        headers=headers,
        method='GET'
    )
    
    # 重试机制
    for attempt in range(MAX_RETRIES):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.URLError as e:
            if attempt == MAX_RETRIES - 1:
                logger.error(f"请求失败: {str(e)}")
                raise
            logger.warning(f"请求失败，正在重试 ({attempt + 1}/{MAX_RETRIES}): {str(e)}")
            time.sleep(RETRY_DELAY)
        except Exception as e:
            logger.error(f"未知错误: {str(e)}")
            raise

def get_templates() -> List[Dict]:
    """获取所有模板数据"""
    limit = 100
    page = 1
    total = 1
    templates = []
    
    try:
        # 拉取模板列表（自动翻页）
        while (page - 1) * limit < total:
            params = {
                "sortBy": "default",
                "page": page,
                "limit": limit,
                "tags": ""
            }
            
            try:
                j = safe_request(LIST_URL, params, headers)
                
                # 验证API响应
                if j.get("code") != 0:
                    raise RuntimeError(f"列表接口错误：{j}")
                
                if not isinstance(j.get("data"), dict):
                    raise ValueError("API响应数据格式错误：缺少data字段")
                
                batch = j["data"].get("list", [])
                total = j["data"].get("total", 0)
                
                # 验证每个模板数据
                valid_templates = [t for t in batch if validate_template_data(t)]
                if len(valid_templates) != len(batch):
                    logger.warning(f"第 {page} 页存在无效模板数据")
                
                logger.info(f"📥 第 {page} 页：{len(valid_templates)} 条（累计 {len(templates) + len(valid_templates)}/{total}）")
                templates.extend(valid_templates)
                page += 1
                
                # 添加短暂延迟，避免请求过快
                time.sleep(0.5)
                
            except Exception as e:
                logger.error(f"处理第 {page} 页时出错: {str(e)}")
                raise
                
        logger.info(f"\n✅ 列表拉取完毕，共 {len(templates)} 个模板\n")
        return templates
        
    except Exception as e:
        logger.error(f"获取模板列表失败：{str(e)}")
        raise

def display_templates(templates: List[Dict]):
    """优化模板数据的展示"""
    # 按ID排序
    templates.sort(key=lambda x: x['id'])
    
    # 计算列宽
    id_width = max(len(str(t['id'])) for t in templates)
    name_width = max(len(t['title']) for t in templates)
    
    # 打印表头
    print("\n模板ID".ljust(id_width + 2) + "状态" + "模板名称".ljust(name_width + 2))
    print("-" * (id_width + name_width + 10))
    
    # 打印数据
    for tpl in templates:
        # 验证名称
        is_valid = validate_template_name(tpl['title'])
        status = "✅ " if is_valid else "❌"
        
        # 格式化输出
        id_str = str(tpl['id']).ljust(id_width + 2)
        name_str = tpl['title'].ljust(name_width + 2)
        print(f"{id_str}{status}{name_str}")

def analyze_templates(templates: List[Dict]) -> Dict:
    """分析模板数据"""
    stats = {
        "total": len(templates),
        "valid_names": 0,
        "invalid_names": 0,
        "name_lengths": {
            "min": float('inf'),
            "max": 0,
            "avg": 0
        }
    }
    
    total_length = 0
    for tpl in templates:
        name = tpl['title']
        if validate_template_name(name):
            stats["valid_names"] += 1
        else:
            stats["invalid_names"] += 1
            
        length = len(name)
        stats["name_lengths"]["min"] = min(stats["name_lengths"]["min"], length)
        stats["name_lengths"]["max"] = max(stats["name_lengths"]["max"], length)
        total_length += length
    
    if templates:
        stats["name_lengths"]["avg"] = total_length / len(templates)
    
    return stats

def main():
    """主函数"""
    try:
        templates = get_templates()
        
        # 显示模板列表
        display_templates(templates)
        
        # 显示统计信息
        stats = analyze_templates(templates)
        print("\n=== 统计信息 ===")
        print(f"总模板数：{stats['total']}")
        print(f"有效名称：{stats['valid_names']}")
        print(f"无效名称：{stats['invalid_names']}")
        print("\n名称长度统计：")
        print(f"最短：{stats['name_lengths']['min']}")
        print(f"最长：{stats['name_lengths']['max']}")
        print(f"平均：{stats['name_lengths']['avg']:.1f}")
            
    except Exception as e:
        logger.error(f"程序执行失败：{str(e)}")
        print(f"\n❌ 程序执行失败，请查看日志文件：{log_file}")
        sys.exit(1)

if __name__ == "__main__":
    main()


