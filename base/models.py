from django.db import models
from django.contrib.auth.models import User
from  django.conf import settings

# Create your models here.

class CPDataModel(models.Model):
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    today = models.DateField(null=True)
    deviceid = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    tit = models.CharField(max_length=1, null=True)
    assessmentType = models.CharField(max_length=50)
    data_assess = models.DateTimeField()
    SB_ao = models.CharField(max_length=10)
    SB_B_1 = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    SB_B_2 = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    SB_area = models.IntegerField()
    SB_nahia = models.IntegerField(null=True)
    SB_cfac_name = models.CharField(max_length=255, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=20, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=20, null=True)
    SB_B_3 = models.CharField(max_length=255, null=True)
    cp = models.CharField(max_length=150)
    infonote = models.CharField(max_length=1, null=True)
    ass_modality = models.IntegerField(max_length=255)
    name_ben = models.CharField(max_length=255)
    ben_fath = models.CharField(max_length=255)
    ben_gender = models.CharField(max_length=10)
    ben_age = models.IntegerField()
    female_status = models.CharField(max_length=15, null=True)
    mob = models.CharField(max_length=10, null=True)
    id_doc = models.CharField(max_length=10)
    id_doc_other = models.CharField(max_length=255,  null=True)
    id_number = models.CharField(max_length=100, null=True)
    HH_head = models.CharField(max_length=25, null=True)
    date_return = models.DateField(null=True)
    iom_id = models.CharField(max_length=100, null=True)
    is_principal = models.BooleanField(null=True)
    name_p = models.CharField(max_length=255,null=True)
    p_fath = models.CharField(max_length=255,null=True)
    p_gender = models.CharField(max_length=10, null=True)
    p_age = models.IntegerField(null=True)
    p_mob = models.CharField(max_length=10, null=True)
    p_id_doc = models.CharField(max_length=255, null=True), 
    p_id_doc_other = models.CharField(max_length=255, null=True)
    p_id_number = models.CharField(max_length=100, null=True)
    cfac_Q1 = models.BooleanField(null=True)
    cfac_Q2 = models.BooleanField(null=True)
    cfac_Q3 = models.BooleanField(null=True)
    cfac_Q4 = models.BooleanField(null=True)
    cfac_Q5 = models.BooleanField(null=True)
    cfac_Q6 = models.BooleanField(null=True)
    cfac_Q7 = models.BooleanField(null=True)
    cfac_Q8 = models.BooleanField(null=True)
    cfac_Q9 = models.BooleanField(null=True)
    cfac_Q10 = models.BooleanField(null=True)
    cfac_Q11 = models.BooleanField(null=True)
    cfac_Q12 = models.BooleanField(null=True)
    cfac_Q13 = models.BooleanField(null=True)
    cfac_exclusion = models.BooleanField(null=True)
    ass_modality = models.BooleanField(null=True)
    observation = models.BooleanField(null=True)
    ag_work = models.BooleanField(null=True)
    alter_name = models.CharField(max_length=255,null=True)
    atlter_fath = models.CharField(max_length=255,null=True)
    alter_gender = models.CharField(max_length=10,null=True)
    alter_age = models.IntegerField(null=True)
    alter_mob = models.CharField(max_length=10,null=True)
    alter_id_doc = models.CharField(max_length=255,null=True)
    alter_id_doc_other = models.CharField(max_length=255, null=True)
    alter_id_number = models.CharField(max_length=255,null=True)
    A1 = models.BooleanField()
    A2 = models.BooleanField()
    A3 = models.BooleanField()
    A4 = models.BooleanField()
    A5 = models.BooleanField()
    A6 = models.BooleanField()
    A7 = models.BooleanField()
    A8 = models.BooleanField()
    A9 = models.BooleanField()
    A10 = models.BooleanField()
    A11 = models.BooleanField()
    A12 = models.BooleanField()
    A13 = models.BooleanField()
    exclusion_1 = models.BooleanField()
    child_5 = models.BooleanField()
    child_5Num = models.IntegerField(null=True)
    c1age = models.IntegerField(null=True)
    c1gen = models.CharField(max_length=10, null=True)
    c2age = models.IntegerField(null=True)
    c2gen = models.CharField(max_length=10, null=True)
    c3age = models.IntegerField(null=True)
    c3gen = models.CharField(max_length=10,null=True)
    c4age = models.IntegerField(null=True)
    c4gen = models.CharField(max_length=10,null=True)
    c5age = models.IntegerField(null=True)
    c5gen = models.CharField(max_length=10,null=True)
    plw = models.BooleanField()
    pbw_num = models.IntegerField()
    name_surv = models.CharField(max_length=255)
    mob_sur = models.CharField(max_length=10)
    tpm_org = models.CharField(max_length=255, null=True)
    tpm_name_surv = models.CharField(max_length=255, null=True)
    tpm_mob_sur = models.CharField(max_length=20, null=True)
    CFAC_Calculation = models.IntegerField()
    CP_Calculation = models.IntegerField()
    difference = models.IntegerField()
    FO_shortcut = models.CharField(max_length=255)
    vul = models.CharField(max_length=10)
    vul_note = models.CharField(max_length=10, null=True)
    display = models.CharField(max_length=255, null=True)
    display_1 = models.CharField(max_length=255, null=True)
    comm = models.CharField(max_length=255, null=True)
    meta_instanceID = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=100, null=True)
    note = models.CharField(max_length=100, null=True)
    isValidated = models.BooleanField(null=True)
    id_r = models.CharField(max_length=100, null=True)
    # _id = models.IntegerField(unique=True)
    # _uuid = models.CharField(max_length=255)
    # _submission_time = models.DateTimeField()
    SubmissionDate = models.DateTimeField()
    formhub_uuid = models.UUIDField(null=True)
    # _duration = models.IntegerField()
    # _submitted_by = models.CharField(max_length=255)
    # _xform_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.key
    
    verbose_name = 'CP Data '
    verbose_name_plural = 'CP Data'

