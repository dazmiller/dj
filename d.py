# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models



class Companies(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(max_length=60, blank=True, null=True)
    business_name = models.CharField(max_length=60, blank=True, null=True)
    address1 = models.CharField(max_length=60, blank=True, null=True)
    address2 = models.CharField(max_length=60, blank=True, null=True)
    suburb = models.CharField(max_length=60, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    postcode = models.CharField(max_length=4, blank=True, null=True)
    active = models.IntegerField(blank=True, null=True)
    subscription_id = models.IntegerField(blank=True, null=True)
    tagline = models.CharField(max_length=60, blank=True, null=True)
    trading_name = models.CharField(max_length=60, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'companies'



class FuneralInsurance(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    smoker = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cover_amount = models.IntegerField(blank=True, null=True)
    resident_country = models.CharField(max_length=45, blank=True, null=True)
    residency_status = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funeral_insurance'


class FuneralInsuranceQuotes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    request_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    last_updated_by_id = models.IntegerField(blank=True, null=True)
    last_updated_by_name = models.CharField(max_length=90, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    open = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_price = models.IntegerField(blank=True, null=True)
    max_price = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    additional_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funeral_insurance_quotes'


class FuneralInsurances(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    smoker = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cover_amount = models.IntegerField(blank=True, null=True)
    resident_country = models.CharField(max_length=255, blank=True, null=True)
    residency_status = models.CharField(max_length=255, blank=True, null=True)
    dob = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'funeral_insurances'




class LifeInsuranceQuotes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    request_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    last_updated_by_id = models.IntegerField(blank=True, null=True)
    last_updated_by_name = models.CharField(max_length=90, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)
    min_price = models.IntegerField(blank=True, null=True)
    max_price = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    additional_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'life_insurance_quotes'


class LifeInsurances(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    batch_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=2, blank=True, null=True)
    smoker = models.IntegerField(blank=True, null=True)
    last_smoked = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    cover_amount = models.IntegerField(blank=True, null=True)
    country_residence = models.CharField(max_length=45, blank=True, null=True)
    residency_status = models.CharField(max_length=45, blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cancer = models.IntegerField(blank=True, null=True)
    diabetes = models.IntegerField(blank=True, null=True)
    blood_disorder = models.IntegerField(blank=True, null=True)
    cancer_type = models.CharField(max_length=255, blank=True, null=True)
    cancer_spread = models.IntegerField(blank=True, null=True)
    cancer_clear_10 = models.IntegerField(blank=True, null=True)
    diabetes_complications = models.IntegerField(blank=True, null=True)
    blood_disorder_type = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure = models.IntegerField(blank=True, null=True)
    cholesterol = models.IntegerField(blank=True, null=True)
    heart_problem = models.IntegerField(blank=True, null=True)
    blood_pressure_treatment = models.CharField(max_length=255, blank=True, null=True)
    kidney_problem = models.IntegerField(blank=True, null=True)
    cholesterol_treatment = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_check_12 = models.IntegerField(blank=True, null=True)
    heart_problem_details = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal = models.IntegerField(blank=True, null=True)
    bladder_problem = models.IntegerField(blank=True, null=True)
    lung_problem = models.IntegerField(blank=True, null=True)
    gastro_problem_details = models.CharField(max_length=255, blank=True, null=True)
    hernia_further_problems = models.IntegerField(blank=True, null=True)
    gastritis_episodes = models.IntegerField(blank=True, null=True)
    gallstones_removed = models.IntegerField(blank=True, null=True)
    gallstones_ongoing = models.IntegerField(blank=True, null=True)
    ulcer_hospitialised = models.IntegerField(blank=True, null=True)
    gastro_other_treatment = models.IntegerField(blank=True, null=True)
    gastro_problems_5y = models.IntegerField(blank=True, null=True)
    kydney_bladder_problem_details = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_details = models.CharField(max_length=255, blank=True, null=True)
    neurological = models.IntegerField(blank=True, null=True)
    muscular_skeletal = models.IntegerField(blank=True, null=True)
    mental_health_5y = models.IntegerField(blank=True, null=True)
    neurological_problem_details = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_problem_details = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_neck_back = models.IntegerField(blank=True, null=True)
    muscle_injury_strain_symptoms_2y = models.IntegerField(blank=True, null=True)
    fracture_back_neck_skull = models.IntegerField(blank=True, null=True)
    fracture_any_problems_2y = models.IntegerField(blank=True, null=True)
    arthritis_details = models.CharField(max_length=255, blank=True, null=True)
    gout_tendonitis_tenosynovitis_2y = models.IntegerField(blank=True, null=True)
    muscular_skeletal_sports_injury = models.IntegerField(blank=True, null=True)
    muscular_skeletal_joint_neck_back = models.IntegerField(blank=True, null=True)
    mental_health_details = models.CharField(max_length=255, blank=True, null=True)
    alcohol_28_week = models.IntegerField(blank=True, null=True)
    illegal_drugs_5y = models.IntegerField(blank=True, null=True)
    hiv_positive = models.IntegerField(blank=True, null=True)
    alcohol_professional_help = models.IntegerField(blank=True, null=True)
    alcohol_detox_hospital = models.IntegerField(blank=True, null=True)
    illegal_drug_use_details = models.CharField(max_length=255, blank=True, null=True)
    other_medical_conditions = models.CharField(max_length=255, blank=True, null=True)
    family_member_cancer_60 = models.IntegerField(blank=True, null=True)
    seeking_medical_advice_currently_details = models.CharField(max_length=255, blank=True, null=True)
    thyroid_problem_2y = models.IntegerField(blank=True, null=True)
    thryoid_surgery_radio_6m = models.IntegerField(blank=True, null=True)
    current_medical_treatment_professions = models.CharField(max_length=255, blank=True, null=True)
    family_member_illness_details = models.CharField(max_length=255, blank=True, null=True)
    family_2_or_more_heart_disease = models.IntegerField(blank=True, null=True)
    family_2_or_more_stroke = models.IntegerField(blank=True, null=True)
    kidney_disease_polycystic = models.IntegerField(blank=True, null=True)
    family_2_or_more_diabetes = models.IntegerField(blank=True, null=True)
    cancer_type_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    family_count_colon_rectal_60 = models.IntegerField(blank=True, null=True)
    colon_rectal_before_50 = models.IntegerField(blank=True, null=True)
    family_count_prostate_cancer_60 = models.IntegerField(blank=True, null=True)
    prostate_cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_2_more_same_cancer_60 = models.IntegerField(blank=True, null=True)
    cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_count_testicular_cancer_field = models.IntegerField(db_column='family_count_testicular_cancer_', blank=True, null=True)  # Field renamed because it ended with '_'.
    testicular_cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_count_ms_60 = models.IntegerField(blank=True, null=True)
    family_count_parkinsons_60 = models.IntegerField(blank=True, null=True)
    family_count_motor_neurone_60 = models.IntegerField(blank=True, null=True)
    risky_occupation = models.CharField(max_length=255, blank=True, null=True)
    recreational_activities = models.CharField(max_length=255, blank=True, null=True)
    type_of_cancer_when_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    cancer_medicated_treated = models.CharField(max_length=255, blank=True, null=True)
    cancer_state_remission = models.CharField(max_length=255, blank=True, null=True)
    diabetes_first_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    diabetes_medication_control = models.CharField(max_length=255, blank=True, null=True)
    diabetes_tests_12m = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_medication = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_tests_12m = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_high_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_medication = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_test = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    cholestrol_medication = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_test = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_medication = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_test_12m = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_medication = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_current_state = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_medication = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_current_state = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_medication = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_current_state = models.CharField(max_length=255, blank=True, null=True)
    neurological_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    neurological_medication = models.CharField(max_length=255, blank=True, null=True)
    neurological_current_state = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_medication = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_current_status = models.CharField(max_length=255, blank=True, null=True)
    mental_health_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    mental_health_caused_event_illness = models.CharField(max_length=255, blank=True, null=True)
    mental_health_medication = models.CharField(max_length=255, blank=True, null=True)
    alcohol_typical_use = models.CharField(max_length=255, blank=True, null=True)
    alcohol_consulted_professional = models.CharField(max_length=255, blank=True, null=True)
    alcohol_alcoholism_or_counselling = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_use = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_consulted_professional = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_have_stopped_period = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_symptoms = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_profession = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_tests = models.CharField(max_length=255, blank=True, null=True)
    family_members_illness_list = models.CharField(max_length=1024, blank=True, null=True)
    family_members_medical_tests_you_had_related = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'life_insurances'


class MortgageInsuranceQuotes(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)   
    request_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    last_updated_by_id = models.IntegerField(blank=True, null=True)
    last_updated_by_name = models.CharField(max_length=90, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    open = models.TextField(blank=True, null=True)  # This field type is a guess.
    min_price = models.IntegerField(blank=True, null=True)
    max_price = models.IntegerField(blank=True, null=True)
    batch_id = models.IntegerField(blank=True, null=True)
    additional_user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mortgage_insurance_quotes'


class MortgageInsurances(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    batch_id = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=8, blank=True, null=True)
    smoker = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    mortgage_recent = models.IntegerField(blank=True, null=True)
    mortgage_amount = models.IntegerField(blank=True, null=True)
    lender_name = models.CharField(max_length=45, blank=True, null=True)
    lender_branch = models.CharField(max_length=45, blank=True, null=True)
    lender_city = models.CharField(max_length=45, blank=True, null=True)
    country_resident = models.CharField(max_length=45, blank=True, null=True)
    resident_status = models.CharField(max_length=45, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    cancer_status = models.IntegerField(blank=True, null=True)
    cancer_types = models.CharField(max_length=255, blank=True, null=True)
    diabetes_status = models.IntegerField(blank=True, null=True)
    blood_disorder_status = models.IntegerField(blank=True, null=True)
    diabeties_complications = models.IntegerField(blank=True, null=True)
    diabetes_complications_details = models.CharField(max_length=255, blank=True, null=True)
    high_blood_pressure = models.IntegerField(blank=True, null=True)
    high_cholesterol = models.IntegerField(blank=True, null=True)
    heart_problems = models.IntegerField(blank=True, null=True)
    high_blood_pressure_treatment = models.CharField(max_length=45, blank=True, null=True)
    high_blood_pressure_heart_kidney_problem = models.IntegerField(blank=True, null=True)
    high_cholesterol_treatment = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_checked_12m = models.IntegerField(blank=True, null=True)
    last_cholesterol_check_status = models.CharField(max_length=45, blank=True, null=True)
    last_cholesterol_check_reading = models.CharField(max_length=45, blank=True, null=True)
    heart_problems_details = models.CharField(max_length=255, blank=True, null=True)
    gastro_problems_status = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_problems_status = models.CharField(max_length=255, blank=True, null=True)
    breathing_lung_problem_status = models.CharField(max_length=255, blank=True, null=True)
    gastro_problems_details = models.CharField(max_length=255, blank=True, null=True)
    hernia_repaired = models.IntegerField(blank=True, null=True)
    num_gastritis_12m = models.CharField(max_length=8, blank=True, null=True)
    gallstones_removed = models.IntegerField(blank=True, null=True)
    gallstones_ongoing_issues = models.IntegerField(blank=True, null=True)
    ulcer_hospitlisation_2d = models.IntegerField(blank=True, null=True)
    other_gastro_problems_12m = models.IntegerField(blank=True, null=True)
    num_gastro_issues_5y = models.IntegerField(blank=True, null=True)
    kidney_problem_details = models.CharField(max_length=255, blank=True, null=True)
    breathing_problems_details = models.CharField(max_length=255, blank=True, null=True)
    risky_occupation = models.CharField(max_length=255, blank=True, null=True)
    recreational_activities = models.CharField(max_length=255, blank=True, null=True)
    diabetes_medication_control = models.CharField(max_length=255, blank=True, null=True)
    type_of_cancer_when_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    cancer_medicated_treated = models.CharField(max_length=255, blank=True, null=True)
    cancer_state_remission = models.CharField(max_length=255, blank=True, null=True)
    diabetes_first_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    diabetes_tests_12m = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_medication = models.CharField(max_length=255, blank=True, null=True)
    blood_disorder_tests_12m = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_high_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_medication = models.CharField(max_length=255, blank=True, null=True)
    blood_pressure_test = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    cholestrol_medication = models.CharField(max_length=255, blank=True, null=True)
    cholesterol_test = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_medication = models.CharField(max_length=255, blank=True, null=True)
    heart_condition_test_12m = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_medication = models.CharField(max_length=255, blank=True, null=True)
    gastro_intestinal_current_state = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_medication = models.CharField(max_length=255, blank=True, null=True)
    kidney_bladder_current_state = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_medication = models.CharField(max_length=255, blank=True, null=True)
    lung_problem_current_state = models.CharField(max_length=255, blank=True, null=True)
    neurological_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    neurological_medication = models.CharField(max_length=255, blank=True, null=True)
    neurological_current_state = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_medication = models.CharField(max_length=255, blank=True, null=True)
    muscular_skeletal_current_status = models.CharField(max_length=255, blank=True, null=True)
    mental_health_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    mental_health_caused_event_illness = models.CharField(max_length=255, blank=True, null=True)
    mental_health_medication = models.CharField(max_length=255, blank=True, null=True)
    alcohol_typical_use = models.CharField(max_length=255, blank=True, null=True)
    alcohol_consulted_professional = models.CharField(max_length=255, blank=True, null=True)
    alcohol_alcoholism_or_counselling = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_use = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_consulted_professional = models.CharField(max_length=255, blank=True, null=True)
    illegal_drugs_have_stopped_period = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_symptoms = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_profession = models.CharField(max_length=255, blank=True, null=True)
    current_medical_advice_tests = models.CharField(max_length=255, blank=True, null=True)
    family_member_illness_details = models.CharField(max_length=255, blank=True, null=True)
    family_2_or_more_heart_disease = models.IntegerField(blank=True, null=True)
    family_2_or_more_stroke = models.IntegerField(blank=True, null=True)
    kidney_disease_polycystic = models.IntegerField(blank=True, null=True)
    family_2_or_more_diabetes = models.IntegerField(blank=True, null=True)
    cancer_type_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    family_count_colon_rectal_60 = models.IntegerField(blank=True, null=True)
    colon_rectal_before_50 = models.IntegerField(blank=True, null=True)
    family_count_prostate_cancer_60 = models.IntegerField(blank=True, null=True)
    prostate_cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_2_more_same_cancer_60 = models.IntegerField(blank=True, null=True)
    cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_count_testicular_cancer_60 = models.IntegerField(blank=True, null=True)
    testicular_cancer_before_50 = models.IntegerField(blank=True, null=True)
    family_count_ms_60 = models.IntegerField(blank=True, null=True)
    family_count_parkinsons_60 = models.IntegerField(blank=True, null=True)
    family_count_motor_neurone_60 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mortgage_insurances'



class Products(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    deleted_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Profiles(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=45, blank=True, null=True)
    middlename = models.CharField(max_length=45, blank=True, null=True)
    surname = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    smoker = models.TextField(blank=True, null=True)  # This field type is a guess.
    avdrinks = models.IntegerField(blank=True, null=True)
    address1 = models.CharField(max_length=90, blank=True, null=True)
    address2 = models.CharField(max_length=90, blank=True, null=True)
    address3 = models.CharField(max_length=90, blank=True, null=True)
    suburb = models.CharField(max_length=45, blank=True, null=True)
    state = models.CharField(max_length=10, blank=True, null=True)
    postcode = models.IntegerField(blank=True, null=True)
    email1 = models.CharField(max_length=90, blank=True, null=True)
    email2 = models.CharField(max_length=90, blank=True, null=True)
    phone_home = models.CharField(max_length=45, blank=True, null=True)
    phone_mob = models.CharField(max_length=45, blank=True, null=True)
    msn = models.CharField(max_length=90, blank=True, null=True)
    twitter = models.CharField(max_length=90, blank=True, null=True)
    facebook = models.CharField(max_length=90, blank=True, null=True)
    wechat = models.CharField(max_length=90, blank=True, null=True)
    profession = models.CharField(max_length=90, blank=True, null=True)
    profilecol = models.CharField(max_length=45, blank=True, null=True)
    title = models.CharField(max_length=45, blank=True, null=True)
    child1_name = models.CharField(max_length=45, blank=True, null=True)
    child1_birthdate = models.DateField(blank=True, null=True)
    child1_sex = models.CharField(max_length=10, blank=True, null=True)
    child2_name = models.CharField(max_length=45, blank=True, null=True)
    child2_birthdate = models.DateField(blank=True, null=True)
    child2_sex = models.CharField(max_length=10, blank=True, null=True)
    child3_name = models.CharField(max_length=45, blank=True, null=True)
    child3_birthdate = models.DateField(blank=True, null=True)
    child3_sex = models.CharField(max_length=10, blank=True, null=True)
    child4_name = models.CharField(max_length=45, blank=True, null=True)
    child4_birthdatae = models.DateField(blank=True, null=True)
    child4_sex = models.CharField(max_length=10, blank=True, null=True)
    child5_name = models.CharField(max_length=45, blank=True, null=True)
    child5_birthdate = models.DateField(blank=True, null=True)
    child5_sex = models.CharField(max_length=10, blank=True, null=True)
    no_children = models.IntegerField(blank=True, null=True)
    no_pets = models.IntegerField(blank=True, null=True)
    pet1_name = models.CharField(max_length=45, blank=True, null=True)
    pet1_type = models.CharField(max_length=45, blank=True, null=True)
    pet1_sex = models.CharField(max_length=10, blank=True, null=True)
    pet2_name = models.CharField(max_length=45, blank=True, null=True)
    pet2_type = models.CharField(max_length=45, blank=True, null=True)
    pet2_sex = models.CharField(max_length=10, blank=True, null=True)
    pet3_name = models.CharField(max_length=45, blank=True, null=True)
    pet3_sex = models.CharField(max_length=10, blank=True, null=True)
    pet3_type = models.CharField(max_length=45, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    options_radios = models.CharField(max_length=191, blank=True, null=True)
    a = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'profiles'


class Providers(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='CompanyName', max_length=45, blank=True, null=True)  # Field name made lowercase.
    companycode = models.CharField(db_column='CompanyCode', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone1 = models.CharField(db_column='Phone1', max_length=45, blank=True, null=True)  # Field name made lowercase.
    phone2 = models.CharField(db_column='Phone2', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=45, blank=True, null=True)  # Field name made lowercase.
    website = models.CharField(db_column='Website', max_length=45, blank=True, null=True)  # Field name made lowercase.
    information = models.CharField(db_column='Information', max_length=255, blank=True, null=True)  # Field name made lowercase.
    sectorcoverage = models.CharField(db_column='SectorCoverage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    active = models.IntegerField(blank=True, null=True)
    country = models.CharField(db_column='Country', max_length=45, blank=True, null=True)  # Field name made lowercase.
    mailaddress = models.CharField(db_column='MailAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    operationhours = models.CharField(db_column='OperationHours', max_length=255, blank=True, null=True)  # Field name made lowercase.
    officeaddress = models.CharField(db_column='OfficeAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.
    phone3 = models.CharField(db_column='Phone3', max_length=45, blank=True, null=True)  # Field name made lowercase.
    membersince = models.DateField(db_column='MemberSince', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'providers'


class QuoteContactRequests(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    user_id = models.IntegerField(blank=True, null=True)
    quote_type = models.CharField(max_length=45, blank=True, null=True)
    quote_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    client_request_date_time = models.DateTimeField(blank=True, null=True)
    provider_confirm_date_time = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_contact_requests'


class QuoteMessages(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)    
    quote_id = models.IntegerField(blank=True, null=True)
    provider_id = models.IntegerField(blank=True, null=True)
    provider_name = models.CharField(max_length=90, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    isread = models.IntegerField(blank=True, null=True)
    created_datetime = models.DateTimeField(blank=True, null=True)
    read_datetime = models.DateTimeField(blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quote_messages'



