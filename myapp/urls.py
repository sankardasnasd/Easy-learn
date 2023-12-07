"""
URL configuration for Easy_learn project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', views.home),

    path('login/', views.login),
    path('login_post/', views.login_post),

    path('cng_pswrd/', views.cng_pswrd),
    path('cng_pswrd_pst/', views.cng_pswrd_pst),

    path('view_userprofile/', views.view_userprofile),

    path('complaint/', views.complaint),

    path('reply/<id>', views.reply),
    path('reply_pst/', views.reply_pst),

    path('review/', views.review),
    path('review_pst/', views.review_pst),

    path('alogout/', views.alogout),

###########USER#######

    path('register/', views.register),
    path('register_pst/', views.register_pst),

    path('u_cng_pswrd/', views.u_cng_pswrd),
    path('u_cng_pswrd_pst/', views.u_cng_pswrd_pst),

    path('user_home/', views.user_home),

    path('view_profile/', views.view_profile),

    path('edit_prof/', views.edit_prof),
    path('edit_prof_pst/', views.edit_prof_pst),




    path('user_alg/', views.user_alg),
    path('user_alg_post/', views.user_alg_post),
    path('user_file_upload_post/', views.user_file_upload_post),
    path('user_view_files/', views.user_view_files),

    path('sendreviewrating/', views.sendreviewrating),
    path('sendreviewrating_post/', views.sendreviewrating_post),


    path('logout/', views.logout),
]