class CPDataModel1(models.Model):
    MODALITY = [
        (1, 'FOOD'),
        (2, 'CBT'),
    ]
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    today = models.DateField(null=True)
    deviceid = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    tit = models.CharField(max_length=1, null=True)
    assessmentType = models.CharField(max_length=50)
    data_assess = models.DateTimeField()
    SB_ao = models.CharField(max_length=10)
    SB_B_1 = models.CharField(max_length=50)
    SB_province = models.CharField(max_length=50)
    SB_B_2 = models.CharField(max_length=50)
    SB_district = models.CharField(max_length=50)
    SB_area = models.IntegerField()
    SB_nahia = models.IntegerField(null=True)
    SB_cfac_name = models.CharField(max_length=255, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=20, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=20, null=True)
    SB_B_3 = models.CharField(max_length=255, null=True)
    cp = models.CharField(max_length=150)
    infonote = models.CharField(max_length=1, null=True)
    ass_modality = models.IntegerField(choices=MODALITY)
    name_ben = models.CharField(max_length=255)
    ben_fath = models.CharField(max_length=255)
    ben_gender = models.CharField(max_length=10)
    ben_age = models.IntegerField()
    female_status = models.CharField(max_length=15, null=True)
    mob = models.CharField(max_length=10, null=True)
    id_doc = models.CharField(max_length=10)
    id_doc_other = models.CharField(max_length=255,  null=True)
    id_number = models.CharField(max_length=100, null=True)
    HH_head = models.CharField(max_length=25, null=True)
    date_return = models.DateField(null=True)
    iom_id = models.CharField(max_length=100, null=True)
    is_principal = models.BooleanField(null=True)
    name_p = models.CharField(max_length=255,null=True)
    p_fath = models.CharField(max_length=255,null=True)
    p_gender = models.CharField(max_length=10, null=True)
    p_age = models.IntegerField(null=True)
    p_mob = models.CharField(max_length=10, null=True)
    p_id_doc = models.CharField(max_length=255, null=True)
    p_id_doc_other = models.CharField(max_length=255, null=True)
    p_id_number = models.CharField(max_length=100, null=True)
    cfac_Q1 = models.BooleanField(null=True)
    cfac_Q2 = models.BooleanField(null=True)
    cfac_Q3 = models.BooleanField(null=True)
    cfac_Q4 = models.BooleanField(null=True)
    cfac_Q5 = models.BooleanField(null=True)
    cfac_Q6 = models.BooleanField(null=True)
    cfac_Q7 = models.BooleanField(null=True)
    cfac_Q8 = models.BooleanField(null=True)
    cfac_Q9 = models.BooleanField(null=True)
    cfac_Q10 = models.BooleanField(null=True)
    cfac_Q11 = models.BooleanField(null=True)
    cfac_Q12 = models.BooleanField(null=True)
    cfac_Q13 = models.BooleanField(null=True)
    cfac_exclusion = models.BooleanField(null=True)
    # ass_modality = models.BooleanField(null=True)
    observation = models.BooleanField(null=True)
    ag_work = models.BooleanField(null=True)
    alter_name = models.CharField(max_length=255,null=True)
    atlter_fath = models.CharField(max_length=255,null=True)
    alter_gender = models.CharField(max_length=10,null=True)
    alter_age = models.IntegerField(null=True)
    alter_mob = models.CharField(max_length=10,null=True)
    alter_id_doc = models.CharField(max_length=255,null=True)
    alter_id_doc_other = models.CharField(max_length=255, null=True)
    alter_id_number = models.CharField(max_length=255,null=True)
    A1 = models.BooleanField()
    A2 = models.BooleanField()
    A3 = models.BooleanField()
    A4 = models.BooleanField()
    A5 = models.BooleanField()
    A6 = models.BooleanField()
    A7 = models.BooleanField()
    A8 = models.BooleanField()
    A9 = models.BooleanField()
    A10 = models.BooleanField()
    A11 = models.BooleanField()
    A12 = models.BooleanField()
    A13 = models.BooleanField()
    exclusion_1 = models.BooleanField()
    child_5 = models.BooleanField()
    child_5Num = models.IntegerField(null=True)
    c1age = models.IntegerField(null=True)
    c1gen = models.CharField(max_length=10, null=True)
    c2age = models.IntegerField(null=True)
    c2gen = models.CharField(max_length=10, null=True)
    c3age = models.IntegerField(null=True)
    c3gen = models.CharField(max_length=10,null=True)
    c4age = models.IntegerField(null=True)
    c4gen = models.CharField(max_length=10,null=True)
    c5age = models.IntegerField(null=True)
    c5gen = models.CharField(max_length=10,null=True)
    plw = models.BooleanField()
    pbw_num = models.IntegerField(null=True)
    name_surv = models.CharField(max_length=255)
    mob_sur = models.CharField(max_length=10)
    tpm_org = models.CharField(max_length=255, null=True)
    tpm_name_surv = models.CharField(max_length=255, null=True)
    tpm_mob_sur = models.CharField(max_length=20, null=True)
    CFAC_Calculation = models.IntegerField()
    CP_Calculation = models.IntegerField()
    difference = models.IntegerField()
    FO_shortcut = models.CharField(max_length=255)
    vul = models.CharField(max_length=10)
    vul_note = models.CharField(max_length=10, null=True)
    display = models.CharField(max_length=255, null=True)
    display_1 = models.CharField(max_length=255, null=True)
    comm = models.CharField(max_length=255, null=True)
    meta_instanceID = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=100, unique=True)
    note = models.CharField(max_length=100, null=True)
    isValidated = models.BooleanField(null=True)
    id_r = models.CharField(max_length=100, null=True)
    # _id = models.IntegerField(unique=True)
    # _uuid = models.CharField(max_length=255)
    # _submission_time = models.DateTimeField()
    SubmissionDate = models.DateTimeField()
    formhub_uuid = models.UUIDField(null=True)
    # _duration = models.IntegerField()
    # _submitted_by = models.CharField(max_length=255)
    # _xform_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, )
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "CP Data"
        verbose_name_plural = "CP Data"

