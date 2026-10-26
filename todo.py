# 命令行待办工具 v1.0
import sys
import os
FILE="todo.txt"
def add_task(task):
    with open(FILE,"a",encoding="utf-8") as f:
        f.write(f"{task}\n")

def list_tasks():
    if not os.path.exists(FILE):
        print("没有任务")
        return

    with open(FILE,"r",encoding="utf-8") as a:
        lines=a.readlines()

    for i,line in enumerate(lines,start=1):
        print(f"{i}. {line.strip()}")

    print(f"共 {len(lines)} 条任务")

def remove_task(index):
    if not os.path.exists(FILE):
        print("没有任务")
        return

    with open(FILE,"r",encoding="utf-8") as f:
        lines=f.readlines()

    if index < 1 or index > len(lines):
        print("无效")
        return

    removed=lines.pop(index-1).strip()
    with open(FILE,"w",encoding="utf-8") as f:
        f.writelines(lines)

    print(f"已删除:{removed}")

def done_task(index):
    if not os.path.exists(FILE):
        print("没有任务")
        return
    with open(FILE,"r",encoding="utf-8") as f:
        lines=f.readlines()

    if index<1 or index>len(lines):
        print("序号无效")
        return

    line=lines[index-1].strip()
    if line.startswith("[x]"):
        print("已经完成了")
        return

    lines[index-1]=f"[x] {line}\n"

    with open(FILE,"w",encoding="utf-8") as f:
        f.writelines(lines)

    print(f"已完成{line}")

def main():
    if len(sys.argv) < 2:
        print('用法: python3 todo.py add "任务"')
        print("      python3 todo.py list")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("请提供任务内容")
            return
        task = sys.argv[2]
        add_task(task)
        print(f"已添加: {task}")
    elif command == "list":
        list_tasks()
    elif command == "remove":
        if len(sys.argv) < 3:
            print("请提供要删除的序号")
            return
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("序号必须是数字")
            return
        remove_task(index)

    elif command == "done":
        if len(sys.argv) < 3:
            print("请提供要完成的序号")
            return
        try:
            index = int(sys.argv[2])
        except ValueError:
            print("序号必须是数字")
            return
        done_task(index)
    else:
        print("未知命令")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)