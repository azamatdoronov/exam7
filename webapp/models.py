from django.db import models


class BaseModel(models.Model):
    created_p = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_p = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Poll(BaseModel):
    question = models.TextField(max_length=300, null=False, blank=False, verbose_name="Вопрос")

    # tags = models.ManyToManyField("webapp.Tag", related_name="articles", blank=True)

    def __str__(self):
        return f"{self.id}. {self.question}"

    # def get_absolute_url(self):
    #     return reverse("article_view", kwargs={"pk": self.pk})

    class Meta:
        db_table = "polls"
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"


class Choice(BaseModel):
    text_answer = models.TextField(max_length=500, null=False, blank=False, verbose_name='Ответ')
    poll = models.ForeignKey("webapp.Poll", on_delete=models.CASCADE, related_name="choices",
                             verbose_name='Опрос')

    def __str__(self):
        return f"{self.id}. {self.text_answer}"

    class Meta:
        db_table = "choices"
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


# class Tag(BaseModel):
#     name = models.CharField(max_length=31, verbose_name='Тег')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = "tags"
#         verbose_name = "Тэг"
#         verbose_name_plural = "Тэги"
