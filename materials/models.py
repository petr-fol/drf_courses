from django.db import models

NULLABLE = {"null": True, "blank": True}


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="название", help_text="укажите название")
    description = models.TextField(verbose_name="описание", help_text="укажите описание")
    preview = models.ImageField(upload_to="media/courses/", verbose_name="превью", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta :
        verbose_name = "курс"
        verbose_name_plural = "курсы"


class Material(models.Model):
    title = models.CharField(max_length=100, verbose_name="название", help_text="укажите название")
    description = models.TextField(verbose_name="описание", help_text="укажите описание")
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, verbose_name="курс")
    video_link = models.URLField(verbose_name="ссылка на видео", help_text="укажите ссылку на видео", **NULLABLE)
    preview = models.ImageField(upload_to="media/materials/", verbose_name="превью", **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "материал"
        verbose_name_plural = "материалы"

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "урок"
        verbose_name_plural = "уроки"
