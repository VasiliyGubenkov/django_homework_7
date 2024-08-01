from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100,
                            verbose_name="Название категории",
                            help_text="Напишите здесь название категории",
                            unique=True,
                            editable=True)
    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name='Название задачи',
                             help_text='Напишите название задачи',
                             null=False,
                             blank=False,
                             unique=True,
                             editable=True,
                             error_messages={
                                 'blank': 'Это поле не может быть пустым',
                                 'unique': 'Задача с таким названием уже существует'},
                             unique_for_date="date")
    description = models.TextField(verbose_name='Опиcание задачи',
                                   help_text='Подробно опишите эту задачу здесь',
                                   null=True,
                                   blank=True,
                                   editable=True)
    categories = models.ManyToManyField(Category,
                                        related_name='tasks',
                                        help_text='Категории, к которым относится задача')
    spisok_statusov = [('New', 'Новая'), ('In Progress', 'В процессе'), ('Pending', 'В ожидании'), ('Blocked', 'Заблокирована'), ('Done', 'Выполнена')]
    status = models.CharField(max_length=100,
                              choices=spisok_statusov,
                              verbose_name="Статус задачи",
                              help_text="Выберите статус задачи",
                              default='New')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайна',
                                    help_text='Укажите здесь дату и время дедлайна, для этой задачи',
                                    null=True,
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата и время создания задачи",
                                      help_text="Это дата и время, когда задача была создана",
                                      editable=False)
    date = models.DateField(auto_now=True,
                            verbose_name='Дата задачи',
                            help_text='Дата, к которой относится задача',
                            editable=False)
    def __str__(self):
        return self.title


class SubTask(models.Model):
    title = models.CharField(max_length=100,
                             verbose_name="Подзадача для основной задачи",
                             help_text="Укажите подзадачу для другой задачи",
                             unique=False,
                             editable=True,
                             null=False,
                             blank=False,
                             error_messages={'blank': 'Это поле не может быть пустым'})
    description = models.TextField(verbose_name="Описание поздадачи",
                                   help_text="Опишите подзадачу здесь",
                                   null=True,
                                   blank=True,
                                   editable=True)
    task = models.ForeignKey(Task,
                             on_delete=models.CASCADE,
                             related_name='subtasks')
    spisok_statusov = [('New', 'Новая'), ('In Progress', 'В процессе'), ('Pending', 'В ожидании'), ('Blocked', 'Заблокирована'), ('Done', 'Выполнена')]
    status = models.CharField(max_length=100,
                              choices=spisok_statusov,
                              verbose_name="Статус задачи",
                              help_text="Выберите статус задачи",
                              default='New')
    deadline = models.DateTimeField(verbose_name='Дата и время дедлайна',
                                    help_text='Укажите здесь дату и время дедлайна, для этой подзадачи',
                                    null=True,
                                    blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name="Дата и время создания подзадачи",
                                      help_text="Это дата и время, когда подзадача была создана",
                                      editable=False)

