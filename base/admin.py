import csv
from django.http import HttpResponse
from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import CPDataModel1, TPMDataModel, TargetingForms, CSVData, TPMCSVData, Sample1, ModaUser, ModaProjects, CFACList, CP_list, TPM_list, Province, VillageList, District
from django.utils.translation import ngettext
from import_export import resources

from import_export.admin import ImportExportModelAdmin

class CFACListResource(resources.ModelResource):
    class Meta:
        model = CFACList  # or 'core.Book'

admin.site.site_header = 'Targeting Admin'
admin.site.site_title = 'Targeting Admin'

from django.contrib.admin import SimpleListFilter

class SBaoFilter(SimpleListFilter):
    title = 'AO'
    parameter_name = 'SB_ao'
    
    def lookups(self, request, model_admin):
        # Return a list of tuples (value, human-readable name)
        aos = set([obj.cp_id.SB_ao for obj in model_admin.model.objects.all()])
        return [(ao, ao) for ao in aos]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(cp_id__SB_ao=self.value())
        return queryset

class SBprovinceFilter(SimpleListFilter):
    title = 'Province'
    parameter_name = 'SB_province'
    
    def lookups(self, request, model_admin):
        provinces = set([obj.cp_id.SB_province for obj in model_admin.model.objects.all()])
        return [(province, province) for province in provinces]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(cp_id__SB_province=self.value())
        return queryset

class SBdisrictFilter(SimpleListFilter):
    title = 'Disrict'
    parameter_name = 'SB_district'
    
    def lookups(self, request, model_admin):
        provinces = set([obj.cp_id.SB_district for obj in model_admin.model.objects.all()])
        return [(province, province) for province in provinces]
    
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(cp_id__SB_district=self.value())
        return queryset

def export_as_csv(modeladmin, request, queryset):
    model = queryset.model  # Get the model from the queryset
    model_name = model._meta.model_name.capitalize()
    meta = model._meta
    field_names = [field.name for field in meta.fields]

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename={model_name}.csv'
    writer = csv.writer(response)

    writer.writerow(field_names)
    for obj in queryset:
        row = writer.writerow([getattr(obj, field) for field in field_names])

    return response

export_as_csv.short_description = "Export Selected as CSV"

    
@admin.register(TargetingForms)
class TargetingFormsAdmin(admin.ModelAdmin):
    list_display = ('form_type', 'form_id', 'columns_list', 'area_office', 'created_at', 'updated_at', 'created_by')
    search_fields = ('form_type', 'form_id', 'area_office', 'created_by__username')
    list_filter = ('form_type', 'area_office', 'created_at', 'updated_at', 'created_by')
    
@admin.register(CPDataModel1)
class CSVDataAdmin(admin.ModelAdmin):
    list_display = ('name_ben', 'ben_fath', 'ben_gender', 'ben_age', 'key')
    search_fields = ('name_ben', 'ben_fath', 'key')
    list_filter = ('ben_gender', 'assessmentType', 'SB_ao', 'SB_province')

    fieldsets = (
        ('Basic Information', {
            'fields': ('phonenumber', 'username', 'email', 'assessmentType', 'data_assess')
        }),
        ('Location Information', {
            'fields': ('SB_ao', 'SB_B_1', 'SB_province', 'SB_B_2', 'SB_district', 'SB_area', 'SB_nahia', 'SB_cfac_name',
                       'SB_Name_of_the_village_Gozar_Elder', 'SB_Mobile_of_the_village_Gozar_Elder',
                       'SB_Name_of_the_village_Gozar_Elder_001', 'SB_Mobile_of_the_village_Gozar_Elder_001', 'SB_B_3')
        }),
        ('Assessment Details', {
            'fields': ('cp', 'ass_modality')
        }),
        ('Beneficiary Information', {
            'fields': ('name_ben', 'ben_fath', 'ben_gender', 'ben_age', 'mob', 'id_doc', 'id_doc_other', 'id_number')
        }),
        
        ('Return Information', {
            'fields': ('date_return', 'iom_id', 'is_principal')
        }),
        ('Principal Information', {
            'fields': ('name_p', 'p_fath', 'p_gender', 'p_age', 'p_mob', 'p_id_doc', 'p_id_doc_other', 'p_id_number')
        }),
        ('CFAC Information', {
            'fields': tuple(f'cfac_Q{i}' for i in range(1, 14)) + ('cfac_exclusion', )
        }),
        ('Observation', {
            'fields': ('observation',)
        }),
        ('Additional Information', {
            'fields': ('ag_work', 'alter_name', 'atlter_fath', 'alter_gender', 'alter_age', 'alter_mob',
                       'alter_id_doc', 'alter_id_doc_other', 'alter_id_number')
        }),
        ('Assessment Information', {
            'fields': tuple(f'A{i}' for i in range(1, 14)) + ('exclusion_1',)
        }),
        ('Child Information', {
            'fields': ('child_5', 'child_5Num', 'c1age', 'c1gen', 'c2age', 'c2gen', 'c3age', 'c3gen',
                       'c4age', 'c4gen', 'c5age', 'c5gen')
        }),
        ('PLW Information', {
            'fields': ('plw', 'pbw_num')
        }),
        ('Survey Information', {
            'fields': ('name_surv', 'mob_sur', 'tpm_org', 'tpm_name_surv', 'tpm_mob_sur')
        }),
        ('Calculations', {
            'fields': ('CFAC_Calculation', 'CP_Calculation', 'difference')
        }),
        ('Additional Fields', {
            'fields': ('FO_shortcut', 'vul', 'display_1', 'comm')
        }),
    )

   

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('key')
    
    actions = [export_as_csv]

