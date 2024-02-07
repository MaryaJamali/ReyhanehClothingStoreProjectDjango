from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from account.models import User
from django.contrib.auth import logout
from cart.models import Order, OrderDetail
from django.template.loader import render_to_string
from .forms import EditProfileModelForm, ChangePasswordForm


# Class_base_Template_View for UserPanelDashboard Page
@method_decorator(login_required, name='dispatch')
class UserPanelDashboardPage(TemplateView):
    template_name = 'user_panel/user-panel-dashboard.html'


# Class_base_View for EditUserProfile Page
@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')
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
@login_required
def user_panel_menu_component(request: HttpRequest):
    return render(request, 'user_panel/include/user-panel-menu-component.html')


# Function_base_View for user_basket
@login_required
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    # Product price calculation
    total_amount = current_order.calculate_total_price()
    context = {
        'order': current_order,
        'sum': total_amount
    }
    return render(request, 'user_panel/user-cart.html', context=context)


# Function_base_View for remove_order_detail
@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    # Product removal operation
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                             order__user_id=request.user.id).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel/include/user-cart-content.html', context=context)
    })


# Function_base_View for change_order_detail_count
@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')
    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id, order__is_paid=False).first()

    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    if state == 'increase':
        order_detail.count += 1
        order_detail.save()
    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False, user_id=request.user.id)
    total_amount = current_order.calculate_total_price()

    context = {
        'order': current_order,
        'sum': total_amount
    }
    return JsonResponse({
        'status': 'success',
        'body': render_to_string('user_panel/include/user-cart-content.html', context=context)
    })