class TPMDataModel(models.Model):
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    today = models.DateField(null=True)
    deviceid = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    assessmentType = models.CharField(max_length=50)
    ben_id = models.IntegerField() # check to make it duplicate
    data_assess = models.DateTimeField()
    SB_ao = models.CharField(max_length=10)
    SB_B_1 = models.CharField(max_length=50)
    SB_B_2 = models.CharField(max_length=50)
    SB_nahia = models.IntegerField()
    SB_cfac_name = models.CharField(max_length=255, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=20, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=20, null=True)
    SB_B_3 = models.CharField(max_length=255, null=True)
    cp = models.CharField(max_length=150)
    name_ben = models.CharField(max_length=255)
    ben_fath = models.CharField(max_length=255)
    ben_gender = models.CharField(max_length=10)
    ben_age = models.IntegerField()
    mob = models.CharField(max_length=10)
    id_doc = models.CharField(max_length=10)
    id_doc_other = models.CharField(max_length=255,  null=True)
    id_number = models.CharField(max_length=100)
    HH_head_1 = models.BooleanField(null=True)
    HH_head_2 = models.BooleanField(null=True)
    HH_head_3 = models.BooleanField(null=True)
    HH_head_4 = models.BooleanField(null=True)
    HH_head_5 = models.BooleanField(null=True)
    HH_head_6 = models.BooleanField(null=True)
    alter_name = models.CharField(max_length=255,null=True)
    atlter_fath = models.CharField(max_length=255,null=True)
    alter_gender = models.CharField(max_length=10,null=True)
    alter_age = models.IntegerField(null=True)
    alter_mob = models.CharField(max_length=10,null=True)
    A1 = models.BooleanField()
    A2 = models.BooleanField()
    A3 = models.BooleanField()
    A4 = models.BooleanField()
    A5 = models.BooleanField()
    A6 = models.BooleanField()
    A7 = models.BooleanField()
    A8 = models.BooleanField()
    A9 = models.BooleanField()
    A10 = models.BooleanField()
    A11 = models.BooleanField()
    A12 = models.BooleanField()
    A13 = models.BooleanField()
    exclusion_1 = models.BooleanField()
    note_sur = models.CharField(max_length=1, null=True)
    tpm_org = models.CharField(max_length=255, null=True)
    tpm_name_surv = models.CharField(max_length=255, null=True)
    tpm_mob_sur = models.CharField(max_length=20, null=True)
    TPP_Calculation = models.IntegerField()
    vul = models.CharField(max_length=3)
    comm = models.CharField(max_length=255, null=True)
    meta_instanceID = models.CharField(max_length=255, null=True)
    _id = models.IntegerField(unique=True)
    _uuid = models.CharField(max_length=255)
    _submission_time = models.DateTimeField()
    _duration = models.IntegerField()
    _submitted_by = models.CharField(max_length=255)
    _xform_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
    class Meta:
        verbose_name = 'TPM Data'
        verbose_name_plural = 'TPM Data'
    


