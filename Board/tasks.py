from celery import shared_task
from Board.models import Board

@shared_task
def save_board(board_id, content):
    board = Board.objects.get(id=board_id)
    board.content = content
    board.save()
