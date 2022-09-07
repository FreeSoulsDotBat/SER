from datetime import date
from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str
    birthday: date | None
    supervision: str | None
    supervision_area: str | None
    phone: str
    photo: bytes | None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class StudentBase(BaseModel):
    id_user: int
    id_classroom: int
    id_class: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    absences: int
    presences: int
    replacements: int

    class Config:
        orm_mode = True


class CooperatorBase(BaseModel):
    id_user: int


class CooperatorCreate(CooperatorBase):
    pass


class Cooperator(CooperatorBase):
    id: int
    absences: int
    presences: int
    replacements: int

    class Config:
        orm_mode = True


class CooperatorClassBase(BaseModel):
    id_cooperator: int
    id_class: int


class CooperatorClassCreate(CooperatorClassBase):
    pass


class CooperatorClass(CooperatorClassBase):
    id: int

    class Config:
        orm_mode = True


class CooperatorClassroomBase(BaseModel):
    id_cooperator: int
    id_classroom: int


class CooperatorClassroomCreate(CooperatorClassroomBase):
    pass


class CooperatorClassroom(CooperatorClassroomBase):
    id: int

    class Config:
        orm_mode = True


class ClassBase(BaseModel):
    beginning_date: date
    semester: int
    number_students: int
    number_cooperators: int
    number_classrooms: int


class ClassCreate(ClassBase):
    pass


class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True


class ClassroomBase(BaseModel):
    floor: int
    classroom_number: int
    number_students: int
    photo: bytes | None
    last_class_day: date
    next_class_day: date

    id_class: int


class ClassroomCreate(ClassroomBase):
    pass


class Classroom(ClassroomBase):
    id: int

    class Config:
        orm_mode = True


class NotificationBase(BaseModel):
    message: str
    recurrent: bool
    notification_date: date | None
    link: str
    photo: bytes | None
    notification_week_day: int | None


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int
    already_sent: bool

    class Config:
        orm_mode = True


class NotificationClassBase(BaseModel):
    id_notification: int
    id_class: int


class NotificationClassCreate(NotificationClassBase):
    pass


class NotificationClass(NotificationClassBase):
    id: int

    class Config:
        orm_mode = True


class NotificationClassroomBase(BaseModel):
    id_notification: int
    id_classroom: int


class NotificationClassroomCreate(NotificationClassroomBase):
    pass


class NotificationClassroom(NotificationClassroomBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    book_name: str
    actual_chapter: int
    synopsis: str
    beginning_date: date
    end_date: date


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class BookClassBase(BaseModel):
    id_book: int
    id_class: int


class BookClassCreate(BookClassBase):
    pass


class BookClass(BookClassBase):
    id: int

    class Config:
        orm_mode = True