class EstimatedErros(models.Model):
    is_urban = models.BooleanField(default=False)
    pd_number = models.IntegerField(null=True)
    district = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    inclusion_error = models.FloatField(null=True)
    exlusio_error = models.FloatField(null=True)
    
    def __str__(self):
        if self.is_urban:
            return self.province + self.district + ' Urban'
        else:
            return self.province + self.district + ' Rural'
        
class CSVData(models.Model):
    phonenumber = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    assessmentType = models.CharField(max_length=255, null=True, blank=True)
    data_assess = models.DateTimeField(null=True, blank=True)
    SB_ao = models.CharField(max_length=255, null=True, blank=True)
    SB_B_1 = models.CharField(max_length=255, null=True, blank=True)
    SB_province = models.CharField(max_length=255, null=True, blank=True)
    SB_B_2 = models.CharField(max_length=255, null=True, blank=True)
    SB_district = models.CharField(max_length=255, null=True, blank=True)
    SB_area = models.CharField(max_length=255, null=True, blank=True)
    SB_nahia = models.CharField(max_length=255, null=True, blank=True)
    SB_cfac_name = models.CharField(max_length=255, null=True, blank=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True, blank=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True, blank=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True, blank=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True, blank=True)
    SB_B_3 = models.CharField(max_length=255, null=True, blank=True)
    cp = models.CharField(max_length=255, null=True, blank=True)
    ass_modality = models.CharField(max_length=255, null=True, blank=True)
    name_ben = models.CharField(max_length=255, null=True, blank=True)
    ben_fath = models.CharField(max_length=255, null=True, blank=True)
    ben_gender = models.CharField(max_length=255, null=True, blank=True)
    ben_age = models.IntegerField(null=True, blank=True)
    mob = models.CharField(max_length=255, null=True, blank=True)
    id_doc = models.CharField(max_length=255, null=True, blank=True)
    id_doc_other = models.CharField(max_length=255, null=True, blank=True)
    id_number = models.CharField(max_length=255, null=True, blank=True)
    date_return = models.DateField(null=True, blank=True)
    iom_id = models.CharField(max_length=255, null=True, blank=True)
    is_principal = models.BooleanField(null=True, blank=True)
    name_p = models.CharField(max_length=255, null=True, blank=True)
    p_fath = models.CharField(max_length=255, null=True, blank=True)
    p_gender = models.CharField(max_length=255, null=True, blank=True)
    p_age = models.IntegerField(null=True, blank=True)
    p_mob = models.CharField(max_length=255, null=True, blank=True)
    p_id_doc = models.CharField(max_length=255, null=True, blank=True)
    p_id_doc_other = models.CharField(max_length=255, null=True, blank=True)
    p_id_number = models.CharField(max_length=255, null=True, blank=True)
    cfac_consulted = models.BooleanField(null=True, blank=True)
    observation = models.TextField(null=True, blank=True)
    ag_work = models.BooleanField(null=True, blank=True)
    alter_name = models.CharField(max_length=255, null=True, blank=True)
    atlter_fath = models.CharField(max_length=255, null=True, blank=True)
    alter_gender = models.CharField(max_length=255, null=True, blank=True)
    alter_age = models.IntegerField(null=True, blank=True)
    alter_mob = models.CharField(max_length=255, null=True, blank=True)
    alter_id_doc = models.CharField(max_length=255, null=True, blank=True)
    alter_id_doc_other = models.CharField(max_length=255, null=True, blank=True)
    alter_id_number = models.CharField(max_length=255, null=True, blank=True)
    child_5 = models.BooleanField(null=True, blank=True)
    child_5Num = models.IntegerField(null=True, blank=True)
    c1age = models.IntegerField(null=True, blank=True)
    c1gen = models.CharField(max_length=255, null=True, blank=True)
    c2age = models.IntegerField(null=True, blank=True)
    c2gen = models.CharField(max_length=255, null=True, blank=True)
    c3age = models.IntegerField(null=True, blank=True)
    c3gen = models.CharField(max_length=255, null=True, blank=True)
    c4age = models.IntegerField(null=True, blank=True)
    c4gen = models.CharField(max_length=255, null=True, blank=True)
    c5age = models.IntegerField(null=True, blank=True)
    c5gen = models.CharField(max_length=255, null=True, blank=True)
    plw = models.BooleanField(null=True, blank=True)
    pbw_num = models.IntegerField(null=True, blank=True)
    name_surv = models.CharField(max_length=255, null=True, blank=True)
    mob_sur = models.CharField(max_length=255, null=True, blank=True)
    tpm_org = models.CharField(max_length=255, null=True, blank=True)
    tpm_name_surv = models.CharField(max_length=255, null=True, blank=True)
    tpm_mob_sur = models.CharField(max_length=255, null=True, blank=True)
    CFAC_Calculation = models.IntegerField(null=True, blank=True)
    CP_Calculation = models.IntegerField(null=True, blank=True)
    difference = models.IntegerField(null=True, blank=True)
    FO_shortcut = models.CharField(max_length=255, null=True, blank=True)
    vul = models.BooleanField(null=True, blank=True)
    display_1 = models.CharField(max_length=255, null=True, blank=True)
    comm = models.TextField(null=True, blank=True)
    meta_instanceID = models.CharField(max_length=255, null=True, blank=True)
    meta_instanceName = models.CharField(max_length=255, null=True, blank=True)
    _id = models.IntegerField(unique=True)
    _uuid = models.UUIDField(null=True, blank=True)
    _submission_time = models.DateTimeField(null=True, blank=True)
    _date_modified = models.DateTimeField(null=True, blank=True)
    _version = models.CharField(max_length=255, null=True, blank=True)
    _duration = models.IntegerField(null=True, blank=True)
    _submitted_by = models.CharField(max_length=255, null=True, blank=True)
    _xform_id = models.IntegerField(null=True, blank=True)

    # Boolean fields for Yes/No values
    for i in range(1, 14):
        locals()[f'cfac_Q{i}'] = models.BooleanField(null=True, blank=True)
        locals()[f'A{i}'] = models.BooleanField(null=True, blank=True)

    cfac_exclusion = models.BooleanField(null=True, blank=True)
    exclusion_1 = models.BooleanField(null=True, blank=True)

    # Female status fields
    for i in range(1, 9):
        locals()[f'female_status_{i}'] = models.BooleanField(null=True, blank=True)

    # HH_head fields
    for i in [1, 2, 3, 5, 6]:
        locals()[f'HH_head_{i}'] = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return f"{self.name_ben} - {self._id}"

    # class Meta:
    #     verbose_name = "CP Data"
    #     verbose_name_plural = "CP Data"

