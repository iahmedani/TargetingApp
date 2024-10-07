from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.db.models import Count, Q
from .models import CPDataModel1, Sample1, TPM_SC_Data, TPM_EE_Data

# View to get counts of CP Data, Samples, and TPM Data grouped by SB_ao, SB_province, SB_district, and SB_nahia
class DataCountsGroupedView(View):
    def get(self, request):
        # Get count of all records from CPDataModel1 grouped by SB_ao, SB_province, SB_district, and SB_nahia
        data_counts = CPDataModel1.objects.values(
            'SB_ao', 'SB_province', 'SB_district', 'SB_nahia'
        ).annotate(
            cp_row_count=Count('id'),
            sample_count=Count('sample1', filter=Q(sample1__isnull=False)),
            tpm_row_count=Count('sample1__tpm_records', filter=Q(sample1__tpm_records__isnull=False))
        )

        data = [
            {
                'SB_ao': entry['SB_ao'],
                'SB_province': entry['SB_province'],
                'SB_district': entry['SB_district'],
                'SB_nahia': entry['SB_nahia'],
                'cp_row_count': entry['cp_row_count'],
                'sample_count': entry['sample_count'],
                'tpm_row_count': entry['tpm_row_count']
            }
            for entry in data_counts
        ]

        return JsonResponse(data, safe=False)

# View to get summary of CP, TPM, and TPM_EE data by vulnerability (vul) based on given parameters
class DataSummaryView(View):
    def post(self, request):
        import json
        data = json.loads(request.body)
        ao = data.get('ao')
        province = data.get('province')
        district = data.get('district')
        nahia = data.get('nahia')

        # Build filters dynamically to handle cases where nahia is null
        cp_filters = {
            'SB_ao': ao,
            'SB_province': province,
            'SB_district': district,
        }
        if nahia is not None:
            cp_filters['SB_nahia'] = nahia

        # Filter CPDataModel1 records based on given parameters and summarize by vul
        cp_summary = CPDataModel1.objects.filter(**cp_filters).values('vul').annotate(cp_row_count=Count('id'))

        # Filter Sample1 records that have related TPM_SC_Data and summarize by vul
        tpm_summary = Sample1.objects.filter(
            cp_id__SB_ao=ao,
            cp_id__SB_province=province,
            cp_id__SB_district=district,
            cp_id__SB_nahia=nahia if nahia is not None else None,
            tpm_records__isnull=False
        ).values('cp_id__vul').annotate(tpm_row_count=Count('tpm_records')).distinct()

        # Filter TPM_EE_Data records based on given parameters and summarize by vul
        tpm_ee_filters = {
            'SB_ao': ao,
            'SB_province': province,
            'SB_district': district,
        }
        if nahia is not None:
            tpm_ee_filters['SB_nahia'] = nahia

        tpm_ee_summary = TPM_EE_Data.objects.filter(**tpm_ee_filters).values('vul').annotate(tpm_ee_row_count=Count('id')).distinct()

        summary_data = {
            'cp_summary': list(cp_summary),
            'tpm_summary': [
                {
                    'vul': entry['cp_id__vul'],
                    'tpm_row_count': entry['tpm_row_count']
                } for entry in tpm_summary
            ],
            'tpm_ee_summary': [
                {
                    'vul': entry['vul'],
                    'tpm_ee_row_count': entry['tpm_ee_row_count']
                } for entry in tpm_ee_summary
            ]
        }

        return JsonResponse(summary_data, safe=False)

# View to get all data from CPDataModel1 with additional columns from TPM_SC_Data
class CPDataWithTPMView(View):
    def post(self, request):
        import json
        data = json.loads(request.body)
        ao = data.get('ao')
        province = data.get('province')
        district = data.get('district')
        nahia = data.get('nahia')

        # Build filters dynamically to handle cases where nahia is null
        cp_filters = {
            'SB_ao': ao,
            'SB_province': province,
            'SB_district': district,
        }
        if nahia is not None:
            cp_filters['SB_nahia'] = nahia

        # Fetch all CPDataModel1 records with all columns and additional columns from TPM_SC_Data
        cp_data = CPDataModel1.objects.filter(**cp_filters).values(
            *[field.name for field in CPDataModel1._meta.fields],
            'sample1__tpm_records__TPM_Calculation',
            'sample1__tpm_records__vul',
            'sample1__tpm_records__HHFound'
        )

        data = [
            {
                **{field: entry[field] for field in [f.name for f in CPDataModel1._meta.fields]},
                'TPM_Calculation': entry['sample1__tpm_records__TPM_Calculation'],
                'TPM_vul': entry['sample1__tpm_records__vul'],
                'TPM_HHFound': entry['sample1__tpm_records__HHFound']
            }
            for entry in cp_data
        ]

        return JsonResponse(data, safe=False)