import uuid
from django.db import models
from django.contrib.auth.models import User


CODE_SIZE = 6

def generate_random_code():
    return str(uuid.uuid4())[:CODE_SIZE].upper()


class Game(models.Model):
    DRAFT = 'draft'
    OPEN = 'open'
    RUNNING = 'running'
    FINISHED = 'finished'

    STATUS_CHOICES = (
        (DRAFT, 'Draft'),
        (OPEN, 'Open'),
        (RUNNING, 'Running'),
        (FINISHED, 'Finished')
    )

    title = models.CharField(max_length=64)
    code = models.CharField(max_length=CODE_SIZE, db_index=True, unique=True, default=generate_random_code)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default=DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"#{self.code} - {self.title}"


class GameCategory(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='categories')
    title = models.CharField(max_length=64)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title


class GamePlayer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='players')
    is_accepted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PlayerFact(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    player = models.ForeignKey(GamePlayer, on_delete=models.CASCADE)
    category = models.ForeignKey(GameCategory, on_delete=models.CASCADE)
    fact = models.CharField(max_length=64)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class GameRound(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    round = models.PositiveIntegerField()
    player_fact = models.ForeignKey(PlayerFact, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PlayerRoundScore(models.Model):
    game_round = models.ForeignKey(GameRound, on_delete=models.CASCADE)
    score = models.PositiveIntegerField(default=0)
    answer_1 = models.ForeignKey(GamePlayer, on_delete=models.CASCADE, null=True, related_name='rounds_as_1')
    answer_2 = models.ForeignKey(GamePlayer, on_delete=models.CASCADE, null=True, related_name='rounds_as_2')
    answer_3 = models.ForeignKey(GamePlayer, on_delete=models.CASCADE, null=True, related_name='rounds_as_3')
    is_voted = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


