from django.db import models
from ckeditor.fields import RichTextField

class FaqType(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "FAQ Categories"

class Faq(models.Model):
    faqType_id = models.ForeignKey(FaqType, on_delete=models.DO_NOTHING)
    question = models.TextField()
    # answer = models.TextField()
    answer = RichTextField(blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.question

    class Meta:
        verbose_name_plural = "FAQs"
