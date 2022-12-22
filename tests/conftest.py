import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register

from core.models import User
from goals.models import Board, BoardParticipant, Category, Goal, Comment
from tests.factories import (
    UserFactory,
    BoardFactory,
    BoardParticipantFactory,
    CategoryFactory,
    GoalFactory,
    CommentFactory,
)
from todolist import settings


# @pytest.fixture(scope='session')
# def django_db_setup():
#     settings.DATABASES['default'] = {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'postgres',
#         'USER': 'postgres',
#         'PASSWORD': 'postgres',
#         'HOST': 'localhost',
#         'PORT': '5432',
#         'ATOMIC_REQUESTS': True,
#     }


@pytest.fixture
def add_user(db) -> User:
    user = User.objects.create_user(
        username='djohn',
        email='djohn@gmail.com',
        password='SuperPassword1022'
    )
    return user


@pytest.fixture
def auth_user(add_user: User) -> APIClient:
    client = APIClient()
    client.login(username='djohn', password='SuperPassword1022')
    return client


@pytest.fixture
def board() -> Board:
    return BoardFactory.create()


@pytest.fixture
def board_participant(add_user: User, board: Board) -> BoardParticipant:
    return BoardParticipantFactory.create(user=add_user, board=board)


@pytest.fixture
def category(board: Board, add_user: User, board_participant: BoardParticipant) -> Category:
    return CategoryFactory.create(board=board, user=add_user)


@pytest.fixture
def goal(category: Category, add_user: User) -> Goal:
    return GoalFactory.create(user=add_user, category=category)


@pytest.fixture
def comment(goal: Goal, add_user: User) -> Comment:
    return CommentFactory.create(user=add_user, goal=goal)
