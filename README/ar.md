# Vali Mail

مكتبتي مخصصة للفحص والتحقق من عناوين البريد الإلكتروني بطرق متقدمة وفعّالة  

## المميزات

- تحقق من تنسيق البريد الإلكتروني وصحته.
- اكتشاف إذا ما كان البريد الإلكتروني موجودًا في قاعدة البيانات المسربة.
- دعم التحقق من نطاق البريد الإلكتروني.
- دعم مقارنة البريد الإلكتروني مع قائمة البريد السلبي (Blacklist).
- دعم للتكامل مع مزودي خدمات البريد الإلكتروني الشهيرة.

## التثبيت

يمكنك تثبيت المكتبة باستخدام الأمر التالي:


```python
pip install ValiMail
```

## How To Use

# اضافة المكتبة
```python
from ValiMail import vali_mail, check_domain_name, check_if_known,is_dispose_email
```

# استخدام متغيرات المكتبة لفحص الايميلات

```python
email = "example@email.com"
is_valid = vali_mail(email)
is_in_database = check_if_known(email)
is_valid_domain = check_domain_name(email)
is_dispose = is_dispose_email(email)
```
```python
# Print the results
print(f"Is valid email: {is_valid}")
print(f"Is in database: {is_in_database}")
print(f"Has valid domain: {is_valid_domain}")
print(f"Is blacklisted: {is_dispose}")
```


# example.py تم ادراج الكثير من الامثله في ملف 
