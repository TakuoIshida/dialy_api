from django.db import models


class DialyModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)
    content = models.TextField(max_length=400, null=False)
    positiveSentiment = models.FloatField(null=False, default=0)
    negativeSentiment = models.FloatField(null=False, default=0)
    nutralSentiment = models.FloatField(null=False, default=0)
    mixedSentiment = models.FloatField(null=False, default=0)
    isDeleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
