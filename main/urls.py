from django.urls import path,include
from . import views
urlpatterns = [
    path('' ,views.main),
    path('about/',views.about),
    path('blog/',views.blog),
    path('index/',views.index)
    #    هان انا عملتش للمين مسار عشان اول مايفتح الصفحة على الاي بي الاساسي يظهرله المحتوى تبع الدالة ميين ثم بعد هيك كل دالة تانية عملتلها مسار عشان لما ينضاف فوق في الرابط يروح وينفذ المحتوى تبع الدالة

]
