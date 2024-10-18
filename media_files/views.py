from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .helper import uploadProvinceInCsv, uploadDistrictInCsv, uploadtpmInCsv, uploadcpInCsv, uploadCFACInCsv, uploadVillageInCsv, user_access, uploadSample


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at media file handler app page.")

def uploadProvince(request):
    user = request.user
    try:
        uploadProvinceInCsv(user)
        return JsonResponse({'success': 'Province list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, Province list not uploaded'})
    
def uploadDistrict(request):
    user = request.user
    try:
        uploadDistrictInCsv(user)
        return JsonResponse({'success': 'District list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, District list not uploaded'})

def uploadTPM(request):
    user = request.user
    try:
        uploadtpmInCsv(user)
        return JsonResponse({'success': 'TPM list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, TPM list not uploaded'})
    
def uploadCP(request):
    user = request.user
    try:
        uploadcpInCsv(user)
        return JsonResponse({'success': 'CP list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, CP list not uploaded'})
    
def uploadCFAC(request):
    user = request.user
    try:
        uploadCFACInCsv(user)
        return JsonResponse({'success': 'CFAC list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, CFAC list not uploaded'})
    
def uploadVillages(request):
    user = request.user
    try:
        uploadVillageInCsv(user)
        return JsonResponse({'success': 'Village list uploaded successfully'})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, Village list not uploaded'})
    
def uploadSampleToMoDa(request):
    user = request.user
    try:
        uploadSample(user)
        return JsonResponse({'success': 'Sample list uploaded successfully'})
    except Exception as e:
        print(e)
        return JsonResponse({'error': f'{str(e)}, Sample list not uploaded'})
        
def update_user_access(request):
    try:
        a, b = user_access()
        return JsonResponse({'success': 'User access updated successfully, granted access to: '+str(a)+' and revoked access to: '+str(b)})
    except Exception as e:
        return JsonResponse({'error': f'{str(e)}, User access not updated'})
    
    
        