class Sample1(models.Model):
    TYPE_LIST = (
        ('Regular', 'Regular'),
        ('Borderline', 'Borderline')
    )
    is_urban = models.BooleanField()
    ben_id = models.IntegerField(unique=True)
    sample_type = models.CharField(max_length=20,choices=TYPE_LIST)
    cp_id = models.ForeignKey(CPDataModel1, on_delete=models.RESTRICT, null=True)
    key = models.CharField(max_length=100, null=True)
    remarks = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.DO_NOTHING)
    
    def __str__(self):
        if self.is_urban:
            return 'Urban'
        else:
            return 'Rural'
        
    class Meta:
        verbose_name = 'Sample'
        verbose_name_plural = 'Samples'

class Sample(models.Model):
    TYPE_LIST = (
        ('Regular', 'Regular'),
        ('Borderline', 'Borderline')
    )
    is_urban = models.BooleanField()
    ben_id = models.IntegerField(unique=True)
    sample_type = models.CharField(max_length=20,choices=TYPE_LIST)
    cp_id = models.ForeignKey(CSVData, on_delete=models.RESTRICT, null=True)
    remarks = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    
    def __str__(self):
        if self.is_urban:
            return 'Urban'
        else:
            return 'Rural'
        
class TPMCSVData(models.Model):
    sample = models.ForeignKey(Sample, on_delete=models.RESTRICT, null=True, related_name='tpm_records')
    phonenumber = models.CharField(max_length=255, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    assessmentType = models.CharField(max_length=255, blank=True, null=True)
    ben_id = models.IntegerField(unique=True)
    data_assess = models.DateTimeField(blank=True, null=True)
    SB_ao = models.CharField(max_length=255, blank=True, null=True)
    SB_B_1 = models.CharField(max_length=255, blank=True, null=True)
    SB_province = models.CharField(max_length=255, blank=True, null=True)
    SB_B_2 = models.CharField(max_length=255, blank=True, null=True)
    SB_district = models.CharField(max_length=255, blank=True, null=True)
    SB_area = models.CharField(max_length=255, blank=True, null=True)
    SB_nahia = models.CharField(max_length=255, blank=True, null=True)
    SB_cfac_name = models.CharField(max_length=255, blank=True, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, blank=True, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=255, blank=True, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, blank=True, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, blank=True, null=True)
    SB_B_3 = models.CharField(max_length=255, blank=True, null=True)
    cp = models.CharField(max_length=255, blank=True, null=True)
    name_ben = models.CharField(max_length=255, blank=True, null=True)
    ben_fath = models.CharField(max_length=255, blank=True, null=True)
    ben_gender = models.CharField(max_length=50, blank=True, null=True)
    ben_age = models.IntegerField(blank=True, null=True)
    mob = models.CharField(max_length=255, blank=True, null=True)
    id_doc = models.CharField(max_length=255, blank=True, null=True)
    id_doc_other = models.CharField(max_length=255, blank=True, null=True)
    id_number = models.CharField(max_length=255, blank=True, null=True)
    HH_head_1 = models.BooleanField(blank=True, null=True)
    HH_head_2 = models.BooleanField(blank=True, null=True)
    HH_head_3 = models.BooleanField(blank=True, null=True)
    HH_head_5 = models.BooleanField(blank=True, null=True)
    HH_head_6 = models.BooleanField(blank=True, null=True)
    date_return = models.DateField(blank=True, null=True)
    iom_id = models.CharField(max_length=255, blank=True, null=True)
    alter_name = models.CharField(max_length=255, blank=True, null=True)
    alter_gender = models.CharField(max_length=50, blank=True, null=True)
    alter_age = models.IntegerField(blank=True, null=True)
    alter_mob = models.CharField(max_length=255, blank=True, null=True)
    alter_id_doc = models.CharField(max_length=255, blank=True, null=True)
    alter_id_doc_other = models.CharField(max_length=255, blank=True, null=True)
    alter_id_number = models.CharField(max_length=255, blank=True, null=True)
    HHFound = models.BooleanField(blank=True, null=True)
    A1 = models.BooleanField(blank=True, null=True)
    A2 = models.BooleanField(blank=True, null=True)
    A3 = models.BooleanField(blank=True, null=True)
    A4 = models.BooleanField(blank=True, null=True)
    A5 = models.BooleanField(blank=True, null=True)
    A6 = models.BooleanField(blank=True, null=True)
    A7 = models.BooleanField(blank=True, null=True)
    A8 = models.BooleanField(blank=True, null=True)
    A9 = models.BooleanField(blank=True, null=True)
    A10 = models.BooleanField(blank=True, null=True)
    A11 = models.BooleanField(blank=True, null=True)
    A12 = models.BooleanField(blank=True, null=True)
    A13 = models.BooleanField(blank=True, null=True)
    exclusion_1 = models.BooleanField(blank=True, null=True)
    tpm_org = models.CharField(max_length=255, blank=True, null=True)
    tpm_name_surv = models.CharField(max_length=255, blank=True, null=True)
    tpm_mob_sur = models.CharField(max_length=255, blank=True, null=True)
    TPM_Calculation = models.IntegerField(blank=True, null=True)
    vul = models.BooleanField(blank=True, null=True)
    comm = models.TextField(blank=True, null=True)
    _id = models.IntegerField(unique=True)
    _uuid = models.UUIDField(blank=True, null=True)
    _submission_time = models.DateTimeField(blank=True, null=True)
    _date_modified = models.DateTimeField(blank=True, null=True)
    _version = models.CharField(max_length=255, blank=True, null=True)
    _duration = models.DurationField(blank=True, null=True)
    _submitted_by = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.name_ben} - {self._id}"

    class Meta:
        verbose_name = "TPM Data"
        verbose_name_plural = "TPM Data"
    


