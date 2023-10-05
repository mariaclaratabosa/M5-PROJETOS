from django.urls import path
from .views import (
    CreateListCourseView,
    RetrieveUpdateDestroyCourseView,
    AddStudentToCourse,
    DeleteStudentFromCourseView,
)
from contents.views import CreateContentView, RetrieveUpdateDestroyContentView


urlpatterns = [
    path("courses/", CreateListCourseView.as_view()),
    path("courses/<uuid:course_id>/", RetrieveUpdateDestroyCourseView.as_view()),
    path("courses/<uuid:course_id>/contents/", CreateContentView.as_view()),
    path(
        "courses/<uuid:course_id>/contents/<uuid:content_id>/",
        RetrieveUpdateDestroyContentView.as_view(),
    ),
    path("courses/<uuid:course_id>/students/", AddStudentToCourse.as_view()),
    path(
        "courses/<uuid:course_id>/students/<uuid:student_id>/",
        DeleteStudentFromCourseView.as_view(),
    ),
]