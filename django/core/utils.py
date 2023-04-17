import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.utils import timezone
from django.utils.text import slugify


def save_to_import(file):
    """
    Save the 'file' into a temporary dir
    in order to be used by the task queue
    afterwards.
    """
    import_dir = os.path.join(settings.MEDIA_ROOT, 'import-files')
    file_name = '{name}-{now}.{ext}'.format(  # pylint: disable=consider-using-f-string
        name=slugify('.'.join(file.name.split('.')[:-1])),
        now=timezone.now(),
        ext=file.name.split('.')[-1],
    )
    full_dir = os.path.join(import_dir, file_name)

    # Write the file in chunks in order to support
    # bigger files.
    destination = default_storage.open(full_dir, 'wb+')
    for chunk in file.chunks():
        destination.write(chunk)
    destination.close()

    return full_dir