@admin.register(TPMCSVData)
class TPMCSVDataAdmin(admin.ModelAdmin):
    list_display = ('name_ben', 'ben_fath', 'ben_gender', 'ben_age', '_id')
    search_fields = ('name_ben', 'ben_fath', '_id', 'ben_id')
    list_filter = ('ben_gender', 'assessmentType', 'SB_ao', 'SB_province')
    
    actions = [export_as_csv]

    fieldsets = (
        ('Basic Information', {
            'fields': ('phonenumber', 'username', 'email', 'assessmentType', 'ben_id', 'data_assess')
        }),
        ('Location Information', {
            'fields': ('SB_ao', 'SB_B_1', 'SB_province', 'SB_B_2', 'SB_district', 'SB_area', 'SB_nahia', 'SB_cfac_name',
                       'SB_Name_of_the_village_Gozar_Elder', 'SB_Mobile_of_the_village_Gozar_Elder',
                       'SB_Name_of_the_village_Gozar_Elder_001', 'SB_Mobile_of_the_village_Gozar_Elder_001', 'SB_B_3')
        }),
        ('Beneficiary Information', {
            'fields': ('cp', 'name_ben', 'ben_fath', 'ben_gender', 'ben_age', 'mob', 'id_doc', 'id_doc_other', 'id_number')
        }),
        ('Household Head', {
            'fields': ('HH_head_1', 'HH_head_2', 'HH_head_3', 'HH_head_5', 'HH_head_6')
        }),
        ('Return Information', {
            'fields': ('date_return', 'iom_id')
        }),
        ('Alternate Information', {
            'fields': ('alter_name', 'alter_gender', 'alter_age', 'alter_mob', 'alter_id_doc', 'alter_id_doc_other', 'alter_id_number')
        }),
        ('Assessment Information', {
            'fields': ('HHFound', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'exclusion_1')
        }),
        ('TPM Information', {
            'fields': ('tpm_org', 'tpm_name_surv', 'tpm_mob_sur', 'TPM_Calculation')
        }),
        ('Additional Information', {
            'fields': ('vul', 'comm')
        }),
        ('Metadata', {
            'fields': ('_id', '_uuid', '_submission_time', '_date_modified', '_version', '_duration', '_submitted_by')
        }),
    )

    readonly_fields = ('_id', '_uuid', '_submission_time', '_date_modified', '_version', '_duration', '_submitted_by')

    def get_queryset(self, request):
        return super().get_queryset(request).order_by('_id')
    
