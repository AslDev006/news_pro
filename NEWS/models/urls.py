from django.urls import path
from .views import *
urlpatterns = [
    path('', homePageView, name='home'),
    path('404/', not_found, name='pg404'),
    path('news/<slug:slug>', single_page, name='single'),
    path('contact/', contact_page, name='contact'),
    path("category/national", NationalNews, name='national_news'),
    path("category/international", InterNational_News, name='international_news'),
    path("category/society", SocietyNews, name='society_news'),
    path("category/sport", SportNews, name='sport_news'),
    path("category/technology", TechnologyNews, name='technology_news'),
    path("category/fin", FinancialNews, name='financial_news'),
    # *** CRUD ***
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/create/', NewsCreateView.as_view(), name='create_news'),
    path('adminpage/', admin_page, name='admin_page'),
    # *** SEARCH ***
    path('search/', Search_View.as_view(), name='search')
]