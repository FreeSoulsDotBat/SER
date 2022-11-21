from datetime import date
from typing import Optional
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


class UserUpdate(BaseModel):
    email: Optional[str] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    birthday: Optional[date] = None
    supervision: Optional[str] = None
    supervision_area: Optional[str] = None
    phone: Optional[str] = None
    photo: Optional[bytes] = None


class StudentBase(BaseModel):
    id_user: int
    id_classroom: int
    id_class: int


class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int
    absences: int | None
    presences: int | None
    replacements: int | None

    class Config:
        orm_mode = True


class StudentUpdate(BaseModel):
    id_classroom: Optional[int] = None
    id_class: Optional[int] = None
    absences: Optional[int] = None
    presences: Optional[int] = None
    replacements: Optional[int] = None


class CooperatorBase(BaseModel):
    id_user: int


class CooperatorCreate(CooperatorBase):
    pass


class Cooperator(CooperatorBase):
    id: int
    absences: int | None
    presences: int | None
    replacements: int | None

    class Config:
        orm_mode = True


class CooperatorUpdate(BaseModel):
    absences: Optional[int] = None
    presences: Optional[int] = None
    replacements: Optional[int] = None


class CooperatorClassBase(BaseModel):
    id_cooperator: int
    id_class: int


class CooperatorClassCreate(CooperatorClassBase):
    pass


class CooperatorClass(CooperatorClassBase):
    id: int

    class Config:
        orm_mode = True


class CooperatorClassUpdate(BaseModel):
    id_cooperator: Optional[int] = None
    id_class: Optional[int] = None


class CooperatorClassroomBase(BaseModel):
    id_cooperator: int
    id_classroom: int


class CooperatorClassroomCreate(CooperatorClassroomBase):
    pass


class CooperatorClassroom(CooperatorClassroomBase):
    id: int

    class Config:
        orm_mode = True


class CooperatorClassroomUpdate(BaseModel):
    id_cooperator: Optional[int] = None
    id_classroom: Optional[int] = None


class ClassBase(BaseModel):
    beginning_date: date
    semester: int | None = 1
    number_students: int
    number_cooperators: int
    number_classrooms: int


class ClassCreate(ClassBase):
    pass


class Class(ClassBase):
    id: int

    class Config:
        orm_mode = True


class ClassUpdate(BaseModel):
    beginning_date: Optional[date] = None
    semester: Optional[int] = None
    number_students: Optional[int] = None
    number_cooperators: Optional[int] = None
    number_classrooms: Optional[int] = None


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


class ClassroomUpdate(BaseModel):
    floor: Optional[int] = None
    classroom_number: Optional[int] = None
    number_students: Optional[int] = None
    photo: Optional[bytes] = None
    last_class_day: Optional[date] = None
    next_class_day: Optional[date] = None
    id_class: Optional[int] = None


class NotificationBase(BaseModel):
    message: str
    recurrent: bool | None = False
    notification_date: date | None
    link: str
    photo: bytes | None
    notification_week_day: int | None


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int
    already_sent: bool | None = False

    class Config:
        orm_mode = True


class NotificationUpdate(BaseModel):
    message: Optional[str] = None
    recurrent: Optional[bool] = None
    notification_date: Optional[date] = None
    link: Optional[str] = None
    photo: Optional[bytes] = None
    notification_week_day: Optional[int] = None
    already_sent: Optional[bool] = None


class NotificationClassBase(BaseModel):
    id_notification: int
    id_class: int


class NotificationClassCreate(NotificationClassBase):
    pass


class NotificationClass(NotificationClassBase):
    id: int

    class Config:
        orm_mode = True


class NotificationClassUpdate(BaseModel):
    id_notification: Optional[int] = None
    id_class: Optional[int] = None


class NotificationClassroomBase(BaseModel):
    id_notification: int
    id_classroom: int


class NotificationClassroomCreate(NotificationClassroomBase):
    pass


class NotificationClassroom(NotificationClassroomBase):
    id: int

    class Config:
        orm_mode = True


class NotificationClassroomUpdate(BaseModel):
    id_notification: Optional[int] = None
    id_classroom: Optional[int] = None


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


class BookUpdate(BaseModel):
    book_name: Optional[str] = None
    actual_chapter: Optional[int] = None
    synopsis: Optional[str] = None
    beginning_date: Optional[date] = None
    end_date: Optional[date] = None


class BookClassBase(BaseModel):
    id_book: int
    id_class: int


class BookClassCreate(BookClassBase):
    pass


class BookClass(BookClassBase):
    id: int

    class Config:
        orm_mode = True


class BookClassUpdate(BaseModel):
    id_book: Optional[int] = None
    id_class: Optional[int] = None
