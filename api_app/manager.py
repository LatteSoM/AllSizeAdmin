from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, login, password, **extra_fields):
        if not login:
            raise ValueError("Username shoudn't be empty")
        if not password:
            raise ValueError("Password shoudn't be empty")
        # if not role_id:
        #     raise ValueError("role_id shoudn't be empty")
        from .models import Roles
        user = self.model(login=login, **extra_fields)
        extra_fields.setdefault("role_id", Roles.objects.get(name="user"))
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, login, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_superuser", True)
        # extra_fields.setdefault("is_staff", True)
        from .models import Roles
        extra_fields.setdefault("role_id", Roles.objects.get(name="user"))

        # if extra_fields.get("is_staff") is not True:
        #     raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get("role_id") is None:
            raise ValueError("Superuser must have role_id=admin.")
        return self.create_user(login, password, **extra_fields)
