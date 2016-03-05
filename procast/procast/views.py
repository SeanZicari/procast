import logging

from pyramid.view import view_config
import pyramid.httpexceptions as exc

log = logging.getLogger(__name__)


@view_config(route_name='home', renderer='templates/index.jinja2')
def home(request):
    return {}


@view_config(route_name='faq', renderer='templates/faq.jinja2')
def faq(request):
    return {}


@view_config(route_name='contactme', request_method='POST')
def contactme(request):
    request.session.flash("We'll reach out to you shortly to get started!", queue='contact_form')
    return exc.HTTPFound(request.route_url('home'))