import logging
import requests
import time
import os
from pathlib import Path
import pandas as pd
from datetime import datetime
from base.models import Province, TargetingForms, District, CP_list, TPM_list, CFACList, VillageList, ModaProjects, ModaUser, Sample
from .models import UploadLogs



# Load variables from .env file
BASE_MODA_URL = os.getenv('MODA_API_BASE_URL')
MODA_API_KEY = os.getenv('MODA_API_KEY')


HEADER = {'Authorization': f'Token {MODA_API_KEY}'}


def rename_columns(df):
    """Rename columns in a pandas dataframe that contain 'SB/'."""
    columns = df.columns.tolist()
    for i, col in enumerate(columns):
        if "SB/" in col:
            columns[i] = col.replace("SB/", "")
    df.columns = columns
    return df

def media_form_csv(data, col_names, csv_file_path):
    """Save a pandas dataframe to a CSV file."""
    x = data[col_names]
    x = rename_columns(x)
    x.to_csv(csv_file_path, index=False)

def get_media_id(form_id, media_name):
    """Get the media ID of a file uploaded to a form."""
    url = f'{BASE_MODA_URL}metadata?xform={form_id}'
    response = requests.get(url, headers=HEADER)
    
    if response.status_code != 200:
        print(f"Error: Received a non-200 status code: {response.status_code}")
        return None
    
    if not response.content:
        print("Error: Received an empty response")
        return None
    
    try:
        data = response.json()
    except ValueError as e:
        print(f"Error parsing JSON: {e}, received content: {response.content}")
        return None
    
    for item in data:
        if item['data_type'] == 'media' and item['data_value'] == media_name:
            media_id = item['id']
            return media_id
    return None

def delete_media(media_id):
    """Delete a media file from a form."""
    url = f'{BASE_MODA_URL}metadata/{media_id}'
    response = requests.delete(url, headers=HEADER)
    if response.status_code == 204:
        print('Media deleted successfully')
        return True
    else:
        print(f'Error deleting media: {response.status_code} - {response.text}')
        return False




def upload_media(form_id, media_name, file_path, max_retries=5, delay=20):
    """
    Upload a media file to a form with retry mechanism.
    
    Args:
        form_id (str): The ID of the form.
        media_name (str): The name of the media.
        file_path (str): The file path of the media.
        max_retries (int): Maximum number of retry attempts. Default is 5.
        delay (int): Delay in seconds between retries. Default is 20 seconds.
    
    Returns:
        bool: True if upload is successful, False otherwise.
    """
    data = {
        'data_type': 'media',
        'data_value': media_name,
        'xform': form_id
    }
    url = BASE_MODA_URL + 'metadata.json'
    print(f'Uploading media: {media_name} to form: {form_id}, {url}')
    
    for attempt in range(max_retries):
        try:
            with open(file_path, 'rb') as file:
                files = {'data_file': file}
                response = requests.post(url, headers=HEADER, data=data, files=files)
            
            if response.status_code == 201:
                print('Media uploaded successfully')
                return True
            else:
                print(f'Error uploading media: {response.status_code} - {response.text}')
        except Exception as e:
            print(f'An exception occurred during attempt {attempt+1}: {e}')
        
        if attempt < max_retries - 1:
            print(f'Retrying in {delay} seconds...')
            time.sleep(delay)
    
    print('Maximum retry attempts reached. Upload failed.')
    return False

def del_upload_media(form_id, media_name, file_path):
    """Delete a media file from a form and upload a new one."""
    media_id = get_media_id(form_id, media_name)
    if media_id:
        if delete_media(media_id):
            return upload_media(form_id, media_name, file_path)
        return False
    return upload_media(form_id, media_name, file_path)

def provinceSerializer(data):
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label': data.label,
        'label::Dari': data.label_dari,
        'label::Pashto': data.label_pashto,
        'ao': data.ao,
    }

