from django.db import models



class Image(models.Model):
    """Model for one images"""

    image = models.ImageField(upload_to="all_images")

    class Meta:
        verbose_name = "Фотографию"
        verbose_name_plural = "Фотографии"

    def __str__(self):
        return f"photo: {self.id}"


class Car(models.Model):
    """Модель для автомобиля"""

    ACTIVE = "active"
    PASSED = "passed"

    STATUS_CHOICES = (
        (ACTIVE, "Active"),
        (PASSED, "Passed"),
    )
    name = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    price = models.IntegerField()
    owners = models.IntegerField()
    engine = models.CharField(max_length=100)
    power = models.IntegerField()
    gearbox = models.CharField(max_length=100)
    drive = models.CharField(max_length=100)
    body_type = models.CharField(max_length=100)
    mileage = models.IntegerField()
    generation = models.CharField(max_length=100)
    complete_set = models.CharField(max_length=100)
    win_number = models.CharField(max_length=120)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default=ACTIVE)
    photos = models.ManyToManyField(Image)

    class Meta:
        verbose_name = "автомобиль"
        verbose_name_plural = "Автомобили"

    def __str__(self) -> str:
        return f"{self.name} | {self.age} | {self.mileage}"
