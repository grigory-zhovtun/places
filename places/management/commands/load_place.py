import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Image, Place


class Command(BaseCommand):
    help = 'Загружает данные о локации из JSON по ссылке'

    def add_arguments(self, parser):
        parser.add_argument('json_url', type=str, help='Ссылка на JSON файл с данными')

    def handle(self, *args, **options):
        url = options['json_url']

        self.stdout.write(f"Скачиваю данные с {url}...")

        try:
            response = requests.get(url)
            response.raise_for_status()
            location = response.json()
        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(f"Критическая ошибка при скачивании JSON: {e}"))
            return

        try:
            place, created = Place.objects.get_or_create(
                title=location['title'],
                defaults={
                    'short_description': location['description_short'],
                    'long_description': location['description_long'],
                    'lng': location['coordinates']['lng'],
                    'lat': location['coordinates']['lat'],
                }
            )
        except KeyError as e:
            self.stdout.write(self.style.ERROR(f"В JSON отсутствуют обязательные поля: {e}"))
            return

        if created:
            self.stdout.write(self.style.SUCCESS(f"Локация создана: {place.title}"))
        else:
            self.stdout.write(f"Локация уже существует: {place.title}")
            return

        self.stdout.write("Начинаю загрузку фотографий...")

        img_urls = location.get('imgs', [])
        for index, img_url in enumerate(img_urls, start=1):
            try:
                img_response = requests.get(img_url)
                img_response.raise_for_status()

                img_name = img_url.split('/')[-1]
                content = ContentFile(img_response.content)

                new_image = Image(place=place, position=index)
                new_image.image.save(img_name, content, save=True)

                self.stdout.write(f" - Фото {index} ({img_name}) сохранено")

            except requests.exceptions.RequestException as e:
                self.stdout.write(self.style.WARNING(f" - Не удалось скачать фото {img_url}: {e}"))

        self.stdout.write(self.style.SUCCESS("Операция завершена успешно!"))