def uploadProvinceInCsv(user):
    # Filter plans from the last six months
    provinces = Province.objects.all()
    if not provinces:
        raise Exception('No province found')

    # Serialize the plans and return
    province_list = [provinceSerializer(province) for province in provinces]
    
    df = pd.DataFrame(province_list)
    file_name = 'static/moda_media_files/province.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, province_list, provinces

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'province.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='province.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='province.csv', status='Failed', created_by=user)

def districtSerializer(data):
    # list_name	name	label::English	label::Dari	label::Pashto	ao	status	province
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label::English': data.label_english,
        'label::Dari': data.label_dari,
        'label::Pashto': data.label_pashto,
        'ao': data.ao,
        'status': data.status,
        'province': data.province,
    }

def uploadDistrictInCsv(user):
    # Filter plans from the last six months
    districts = District.objects.all()
    
    if not districts:
        raise Exception('No district found')

    # Serialize the plans and return
    district_list = [districtSerializer(district) for district in districts]
    
    df = pd.DataFrame(district_list)
    file_name = 'static/moda_media_files/district.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, district_list, districts

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'district.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='district.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='district.csv', status='Failed', created_by=user)

def tpmSerializer(data):
    #list_name	name	label::English	label::Dari	label::Pashto	ao	status	province
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label::English': data.label_english,
        'label::Dari': data.label_dari,
        'label::Pashto': data.label_pashto,
        'ao': data.ao,
        'status': data.status,
        'province': data.province,
    }

def uploadtpmInCsv(user):
    # Filter plans from the last six months
    tpms = TPM_list.objects.all()
    
    if not tpms:
        raise Exception('No TPM Org found')

    # Serialize the plans and return
    tpm_list = [tpmSerializer(tpm) for tpm in tpms]
    
    df = pd.DataFrame(tpm_list)
    file_name = 'static/moda_media_files/tpm_org.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, tpm_list, tpms

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'tpm_org.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='tpm_org.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='tpm_org.csv', status='Failed', created_by=user)
            
def cpSerializer(data):
    #list_name	name	label::English	label::Dari	label::Pashto	ao	status	province
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label::English': data.label_english,
        'label::Dari': data.label_dari,
        'label::Pashto': data.label_pashto,
        'ao': data.ao,
        'status': data.status,
        'province': data.province,
    }

def uploadcpInCsv(user):
    # Filter plans from the last six months
    cps = CP_list.objects.all()
    
    if not cps:
        raise Exception('No CP found')

    # Serialize the plans and return
    cp_list = [cpSerializer(cp) for cp in cps]
    
    df = pd.DataFrame(cp_list)
    file_name = 'static/moda_media_files/cpList.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, cp_list, cps

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'cp.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='cpList.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='cpList.csv', status='Failed', created_by=user)
            
def cfacSerializer(data):
    #list_name	name	label	ao	province	district	CFAC_FP1	FP1_Number	CFAC_FP2	FP2_Number	Province_code	District_code	CFAC_Name
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label': data.label,
        'ao': data.ao,
        'province': data.province,
        'district': data.district,
        'CFAC_FP1': data.CFAC_FP1,
        'FP1_Number': data.FP1_Number,
        'CFAC_FP2': data.CFAC_FP2,
        'FP2_Number': data.FP2_Number,
        'Province_code': data.Province_code,
        'District_code': data.District_code,
        'CFAC_Name': data.CFAC_Name
    }

def uploadCFACInCsv(user):
    # Filter plans from the last six months
    cfacs = CFACList.objects.all()
    
    if not cfacs:
        raise Exception('No CFAC found')

    # Serialize the plans and return
    cfac_list = [cpSerializer(cfac) for cfac in cfacs]
    
    df = pd.DataFrame(cfac_list)
    file_name = 'static/moda_media_files/cfacList.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, cfac_list, cfacs

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'cfacList.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='cfacList.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='cfacList.csv', status='Failed', created_by=user)
            
