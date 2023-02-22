from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAUTH(JWTAuthentication):
	
	# www_authenticate_realm = "api"
	# media_type = "application/json"

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	self.user_model = get_user_model()

	def authenticate(self, request):
		
		header = self.get_header(request)

		if header is None:
			raw_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE']) or None
		else:
			raw_token = self.get_raw_token(header)
		if raw_token is None:
			return None

		if raw_token:
			request.META['HTTP_AUTHORIZATION'] = f'Bearer {raw_token}'
		
		return super().authenticate(request)