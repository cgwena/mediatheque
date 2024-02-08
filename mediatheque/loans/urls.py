from django.contrib import admin
from django.urls import path
import loans.views


urlpatterns = [
    path('loan/<int:id>', loans.views.media_loan, name='media_loan'),
    path('loan_impossible', loans.views.loan_impossible, name='loan_impossible'),
    path('loan_late', loans.views.loan_late, name='loan_late'), 
]