class ApprovedList(models.Model):
    cp_id = models.ForeignKey(CSVData, on_delete=models.RESTRICT)
    moda_id = models.IntegerField(unique=True, null=True)
    remarks = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE )
    
    
    verbose_name = 'Approved List'
    verbose_name_plural = 'Approved List'
    
    def __str__(self):
        return self.ben_id.username

class MediaFilesType(models.Model):
    file_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.file_name
    
    class Meta:
        verbose_name = 'Media File'
        verbose_name_plural = 'Media Files'

class TargetingForms(models.Model):
    FORM_TYPE = (
        ('CP', 'CP'),
        ('TPM', 'TPM')
    )
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    form_type = models.CharField(max_length=3,choices=FORM_TYPE)
    form_id = models.IntegerField(unique=True)
    columns_list = models.TextField(null=True)
    area_office = models.CharField(max_length=5, choices=AREA_OFFICE)
    moda_media_files = models.ManyToManyField(MediaFilesType)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE )
    
    def __str__(self):
        return str(self.form_id)
    
    # meta class for verbose name
    
    class Meta:
        verbose_name = 'Targeting Form'
        verbose_name_plural = 'Targeting Forms'


class uploads(models.Model):
    fileName = models.CharField(max_length=255)
    file_type = models.CharField(max_length=10)
    filePath = models.FileField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE )

    def __str__(self):
        return self.fileName + ' ' + self.file_type

    verbose_name = 'Upload'
    verbose_name_plural = 'Uploads'


class ModaProjects(models.Model):
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    project_id = models.IntegerField(unique=True)
    project_name = models.CharField(max_length=255)
    area_office = models.CharField(max_length=5, choices=AREA_OFFICE , null=True)
    
    def __str__(self):
        return self.project_name
    
    class Meta:
        verbose_name = 'Moda Project'
        verbose_name_plural = 'Moda Projects'

class ModaUser(models.Model):
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    USER_TYPE = (('TPM', 'TPM'), ('CP', 'CP'))
    moda_username = models.CharField(max_length=255)
    moda_email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    user_type = models.CharField(max_length=3, choices=USER_TYPE)
    area_office = models.CharField(max_length=5, choices=AREA_OFFICE)
    organization_short_name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    access_given = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    def __str__(self):
        return self.moda_username
    
    class Meta:
        verbose_name = 'Moda User'
        verbose_name_plural = 'Moda Users'

