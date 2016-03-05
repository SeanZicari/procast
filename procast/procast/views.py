from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {}


@view_config(route_name='faq', renderer='templates/faq.jinja2')
def faq(request):
    return {}