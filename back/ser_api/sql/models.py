from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, LargeBinary
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    birthday = Column(DateTime)
    supervision = Column(String)
    supervision_area = Column(String)
    phone = Column(String)
    photo = Column(LargeBinary)


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, index=True)
    absences = Column(Integer)
    presences = Column(Integer)
    replacements = Column(Integer)

    id_user = Column(Integer, ForeignKey("user.id"))
    id_classroom = Column(Integer, ForeignKey("classroom.id"))
    id_class = Column(Integer, ForeignKey("class.id"))


class Cooperator(Base):
    __tablename__ = 'cooperator'

    id = Column(Integer, primary_key=True, index=True)
    absences = Column(Integer)
    presences = Column(Integer)
    replacements = Column(Integer)

    id_user = Column(Integer, ForeignKey("user.id"))


class CooperatorClass(Base):
    __tablename__ = 'cooperator_class'

    id = Column(Integer, primary_key=True, index=True)

    id_cooperator = Column(Integer, ForeignKey("cooperator.id"))
    id_class = Column(Integer, ForeignKey("class.id"))


class CooperatorClassroom(Base):
    __tablename__ = 'cooperator_classroom'

    id = Column(Integer, primary_key=True, index=True)

    id_cooperator = Column(Integer, ForeignKey("cooperator.id"))
    id_classroom = Column(Integer, ForeignKey("classroom.id"))


class Class(Base):
    __tablename__ = 'class'

    id = Column(Integer, primary_key=True, index=True)
    beginning_date = Column(DateTime)
    semester = Column(Integer)
    number_students = Column(Integer)
    number_cooperators = Column(Integer)
    number_classrooms = Column(Integer)


class Classroom(Base):
    __tablename__ = 'classroom'

    id = Column(Integer, primary_key=True, index=True)
    floor = Column(Integer)
    classroom_number = Column(Integer)
    number_students = Column(Integer)
    photo = Column(LargeBinary)
    last_class_day = Column(DateTime)
    next_class_day = Column(DateTime)

    id_class = Column(Integer, ForeignKey("class.id"))


class Notification(Base):
    __tablename__ = 'notification'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String)
    recurrent = Column(Boolean)
    notification_date = Column(DateTime)
    link = Column(String)
    photo = Column(LargeBinary)
    notification_week_day = Column(Integer)


class NotificationClass(Base):
    __tablename__ = 'notification_class'

    id = Column(Integer, primary_key=True, index=True)
    id_notification = Column(Integer, ForeignKey("notification.id"))
    id_class = Column(Integer, ForeignKey("class.id"))


class NotificationClassroom(Base):
    __tablename__ = 'notification_classroom'

    id = Column(Integer, primary_key=True, index=True)
    id_notification = Column(Integer, ForeignKey("notification.id"))
    id_classroom = Column(Integer, ForeignKey("classroom.id"))


class Book(Base):
    __tablename__ = 'book'

    id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, unique=True)
    actual_chapter = Column(Integer)
    synopsis = Column(String)
    beginning_date = Column(DateTime)
    end_date = Column(DateTime)


class BookClass(Base):
    __tablename__ = 'book_class'

    id = Column(Integer, primary_key=True, index=True)
    id_book = Column(Integer, ForeignKey("book.id"))
    id_class = Column(Integer, ForeignKey("class.id"))
