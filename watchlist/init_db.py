from app import app, db

print("开始创建数据库...")

with app.app_context():
    try:
        db.create_all()
        print("数据库表创建成功！")
    except Exception as e:
        print(f"创建数据库时出错：{e}") 
