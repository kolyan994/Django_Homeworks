import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_one_course(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/1/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == 1


@pytest.mark.django_db
def test_get_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_filter_course_list_by_id(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?id={courses[0].id}')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_filter_course_list_by_name(client, course_factory):
    courses = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?name={courses[0].name}')
    assert response.status_code == 200
    assert len(response.data) == 1
    assert response.data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', {'name': 'New Course'})
    assert response.status_code == 201
    assert Course.objects.filter(name='New Course').exists()


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    updated_data = {'name': 'Updated Course'}
    url = f'/api/v1/courses/{course.pk}/'
    response = client.put(url, updated_data)
    assert response.status_code == 200
    updated_course = Course.objects.get(pk=course.pk)
    assert updated_course.name == 'Updated Course'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    count = Course.objects.count()
    url = f'/api/v1/courses/{course.pk}/'
    response = client.delete(url)
    assert response.status_code == 204
    assert Course.objects.count() == count - 1