@admin.register(Sample1)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('ben_id', 'get_SB_ao', 'get_SB_province', 'get_district', 'get_nahia', 'get_cfac_name', 'is_urban', 'remarks', 'created_by', 'created_at')
    search_fields = ('get_SB_ao', 'get_SB_province', 'get_district')
    list_filter = (SBaoFilter, SBprovinceFilter,SBdisrictFilter, 'is_urban')
    
    actions = [export_as_csv]
    
    def get_SB_ao(self, obj):
        return obj.cp_id.SB_ao
    get_SB_ao.short_description = 'AO'
    
    
    def get_SB_province(self, obj):
        return obj.cp_id.SB_province
    get_SB_province.short_description = 'Province'
    
    def get_district(self, obj):
        return obj.cp_id.SB_district
    get_district.short_description = 'District'
    
    def get_nahia(self, obj):
        return obj.cp_id.SB_nahia
    get_nahia.short_description = 'Nahia'
    
    def get_cfac_name(self, obj):
        return obj.cp_id.SB_cfac_name
    
    get_cfac_name.short_description = 'CFAC Name'
    
    
    
    def get_queryset(self, request):
        return super().get_queryset(request).order_by('ben_id')
    
    
    
    
@admin.register(ModaProjects)
class ModaProjectsAdmin(admin.ModelAdmin):
    list_display = ('project_id', 'project_name','area_office')
    search_fields = ('project_name','area_office')  # Assuming created_by is linked to the User model

class ModaUserResource(resources.ModelResource):
    class Meta:
        model = ModaUser  # or 'core.Book'
        
@admin.register(ModaUser)
class ModaUserAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ('moda_username', 'moda_email', 'first_name', 'last_name', 'user_type', 'area_office', 'organization_short_name', 'is_active', 'access_given')
    search_fields = ('moda_username', 'moda_email', 'first_name', 'last_name')
    list_filter = ('user_type', 'area_office', 'is_active', 'access_given') 
    
    # not make name plural in admin view

@admin.register(CFACList)
class CFACListAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [CFACListResource]
    list_display = ('list_name', 'name', 'label', 'ao', 'province', 'district', 'CFAC_FP1', 'FP1_Number', 'CFAC_FP2', 'FP2_Number', 'Province_code', 'District_code', 'CFAC_Name')
    search_fields = ('name', 'label', 'province', 'district', 'CFAC_Name')
    list_filter = ('ao', 'province', 'district')

class CPListResource(resources.ModelResource):
    class Meta:
        model = CP_list  # or 'core.Book'
        
@admin.register(CP_list)
class CPListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [CPListResource]
    list_display = ('list_name', 'name', 'label_english', 'label_dari', 'label_pashto', 'ao', 'status', 'province')
    search_fields = ('name', 'label_english', 'label_dari', 'label_pashto', 'province')
    list_filter = ('ao', 'status', 'province')

class TPMListResource(resources.ModelResource):
    class Meta:
        model = TPM_list  # or 'core.Book'
@admin.register(TPM_list)
class TPMListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [TPMListResource]
    list_display = ('list_name', 'name', 'label_english', 'label_dari', 'label_pashto', 'ao', 'status', 'province')
    search_fields = ('name', 'label_english', 'label_dari', 'label_pashto', 'province')
    list_filter = ('ao', 'status', 'province')

class ProvinceResource(resources.ModelResource):
    class Meta:
        model = Province  # or 'core.Book'
@admin.register(Province)
class ProvinceAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [ProvinceResource]
    list_display = ('list_name', 'name', 'label', 'label_dari', 'label_pashto', 'ao')
    search_fields = ('name', 'label', 'label_dari', 'label_pashto')
    list_filter = ('ao',)

class VillageListResource(resources.ModelResource):
    class Meta:
        model = VillageList  # or 'core.Book'
        
@admin.register(VillageList)
class VillageListAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [VillageListResource]
    list_display = ('list_name', 'name', 'label', 'cfac_code', 'province', 'district', 'province_code', 'district_code', 'cfac_name', 'ao')
    search_fields = ('name', 'label', 'cfac_code', 'province', 'district', 'cfac_name')
    list_filter = ('ao', 'province', 'district')
    
class DistrictResource(resources.ModelResource):
    class Meta:
        model = District  # or 'core.Book'

@admin.register(District)
class DistrictAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_classes = [DistrictResource]
    list_display = ('list_name', 'name', 'label_english', 'label_dari', 'label_pashto', 'ao', 'status', 'province')
    search_fields = ('name', 'label_english', 'label_dari', 'label_pashto', 'province')
    list_filter = ('ao', 'province', 'status')
# admin.site.register(TargetingForms, TargetingFormsAdmin)
# admin.site.register(CSVData, CSVDataAdmin)