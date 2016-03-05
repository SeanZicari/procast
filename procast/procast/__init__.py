from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory

my_session_factory = SignedCookieSessionFactory('tickles')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.set_session_factory(my_session_factory)
    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('faq', '/faq')
    config.add_route('contactme', '/contactme')
    config.scan()
    return config.make_wsgi_app()
