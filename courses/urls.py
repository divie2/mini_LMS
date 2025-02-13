from django.urls import path

from courses import views


urlpatterns = [

    path('', views.Homepage.as_view(), name = 'homePage'),
    path('courses', views.CourseDetailApiView.as_view(), name='create-course'),
    path('courses/<str:course_id>', views.CourseDetailApiView.as_view(), name='list-course'),
    path('enrollments', views.EnrollmentListCreateAPIView.as_view(), name='enrollment-list'),


]