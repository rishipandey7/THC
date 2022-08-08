from django.urls import path
from . import views

urlpatterns = [
    path("", views.home,name="home"),
    path("about/", views.about,name="about"),
    path("contact/", views.contact,name="contact"),
    path("tracker/", views.tracker,name="tracker"),
    path("search/", views.search,name="search"),
    path("productview/<int:myid>", views.productview,name="productview"),
    path("checkout/", views.checkout,name="checkout"),
    path("updatetracker/", views.updatetracker,name="updatetracker"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    
    # path("", views.index,name="index"),
]
