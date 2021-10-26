# Django
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    response = f"""
        <h2><a href="{reverse('post_list')}">Access to DRF Browsable API</a></h2>

        <h3> * List, Creart Post:</h3>
            <small>methods: GET, POST</small>
            <h4>/api/v1/post/</h4>
        <h3> * Retreive, Update, Delete Post: </h3>
            <small>methods: GET, PATCH, DELETE</small>
            <h4>/api/v1/post/<code>slug</code>/</h4>
        <h3> * Like/Unlike Post</h3>
            <small>methods: POST</small>
            <h4>/api/v1/post/<code>slug</code>/like/</h4>
    """
    return HttpResponse(response)
