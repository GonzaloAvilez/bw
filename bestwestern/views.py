# coding: utf-8
import pyqrcode
from PIL import Image

from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic import ListView, TemplateView, FormView
from .forms import ContactForm
from slides.models import Slide

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        base_url =  "{0}://{1}{2}".format(
            self.request.scheme,
            self.request.get_host(),
            self.request.path + '34'
            )
        url = pyqrcode.QRCode(base_url, error='H')
        # url = pyqrcode.create(base_url)
        _qr = url.png('_url.png', scale=10)
        qr = Image.open('_url.png')
        qr = qr.convert("RGB")
        width, height = qr.size
        print(url.terminal(quiet_zone=1))
        logo = Image.open(self._get_hotel_logo())
        
        xmin = ymin = int((width/2) - (120/2))
        xmax = ymax = int((width/2) + (120/2))
        logo = logo.resize((xmax - xmin, ymax - ymin))
        qr.paste(logo, (xmin, ymin, xmax, ymax))

        qr.save('_url_logo.jpg')



        slides = Slide.objects.all().order_by('created_at')
        slides_quantity = slides.count()
        total_slides = []
        for i in range(0,slides_quantity):
            total_slides.append(i)
        context.update({
            'slides': slides,
            'total_slides': total_slides,
            })
        return context


    def _get_hotel_logo(self):
        storage = staticfiles_storage.path('img/BW_Logo.png')
        return storage



class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = 'home'


class ServicesView(TemplateView):
    template_name = 'services.html'

class RoomsView(TemplateView):
    template_name = 'rooms.html'


class ReservationPoliciesView(TemplateView):
    template_name = 'reservation_policies.html'


