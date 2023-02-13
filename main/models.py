from django.db import models

# ORM Code


class Question(models.Model): # انشاء جدول وعملتله وراثة من كلاس موديلز والجدول عبارة عن  تخزين اسئلة على الداتا بيز 
    # انشاء الحقول
    question_text = models.CharField(max_length=12) # كاركتير واقصى طول للحقل هو 12
    created_at = models.DateTimeField(auto_now_add=True) # متى أنشأت السؤال يعني ايش التاريه اللي يسجله لتخزين السؤال في الجدول


    def __str__(self):
        # هذه عشان لما يعرض الحقل المخزن في الموقع في صفحة الادمن يعرض النص اللي دخله المستخدم مش اوبجكت 1 وابويجكت 2 وهكذا لا بدي اياه يعرضالنص المدحل
        return self.question_text