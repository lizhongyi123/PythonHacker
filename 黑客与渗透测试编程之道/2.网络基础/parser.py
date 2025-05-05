import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="示例命令行解析器")

# 添加参数
parser.add_argument("--name", type=str, help="输入你的名字")
parser.add_argument("--age", type=int, help="输入你的年龄")

# 解析参数
args = parser.parse_args()

# 使用参数
print(f"你好, {args.name}，你的年龄是 {args.age}。")