def villagesSerializer(data):
    #list_name	name	label	cfac_code	Province	District	Province_code	District_code	CFAC_Name	ao
    return {
        'list_name': data.list_name,
        'name': data.name,
        'label': data.label,
        'cfac_code': data.cfac_code,
        'Province': data.province,
        'District': data.district,
        'Province_code': data.Province_code,
        'District_code': data.District_code,
        'CFAC_Name': data.CFAC_Name,
        'ao': data.ao,
    }

def uploadVillageInCsv(user):
    # Filter plans from the last six months
    villages = VillageList.objects.all()
    if not villages:
        raise Exception('No village found')
    # Serialize the plans and return
    villages_list = [villagesSerializer(village) for village in villages]
    
    df = pd.DataFrame(villages_list)
    file_name = 'static/moda_media_files/villageList.csv'
    df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
    
    # Clean memory
    del df, villages_list, villages

    forms = TargetingForms.objects.all()
    for form in forms:
        try:
            del_upload_media(form.form_id, 'villageList.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='villageList.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='villageList.csv', status='Failed', created_by=user)
            
def SampleSerializer(data):
    #_id, ao, B_1, B_2, area, nahia, cfac_name, Name_of_the_village_Gozar_Elder, Name_of_the_village_Gozar_Elder, Name_of_the_village_Gozar_Elder_001, Mobile_of_the_village_Gozar_Elder_001, B_3, cp, name_ben, ben_fath, ben_gender, ben_age, mob, id_doc, id_doc_other, id_number, HH_head, date_return, iom_id, alter_name, alter_gender, alter_age, alter_mob, alter_id_doc, alter_id_doc_other, alter_id_number
    area_office = {
        'Mazar Area Office':'MAO',
        'Herat Area Office':'HAO',
        'Kandahar Area Office':'KANAO',
        'Jalalabad Area Office':'JAO',
        'Kabul Area Office':'KAO',
        'Faizabad Area Office':'FAO'
    }
    return {
        '_id': data.ben_id,
        'ao': area_office[data.cp_id.SB_ao],
        'B_1': data.cp_id.SB_B_1,
        'B_2': data.cp_id.SB_B_2,
        'area': data.cp_id.SB_area,
        'nahia': data.cp_id.SB_nahia,
        'cfac_name': data.cp_id.SB_cfac_name,
        'Name_of_the_village_Gozar_Elder': data.cp_id.SB_Name_of_the_village_Gozar_Elder,
        'Name_of_the_village_Gozar_Elder': data.cp_id.SB_Name_of_the_village_Gozar_Elder,
        'Name_of_the_village_Gozar_Elder_001': data.cp_id.SB_Name_of_the_village_Gozar_Elder_001,
        'Mobile_of_the_village_Gozar_Elder_001': data.cp_id.SB_Mobile_of_the_village_Gozar_Elder_001,
        'B_3': data.cp_id.SB_B_3,
        'cp': data.cp_id.cp,
        'name_ben': data.cp_id.name_ben,
        'ben_fath': data.cp_id.ben_fath,
        'ben_gender': data.cp_id.ben_gender,
        'ben_age': data.cp_id.ben_age,
        'mob': data.cp_id.mob,
        'id_doc': data.cp_id.id_doc,
        'id_doc_other': data.cp_id.id_doc_other,
        'id_number': data.cp_id.id_number,
        'date_return': data.cp_id.date_return,
        'iom_id': data.cp_id.iom_id,
        'alter_name': data.cp_id.alter_name,
        'alter_gender': data.cp_id.alter_gender,
        'alter_age': data.cp_id.alter_age,
        'alter_mob': data.cp_id.alter_mob,
        'alter_id_doc': data.cp_id.alter_id_doc,
        'alter_id_doc_other': data.cp_id.alter_id_doc_other,
        'alter_id_number': data.cp_id.alter_id_number
    }

