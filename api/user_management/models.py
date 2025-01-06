from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.hashers import make_password
from datetime import date


def upload_path(instance, filename):
    return "/".join(["profile-image", filename])


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field is required.")
        if not password:
            raise ValueError("The Password field is required.")

        extra_fields.setdefault('is_active', True)
        user = self.model(email=self.normalize_email(email), **extra_fields)
        print("user", user)
        user.set_password(password)
        user.save(using=self._db)
        print("user after hadsed password", user)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")

        return self.create_user(email, password, **extra_fields)


class UserData(AbstractUser):
    ADMIN = 1
    OWNER = 2
    STAFF = 3
    USER_TYPE_CHOICES = (
        (ADMIN, "admin of the system"),
        (OWNER, "shop owner"),
        (STAFF, "staff in the branch"),
    )

    last_login = None
    is_superuser = None
    is_staff = None
    username = None
    first_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=6, null=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_type = models.IntegerField(choices=USER_TYPE_CHOICES, default=OWNER)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=1)
    profile_image = models.ImageField(
        blank=True, null=True, upload_to=upload_path, max_length=255
    )

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name","email","user_type"]

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.first_name

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_userdata_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_userdata_permissions',
        blank=True
    )
