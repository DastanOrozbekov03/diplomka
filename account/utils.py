from django.core.mail import send_mail


def send_activation_code(email, activation_code):
    message = f'''
    СИЗ БИЗДИН БАРАКЧАБЫЗГА КАТТАЛУУНУЗ ИЙГИЛИКТУУ ОТТУЮ
    СИЗДИН АККАУНТУНУЗДУ активдештируу учун код: \n{activation_code}
    '''

    send_mail(
        'Аккаунтту активдештируу',
        message,
        'test@gmail.com',
        [email ]    
    )