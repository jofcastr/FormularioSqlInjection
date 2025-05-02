from django.shortcuts import render
from form.models import User
from form.validators import FormValidator

def form(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')

        if not FormValidator.is_numeric(user_id):
            return render(request, 'form.html', {'error': 'Usuario invalido o no creado.'})

        try:
            user = User.objects.get(id=user_id)
            return render(request, 'form.html', {
                'nombre': user.first_name,
                'apellido': user.last_name,
                'resultado': True
            })
        except User.DoesNotExist:
            return render(request, 'form.html', {'error': 'Usuario invalido o no creado.'})
    else:
        return render(request, 'form.html')