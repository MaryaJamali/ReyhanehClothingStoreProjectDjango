from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from account.models import User
from django.contrib.auth import logout
from cart.models import Order
from .forms import EditProfileModelForm, ChangePasswordForm


# Class_base_Template_View for UserPanelDashboard Page
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/user-panel-dashboard.html'


# Class_base_View for EditUserProfile Page
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        # Fetch current user's information
        edit_form = EditProfileModelForm(instance=current_user)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit-profile.html', context=context)

    def post(self, request: HttpRequest):
        current_user = User.objects.filter(id=request.user.id).first()
        # With the "instance" field, the program understands the purpose of the edit
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            phone_number = edit_form.cleaned_data['phone_number']
            if not str(phone_number).isdigit() or len(str(phone_number)) != 11:
                edit_form.add_error('phone_number', 'شماره موبایل باید 11 رقمی و  شامل اعداد باشد')
            else:
                # It is stored directly on the database
                edit_form.save(commit=True)
        context = {
            'form': edit_form,
            'current_user': current_user
        }
        return render(request, 'user_panel/edit-profile.html', context=context)


# Class_base_View for ChangePassword Page
class ChangePasswordPage(View):
    def get(self, request: HttpRequest):
        context = {
            'form': ChangePasswordForm()
        }
        return render(request, 'user_panel/change-password.html', context=context)

    def post(self, request: HttpRequest):
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            current_user: User = User.objects.filter(id=request.user.id).first()
            if current_user.check_password(form.cleaned_data.get('current_password')):
                current_user.set_password(form.cleaned_data.get('password'))
                current_user.save()
                logout(request)
                return redirect(reverse('login_page_view'))
            else:
                form.add_error('password', 'کلمه عبور وارد شده اشتباه می باشد')
        context = {
            'form': form
        }
        return render(request, 'user_panel/change-password.html', context=context)


# Function_base_View for User_panel_menu
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/include/user-panel-menu-component.html')


# Function_base_View for user_basket
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'cart': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel/user-cart.html', context)
