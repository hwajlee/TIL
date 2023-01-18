# polls/models.py
from django.db import models
from django.conf import settings

class Question(models.Model):
    title = models.CharField(max_length=200)
    # 알아서 db 컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Reply(models.Model):
    content = models.CharField(max_length=200)
    # reply.____.all() => 이 reply와 M:N 관계를 가지고 있는 user들이 나와야 한다.
    vote_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        # user.____.all() => 이 User와 M:N Reply가 나와야 한다.
        related_name='vote_replies'
    )
    # db 컬럼은 user_id
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # db 컬럼은 question_id
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # instance method
    def is_voted(self, user): # reply.is_votedd(user) => True / False (답변에 해당 유저가 좋아요를 한 적 있는지?)
        return self.vote_users.filter(pk=user.pk).exists()