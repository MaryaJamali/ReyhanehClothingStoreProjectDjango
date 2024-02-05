from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.utils.crypto import get_random_string
from django.contrib.auth import login, logout
from account.forms import RegisterForm, LoginForm, ForgotPasswordForm, ResetPasswordForm
from django.http import HttpRequest
from django.contrib import messages
from .models import User
from utils.email_service import send_email


# Class_base_View for Register page
class RegisterView(View):
    def get(self, request: HttpRequest):
        # Making a prototype of the form
        register_form = RegisterForm()
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context=context)

    def post(self, request: HttpRequest):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            # The name of the received information taken from the Form for example('first_name')
            # With this command (cleaned_data) ---> Prints the desired information from the desired Form
            first_name = register_form.cleaned_data.get('first_name')
            last_name = register_form.cleaned_data.get('last_name')
            phone_number = register_form.cleaned_data.get('phone_number')
            user_email = register_form.cleaned_data.get('email')
            user_password = register_form.cleaned_data.get('password')
            # Checking the availability of the user
            user: bool = User.objects.filter(email__iexact=user_email).exists()
            if user:
                register_form.add_error('email', 'ایمیل وارد شده تکراری می باشد')
            elif not phone_number.isdigit() or len(phone_number) != 11:
                register_form.add_error('phone_number', 'شماره موبایل باید 11 رقمی و  شامل اعداد باشد')
            else:
                # Create user account for user
                new_user = User(
                    # The variable name is taken from the Model name for example(first_name = ...)
                    first_name=first_name,
                    last_name=last_name,
                    phone_number=phone_number,
                    email=user_email,
                    email_active_code=get_random_string(72),
                    is_active=False,
                    username=user_email)
                new_user.set_password(user_password)
                new_user.save()
                # Send account activation email to user
                send_email('فعالسازی حساب کاربری', new_user.email, {'user': new_user}, 'emails/activate-account.html')
                return redirect(reverse('login_page_view'))
        context = {
            'register_form': register_form
        }
        return render(request, 'account/register.html', context=context)


# Class_base_View for Login page
class ActivateAccountView(View):
    def get(self, request, email_active_code):
        user: User = User.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()
                messages.success(request, 'حساب کاربری شما با موفقیت فعال شد.')
                return redirect(reverse('login_page_view'))
            else:
                messages.info(request, 'حساب کاربری شما قبلاً فعال شده است.')
                return redirect(reverse('login_page_view'))

        return redirect(reverse('error_404_page_view'))


# Class_base_View for Login page
class LoginView(View):
    def get(self, request: HttpRequest):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }
        return render(request, 'account/login.html', context=context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            user_pass = login_form.cleaned_data.get('password')
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                if not user.is_active:
                    login_form.add_error('email', 'حساب کاربری شما فعال نشده است')
                else:
                    # Check the hashed password
                    is_password_correct = user.check_password(user_pass)
                    if is_password_correct:
                        # User login and setting cookies
                        login(request, user)
                        return redirect(reverse('user_panel_dashboard_page_view'))
                    else:
                        login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
            else:
                login_form.add_error('email', 'کاربری با مشخصات وارد شده یافت نشد')
        context = {
            'login_form': login_form
        }
        return render(request, 'account/login.html', context=context)


# Class_base_View for ForgetPassword page
class ForgetPasswordView(View):
    def get(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm()
        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account/forget-password.html', context=context)

    def post(self, request: HttpRequest):
        forget_pass_form = ForgotPasswordForm(request.POST)
        if forget_pass_form.is_valid():
            user_email = forget_pass_form.cleaned_data.get('email')
            # Get the user by email
            user: User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                # Send reset password email to user
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'emails/forgot-password.html')
                return redirect(reverse('home_page_view'))

        context = {
            'forget_pass_form': forget_pass_form
        }
        return render(request, 'account/forget-password.html', context=context)


# Class_base_View for ResetPassword page
class ResetPasswordView(View):
    def get(self, request: HttpRequest, active_code):
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return redirect(reverse('login_page_view'))
        reset_pass_form = ResetPasswordForm()
        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account/reset-password.html', context=context)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: User = User.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return redirect(reverse('error_404_page_view'))
            user_new_pass = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_pass)
            # generate new active code
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return redirect(reverse('login_page_view'))

        context = {
            'reset_pass_form': reset_pass_form,
            'user': user
        }
        return render(request, 'account/reset-password.html', context=context)


# Class_base_View for logout
class LogoutView(View):
    def get(self, request: HttpRequest):
        logout(request)
        return redirect(reverse('login_page_view'))
