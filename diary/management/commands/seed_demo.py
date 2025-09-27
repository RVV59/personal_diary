from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from diary.models import Entry

# Специально подготовленные данные для демонстрации
DEMO_DATA = [
    {
        'title': 'Отличный день в парке',
        'content': 'Сегодня был прекрасный солнечный день! Мы с друзьями отлично погуляли в парке.'
    },
    {
        'title': 'Ужасное совещание',
        'content': 'Чувствую сильное раздражение и гнев после рабочего созвона. Эта токсичная атмосфера меня убивает.'
    },
    {
        'title': 'Планы на следующую неделю',
        'content': 'Нужно запланировать встречу на следующей неделе. Обсудить детали проекта.'
    },
    {
        'title': 'Осенний вечер',
        'content': 'За окном дождь, и на душе немного тоскливо. Вспоминаю ушедшее лето, становится немного грустно.'
    },
]

class Command(BaseCommand):
    help = 'Очищает и заполняет базу данных демонстрационными записями.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Очистка старых данных...'))
        
        # Находим или создаем суперпользователя
        username = 'test'
        password = 'test'
        if not User.objects.filter(username=username).exists():
            self.stdout.write(f'Создание суперпользователя {username}...')
            User.objects.create_superuser(username, 'test@example.com', password)
        else:
            self.stdout.write(f'Суперпользователь {username} уже существует.')

        admin_user = User.objects.get(username=username)

        # Удаляем все записи этого пользователя, чтобы демонстрация была чистой
        Entry.objects.filter(author=admin_user).delete()
        self.stdout.write(self.style.SUCCESS('Старые записи удалены.'))

        self.stdout.write('Создание демонстрационных записей...')
        for item in DEMO_DATA:
            Entry.objects.create(
                author=admin_user,
                title=item['title'],
                content=item['content']
            )
        
        self.stdout.write(self.style.SUCCESS(f'Успешно создано {len(DEMO_DATA)} демонстрационных записей для пользователя {username}.'))
