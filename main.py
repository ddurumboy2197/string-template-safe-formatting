import string

def xavfsiz_tozalash(shablon, ma'lumotlar):
    template = string.Template(shablon)
    return template.substitute(ma'lumotlar)

shablon = "Salom, $name. Sizning yoshingiz $age."
ma'lumotlar = {"name": "Ali", "age": 25}
print(xavfsiz_tozalash(shablon, ma'lumotlar))
```

```python
import string

def xavfsiz_tozalash(shablon, ma'lumotlar):
    template = string.Template(shablon)
    return template.substitute(ma'lumotlar)

shablon = "Salom, ${name}. Sizning yoshingiz ${age}."
ma'lumotlar = {"name": "Ali", "age": 25}
print(xavfsiz_tozalash(shablon, ma'lumotlar))
