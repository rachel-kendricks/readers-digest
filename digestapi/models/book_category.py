from django.db import models


class BookCategory(models.Model):
    date = models.DateField(auto_now_add=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
