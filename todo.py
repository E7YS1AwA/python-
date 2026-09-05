# todo.py
import argparse
import json
import os
from datetime import datetime

DATA_FILE = "todo.json"


def load_tasks():
    """从json文件加载任务列表"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """将任务保存回json文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)


def add_task(desc, priority):
    """新增任务：描述，优先级(1最高,3最低)"""
    tasks = load_tasks()
    new_task = {
        "id": len(tasks) + 1,
        "description": desc,
        "priority": priority,
        "done": False,
        "create_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"✅任务已添加,ID={new_task['id']}")


def mark_done(task_id):
    """根据ID标记任务完成"""
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"✅ID {task_id} 任务已标记完成")
            return
    print(f"❌找不到ID = {task_id} 的任务")


def list_tasks(sort_by_priority=False):
    """列出所有任务，可以选择按优先级升序（数字越小优先级越高）"""
    tasks = load_tasks()
    if sort_by_priority:
        tasks = sorted(tasks, key=lambda x: x["priority"])

    if not tasks:
        print("📭暂无待办任务")
        return

    print(f"{'ID':<4}{'状态':<6}{'优先级':<6}{'创建时间':<20}{'任务描述'}")
    print("‑" * 70)
    for t in tasks:
        status = "✅完成" if t["done"] else "🔲待办"
        print(f"{t['id']:<4}{status:<6}{t['priority']:<6}{t['create_time']:<20}{t['description']}")


def delete_task(task_id):
    """删除指定id任务"""
    tasks = load_tasks()
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"❌找不到ID = {task_id} 的任务")
        return
    save_tasks(new_tasks)
    print(f"🗑️ ID {task_id}任务已删除")


def main():
    parser = argparse.ArgumentParser(description="命令行带优先级待办清单工具")
    subparsers = parser.add_subparsers(dest="command", required=True, help="子命令")

    # add 添加任务
    parser_add = subparsers.add_parser("add", help="添加新任务")
    parser_add.add_argument("desc", type=str, help="任务描述，用引号括起来，例如 \"复习Python\"")
    parser_add.add_argument("-p", "--priority", type=int, choices=[1,2,3], default=2,
                            help="优先级:1最高,2普通(默认),3最低")

    # done 标记完成
    parser_done = subparsers.add_parser("done", help="标记任务完成")
    parser_done.add_argument("id", type=int, help="任务ID")

    # list 列出任务
    parser_list = subparsers.add_parser("list", help="展示全部任务")
    parser_list.add_argument("--sort-pri", action="store_true", help="按优先级从高到低排序")

    # del 删除任务
    parser_del = subparsers.add_parser("del", help="删除任务")
    parser_del.add_argument("id", type=int, help="任务ID")

    args = parser.parse_args()

    if args.command == "add":
        add_task(args.desc, args.priority)
    elif args.command == "done":
        mark_done(args.id)
    elif args.command == "list":
        list_tasks(sort_by_priority=args.sort_pri)
    elif args.command == "del":
        delete_task(args.id)


if __name__ == "__main__":
    main()
