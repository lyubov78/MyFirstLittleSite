from django.http import JsonResponse
from django.views.generic import TemplateView
from .forms import TemplateForm


class MyFormView(TemplateView):
    template_name = 'landing/index.html'

    def post(self, request, **kwargs):

        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму

        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP

            user_agent = request.META.get('HTTP_USER_AGENT')

            data = {
                'name': form.cleaned_data.get('name'),
                'email': form.cleaned_data.get('email'),
                'message': form.cleaned_data.get('message'),
                'ip': ip,
                'user_agent': user_agent
            }

            return JsonResponse(data,
                                json_dumps_params={'indent': 4, 'ensure_ascii': False})

        context = self.get_context_data(**kwargs)  # Получаем контекст, если он есть
        context["form"] = form  # Записываем в контекст форму
        return self.render_to_response(context)  # Возвращаем вызов метода render_to_response
