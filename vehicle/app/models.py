from django.db import models


# class FleetVehicle(models.Model):
#     message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
#     manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
#     company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
#     driver = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
#     future_driver = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
#     model = models.ForeignKey('FleetVehicleModel', models.DO_NOTHING)
#     brand = models.ForeignKey('FleetVehicleModelBrand', models.DO_NOTHING, blank=True, null=True)
#     state = models.ForeignKey('FleetVehicleState', models.DO_NOTHING, blank=True, null=True)
#     seats = models.IntegerField(blank=True, null=True)
#     doors = models.IntegerField(blank=True, null=True)
#     horsepower = models.IntegerField(blank=True, null=True)
#     power = models.IntegerField(blank=True, null=True)
#     category = models.ForeignKey('FleetVehicleModelCategory', models.DO_NOTHING, blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(max_length=-1, blank=True, null=True)
#     license_plate = models.CharField(max_length=-1, blank=True, null=True)
#     vin_sn = models.CharField(max_length=-1, blank=True, null=True)
#     color = models.CharField(max_length=-1, blank=True, null=True)
#     location = models.CharField(max_length=-1, blank=True, null=True)
#     model_year = models.CharField(max_length=-1, blank=True, null=True)
#     odometer_unit = models.CharField(max_length=-1)
#     transmission = models.CharField(max_length=-1, blank=True, null=True)
#     fuel_type = models.CharField(max_length=-1, blank=True, null=True)
#     co2_standard = models.CharField(max_length=-1, blank=True, null=True)
#     frame_type = models.CharField(max_length=-1, blank=True, null=True)
#     next_assignation_date = models.DateField(blank=True, null=True)
#     acquisition_date = models.DateField(blank=True, null=True)
#     write_off_date = models.DateField(blank=True, null=True)
#     first_contract_date = models.DateField(blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     trailer_hook = models.BooleanField(blank=True, null=True)
#     plan_to_change_car = models.BooleanField(blank=True, null=True)
#     plan_to_change_bike = models.BooleanField(blank=True, null=True)
#     electric_assistance = models.BooleanField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)
#     horsepower_tax = models.FloatField(blank=True, null=True)
#     co2 = models.FloatField(blank=True, null=True)
#     car_value = models.FloatField(blank=True, null=True)
#     net_car_value = models.FloatField(blank=True, null=True)
#     residual_value = models.FloatField(blank=True, null=True)
#     frame_size = models.FloatField(blank=True, null=True)
#     driver_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
#     future_driver_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
#     mobility_card = models.CharField(max_length=-1, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle'


# class FleetVehicleModelBrand(models.Model):
#     model_count = models.IntegerField(blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(max_length=-1)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle_model_brand'


# class FleetVehicleModelCategory(models.Model):
#     sequence = models.IntegerField(blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(unique=True, max_length=-1)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle_model_category'


# class TrxFleetDriver(models.Model):
#     id = models.CharField(primary_key=True, max_length=50)
#     account_id = models.CharField(max_length=50, blank=True, null=True)
#     driver_id = models.CharField(max_length=50, blank=True, null=True)
#     driver_name = models.CharField(max_length=50, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'trx_fleet_driver'


