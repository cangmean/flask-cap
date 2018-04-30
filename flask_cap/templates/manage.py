"""
管理
"""
from flask_script import Server, Manager
from {{ project_name }}.app import create_app
from {{ project_name }}.models import db, User, Role
from {{ project_name }}.utils import get_code

# pylint: disable=all

app = create_app()
manager = Manager(app)


@manager.command
def init():
    drop()
    db.create_all()
    # 初始化角色
    role_name_list = ['注册用户', '管理员']
    roles = [{'name': role_name} for role_name in role_name_list]
    db.session.bulk_insert_mappings(
        Role, roles
    )
    # 初始化用户
    role = Role.query.filter_by(name="管理员").first()
    user = User.create('admin', 'admin123', role=role)
    db.session.add(user)
    db.session.commit()


@manager.command
def drop():
    db.drop_all()

manager.add_command('run', Server(
    host='127.0.0.1',
    port=5000,
    use_reloader=True,
    use_debugger=True
))


def main():
    manager.run()

if __name__ == '__main__':
    main()