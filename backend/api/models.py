from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from unidecode import unidecode

from account.models import Account

# Categories can be added by admin only (Admin Panel)
class Category(models.Model):
   name  = models.CharField(_("Name"), max_length=50, unique=True)
   slug  = models.SlugField(_("Slug"), null=True, blank=True)
   image = models.ImageField(_("Image"), upload_to='uploads/categories/', null=True, blank=True)

   class Meta:
      verbose_name_plural = 'Categories'

   def __str__(self):
      return self.name
   
   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(unidecode(self.name))
      return super(Category, self).save(*args, **kwargs)

class Item(models.Model):
   name        = models.CharField(_("Name"), max_length=50)
   slug        = models.SlugField(_("Slug"), unique=True, null=True, blank=True)
   image       = models.ImageField(_("Item's Image"), upload_to="uploads/items/%Y/%m/%d")
   description = models.TextField(_("Description"))
   is_active   = models.BooleanField(_("is Active"), default=False)
   createdAt   = models.DateTimeField(_("Created"), auto_now_add=True)
   updatedAt   = models.DateTimeField(_("Updated"), auto_now=True)
   requester   = models.ForeignKey(Account, verbose_name=_("Requester"), on_delete=models.CASCADE)
   category    = models.ForeignKey("Category", verbose_name=_("Category"), on_delete=models.CASCADE)

   def __str__(self):
      return self.name
   
   def save(self, *args, **kwargs):
      if not self.slug:
         self.slug = slugify(unidecode(self.name))
      return super(Item, self).save(*args, **kwargs)