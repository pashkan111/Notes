from django.db import models
import uuid


# Заметка должна содержать:
#     • заголовок
#     • содержимое (текст с поддержкой базового HTML-форматирования
#     • дату/время создания
#     • категорию:
#         ◦ Ссылка
#         ◦ Заметка
#         ◦ Памятка
#         ◦ TODO
#         ◦ …
#     • отметку “избранная”
#     • опциональный id для доступа по прямой ссылке (uuid)


class Category(models.Model):
    name = models.CharField(max_length=100)


class Note(models.Model):
    guid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=100)
    text = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name