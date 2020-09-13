""" Models for the base application.

All apps should use the BaseModel as parent for all models
"""

# django
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# base
from ..managers import BaseManager
from .. import utils


def get_new_id():
    """
    Get random string to be used as id
    """
    return utils.random_string(length=8, include_spaces=False)


# public methods
def file_path(self, name):
    """
    Generic method to give to a FileField or ImageField in it's upload_to
    parameter.

    This returns the name of the class, concatenated with the id of the
    object and the name of the file.
    """
    base_path = '{}/{}/{}'

    return base_path.format(
        self.__class__.__name__,
        utils.random_string(30),
        name
    )


class BaseModel(models.Model):
    """ An abstract class that every model should inherit from """
    BOOLEAN_CHOICES = ((False, _('No')), (True, _('Yes')))

    id = models.CharField(
        _('ID'),
        db_index=True,
        primary_key=True,
        max_length=8,
        unique=True,
        default=get_new_id,
    )
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this row should be treated as '
                    'active. Unselect this instead of deleting it.'),
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_("creation date"),
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        null=True,
        help_text=_("edition date"),
    )

    # using BaseManager
    objects = BaseManager()

    class Meta:
        """ set to abstract """
        abstract = True

    def save(self, *args, **kwargs):
        # ensure that the id is unique
        if not self.id:
            self.id = get_new_id()

            while (
                self.__class__.objects
                .filter(id=self.id)
                .exists()
            ):
                self.id = get_new_id()
        # finally save the object
        super(BaseModel, self).save(*args, **kwargs)

    # public methods
    def update(self, **kwargs):
        """ proxy method for the QuerySet: update method
        highly recommended when you need to save just one field

        """
        kwargs['updated_at'] = timezone.now()

        for kw in kwargs:
            self.__setattr__(kw, kwargs[kw])

        self.__class__.objects.filter(pk=self.pk).update(**kwargs)

    def to_dict(instance, fields=None, exclude=None):
        """
        Returns a dict containing the data in ``instance``

        ``fields`` is an optional list of field names. If provided, only the
        named fields will be included in the returned dict.

        ``exclude`` is an optional list of field names. If provided, the named
        fields will be excluded from the returned dict, even if they are listed
        in the ``fields`` argument.
        """

        opts = instance._meta
        data = {}
        for f in opts.fields + opts.many_to_many:
            if fields and f.name not in fields:
                continue
            if exclude and f.name in exclude:
                continue
            if isinstance(f, models.fields.related.ManyToManyField):
                # If the object doesn't have a primary key yet, just use an
                # emptylist for its m2m fields. Calling f.value_from_object
                # will raise an exception.
                if instance.pk is None:
                    data[f.name] = []
                else:
                    # MultipleChoiceWidget needs a list of pks, not objects.
                    data[f.name] = list(
                        f.value_from_object(instance)
                        .values_list('pk', flat=True)
                    )
            else:
                data[f.name] = f.value_from_object(instance)
        return data
