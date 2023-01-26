from .models import GeneralDTable
def get_notified(request):
    general_datable_1 = ""
    user = request.user
    if user.is_authenticated:
        general_datable_1 = GeneralDTable.objects.filter(etape = request.user.etape).values()  
        return {'general_datable_1' : general_datable_1}
    return {'general_datable_1' : general_datable_1}