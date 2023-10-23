from django.urls import path, re_path
from .views import homePageView, aboutPageView, \
    articlePageView, search, date, filterView

urlpatterns = [
  path('', homePageView, name='home'),
  path('about/', aboutPageView, name='about'),
  path("articles/<int:id>/", articlePageView, name='article'),
  path("articles/<str:keyword>/<int:id>/", search),
  #path("articles/<int:year>/<int:month>/<slug:slug>/", date),
  re_path(r"^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$",date),
  #re_path("^articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-]+)/$",date),
  # shorter unnamed group - not recommend since introduce meaning of argument errors 
  #re_path("^articles/([0-9]{4})/([0-9]{2})/([\w-]+)/$",date), 
  
  # Exercise Solution
  # to run modify to def aboutPageView(request,id):
  #re_path(r"^articles/(?P<id>\d+)/$",aboutPageView),
  # to run modify to def aboutPageView(request,id,lang):
  #re_path(r"^search/(?P<id>[a-zA-Z_]+)/page/(?P<lang>[a-zA-Z]{2})/$",aboutPageView),
  
  path('filter/', filterView)
]
