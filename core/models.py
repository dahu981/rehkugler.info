from django.db import models


class LeadCapture(models.Model):
    email = models.EmailField()
    resource = models.CharField(max_length=50, choices=[
        ('eas', 'EAS-Leitfaden'),
        ('steuern', 'Steuern-Handout'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.email} – {self.resource} ({self.created_at:%Y-%m-%d})"