# class HrEmployee(models.Model):
#     resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
#     company = models.ForeignKey('ResCompany', models.DO_NOTHING)
#     resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
#     message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
#     color = models.IntegerField(blank=True, null=True)
#     department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
#     job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
#     address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
#     work_contact = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
#     work_location = models.ForeignKey('HrWorkLocation', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
#     parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
#     coach = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
#     address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
#     country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
#     children = models.IntegerField(blank=True, null=True)
#     country_of_birth = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country_of_birth', blank=True, null=True)
#     bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
#     km_home_work = models.IntegerField(blank=True, null=True)
#     departure_reason = models.ForeignKey('HrDepartureReason', models.DO_NOTHING, blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(max_length=-1, blank=True, null=True)
#     job_title = models.CharField(max_length=-1, blank=True, null=True)
#     work_phone = models.CharField(max_length=-1, blank=True, null=True)
#     mobile_phone = models.CharField(max_length=-1, blank=True, null=True)
#     work_email = models.CharField(max_length=-1, blank=True, null=True)
#     employee_type = models.CharField(max_length=-1)
#     gender = models.CharField(max_length=-1, blank=True, null=True)
#     marital = models.CharField(max_length=-1, blank=True, null=True)
#     spouse_complete_name = models.CharField(max_length=-1, blank=True, null=True)
#     place_of_birth = models.CharField(max_length=-1, blank=True, null=True)
#     ssnid = models.CharField(max_length=-1, blank=True, null=True)
#     sinid = models.CharField(max_length=-1, blank=True, null=True)
#     identification_id = models.CharField(max_length=-1, blank=True, null=True)
#     passport_id = models.CharField(max_length=-1, blank=True, null=True)
#     permit_no = models.CharField(max_length=-1, blank=True, null=True)
#     visa_no = models.CharField(max_length=-1, blank=True, null=True)
#     certificate = models.CharField(max_length=-1, blank=True, null=True)
#     study_field = models.CharField(max_length=-1, blank=True, null=True)
#     study_school = models.CharField(max_length=-1, blank=True, null=True)
#     emergency_contact = models.CharField(max_length=-1, blank=True, null=True)
#     emergency_phone = models.CharField(max_length=-1, blank=True, null=True)
#     barcode = models.CharField(unique=True, max_length=-1, blank=True, null=True)
#     pin = models.CharField(max_length=-1, blank=True, null=True)
#     spouse_birthdate = models.DateField(blank=True, null=True)
#     birthday = models.DateField(blank=True, null=True)
#     visa_expire = models.DateField(blank=True, null=True)
#     work_permit_expiration_date = models.DateField(blank=True, null=True)
#     departure_date = models.DateField(blank=True, null=True)
#     additional_note = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     departure_description = models.TextField(blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     work_permit_scheduled_activity = models.BooleanField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)
#     contract = models.ForeignKey('HrContract', models.DO_NOTHING, blank=True, null=True)
#     vehicle = models.CharField(max_length=-1, blank=True, null=True)
#     first_contract_date = models.DateField(blank=True, null=True)
#     contract_warning = models.BooleanField(blank=True, null=True)
#     expense_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
#     leave_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
#     mobility_card = models.CharField(max_length=-1, blank=True, null=True)
#     last_attendance = models.ForeignKey('HrAttendance', models.DO_NOTHING, blank=True, null=True)
#     last_check_in = models.DateTimeField(blank=True, null=True)
#     last_check_out = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'hr_employee'
#         unique_together = (('user', 'company'),)


# class TrxFleetWorkingVehicleDriver(models.Model):
#     vehicle_id = models.CharField(max_length=50, blank=True, null=True)
#     drive_id = models.CharField(max_length=50, blank=True, null=True)
#     parent_id = models.IntegerField(blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     start_time = models.TimeField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     end_time = models.TimeField(blank=True, null=True)
#     order = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'trx_fleet_working_vehicle_driver'


# class FleetVehicleModel(models.Model):
#     brand = models.ForeignKey(FleetVehicleModelBrand, models.DO_NOTHING)
#     category = models.ForeignKey(FleetVehicleModelCategory, models.DO_NOTHING, blank=True, null=True)
#     model_year = models.IntegerField(blank=True, null=True)
#     seats = models.IntegerField(blank=True, null=True)
#     doors = models.IntegerField(blank=True, null=True)
#     power = models.IntegerField(blank=True, null=True)
#     horsepower = models.IntegerField(blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(max_length=-1)
#     vehicle_type = models.CharField(max_length=-1)
#     transmission = models.CharField(max_length=-1, blank=True, null=True)
#     color = models.CharField(max_length=-1, blank=True, null=True)
#     co2_standard = models.CharField(max_length=-1, blank=True, null=True)
#     default_fuel_type = models.CharField(max_length=-1, blank=True, null=True)
#     active = models.BooleanField(blank=True, null=True)
#     trailer_hook = models.BooleanField(blank=True, null=True)
#     electric_assistance = models.BooleanField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)
#     default_co2 = models.FloatField(blank=True, null=True)
#     horsepower_tax = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle_model'


# class FleetVehicleOdometer(models.Model):
#     vehicle = models.ForeignKey(FleetVehicle, models.DO_NOTHING)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.CharField(max_length=-1, blank=True, null=True)
#     date = models.DateField(blank=True, null=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)
#     value = models.FloatField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle_odometer'
        
# class FleetVehicleTag(models.Model):
#     color = models.IntegerField(blank=True, null=True)
#     create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
#     write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
#     name = models.JSONField(unique=True)
#     create_date = models.DateTimeField(blank=True, null=True)
#     write_date = models.DateTimeField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'fleet_vehicle_tag'
