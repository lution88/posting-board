from django.db import models


class Posting(models.Model):
    class Meta:
        db_table = "posting"

    title = models.CharField("제목", max_length=20)
    content = models.CharField("본문", max_length=200)
    password = models.CharField("비밀번호", max_length=255)

    dt_created = models.DateTimeField("생성일", auto_now_add=True)
    dt_updated = models.DateTimeField("수정일", auto_now=True)

    def __str__(self):
        return self.title
