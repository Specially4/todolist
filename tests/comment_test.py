import json

import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from core.models import User
from goals.models import Comment, Goal
from goals.serializers import CommentSerializer


@pytest.mark.django_db
def test_create(auth_user: APIClient, add_user: User, goal: Goal) -> None:
    response = auth_user.post(
        reverse('create_comment'),
        data={
           'text': 'test comment',
           'user': add_user.pk,
           'goal': goal.pk,
        },
    )
    expected_response = {
        'id': response.data.get('id'),
        'text': 'test comment',
        'goal': str(goal.pk),
        'created': response.data.get('created'),
        'updated': response.data.get('updated'),
    }

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_retrieve(auth_user: APIClient, add_user: User, comment: Comment, goal: Goal) -> None:
    response = auth_user.get(reverse('retrieve_comment', args=[comment.pk]))

    expected_response = CommentSerializer(instance=comment).data

    assert response.status_code == 200
    assert response.data == expected_response


@pytest.mark.django_db
def test_delete(auth_user: APIClient, goal: Goal, comment: Comment) -> None:
    response = auth_user.delete(reverse('retrieve_comment', args=[comment.pk]))

    assert response.status_code == 204


@pytest.mark.django_db
def test_update(auth_user: APIClient, goal: Goal, add_user: User, comment: Comment) -> None:
    response = auth_user.put(
        reverse('retrieve_comment', args=[comment.pk]),
        data=json.dumps({
            'text': 'put comment',
            'goal': goal.pk
        }),
        content_type='application/json'
    )

    assert response.status_code == 200
    assert response.data.get('text') == 'put comment'
