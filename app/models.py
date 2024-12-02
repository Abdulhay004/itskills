from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Internship(models.Model):
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    requirements = models.TextField()
    duration = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company_name} - {self.position}"


class InProgress(models.Model):
    internship = models.ForeignKey(Internship, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.user} - {self.internship}"



class Components(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class IconPack(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class DesignNewChanges(models.Model):
    description = models.TextField()
    date_changed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Change on {self.date_changed}"


class MobileApp(models.Model):
    version = models.CharField(max_length=50)
    changelog = models.TextField()
    release_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Version {self.version}"



class MobileAppWireframe(models.Model):
    app_version = models.ForeignKey(MobileApp, on_delete=models.CASCADE)
    description = models.TextField(blank=True)


    def __str__(self):
        return f"Wireframe for {self.app_version}"



