from django import template
from account.forms import LoginForm

register = template.Library()


# InclusionTag for site_login_component
@register.inclusion_tag('base/site-login-component.html', takes_context=True)
def site_login_component(context):
    login_form = LoginForm()
    return {
        'login_form': login_form,
        'context': context
    }


# InclusionTag for site_search_component
@register.inclusion_tag('base/site-search-component.html')
def site_search_component():
    return
