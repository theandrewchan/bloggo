from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #################################################################
    # Question 1
    #
    # REPLACE THE BELOW LINE with the correct view and URL for the about page
    url(r'^not_the_right_url/$', views.index, name='about'),
    #################################################################
    # Question 2
    #
    # Notice the (?P<pk>\d+) in the URL.
    # This captures any numberic value in that part of the URL and passes the number as a parameter
    # named 'pk' to the URL's view function.
    #
    # REPLACE THE BELOW LINE with the correct view and URL for the post details page
    url(r'^also_not_right/(?P<pk>\d+)$', views.index, name='post_details'),
]