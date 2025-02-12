from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from .models import Course, Enrollment
from .serializers import CreateCourseSerializer, ListCoursesSerializer, UpdateCourseSerializer, EnrollmentSerializer

class CourseDetailApiView(APIView):

    def post(self , request):

        """Create Course"""

        serializer = CreateCourseSerializer(data = request.data)

        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()

                return Response({'message': 'Course Created!'}, status= status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:

            return Response({"error": f"{e}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get(self, request, course_id = None):
        """List Course"""
        if course_id:
            try:
                course = Course.objects.get(pk=course_id)
                serializer = ListCoursesSerializer(course)

                return Response({'message': 'Course retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)



            except Course.DoesNotExist:
                return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        courses = Course.objects.all()

        if not courses.exists():
            return Response(
                {'message': 'No courses available', 'data': []},
                status=status.HTTP_204_NO_CONTENT
            )

        serializer = ListCoursesSerializer(courses, many=True)
        return Response({'message': 'Data fetched successfully', 'data': serializer.data}, status = status.HTTP_200_OK)

    def patch(self, request, course_id):
        """Update Course"""

        try:
                course = Course.objects.get(id=course_id)
                serializer = UpdateCourseSerializer(course, partial=True)
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response({'message': 'Course updated successfully', 'data': serializer.data}, status=status.HTTP_200_OK)

                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Course.DoesNotExist:
                return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

    def delete(self,request, course_id):
        """Delete course"""
        try:
            # course_name = request.data.get("name")
            course = Course.objects.get(pk=course_id)

            course.delete()
            return Response({"message": "Course deleted successfully"}, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({"message": "Invalid course name"}, status=status.HTTP_400_BAD_REQUEST)


class EnrollmentListCreateAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        
        user_id = request.query_params.get('user_id')
        course_id = request.query_params.get('course_id')

        queryset = Enrollment.objects.all()

        if user_id:
            queryset = queryset.filter(user_id=user_id)
        if course_id:
            queryset = queryset.filter(course_id=course_id)

        serializer = EnrollmentSerializer(queryset, many=True)
        return Response({'message': 'Enrollments retrieved successfully', 'data': serializer.data}, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = EnrollmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User enrolled successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




