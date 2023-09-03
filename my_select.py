from sqlalchemy import func, desc, and_, distinct, select
import sys

sys.path.insert(0, 'D:/python/Task_12')

from models import Teacher, Student, Discipline, Grade, Group
from database import session


select_1 = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
print(select_1)


select_2 = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).where(Grade.discipline_id == 3).join(Student).group_by(Student).order_by(desc('avg_grade')).first()
print(select_2)


select_3 = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).join(Student).where(Grade.discipline_id == 4).group_by(Group.id).order_by(desc('avg_grade')).all()
print(select_3)


select_4 = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
    .select_from(Grade).group_by(Group.id).order_by(desc('avg_grade')).all()
print(select_4)


teacher_id = 2
select_5 = session.query(Teacher.fullname, Discipline.name) \
    .select_from(Discipline)\
    .join(Teacher)\
    .where(and_(Discipline.teacher_id == teacher_id, Teacher.id == teacher_id))\
    .all()
print(select_5)


id = 1
select_6 = session.query(Group.name, Student.fullname) \
    .select_from(Student)\
    .join(Group)\
    .where(and_(Group.id == id))\
    .all()
print(select_6)


group_id = 1
sub_id = 3
select_7 = session.query(Group.name, Student.fullname, Grade.grade) \
    .select_from(Student)\
    .join(Group)\
    .join(Grade)\
    .where(and_(Group.id == group_id, Grade.discipline_id == sub_id))\
    .all()
print(select_7)


select_8 = session.query(distinct(Teacher.fullname), func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Grade) \
        .join(Discipline)  \
        .join(Teacher) \
        .where(Teacher.id == 2).group_by(Teacher.fullname).order_by(desc('avg_grade')).all()
print(select_8)


student_id = 7
select_9 = session.query(Student.fullname, Discipline.name) \
    .select_from(Student)\
    .join(Grade)\
    .join(Discipline)\
    .where(and_(Student.id == student_id))\
    .distinct() \
    .all()
print(select_9)


student_id = 4
teacher_id = 2
select_10 = session.query(Student.fullname, Teacher.fullname,Discipline.name) \
    .select_from(Student)\
    .join(Grade)\
    .join(Discipline)\
    .join(Teacher)\
    .where(and_(Student.id == student_id, Teacher.id == teacher_id))\
    .distinct() \
    .all()
print(select_10)