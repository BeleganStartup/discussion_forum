# discussion_forum

Predict Systems Interview

**WARNING: .env file should never pushed to a git repository, but we do it in this case for testing purpose.**

`1/ python manage.py makemigrations`

`2/ python manage.py migrate`

`3/ python manage.py createsuperuser`

`4/ python manage.py runserver`


Testings:

- Only models are tested.
- Serializers are not tested.
- Views are not tested.
- Coverage is not enough, need more working.


Populating:

`1/ python manage.py shell`

`2/ from source.populate_db import *`

`3/ all_users = populate_users(50000)`

`4/ from forum.models import Like`

`5/ latest_post_likes = Like.objects.last()`

`5/ add_to_likes(all_users, latest_post_likes)`