class CFACList(models.Model):
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    list_name = models.CharField(max_length=255, default='cfac_list')
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    ao = models.CharField(max_length=5, choices=AREA_OFFICE)
    province = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    CFAC_FP1 = models.CharField(max_length=255)
    FP1_Number = models.CharField(max_length=255)
    CFAC_FP2 = models.CharField(max_length=255)
    FP2_Number = models.CharField(max_length=255)
    Province_code = models.CharField(max_length=255)
    District_code = models.CharField(max_length=255)
    CFAC_Name = models.CharField(max_length=255)

    
    
    def __str__(self):
        return self.list_name
    
    class Meta:
        verbose_name = 'CFAC List'
        verbose_name_plural = 'CFAC List'
        unique_together = ('name', 'province', 'district')
        
        
class CP_list(models.Model):  # Replace YourModelName with the desired model name
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    list_name = models.CharField(max_length=255, default='cp')
    name = models.CharField(max_length=255)
    label_english = models.CharField(max_length=255)
    label_dari = models.CharField(max_length=255)
    label_pashto = models.CharField(max_length=255)
    ao = models.CharField(max_length=5, choices=AREA_OFFICE)
    status = models.CharField(max_length=255)
    province = models.CharField(max_length=255,null=True)
    
    
    def __str__(self):
        return self.list_name
    
    class Meta:
        verbose_name = 'CP List'
        verbose_name_plural = 'CP List'
        unique_together = ('name', 'ao')
        
        
class TPM_list(models.Model):
    list_name = models.CharField(max_length=255, default='tpm_org')
    name = models.CharField(max_length=255)
    label_english = models.CharField(max_length=255)
    label_dari = models.CharField(max_length=255)
    label_pashto = models.CharField(max_length=255)
    ao = models.CharField(max_length=255)
    status = models.CharField(max_length=255, null=True)
    province = models.CharField(max_length=255, null=True)
    
    
    def __str__(self):
        return self.list_name
    
    class Meta:
        verbose_name = 'TPM List'
        verbose_name_plural = 'TPM List'
        unique_together = ('name', 'ao')
        
class Province(models.Model):
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO'),
    
    )
    list_name = models.CharField(max_length=255, default='province')
    name = models.CharField(max_length=255, unique=True)
    label = models.CharField(max_length=255)
    label_dari = models.CharField(max_length=255)
    label_pashto = models.CharField(max_length=255)
    ao = models.CharField(max_length=5, choices=AREA_OFFICE) # Assuming 'ao' refers to a short code, e.g., 'KAO'
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Province'
        verbose_name_plural = 'Provinces'

class VillageList(models.Model):
    
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO')
    )
    list_name = models.CharField(max_length=255, default='village_list')
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    cfac_code = models.CharField(max_length=255)
    province = models.CharField(max_length=255) #should i connect with province model
    district = models.CharField(max_length=255) #should i connect with district model
    province_code = models.CharField(max_length=255) #should i connect with province model
    district_code = models.CharField(max_length=255) #should i connect with district model
    cfac_name = models.CharField(max_length=255) # should i connect with cfac model
    ao = models.CharField(max_length=5, choices=AREA_OFFICE) 
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Village List'
        verbose_name_plural = 'Village Lists'
        unique_together = ('name', 'district_code')

class District(models.Model):
    AREA_OFFICE = (
        ('FAO', 'FAO'),
        ('HAO', 'HAO'),
        ('JAO', 'JAO'),
        ('KAO', 'KAO'),
        ('KANAO', 'KANAO'),
        ('MAO', 'MAO')
    )
    list_name = models.CharField(max_length=255, default='district')
    name = models.CharField(max_length=255, unique=True)
    label_english = models.CharField(max_length=255)
    label_dari = models.CharField(max_length=255)
    label_pashto = models.CharField(max_length=255)
    ao = models.CharField(max_length=5, choices=AREA_OFFICE) 
    status = models.CharField(max_length=255, null=True, blank=True)  # Optional field
    province = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'District'
        verbose_name_plural = 'Districts'
        
class media_files(models.Model):
    file_name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.file_name
    
    class Meta:
        verbose_name = 'Media File'
        verbose_name_plural = 'Media Files'
        
        
        
        
#### TPM Models

