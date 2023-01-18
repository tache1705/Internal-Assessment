"""Website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from frontPage.views import home_view, cover_page
from busTools.views import break_even, decision_tree, force_field, graphing, ffdiagram, graphdiagram, begraph, treediagram


urlpatterns = [
    path("", cover_page, name="Cover Page"),
    path("home/", home_view, name="Home Page"),
    path('admin/', admin.site.urls),
    path('breakeven/', break_even, name="Break-even"),
    path('begraph/', begraph, name="Break-even Graph"),
    path('decision/', decision_tree, name="Decision Tree"),
    path('treediagram/', treediagram, name="Decision Tree Diagram"),
    path('forcefield/', force_field, name="Force Field"),
    path("ffdiagram/", ffdiagram, name="Force Field Diagram"),
    path('graphing/', graphing, name="Graphing"),
    path('graphdiagram/', graphdiagram, name="Graph Final Diagram")
]
