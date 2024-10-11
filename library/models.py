from django.db import models


class Author(models.Model):
    """
    Модель автора
    """

    first_name = models.CharField(
        max_length=50,
        verbose_name="Имя",
        help_text="Имя автора (тип: строка, макс. длина - 50 символов).",
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name="Фамилия",
        help_text="Фамилия автора (тип: строка, макс. длина - 50 символов).",
    )
    birth_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата рождения",
        help_text="Дата рождения автора "
        "(тип: дата, необязательное поле, так как не для всех авторов известна).",
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """
    Модель книги.
    Удаляется каскадно при удалении автора
    """

    title = models.CharField(
        max_length=100,
        verbose_name="Название",
        help_text="Название книги (тип: строка, макс. длина - 100 символов).",
    )
    publication_date = models.DateField(
        verbose_name="Дата публикации", help_text="Дата выхода книги (тип: дата)."
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name="books",
        verbose_name="Автор",
        help_text="Автор книги (тип: целое число, ID модели Author).",
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