class TPM_SC_Data(models.Model):
    # sample = models.ForeignKey(Sample1, on_delete=models.RESTRICT, null=True, related_name='tpm_records')
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    today = models.DateField(null=True)
    deviceid = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    assessmentType = models.CharField(max_length=50)
    ben_id = models.CharField(max_length=15, unique=True)
    SB_moda_key = models.CharField(max_length=100, unique=True)
    data_assess = models.DateTimeField()
    SB_ao = models.CharField(max_length=10)
    SB_B_1 = models.CharField(max_length=50)
    SB_province = models.CharField(max_length=50)
    SB_B_2 = models.CharField(max_length=50)
    SB_district = models.CharField(max_length=50)
    SB_area = models.CharField(max_length=10, null=True)
    SB_nahia = models.IntegerField(null=True)
    SB_cfac_name = models.CharField(max_length=255, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=20, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=20, null=True)
    SB_B_3 = models.CharField(max_length=255, null=True)
    HHFound = models.BooleanField()
    cp = models.CharField(max_length=150, null=True)
    A1 = models.BooleanField(null=True)
    A2 = models.BooleanField(null=True)
    A3 = models.BooleanField(null=True)
    A4 = models.BooleanField(null=True)
    A5 = models.BooleanField(null=True)
    A6 = models.BooleanField(null=True)
    A7 = models.BooleanField(null=True)
    A8 = models.BooleanField(null=True)
    A9 = models.BooleanField(null=True)
    A10 = models.BooleanField(null=True)
    A11 = models.BooleanField(null=True)
    A12 = models.BooleanField(null=True)
    A13 = models.BooleanField(null=True)
    exclusion_1 = models.BooleanField(null=True)
    tpm_org = models.CharField(max_length=255, null=True)
    tpm_name_surv = models.CharField(max_length=255, null=True)
    tpm_mob_sur = models.CharField(max_length=20, null=True)
    TPM_Calculation = models.IntegerField(null=True)
    vul = models.CharField(max_length=10, null=True)
    comm = models.CharField(max_length=255, null=True)
    meta_instanceID = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=100, unique=True)
    isValidated = models.BooleanField(null=True)
    formhub_uuid = models.UUIDField(null=True)
    SubmissionDate = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.ben_id
    
    class Meta:
        verbose_name = 'TPM Spotcheck Data'
        verbose_name_plural = 'TPM Spotcheck Data'
        
class TPM_EE_Data(models.Model):
    MODALITY = [
        (1, 'FOOD'),
        (2, 'CBT'),
    ]
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    today = models.DateField(null=True)
    deviceid = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=20, null=True)
    username = models.CharField(max_length=100, null=True)
    email = models.EmailField(null=True)
    tit = models.CharField(max_length=1, null=True)
    assessmentType = models.CharField(max_length=50)
    data_assess = models.DateTimeField()
    SB_ao = models.CharField(max_length=10)
    SB_B_1 = models.CharField(max_length=50)
    SB_province = models.CharField(max_length=50)
    SB_B_2 = models.CharField(max_length=50)
    SB_district = models.CharField(max_length=50)
    SB_area = models.IntegerField()
    SB_nahia = models.IntegerField(null=True)
    SB_cfac_name = models.CharField(max_length=255, null=True)
    SB_Name_of_the_village_Gozar_Elder = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder = models.CharField(max_length=20, null=True)
    SB_Name_of_the_village_Gozar_Elder_001 = models.CharField(max_length=255, null=True)
    SB_Mobile_of_the_village_Gozar_Elder_001 = models.CharField(max_length=20, null=True)
    SB_B_3 = models.CharField(max_length=255, null=True)
    cp = models.CharField(max_length=150)
    infonote = models.CharField(max_length=1, null=True)
    name_ben = models.CharField(max_length=255)
    ben_fath = models.CharField(max_length=255)
    ben_gender = models.CharField(max_length=10)
    ben_age = models.IntegerField()
    female_status = models.CharField(max_length=15, null=True)
    mob = models.CharField(max_length=10, null=True)
    id_doc = models.CharField(max_length=10)
    id_doc_other = models.CharField(max_length=255,  null=True)
    id_number = models.CharField(max_length=100, null=True)
    HH_head = models.CharField(max_length=25, null=True)
    date_return = models.DateField(null=True)
    iom_id = models.CharField(max_length=100, null=True)
    # ass_modality = models.BooleanField(null=True)
    alter_name = models.CharField(max_length=255,null=True)
    atlter_fath = models.CharField(max_length=255,null=True)
    alter_gender = models.CharField(max_length=10,null=True)
    alter_age = models.IntegerField(null=True)
    alter_mob = models.CharField(max_length=10,null=True)
    alter_id_doc = models.CharField(max_length=255,null=True)
    alter_id_doc_other = models.CharField(max_length=255, null=True)
    alter_id_number = models.CharField(max_length=255,null=True)
    A1 = models.BooleanField()
    A2 = models.BooleanField()
    A3 = models.BooleanField()
    A4 = models.BooleanField()
    A5 = models.BooleanField()
    A6 = models.BooleanField()
    A7 = models.BooleanField()
    A8 = models.BooleanField()
    A9 = models.BooleanField()
    A10 = models.BooleanField()
    A11 = models.BooleanField()
    A12 = models.BooleanField()
    A13 = models.BooleanField()
    exclusion_1 = models.BooleanField()
    tpm_org = models.CharField(max_length=255, null=True)
    tpm_name_surv = models.CharField(max_length=255, null=True)
    tpm_mob_sur = models.CharField(max_length=20, null=True)
    TPM_Calculation = models.IntegerField(null=True)
    vul = models.CharField(max_length=10)
    comm = models.CharField(max_length=255, null=True)
    meta_instanceID = models.CharField(max_length=255, null=True)
    key = models.CharField(max_length=100, unique=True)
    isValidated = models.BooleanField(null=True)
    SubmissionDate = models.DateTimeField()
    formhub_uuid = models.UUIDField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by =  models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, )
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        verbose_name = "TPM EE Data"
        verbose_name_plural = "TPM EE Data"