def uploadSample(user):
   # get full name based on FAO	Faizabad Area Office
    # MAO	Mazar Area Office
    # HAO	Herat Area Office 
    # KANAO	Kandahar Area Office
    # JAO	Jalalabad Area Office 
    # KAO	Kabul Area Office
    
    area_office = {
        'MAO': 'Mazar Area Office',
        'HAO': 'Herat Area Office',
        'KANAO': 'Kandahar Area Office',
        'JAO':'Jalalabad Area Office',
        'KAO': 'Kabul Area Office',
        'FAO':'Faizabad Area Office'
    }
    
    forms = TargetingForms.objects.filter(form_type='TPM')
    for form in forms:
        ao = form.area_office
        x = area_office[ao]
    # Filter plans from the last six months
        Samples = Sample.objects.filter(cp_id__SB_ao=x)
        if not Samples:
            raise Exception('No Sample found')
        # Serialize the plans and return
        sample_list = [SampleSerializer(sample) for sample in Samples]
        
        df = pd.DataFrame(sample_list)
        file_name = 'static/moda_media_files/BenTargeting.csv'
        df.to_csv(file_name, index=False, header=True, encoding='utf-8-sig')
        
        # Clean memory
        del df, sample_list, Samples

        try:
            del_upload_media(form.form_id, 'BenTargeting.csv', file_name)
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='BenTargeting.csv', status='Success', created_by=user)
        except Exception as e:
            print(f'Error uploading media: {e}')
            UploadLogs.objects.create(form_id=form.form_id, form_name=str(form.form_id), file_name='BenTargeting.csv', status='Failed', created_by=user)
            
def get_correct_username(email):
    url = f'{BASE_MODA_URL}users'
    params = {
    'search': email
    }
    try:
        response = requests.get(url, headers=HEADER, params=params)
        if response.status_code == 200:
            data = response.json()
            if data:
                return data[0]['username']
            return None
    except Exception as e:
        print(f'Error getting username: {e}')
        return None

def revoke_access(username, project_id):
    url = f'{BASE_MODA_URL}projects/{project_id}/share'
    # Define the data payload
    data = {
        'username': username,
        'role': 'dataentry-only',
        'remove': 'True'
    }
    try:
        response = requests.put(url, headers=HEADER, data=data)
        if response.status_code == 200 or response.status_code == 204:
            print('Access revoked successfully')
            return True
        else:
            print(f'Error revoking access: {response.status_code} - {response.text}')
            return False
    except Exception as e:
        print(f'Error revoking access: {e}')
        return False
    
def grant_access(username, project_id):
    url = f'{BASE_MODA_URL}projects/{project_id}/share'
    # Define the data payload
    data = {
        'username': username,
        'role': 'dataentry'
    }
    try:
        response = requests.put(url, headers=HEADER, data=data)
        print(response)
        if response.status_code == 201 or response.status_code == 204:
            print('Access granted successfully')
            return True
        else:
            print(f'Error granting access: {response.status_code} - {response.text}')
            return False
    except Exception as e:
        print(f'Error granting access: {e}')
        return False
    
def user_access():
    access_given = 0
    revoked_access = 0
    project = ModaProjects.objects.all()
    if not project:
        raise Exception('No projects found')
    
    checkUser = ModaUser.objects.all()
    if not checkUser:
        raise Exception('No users found')
    
    for proj in project:
        ao = proj.area_office
        users = ModaUser.objects.filter(area_office=ao, is_active=True, access_given=False)
        if users:
            for user in users:
                username = get_correct_username(user.moda_email)
                if username:
                    y = grant_access(username, proj.project_id)
                    if y:
                        user.access_given = True
                        user.save()
                        access_given += 1
                    
        revert_users = ModaUser.objects.filter(area_office=ao, is_active=False, access_given=True)
        if revert_users:
            for user in revert_users:
                username = get_correct_username(user.moda_email)
                if username:
                    x = revoke_access(username, proj.project_id)
                    if x:
                        user.access_given = False
                        user.save()
                        revoked_access += 1
                    
    return access_given, revoked_access
                    
        
   