from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

# Create your models here.
class Sprint(models.Model):

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end


class Task(models.Model):

    STATUS_TODO=1
    STATUS_IN_PROGRESS=2
    STATUS_TESTING=3
    STATUS_DONE=4

    STATUS_CHOICE=(
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    )

    name = models.CharField(max_length=100)

    description = models.TextField(blank=True, default='')

    sprint = models.ForeignKey(Sprint, blank=True, null=True)

    status = models.SmallIntegerField(choices=STATUS_CHOICE, default=STATUS_TODO)

    order = models.SmallIntegerField(default=0)

    assigned = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)

    started = models.DateField(blank=True, null=True)
    
    due = models.DateField(blank=True, null=True)

    completed = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name

