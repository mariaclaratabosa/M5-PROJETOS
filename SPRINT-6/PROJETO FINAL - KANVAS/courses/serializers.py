from rest_framework import serializers
from courses.models import Course
from students_courses.serializers import StudentCourseSerializer
from contents.serializers import ContentSerializer
from rest_framework.validators import UniqueValidator
from accounts.models import Account
from rest_framework.exceptions import ValidationError


class CourseSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(read_only=True, many=True)
    students_courses = StudentCourseSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses"
        ]
        extra_kwargs = {
            "id": {"read_only": True},
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            },
        }

    def create(self, validated_data: dict):
        return Course.objects.create(**validated_data)


class CourseStudentsSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)
    students_courses = StudentCourseSerializer(read_only=True, many=True)

    class Meta:
        model = Course
        fields = ["id", "name", "students_courses"]

    def update(self, instance: Course, validated_data: dict):
        data = self.initial_data["students_courses"][0]
        student_email = data.get("student_email")

        student = Account.objects.filter(email=student_email).first()

        if not student:
            raise ValidationError(
                {"detail": f"No active accounts was found: {student_email}."}
            )
        else:
            instance.students.add(student)
            return super().update(instance, validated_data)