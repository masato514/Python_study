import os

from django.db import models

from accounts.models import CustomUser

from django.core.validators import FileExtensionValidator

#import glob

class Play(models.Model):
    """プレイモデル"""


    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザー', on_delete = models.PROTECT)
    title = models.CharField(verbose_name = 'タイトル', max_length = 40)

    attach1 = models.FileField(
    verbose_name='添付ファイル',
    )

    attach2 = models.FileField(
    verbose_name='添付ファイル',
    default = 'なし',
    )

    attach3 = models.FileField(
    verbose_name='添付ファイル',
    default = 'なし',
    )

    

    created_at = models.DateTimeField(verbose_name = '作成日時', auto_now_add = True)
    update_at = models.DateTimeField(verbose_name = '更新日時', auto_now = True)

    class Meta:
        verbose_name_plural = 'Play'

    def __str__(self):
        return self.title