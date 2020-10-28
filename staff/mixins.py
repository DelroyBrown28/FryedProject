from django.shortcuts import redirect


class StaffUserMixin(object):
    def dispath(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('home')
        return super(StaffUserMixin, self).dispath(request, *args, **kwargs)
