from typing import Any
from django.contrib.auth.models import UserManager

class CustomUserManager(UserManager):
    def create_user(self, email, password, **extra_fields) -> Any:     
        user = self.model(
            email=self.normalize_email(email),
            username=extra_fields.pop('username', email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email: str | None, password: str | None, **extra_fields: Any) -> Any:
        extra_fields.setdefault('username', email)
        user  = self.create_user(
            email=self.normalize_email(email),
            password=password,
        )

        user.is_staff = True
        user.is_superuser = True
        user.eh_tutor = False
        user.save(using=self._db)
        return user
