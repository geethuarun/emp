from employees import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("employees",views.EmployeeViewset,basename="employee")



urlpatterns=[

]+router.urls