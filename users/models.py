from django.db import models
# from django.contrib.auth.models import (
#     AbstractBaseUser, PermissionsMixin, BaseUserManager
# )


# class UserManager(BaseUserManager):
#     def _create_user(self, email, password, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         if not email:
#             raise ValueError('The given email must be set')
#         try:
#             user = self.model(email=email, **extra_fields)
#             user.set_password(password)
#             user.save(using=self._db)
#             return user
#         except:
#             raise
 
#     def create_user(self, email, password=None, **extra_fields):
#         return self._create_user(email, password, **extra_fields)
 
#     def create_superuser(self, email, password, **extra_fields):
#         return self._create_user(email, password=password, **extra_fields)


class Members(models.Model):
    member_id = models.BigIntegerField()
    membertypeid = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=100, blank=True, null=True, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    challenge_question = models.CharField(max_length=100, blank=True, null=True)
    challenge_answer = models.CharField(max_length=100, blank=True, null=True)
    datedisabled = models.CharField(max_length=255, blank=True, null=True)
    disabled = models.BooleanField(blank=True, null=True)
    profiletype = models.IntegerField(blank=True, null=True)

    is_authenticated = True
    id = 1

    def __str__(self):
        return self.username

    class Meta:
        db_table = "members"
        managed = True
        verbose_name = 'Member List'







# # # This is an auto-generated Django model module.
# # # You'll have to do the following manually to clean this up:
# # #   * Rearrange models' order
# # #   * Make sure each model has one field with primary_key=True
# # #   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
# # #   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# # # Feel free to rename the models, but don't rename db_table values or field names.
# # from django.db import models


# # class Accomadditinfo(models.Model):
# #     bookingid = models.BigIntegerField(primary_key=True)
# #     fname = models.CharField(max_length=50, blank=True, null=True)
# #     sname = models.CharField(max_length=50, blank=True, null=True)
# #     idnumber = models.CharField(max_length=50, blank=True, null=True)
# #     intials = models.CharField(max_length=5, blank=True, null=True)
# #     cell = models.CharField(max_length=50, blank=True, null=True)
# #     tel = models.CharField(max_length=50, blank=True, null=True)
# #     fax = models.CharField(max_length=50, blank=True, null=True)
# #     title = models.CharField(max_length=5, blank=True, null=True)
# #     email = models.CharField(max_length=50, blank=True, null=True)
# #     addr1 = models.CharField(max_length=150, blank=True, null=True)
# #     addr2 = models.CharField(max_length=150, blank=True, null=True)
# #     city = models.CharField(max_length=50, blank=True, null=True)
# #     province = models.CharField(max_length=50, blank=True, null=True)
# #     country = models.CharField(max_length=50, blank=True, null=True)
# #     postcode = models.CharField(max_length=10, blank=True, null=True)
# #     ratename = models.CharField(max_length=50, blank=True, null=True)
# #     paymethod = models.CharField(max_length=50, blank=True, null=True)
# #     ccholdername = models.CharField(max_length=50, blank=True, null=True)
# #     cctype = models.CharField(max_length=25, blank=True, null=True)
# #     ccepiry = models.CharField(max_length=10, blank=True, null=True)
# #     ccnumber = models.CharField(max_length=25, blank=True, null=True)
# #     cccvv = models.CharField(max_length=8, blank=True, null=True)
# #     fq1 = models.CharField(max_length=50, blank=True, null=True)
# #     fq2 = models.CharField(max_length=50, blank=True, null=True)
# #     guarmethod = models.CharField(max_length=50, blank=True, null=True)
# #     contactname = models.CharField(max_length=50, blank=True, null=True)
# #     initials = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accomadditinfo'


# # class Accommbreakdown(models.Model):
# #     reservationid = models.BigIntegerField(primary_key=True)
# #     typeid = models.IntegerField()
# #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommbreakdown'
# #         unique_together = (('reservationid', 'typeid'),)


# # class Accommbreakdowntype(models.Model):
# #     typeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=90)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommbreakdowntype'


# # class Accommodation(models.Model):
# #     bookingid = models.BigIntegerField(primary_key=True)
# #     reservationnumber = models.CharField(max_length=255)
# #     hotelcode = models.CharField(max_length=255)
# #     roomtypecode = models.CharField(max_length=255)
# #     numberadults = models.IntegerField(blank=True, null=True)
# #     numberchildren = models.IntegerField(blank=True, null=True)
# #     checkindate = models.DateTimeField()
# #     checkoutdate = models.DateTimeField()
# #     numberunits = models.IntegerField()
# #     rateplancode = models.CharField(max_length=255, blank=True, null=True)
# #     membership_id = models.CharField(max_length=255, blank=True, null=True)
# #     totalaftertax = models.DecimalField(max_digits=20, decimal_places=2)
# #     personaldetailsid = models.BigIntegerField(blank=True, null=True)
# #     paymentdetailsid = models.BigIntegerField(blank=True, null=True)
# #     paymentdeadline = models.DateTimeField(blank=True, null=True)
# #     deadlinepaymentamount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField()
# #     invoiceid = models.BigIntegerField(blank=True, null=True)
# #     resstatus = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='resstatus')
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid')
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     onrequest = models.CharField(max_length=10, blank=True, null=True)
# #     bookingengineid = models.BigIntegerField(blank=True, null=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     roomdescription = models.CharField(max_length=300, blank=True, null=True)
# #     ratedescription = models.TextField(blank=True, null=True)
# #     hoteldetailsid = models.BigIntegerField(blank=True, null=True)
# #     membershipid = models.CharField(max_length=255, blank=True, null=True)
# #     mobid = models.ForeignKey('Meansofbookinghotel', models.DO_NOTHING, db_column='mobid', blank=True, null=True)
# #     accomadditinfoid = models.ForeignKey(Accomadditinfo, models.DO_NOTHING, db_column='accomadditinfoid', blank=True, null=True)
# #     remarks = models.CharField(max_length=500, blank=True, null=True)
# #     paymentmechanismid = models.ForeignKey('Paymentmechanism', models.DO_NOTHING, db_column='paymentmechanismid', blank=True, null=True)
# #     hotelratecategory = models.CharField(max_length=255, blank=True, null=True)
# #     vatableamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     nonvatableamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     vatamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     invoicefileid = models.ForeignKey('Invoicefile', models.DO_NOTHING, db_column='invoicefileid', blank=True, null=True)
# #     booktotalfatertax = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     invoice_invoiceid = models.ForeignKey('Invoice', models.DO_NOTHING, db_column='invoice_invoiceid', blank=True, null=True)
# #     tripglcodeid = models.ForeignKey('Tripglcode', models.DO_NOTHING, db_column='tripglcodeid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommodation'
# #         unique_together = (('bookingid', 'reservationid'),)


# # class AccommodationCatalogue(models.Model):
# #     accomcatalogueid = models.BigAutoField(primary_key=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     insertdate = models.DateTimeField(blank=True, null=True)
# #     price = models.FloatField()
# #     roomtype = models.CharField(max_length=255, blank=True, null=True)
# #     hotelid = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='hotelid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommodation_catalogue'


# # class AccommodationInvoicefile(models.Model):
# #     accommodation_bookingid = models.ForeignKey(Accommodation, models.DO_NOTHING, db_column='accommodation_bookingid')
# #     invoicefiles = models.ForeignKey('Invoicefile', models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommodation_invoicefile'


# # class Accommodationprovider(models.Model):
# #     id = models.ForeignKey('Serviceprovider', models.DO_NOTHING, db_column='id', primary_key=True)
# #     hotelid = models.ForeignKey('Hotel', models.DO_NOTHING, db_column='hotelid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommodationprovider'


# # class Accommodationproviderpreference(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     pbeecontributionlevel = models.CharField(max_length=255, blank=True, null=True)
# #     ppreferencetype = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovideruri = models.CharField(max_length=255, blank=True, null=True)
# #     client_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     supplier_engineid = models.ForeignKey('Bookingengine', models.DO_NOTHING, db_column='supplier_engineid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accommodationproviderpreference'


# # class Accomodationhotelchainassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     hotelchainuri = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey('Assertion', models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accomodationhotelchainassertion'


# # class Accomodationrequest(models.Model):
# #     requestid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     city = models.CharField(max_length=40, blank=True, null=True)
# #     country = models.CharField(max_length=50, blank=True, null=True)
# #     checkindate = models.DateTimeField(blank=True, null=True)
# #     checkoutdate = models.DateTimeField(blank=True, null=True)
# #     hotelname = models.CharField(max_length=75, blank=True, null=True)
# #     days = models.IntegerField(blank=True, null=True)
# #     info = models.CharField(max_length=150, blank=True, null=True)
# #     billinginfo = models.CharField(max_length=50, blank=True, null=True)
# #     hotel_id = models.IntegerField(blank=True, null=True)
# #     roomtype = models.CharField(max_length=50, blank=True, null=True)
# #     smoking = models.CharField(max_length=50, blank=True, null=True)
# #     hotelregion = models.CharField(max_length=50, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'accomodationrequest'


# # class Account(models.Model):
# #     accountid = models.BigIntegerField(primary_key=True)
# #     member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     statusid = models.IntegerField(blank=True, null=True)
# #     programid = models.BigIntegerField(blank=True, null=True)
# #     accounttype = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'account'


# # class Accounttype(models.Model):
# #     accounttypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'accounttype'


# # class AdditionalApprover(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     company = models.CharField(max_length=255, blank=True, null=True)
# #     email_address = models.CharField(max_length=255, blank=True, null=True)
# #     firstname = models.CharField(max_length=255, blank=True, null=True)
# #     person_id = models.BigIntegerField(blank=True, null=True)
# #     staff_code = models.CharField(max_length=255, blank=True, null=True)
# #     surname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'additional_approver'


# # class Additionalemail(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     emailaddress = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'additionalemail'


# # class Address(models.Model):
# #     address_id = models.BigIntegerField(primary_key=True)
# #     member_id = models.BigIntegerField()
# #     type_id = models.IntegerField()
# #     line1 = models.CharField(max_length=40, blank=True, null=True)
# #     line2 = models.CharField(max_length=40, blank=True, null=True)
# #     line3 = models.CharField(max_length=40, blank=True, null=True)
# #     line4 = models.CharField(max_length=40, blank=True, null=True)
# #     postal_code = models.CharField(max_length=8, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'address'


# # class Addressdetail(models.Model):
# #     addressid = models.AutoField(primary_key=True)
# #     address = models.CharField(max_length=255, blank=True, null=True)
# #     province = models.CharField(max_length=255, blank=True, null=True)
# #     postcode = models.CharField(max_length=255, blank=True, null=True)
# #     cityregion = models.CharField(max_length=255, blank=True, null=True)
# #     cityname = models.CharField(max_length=255, blank=True, null=True)
# #     countrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='countrycode', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'addressdetail'


# # class AdminType(models.Model):
# #     admin_type_id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=30, blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'admin_type'


# # class AdminTypeAdminType(models.Model):
# #     admin_type_admin_type = models.ForeignKey(AdminType, models.DO_NOTHING, primary_key=True)
# #     assignableroles_admin_type = models.ForeignKey(AdminType, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'admin_type_admin_type'
# #         unique_together = (('admin_type_admin_type', 'assignableroles_admin_type'),)


# # class Administrator(models.Model):
# #     admin_id = models.BigIntegerField(primary_key=True)
# #     member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     admin_type = models.ForeignKey(AdminType, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'administrator'


# # class Agencycorporatelink(models.Model):
# #     agencyid = models.BigIntegerField(primary_key=True)
# #     merchant_id = models.BigIntegerField()
# #     linkid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'agencycorporatelink'
# #         unique_together = (('agencyid', 'merchant_id'),)


# # class Agencytype(models.Model):
# #     agencytypeid = models.IntegerField(primary_key=True)
# #     typename = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'agencytype'


# # class Airlineclasses(models.Model):
# #     classid = models.IntegerField(primary_key=True)
# #     code = models.CharField(max_length=15, blank=True, null=True)
# #     name = models.CharField(max_length=25, blank=True, null=True)
# #     displayorder = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'airlineclasses'


# # class Airlines(models.Model):
# #     airlineid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=150)
# #     flight_designator = models.CharField(max_length=30)
# #     merchant_id = models.BigIntegerField(blank=True, null=True)
# #     payexpiryhours = models.IntegerField(blank=True, null=True)
# #     ticketcode = models.CharField(max_length=10, blank=True, null=True)
# #     type = models.BigIntegerField(blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'airlines'


# # class Airport(models.Model):
# #     iatacode = models.CharField(primary_key=True, max_length=255)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'airport'


# # class Allofassertion(models.Model):
# #     id = models.ForeignKey('Assertion', models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'allofassertion'


# # class Alreadyrequested(models.Model):
# #     key = models.CharField(primary_key=True, max_length=255)
# #     requestedvalue = models.BooleanField()

# #     class Meta:
# #         managed = False
# #         db_table = 'alreadyrequested'


# # class Alternativeapproverconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     enddatetime = models.DateTimeField(blank=True, null=True)
# #     startdatetime = models.DateTimeField(blank=True, null=True)
# #     alternateapproverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='alternateapproverid', blank=True, null=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'alternativeapproverconfig'


# # class Amenity(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     description = models.CharField(max_length=16384, blank=True, null=True)
# #     lastupdatedat = models.DateTimeField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'amenity'


# # class Amexstatements(models.Model):
# #     statementid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=80, blank=True, null=True)
# #     periodstart = models.DateTimeField(blank=True, null=True)
# #     periodend = models.DateTimeField(blank=True, null=True)
# #     accountnr = models.CharField(max_length=30, blank=True, null=True)
# #     controlaccount = models.CharField(max_length=30, blank=True, null=True)
# #     plasticnr = models.CharField(max_length=200, blank=True, null=True)
# #     transtype = models.CharField(max_length=30, blank=True, null=True)
# #     transdate = models.DateTimeField(blank=True, null=True)
# #     processdate = models.DateTimeField(blank=True, null=True)
# #     referencenr = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)
# #     ordernr = models.CharField(max_length=25, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     filepacketid = models.BigIntegerField(blank=True, null=True)
# #     airline = models.CharField(max_length=50, blank=True, null=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     passengername = models.CharField(max_length=50, blank=True, null=True)
# #     ticketnr = models.CharField(max_length=20, blank=True, null=True)
# #     ticketcode = models.CharField(max_length=10, blank=True, null=True)
# #     matched = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'amexstatements'


# # class Andrekammiesapprovalstmp(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approvalrequestid = models.CharField(max_length=-1, blank=True, null=True)
# #     occurredat = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'andrekammiesapprovalstmp'


# # class Anyofassertion(models.Model):
# #     id = models.ForeignKey('Assertion', models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'anyofassertion'


# # class ApprovalBookerNotification(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     corporateuri = models.CharField(max_length=255)
# #     emailaddress = models.CharField(max_length=255)
# #     emailname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approval_booker_notification'


# # class Approvalautoescalationroleconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approvalrole = models.CharField(max_length=255, blank=True, null=True)
# #     grouppredicate = models.CharField(max_length=255, blank=True, null=True)
# #     hierarchylevel = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     criteriaid = models.ForeignKey('Approvalautoselectioncriteriaconfig', models.DO_NOTHING, db_column='criteriaid', blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoescalationroleconfig'


# # class Approvalautoescalationruleconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     fieldname = models.CharField(max_length=255, blank=True, null=True)
# #     fieldpredicate = models.CharField(max_length=255, blank=True, null=True)
# #     fieldunit = models.CharField(max_length=255, blank=True, null=True)
# #     fieldvalue = models.CharField(max_length=255, blank=True, null=True)
# #     groupid = models.BigIntegerField(blank=True, null=True)
# #     grouppredicate = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     criteriaid = models.ForeignKey('Approvalautoselectioncriteriaconfig', models.DO_NOTHING, db_column='criteriaid', blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoescalationruleconfig'


# # class Approvalautoselectionactivation(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     autoselectionenabled = models.BooleanField(blank=True, null=True)
# #     createuser = models.BigIntegerField(blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectionactivation'


# # class Approvalautoselectionapproverconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     createruserid = models.BigIntegerField(blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     requestorid = models.BigIntegerField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectionapproverconfig'


# # class Approvalautoselectionconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     active = models.BooleanField()
# #     approvalstrategy = models.CharField(max_length=255, blank=True, null=True)
# #     costcentreid = models.BigIntegerField(blank=True, null=True)
# #     createuser = models.BigIntegerField(blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     selectedmerchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='selectedmerchantid', blank=True, null=True)
# #     createmerchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='createmerchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectionconfig'


# # class Approvalautoselectioncriteriaconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     selectionconfigid = models.ForeignKey(Approvalautoselectionconfig, models.DO_NOTHING, db_column='selectionconfigid', blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectioncriteriaconfig'


# # class Approvalautoselectionroleconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approvalrole = models.CharField(max_length=255, blank=True, null=True)
# #     hierarchylevel = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     criteriaid = models.ForeignKey(Approvalautoselectioncriteriaconfig, models.DO_NOTHING, db_column='criteriaid', blank=True, null=True)
# #     grouppredicate = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectionroleconfig'


# # class Approvalautoselectionruleconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     fieldname = models.CharField(max_length=255, blank=True, null=True)
# #     fieldpredicate = models.CharField(max_length=255, blank=True, null=True)
# #     fieldvalue = models.CharField(max_length=255, blank=True, null=True)
# #     groupid = models.BigIntegerField(blank=True, null=True)
# #     grouppredicate = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     criteriaid = models.ForeignKey(Approvalautoselectioncriteriaconfig, models.DO_NOTHING, db_column='criteriaid', blank=True, null=True)
# #     fieldunit = models.CharField(max_length=255, blank=True, null=True)
# #     approvaltime = models.BigIntegerField(blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     tripstartwithtime = models.BigIntegerField(blank=True, null=True)
# #     triptotalcost = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalautoselectionruleconfig'


# # class Approvalcompanyhierarchyautoselectionconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approverhierarchylevel = models.IntegerField(blank=True, null=True)
# #     approverhierarchyrole = models.CharField(max_length=255, blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)
# #     autoselectedapproverid = models.ForeignKey(Approvalautoselectionapproverconfig, models.DO_NOTHING, db_column='autoselectedapproverid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalcompanyhierarchyautoselectionconfig'


# # class Approvaldefaultcompanyautoapproverconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approverhierarchylevel = models.IntegerField(blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)
# #     autoselectedapproverid = models.ForeignKey(Approvalautoselectionapproverconfig, models.DO_NOTHING, db_column='autoselectedapproverid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvaldefaultcompanyautoapproverconfig'


# # class Approvalgroup(models.Model):
# #     approvalgroupid = models.IntegerField(primary_key=True)
# #     deleted = models.BooleanField(blank=True, null=True)
# #     groupname = models.CharField(max_length=255, blank=True, null=True)
# #     approvalgrouphierarchyid = models.ForeignKey('Approvalgrouphierarchy', models.DO_NOTHING, db_column='approvalgrouphierarchyid', blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalgroup'


# # class Approvalgrouphierarchy(models.Model):
# #     approvalgrouphierarchyid = models.IntegerField(primary_key=True)
# #     approvers = models.TextField(blank=True, null=True)  # This field type is a guess.
# #     level = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalgrouphierarchy'


# # class Approvalindividualautoselectionhierarchy(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approverhierarchylevel = models.IntegerField(blank=True, null=True)
# #     approverhierarchyrole = models.CharField(max_length=255, blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     requestorid = models.BigIntegerField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)
# #     autoselectedapproverid = models.ForeignKey(Approvalautoselectionapproverconfig, models.DO_NOTHING, db_column='autoselectedapproverid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalindividualautoselectionhierarchy'


# # class Approvalrequest(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     messagetoapprover = models.CharField(max_length=255, blank=True, null=True)
# #     messagetorequestor = models.CharField(max_length=255, blank=True, null=True)
# #     requesteddate = models.DateTimeField(blank=True, null=True)
# #     approver = models.ForeignKey('Person', models.DO_NOTHING, db_column='approver', blank=True, null=True)
# #     requested = models.ForeignKey('Triprequirements', models.DO_NOTHING, db_column='requested', blank=True, null=True)
# #     quotes = models.ForeignKey('Quoteresponse', models.DO_NOTHING, db_column='quotes', blank=True, null=True)
# #     shortconvid = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalrequest'


# # class Approvalsubmission(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approvalrequestid = models.CharField(max_length=255, blank=True, null=True)
# #     conclusion = models.CharField(max_length=255, blank=True, null=True)
# #     conclusionmessage = models.CharField(max_length=4000, blank=True, null=True)
# #     modifyable = models.CharField(max_length=255, blank=True, null=True)
# #     resubmissionof = models.BigIntegerField(blank=True, null=True)
# #     requesteddate = models.DateTimeField(blank=True, null=True)
# #     requested = models.ForeignKey('Triprequirements', models.DO_NOTHING, db_column='requested', blank=True, null=True)
# #     conclusiondate = models.DateTimeField(blank=True, null=True)
# #     approvalrequestxml = models.BinaryField(blank=True, null=True)
# #     escalationlevel = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalsubmission'


# # class ApprovalsubmissionSupplierbookingconfirmation(models.Model):
# #     approvalsubmission = models.ForeignKey(Approvalsubmission, models.DO_NOTHING)
# #     automaticallybookedservices_uri = models.ForeignKey('Supplierbookingconfirmation', models.DO_NOTHING, db_column='automaticallybookedservices_uri', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalsubmission_supplierbookingconfirmation'


# # class Approvalsubmissionaction(models.Model):
# #     companyuri = models.CharField(primary_key=True, max_length=255)
# #     actionpath = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'approvalsubmissionaction'


# # class Assertion(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     allof_assertion = models.ForeignKey(Allofassertion, models.DO_NOTHING, blank=True, null=True)
# #     anyof_assertion = models.ForeignKey(Anyofassertion, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'assertion'


# # class Authorizations(models.Model):
# #     tableid = models.BigIntegerField(primary_key=True)
# #     bankauthid = models.CharField(max_length=80, blank=True, null=True)
# #     switchid = models.IntegerField()
# #     reservationid = models.BigIntegerField(blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'authorizations'


# # class Autoapprovalapproverconfig(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)
# #     linemanagerid = models.ForeignKey('Person', models.DO_NOTHING, db_column='linemanagerid', blank=True, null=True)
# #     bypassapproval = models.BooleanField(blank=True, null=True)
# #     mandatelevelamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     lobid = models.ForeignKey('Lob', models.DO_NOTHING, db_column='lobid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'autoapprovalapproverconfig'


# # class Autopayactivation(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     createuser = models.BigIntegerField(blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'autopayactivation'


# # class Aviscargroupdetail(models.Model):
# #     cargroupsid = models.BigIntegerField(primary_key=True)
# #     doors = models.SmallIntegerField(blank=True, null=True)
# #     seats = models.SmallIntegerField(blank=True, null=True)
# #     aircon = models.SmallIntegerField(blank=True, null=True)
# #     automatic = models.SmallIntegerField(blank=True, null=True)
# #     sunroof = models.SmallIntegerField(blank=True, null=True)
# #     antilockbrakes = models.SmallIntegerField(blank=True, null=True)
# #     radiocassette = models.SmallIntegerField(blank=True, null=True)
# #     driverairbag = models.SmallIntegerField(blank=True, null=True)
# #     passengerairbag = models.SmallIntegerField(blank=True, null=True)
# #     electricwindows = models.SmallIntegerField(blank=True, null=True)
# #     powersteering = models.SmallIntegerField(blank=True, null=True)
# #     rearseatbelts = models.SmallIntegerField(blank=True, null=True)
# #     fourwheeldrive = models.SmallIntegerField(blank=True, null=True)
# #     radioonly = models.SmallIntegerField(blank=True, null=True)
# #     sippcode = models.CharField(max_length=10, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'aviscargroupdetail'


# # class Aviscarrentalmap(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     avisstatementid = models.ForeignKey('Avisstatement', models.DO_NOTHING, db_column='avisstatementid', blank=True, null=True)
# #     rentalid = models.ForeignKey('Carrental', models.DO_NOTHING, db_column='rentalid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'aviscarrentalmap'


# # class Aviscountry(models.Model):
# #     countrycode = models.CharField(primary_key=True, max_length=2)
# #     countryname = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'aviscountry'


# # class Avislocation(models.Model):
# #     locationcode = models.CharField(primary_key=True, max_length=10)
# #     locationname = models.CharField(max_length=50, blank=True, null=True)
# #     regioncode = models.CharField(max_length=10, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     proconlocationcode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'avislocation'


# # class Avismiscellanouscodes(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     code = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'avismiscellanouscodes'


# # class Avisregion(models.Model):
# #     regioncode = models.CharField(primary_key=True, max_length=3)
# #     regionname = models.CharField(max_length=50, blank=True, null=True)
# #     countrycode = models.CharField(max_length=2, blank=True, null=True)
# #     continentcode = models.CharField(max_length=3, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'avisregion'


# # class Avisstatement(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     billeddays = models.IntegerField(blank=True, null=True)
# #     contractfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     matched = models.BooleanField(blank=True, null=True)
# #     ratecode = models.CharField(max_length=255, blank=True, null=True)
# #     taxamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     airportsurcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     statementperiod = models.CharField(max_length=255, blank=True, null=True)
# #     rentalcheckindate = models.DateTimeField(blank=True, null=True)
# #     rentalcheckoutdate = models.DateTimeField(blank=True, null=True)
# #     stationname = models.CharField(max_length=255, blank=True, null=True)
# #     rentalagreementno = models.CharField(max_length=255, blank=True, null=True)
# #     accountno = models.CharField(max_length=255, blank=True, null=True)
# #     voucherno = models.CharField(max_length=255, blank=True, null=True)
# #     nameav = models.CharField(max_length=255, blank=True, null=True)
# #     customername = models.CharField(max_length=255, blank=True, null=True)
# #     carchargecode = models.CharField(max_length=255, blank=True, null=True)
# #     cardrivencode = models.CharField(max_length=255, blank=True, null=True)
# #     costcontrolinfo = models.CharField(max_length=255, blank=True, null=True)
# #     frequentflyerno = models.CharField(max_length=255, blank=True, null=True)
# #     drivendistance = models.IntegerField(blank=True, null=True)
# #     amounttmw = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     amountcdw = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     amounttlw = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     amountpai = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     amountntm = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     deliverycollection = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     tourismlevy = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     petrolfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     onewayfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     chargecode = models.CharField(max_length=255, blank=True, null=True)
# #     chargedescription = models.CharField(max_length=255, blank=True, null=True)
# #     misccharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     rentalamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     reservationno = models.CharField(max_length=255, blank=True, null=True)
# #     govtbusinessflag = models.BooleanField(blank=True, null=True)
# #     iatanumber = models.CharField(max_length=255, blank=True, null=True)
# #     iataname = models.CharField(max_length=255, blank=True, null=True)
# #     carreservedcode = models.CharField(max_length=255, blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'avisstatement'


# # class Aviswizardcorporatelink(models.Model):
# #     aviswizardid = models.BigIntegerField(primary_key=True)
# #     wizardnumber = models.CharField(max_length=255, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'aviswizardcorporatelink'


# # class BankDetails(models.Model):
# #     bnk_details_id = models.BigIntegerField(primary_key=True)
# #     bank_name = models.CharField(max_length=30, blank=True, null=True)
# #     branch_name = models.CharField(max_length=50, blank=True, null=True)
# #     branch_number = models.CharField(max_length=20, blank=True, null=True)
# #     account_type = models.CharField(max_length=20, blank=True, null=True)
# #     account_number = models.CharField(max_length=20, blank=True, null=True)
# #     account_name = models.CharField(max_length=30, blank=True, null=True)
# #     cash_details_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bank_details'


# # class Bankaccount(models.Model):
# #     accountnumber = models.CharField(max_length=255, blank=True, null=True)
# #     statementitem_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bankaccount'


# # class Batch(models.Model):
# #     batchid = models.BigIntegerField(primary_key=True)
# #     messageid = models.BigIntegerField()
# #     fromname = models.CharField(max_length=50, blank=True, null=True)
# #     fromaaccountid = models.BigIntegerField(blank=True, null=True)
# #     networkproviderid = models.BigIntegerField(blank=True, null=True)
# #     netprovmessageid = models.CharField(max_length=100, blank=True, null=True)
# #     starttime = models.DateTimeField()
# #     providerbatchid = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'batch'


# # class Batchgroup(models.Model):
# #     batchgroupid = models.BigIntegerField(primary_key=True)
# #     batchid = models.BigIntegerField()
# #     cellnumberemail = models.CharField(max_length=60, blank=True, null=True)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     errorid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'batchgroup'


# # class Batchgroupfield(models.Model):
# #     fieldid = models.BigIntegerField(primary_key=True)
# #     batchgroupid = models.BigIntegerField()
# #     field = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'batchgroupfield'


# # class Batchmerchantpaymentmap(models.Model):
# #     batchpaymentrqid = models.BigIntegerField(primary_key=True)
# #     merpaymentrqid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'batchmerchantpaymentmap'
# #         unique_together = (('batchpaymentrqid', 'merpaymentrqid'),)


# # class Batchpaymentrequest(models.Model):
# #     batchpaymentid = models.BigIntegerField(primary_key=True)
# #     sentflag = models.IntegerField()
# #     senttime = models.DateTimeField(blank=True, null=True)
# #     scheduledtime = models.DateTimeField()
# #     minimumtx = models.IntegerField(blank=True, null=True)
# #     maximumtx = models.IntegerField(blank=True, null=True)
# #     switchid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'batchpaymentrequest'


# # class Bidvestcarrentalmap(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     bidveststatementid = models.ForeignKey('Bidveststatement', models.DO_NOTHING, db_column='bidveststatementid', blank=True, null=True)
# #     rentalid = models.ForeignKey('Carrental', models.DO_NOTHING, db_column='rentalid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bidvestcarrentalmap'


# # class Bidveststatement(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     actualvehiclegrp = models.CharField(max_length=255, blank=True, null=True)
# #     additionaldrivercharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     adminfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     airline = models.CharField(max_length=255, blank=True, null=True)
# #     airportsurcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     bagaggeinsurance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     chargedvehiclegrp = models.CharField(max_length=255, blank=True, null=True)
# #     clientname1 = models.CharField(max_length=255, blank=True, null=True)
# #     clientname2 = models.CharField(max_length=255, blank=True, null=True)
# #     clientno = models.CharField(max_length=255, blank=True, null=True)
# #     co2emissionrate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     contractfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     costcentre = models.CharField(max_length=255, blank=True, null=True)
# #     crossbordercharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     damagerwaivercost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     days = models.CharField(max_length=255, blank=True, null=True)
# #     deliverycharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     distancecost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     enddate = models.CharField(max_length=255, blank=True, null=True)
# #     endtime = models.CharField(max_length=255, blank=True, null=True)
# #     extref = models.CharField(max_length=255, blank=True, null=True)
# #     frequentflyer = models.CharField(max_length=255, blank=True, null=True)
# #     fuelcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     iatanumber = models.CharField(max_length=255, blank=True, null=True)
# #     inbranch = models.CharField(max_length=255, blank=True, null=True)
# #     inregistrationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     invoicedate = models.CharField(max_length=255, blank=True, null=True)
# #     kilometres = models.CharField(max_length=255, blank=True, null=True)
# #     lodgecardno = models.CharField(max_length=255, blank=True, null=True)
# #     model = models.CharField(max_length=255, blank=True, null=True)
# #     navigationunitcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     netttrans = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     onewaydropoffcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     othercharges = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     outbranch = models.CharField(max_length=255, blank=True, null=True)
# #     outregistrationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     paicost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     paynumber = models.CharField(max_length=255, blank=True, null=True)
# #     paytype = models.CharField(max_length=255, blank=True, null=True)
# #     pricelistnumber = models.CharField(max_length=255, blank=True, null=True)
# #     profilegroupcode = models.CharField(max_length=255, blank=True, null=True)
# #     promotioncode = models.CharField(max_length=255, blank=True, null=True)
# #     rentalagreementno = models.CharField(max_length=255, blank=True, null=True)
# #     rentalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     rentercustomernumber = models.CharField(max_length=255, blank=True, null=True)
# #     ressourcename = models.CharField(max_length=255, blank=True, null=True)
# #     stampdutycharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     startdate = models.CharField(max_length=255, blank=True, null=True)
# #     starttime = models.CharField(max_length=255, blank=True, null=True)
# #     sundrycost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     tariffperiodcode = models.CharField(max_length=255, blank=True, null=True)
# #     tax = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     theftordamagescharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     theftwaivercost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     totalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     totalraco2 = models.FloatField(blank=True, null=True)
# #     tourismlevy = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     transnumber = models.CharField(max_length=255, blank=True, null=True)
# #     transtype = models.CharField(max_length=255, blank=True, null=True)
# #     travellername = models.CharField(max_length=255, blank=True, null=True)
# #     windscreentyrewaiver = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bidveststatement'


# # class Bookingcentrecodes(models.Model):
# #     code = models.CharField(max_length=-1)

# #     class Meta:
# #         managed = False
# #         db_table = 'bookingcentrecodes'


# # class Bookingchangecost(models.Model):
# #     changeid = models.BigIntegerField(primary_key=True)
# #     airlineid = models.BigIntegerField()
# #     type = models.CharField(max_length=50)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2)
# #     cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bookingchangecost'


# # class Bookingchannel(models.Model):
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bookingchannel'


# # class Bookingengine(models.Model):
# #     engineid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=60)
# #     uniformresourcelocator = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bookingengine'


# # class Branch(models.Model):
# #     branchid = models.IntegerField(primary_key=True)
# #     branchname = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'branch'


# # class Bussuppliers(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     servicecode = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovidername = models.CharField(max_length=255, blank=True, null=True)
# #     vandorcode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bussuppliers'


# # class Bustransit(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     departuredatetime = models.DateTimeField(blank=True, null=True)
# #     goingto = models.CharField(max_length=255, blank=True, null=True)
# #     leavingfrom = models.CharField(max_length=255, blank=True, null=True)
# #     busclass = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovider = models.CharField(max_length=255, blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=255, blank=True, null=True)
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid', blank=True, null=True)
# #     status_resstatus = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='status_resstatus', blank=True, null=True)
# #     reservationnumber = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'bustransit'


# # class Cachedimagedata(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     data = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cachedimagedata'


# # class Cachedpicture(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     contenttype = models.CharField(max_length=255, blank=True, null=True)
# #     width = models.IntegerField()
# #     height = models.IntegerField()
# #     published = models.DateTimeField(blank=True, null=True)
# #     rank = models.IntegerField(blank=True, null=True)
# #     filesize = models.BigIntegerField()
# #     subjecturi = models.CharField(max_length=255, blank=True, null=True)
# #     pictureuri = models.CharField(max_length=255, blank=True, null=True)
# #     imagedata = models.ForeignKey(Cachedimagedata, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cachedpicture'


# # class CaptchaWhitelist(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     ipaddress = models.CharField(max_length=255, blank=True, null=True)
# #     ipaddressdescription = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'captcha_whitelist'


# # class Carautovoucherconfiguration(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     code = models.CharField(max_length=255, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carautovoucherconfiguration'


# # class Carboncopyemail(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     emailaddress = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carboncopyemail'


# # class Carbonemission(models.Model):
# #     carbonemissionid = models.BigIntegerField(primary_key=True)
# #     carbonemissionsinkg = models.FloatField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carbonemission'


# # class Carbonemissionderivedvalues(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     carbonemissionsinkg = models.FloatField(blank=True, null=True)
# #     longhauldistanceflown = models.FloatField(blank=True, null=True)
# #     longhaulsectorsflown = models.IntegerField(blank=True, null=True)
# #     mediumhauldistanceflown = models.FloatField(blank=True, null=True)
# #     mediumhaulsectorsflown = models.IntegerField(blank=True, null=True)
# #     shorthauldistanceflown = models.FloatField(blank=True, null=True)
# #     shorthaulsectorsflown = models.IntegerField(blank=True, null=True)
# #     totaldistanceflown = models.FloatField(blank=True, null=True)
# #     totalsectorsflown = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carbonemissionderivedvalues'


# # class Carclassassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     industryclass = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carclassassertion'


# # class Carclassproviderspecificassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     providerspecificclass = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carclassproviderspecificassertion'


# # class Card(models.Model):
# #     cardnumber = models.CharField(primary_key=True, max_length=20)
# #     statusid = models.IntegerField(blank=True, null=True)
# #     expirydate = models.DateTimeField(blank=True, null=True)
# #     issuedate = models.DateTimeField(blank=True, null=True)
# #     pin = models.IntegerField(blank=True, null=True)
# #     account_id = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'card'


# # class Carddetail(models.Model):
# #     carddetailuri = models.CharField(primary_key=True, max_length=255)
# #     number = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     expirydate = models.DateField(blank=True, null=True)
# #     holdername = models.CharField(max_length=255, blank=True, null=True)
# #     issuer = models.CharField(max_length=255, blank=True, null=True)
# #     seriescode = models.CharField(max_length=255, blank=True, null=True)
# #     pin = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carddetail'


# # class Cardhist(models.Model):
# #     cardhistid = models.BigIntegerField(primary_key=True)
# #     cardnumber = models.CharField(max_length=30, blank=True, null=True)
# #     actionid = models.IntegerField(blank=True, null=True)
# #     reasonid = models.IntegerField(blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)
# #     adminid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cardhist'


# # class Cardimage(models.Model):
# #     memberid = models.BigIntegerField(primary_key=True)
# #     cardzerobuffer = models.CharField(max_length=10)
# #     name = models.CharField(max_length=50)
# #     surname = models.CharField(max_length=50)
# #     initial = models.CharField(max_length=10)
# #     branchname = models.CharField(max_length=60)
# #     imagelocation = models.CharField(max_length=100, blank=True, null=True)
# #     expdate = models.CharField(max_length=4, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cardimage'


# # class Cardvault(models.Model):
# #     cardvaulturi = models.CharField(primary_key=True, max_length=255)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     token = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cardvault'


# # class Cargroups(models.Model):
# #     groupid = models.BigIntegerField(primary_key=True)
# #     id = models.CharField(max_length=10)
# #     description = models.CharField(max_length=100)
# #     carsupplierid = models.BigIntegerField()
# #     avisregioncode = models.CharField(max_length=3, blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)
# #     carsuppliertype = models.IntegerField(blank=True, null=True)
# #     ranking = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cargroups'


# # class Cargrouptypes(models.Model):
# #     groupid = models.BigIntegerField(primary_key=True)
# #     id = models.CharField(max_length=20)
# #     description = models.CharField(max_length=100)
# #     carsupplierid = models.BigIntegerField()
# #     avisregioncode = models.CharField(max_length=3, blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)
# #     carsuppliertype = models.IntegerField(blank=True, null=True)
# #     ranking = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cargrouptypes'


# # class Carhirerequest(models.Model):
# #     requestid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     rentalpoint = models.CharField(max_length=50, blank=True, null=True)
# #     rentaldate = models.DateTimeField(blank=True, null=True)
# #     days = models.IntegerField(blank=True, null=True)
# #     maximumclass = models.CharField(max_length=50, blank=True, null=True)
# #     billinginfo = models.CharField(max_length=50, blank=True, null=True)
# #     cargroupid = models.CharField(max_length=50, blank=True, null=True)
# #     carhire = models.CharField(max_length=75, blank=True, null=True)
# #     transmission = models.CharField(max_length=25, blank=True, null=True)
# #     pickupcountry = models.CharField(max_length=50, blank=True, null=True)
# #     dropoffcountry = models.CharField(max_length=50, blank=True, null=True)
# #     pickuplocation = models.CharField(max_length=100, blank=True, null=True)
# #     dropofflocation = models.CharField(max_length=100, blank=True, null=True)
# #     start_datetime = models.DateTimeField(blank=True, null=True)
# #     end_datetime = models.DateTimeField(blank=True, null=True)
# #     pickupdatetime = models.DateTimeField(blank=True, null=True)
# #     dropoffdatetime = models.DateTimeField(blank=True, null=True)
# #     pickupcountry_id = models.CharField(max_length=1, blank=True, null=True)
# #     dropoffcountry_id = models.CharField(max_length=1, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carhirerequest'


# # class Caritemdetail(models.Model):
# #     id = models.ForeignKey('Statementitemdetail', models.DO_NOTHING, db_column='id', primary_key=True)
# #     rentalagreementnumber = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'caritemdetail'


# # class CaritemdetailCarrental(models.Model):
# #     caritemdetail = models.ForeignKey(Caritemdetail, models.DO_NOTHING)
# #     carrental_rentalid = models.ForeignKey('Carrental', models.DO_NOTHING, db_column='carrental_rentalid')

# #     class Meta:
# #         managed = False
# #         db_table = 'caritemdetail_carrental'


# # class CaritemdetailOtheritems(models.Model):
# #     caritemdetail = models.ForeignKey(Caritemdetail, models.DO_NOTHING)
# #     otheritems_otheritemid = models.ForeignKey('Otheritems', models.DO_NOTHING, db_column='otheritems_otheritemid')

# #     class Meta:
# #         managed = False
# #         db_table = 'caritemdetail_otheritems'


# # class Carrental(models.Model):
# #     rentalid = models.BigIntegerField(primary_key=True)
# #     reservationnumber = models.CharField(max_length=150)
# #     from_date = models.DateTimeField()
# #     to_date = models.DateTimeField(blank=True, null=True)
# #     actual_duration = models.IntegerField(blank=True, null=True)
# #     charged_duration = models.IntegerField(blank=True, null=True)
# #     rental_office_tel = models.CharField(max_length=15, blank=True, null=True)
# #     rental_office_add = models.CharField(max_length=1024, blank=True, null=True)
# #     return_office_tel = models.CharField(max_length=15, blank=True, null=True)
# #     return_office_add = models.CharField(max_length=1024, blank=True, null=True)
# #     car_group = models.ForeignKey(Cargroups, models.DO_NOTHING, blank=True, null=True)
# #     rental_price = models.DecimalField(max_digits=20, decimal_places=2)
# #     rental_duration = models.IntegerField(blank=True, null=True)
# #     addition_cost = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     carsupplierid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='carsupplierid', blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     status = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='status', blank=True, null=True)
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid')
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     estkm = models.BigIntegerField(blank=True, null=True)
# #     additexpexcl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     additexpincl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     rentalcostexc = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     rentalcostincl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     waiversexcl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     waiversincl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     costtax = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     totalexcl = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
# #     pickuplocationcode = models.CharField(max_length=200, blank=True, null=True)
# #     dropofflocationcode = models.CharField(max_length=200, blank=True, null=True)
# #     wizardnumber = models.CharField(max_length=50, blank=True, null=True)
# #     awdnumber = models.CharField(max_length=50, blank=True, null=True)
# #     redclubnumber = models.CharField(max_length=50, blank=True, null=True)
# #     loyaltyprogramcode = models.CharField(max_length=50, blank=True, null=True)
# #     loyaltyprogramnum = models.CharField(max_length=50, blank=True, null=True)
# #     vouchernumber = models.CharField(max_length=100, blank=True, null=True)
# #     vouchertype = models.CharField(max_length=100, blank=True, null=True)
# #     remarks = models.CharField(max_length=250, blank=True, null=True)
# #     carsuppliertype = models.IntegerField(blank=True, null=True)
# #     addressid = models.ForeignKey(Addressdetail, models.DO_NOTHING, db_column='addressid', blank=True, null=True)
# #     sippcode = models.CharField(max_length=255, blank=True, null=True)
# #     travelreservation = models.ForeignKey('Travelreservation', models.DO_NOTHING, db_column='travelreservation', blank=True, null=True)
# #     cardescription = models.CharField(max_length=255, blank=True, null=True)
# #     transmission = models.CharField(max_length=255, blank=True, null=True)
# #     distancecostdescription = models.CharField(max_length=255, blank=True, null=True)
# #     car_group_type = models.ForeignKey(Cargrouptypes, models.DO_NOTHING, blank=True, null=True)
# #     collection_address_1 = models.CharField(max_length=250, blank=True, null=True)
# #     collection_address_2 = models.CharField(max_length=250, blank=True, null=True)
# #     collection_address_3 = models.CharField(max_length=250, blank=True, null=True)
# #     delivery_address_1 = models.CharField(max_length=250, blank=True, null=True)
# #     delivery_address_2 = models.CharField(max_length=250, blank=True, null=True)
# #     delivery_address_3 = models.CharField(max_length=250, blank=True, null=True)
# #     tripglcodeid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carrental'
# #         unique_together = (('rentalid', 'reservationid'),)


# # class CarrentalAmenity(models.Model):
# #     carrental_rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='carrental_rentalid')
# #     amenities = models.ForeignKey(Amenity, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'carrental_amenity'


# # class CarrentalDistancecost(models.Model):
# #     carrental_rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='carrental_rentalid')
# #     distancecosts = models.ForeignKey('Distancecost', models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'carrental_distancecost'


# # class CarrentalInvoicefile(models.Model):
# #     carrental_rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='carrental_rentalid', primary_key=True)
# #     invoices = models.ForeignKey('Invoicefile', models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'carrental_invoicefile'
# #         unique_together = (('carrental_rentalid', 'invoices'),)


# # class Carsupplier(models.Model):
# #     carsupplierid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.BigIntegerField()
# #     carsuppliertype = models.IntegerField(blank=True, null=True)
# #     suppliercode = models.CharField(max_length=255, blank=True, null=True)
# #     vendornumber = models.CharField(max_length=255, blank=True, null=True)
# #     assertiontype = models.CharField(max_length=255, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carsupplier'


# # class Carsupplierinclusionlist(models.Model):
# #     preferredsupplier_id = models.BigIntegerField(primary_key=True)
# #     company = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     supplier = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carsupplierinclusionlist'


# # class Carsuppliersassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     carsupplier = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     supplier = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carsuppliersassertion'


# # class Cartransmissionassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     transmissiontype = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cartransmissionassertion'


# # class Carvoucherconfiguration(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     company = models.CharField(max_length=255, blank=True, null=True)
# #     supplier = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'carvoucherconfiguration'


# # class Carvouchertype(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     name = models.CharField(max_length=255)
# #     supplierid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'carvouchertype'


# # class Cashdetails(models.Model):
# #     cash_details_id = models.BigIntegerField(primary_key=True)
# #     accountid = models.BigIntegerField(blank=True, null=True)
# #     balance = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cashdetails'


# # class Cashtransactions(models.Model):
# #     transactionid = models.BigIntegerField(primary_key=True)
# #     debitcredit = models.IntegerField(blank=True, null=True)
# #     transactiontypeid = models.BigIntegerField(blank=True, null=True)
# #     accountid = models.BigIntegerField()
# #     amount = models.DecimalField(max_digits=20, decimal_places=2)
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     invoiceid = models.BigIntegerField()
# #     fromaccount = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cashtransactions'


# # class Category(models.Model):
# #     cat_id = models.CharField(primary_key=True, max_length=18)
# #     description = models.CharField(max_length=18)
# #     parent_cat_id = models.CharField(max_length=18)
# #     name = models.CharField(max_length=18)
# #     created = models.CharField(max_length=18)

# #     class Meta:
# #         managed = False
# #         db_table = 'category'


# # class Ccdetails(models.Model):
# #     ccdetailsid = models.BigIntegerField(primary_key=True)
# #     ccnumber = models.CharField(max_length=200)
# #     cctype = models.CharField(max_length=10, blank=True, null=True)
# #     ccholdername = models.CharField(max_length=70, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ccdetails'


# # class Changeflightrequest(models.Model):
# #     id = models.CharField(primary_key=True, max_length=255)
# #     arrive = models.DateTimeField(blank=True, null=True)
# #     depart = models.DateTimeField(blank=True, null=True)
# #     flight = models.CharField(max_length=255, blank=True, null=True)
# #     leg_fare = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     provider = models.CharField(max_length=255, blank=True, null=True)
# #     rate_source = models.CharField(max_length=255, blank=True, null=True)
# #     reasonforchange = models.CharField(max_length=255, blank=True, null=True)
# #     route = models.CharField(max_length=255, blank=True, null=True)
# #     seat_class = models.CharField(max_length=255, blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'changeflightrequest'


# # class Charity(models.Model):
# #     charity_id = models.BigIntegerField(primary_key=True)
# #     member_id = models.BigIntegerField()
# #     charity_name = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     url = models.CharField(max_length=90, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'charity'


# # class Chaufferdrivenvehicleassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     supplier = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'chaufferdrivenvehicleassertion'


# # class Cities(models.Model):
# #     region = models.IntegerField(blank=True, null=True)
# #     subregion = models.CharField(max_length=255, blank=True, null=True)
# #     ufi = models.CharField(max_length=255, blank=True, null=True)
# #     uni = models.CharField(max_length=255, blank=True, null=True)
# #     dsg = models.CharField(max_length=255, blank=True, null=True)
# #     cc_fpis = models.CharField(max_length=255, blank=True, null=True)
# #     cc_iso = models.ForeignKey('Country', models.DO_NOTHING, db_column='cc_iso', blank=True, null=True)
# #     full_name = models.CharField(max_length=255, blank=True, null=True)
# #     full_name_nd = models.CharField(max_length=255, blank=True, null=True)
# #     sort_name = models.CharField(max_length=255, blank=True, null=True)
# #     adm1 = models.CharField(max_length=255, blank=True, null=True)
# #     adm1_full_name = models.CharField(max_length=255, blank=True, null=True)
# #     adm2 = models.CharField(max_length=255, blank=True, null=True)
# #     adm2fullname = models.CharField(max_length=255, blank=True, null=True)
# #     latitude = models.CharField(max_length=255, blank=True, null=True)
# #     longitude = models.CharField(max_length=255, blank=True, null=True)
# #     population = models.IntegerField(blank=True, null=True)
# #     timezone = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
# #     adm2population = models.IntegerField(blank=True, null=True)
# #     adm2_full_name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cities'


# # class Citiescodes(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     cityname = models.CharField(max_length=255, blank=True, null=True)
# #     code = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'citiescodes'


# # class Clientaccountnumbers(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     accountnumber = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'clientaccountnumbers'


# # class Clientairlinepreference(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     airlinecode = models.CharField(max_length=255, blank=True, null=True)
# #     client_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'clientairlinepreference'


# # class Clientairlineproviderspecificclasspreference(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     providerspecificclass = models.CharField(max_length=255, blank=True, null=True)
# #     client_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'clientairlineproviderspecificclasspreference'


# # class Clientprofilefeature(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     enabled = models.BooleanField()
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     profilefeature = models.ForeignKey('Profilefeature', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'clientprofilefeature'


# # class Clientserviceproviderpreference(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     serviceprovideruri = models.CharField(max_length=255, blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     client_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     supplier_engineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='supplier_engineid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'clientserviceproviderpreference'


# # class Companyapprovalpolicy(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approvalrequired = models.BooleanField(blank=True, null=True)
# #     merchant_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     spendthreshold = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     approvalpolicy = models.CharField(max_length=255, blank=True, null=True)
# #     conditioncheckfailure = models.CharField(max_length=255, blank=True, null=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     constraint = models.ForeignKey(Assertion, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyapprovalpolicy'


# # class CompanyapprovalpolicyLeon(models.Model):
# #     id = models.BigIntegerField(blank=True, null=True)
# #     approvalrequired = models.BooleanField(blank=True, null=True)
# #     merchant_merchant_id = models.BigIntegerField(blank=True, null=True)
# #     spendthreshold = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     approvalpolicy = models.CharField(max_length=255, blank=True, null=True)
# #     conditioncheckfailure = models.CharField(max_length=255, blank=True, null=True)
# #     company_merchant_id = models.BigIntegerField(blank=True, null=True)
# #     constraint_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyapprovalpolicy_leon'


# # class Companyautomaticbookingpreference(models.Model):
# #     automaticbookingpreferenceid = models.BigIntegerField(primary_key=True)
# #     automaticbookingpreference = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyautomaticbookingpreference'


# # class Companyevaluatorselectionstrategy(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     defaultselection = models.BooleanField()
# #     displayname = models.CharField(max_length=255, blank=True, null=True)
# #     selectionstrategy = models.CharField(max_length=255, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchant', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyevaluatorselectionstrategy'


# # class Companygroup(models.Model):
# #     groupid = models.CharField(primary_key=True, max_length=255)
# #     description = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companygroup'


# # class CompanyitinsyncAutosubscription(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     destination_uri = models.CharField(max_length=255, blank=True, null=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyitinsync_autosubscription'


# # class Companyorders(models.Model):
# #     orderid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)
# #     ordernumber = models.CharField(max_length=50, blank=True, null=True)
# #     xmlpacket = models.TextField(blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyorders'


# # class Companyprofileaccess(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyprofileaccess'


# # class CompanyprofileaccessProfileaccesscredentialtypes(models.Model):
# #     companyprofileaccess = models.ForeignKey(Companyprofileaccess, models.DO_NOTHING)
# #     profileaccesscredentialtypes = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companyprofileaccess_profileaccesscredentialtypes'


# # class Companypurchasecontrolsupplier(models.Model):
# #     companypurchasecontrolsupplierid = models.BigIntegerField(primary_key=True)
# #     company = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     purchasecontrolsupplier = models.ForeignKey('Purchasecontrolsupplier', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companypurchasecontrolsupplier'


# # class Companysuperapprover(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     approverid = models.ForeignKey('Person', models.DO_NOTHING, db_column='approverid', blank=True, null=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'companysuperapprover'


# # class Constraintassertiontable(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     constrainturi = models.CharField(max_length=255, blank=True, null=True)
# #     enforceability = models.CharField(max_length=255, blank=True, null=True)
# #     applicable = models.ForeignKey(Assertion, models.DO_NOTHING, blank=True, null=True)
# #     requirement = models.ForeignKey(Assertion, models.DO_NOTHING, blank=True, null=True)
# #     constraint = models.ForeignKey('Policy', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'constraintassertiontable'


# # class Constrainttable(models.Model):
# #     constraintid = models.BigIntegerField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'constrainttable'


# # class Constraintviolation(models.Model):
# #     constraintviolationid = models.BigIntegerField(primary_key=True)
# #     datetime = models.DateTimeField(blank=True, null=True)
# #     bookingconfirmation = models.CharField(max_length=255, blank=True, null=True)
# #     trip_trip = models.ForeignKey('Trip', models.DO_NOTHING, blank=True, null=True)
# #     violatedby_agentid = models.ForeignKey('Travelagent', models.DO_NOTHING, db_column='violatedby_agentid', blank=True, null=True)
# #     violationreason = models.CharField(max_length=1024, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     violatedbyperson_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     additionalcomments = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'constraintviolation'


# # class ConstraintviolationConstraintassertiontable(models.Model):
# #     constraintviolation_constraintviolationid = models.ForeignKey(Constraintviolation, models.DO_NOTHING, db_column='constraintviolation_constraintviolationid')
# #     constraints = models.ForeignKey(Constraintassertiontable, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'constraintviolation_constraintassertiontable'


# # class ConstraintviolationConstrainttable(models.Model):
# #     constraintviolation_constraintviolationid = models.ForeignKey(Constraintviolation, models.DO_NOTHING, db_column='constraintviolation_constraintviolationid')
# #     constraints_constraintid = models.ForeignKey(Constrainttable, models.DO_NOTHING, db_column='constraints_constraintid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'constraintviolation_constrainttable'


# # class Consultantassistancepreference(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     req_notify_mail = models.CharField(max_length=512, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'consultantassistancepreference'


# # class Contact(models.Model):
# #     contact_id = models.BigIntegerField(primary_key=True)
# #     member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     title = models.ForeignKey('Title', models.DO_NOTHING, blank=True, null=True)
# #     fname = models.CharField(max_length=255, blank=True, null=True)
# #     sname = models.CharField(max_length=255, blank=True, null=True)
# #     email = models.CharField(max_length=100, blank=True, null=True)
# #     telephone = models.CharField(max_length=100, blank=True, null=True)
# #     fax = models.CharField(max_length=100, blank=True, null=True)
# #     cell = models.CharField(max_length=100, blank=True, null=True)
# #     address1 = models.CharField(max_length=250, blank=True, null=True)
# #     address2 = models.CharField(max_length=250, blank=True, null=True)
# #     post_code = models.CharField(max_length=100, blank=True, null=True)
# #     country_code = models.CharField(max_length=2, blank=True, null=True)
# #     province = models.ForeignKey('Province', models.DO_NOTHING, blank=True, null=True)
# #     city = models.CharField(max_length=255, blank=True, null=True)
# #     language_id = models.IntegerField(blank=True, null=True)
# #     con_type_id = models.IntegerField(blank=True, null=True)
# #     lang_code = models.CharField(max_length=6, blank=True, null=True)
# #     postaladdress1 = models.CharField(max_length=250, blank=True, null=True)
# #     postaladdress2 = models.CharField(max_length=250, blank=True, null=True)
# #     postalpost_code = models.CharField(max_length=100, blank=True, null=True)
# #     postalprovince_id = models.IntegerField(blank=True, null=True)
# #     postalcountry_code = models.CharField(max_length=2, blank=True, null=True)
# #     workphone = models.CharField(max_length=100, blank=True, null=True)
# #     contactmethodid = models.IntegerField(blank=True, null=True)
# #     postalcity = models.CharField(max_length=255, blank=True, null=True)
# #     birthdate = models.DateField(blank=True, null=True)
# #     idnumber = models.CharField(max_length=50, blank=True, null=True)
# #     passport = models.CharField(max_length=255, blank=True, null=True)
# #     gender = models.CharField(max_length=255, blank=True, null=True)
# #     agegroup = models.CharField(max_length=255, blank=True, null=True)
# #     middlename = models.CharField(max_length=255, blank=True, null=True)
# #     driverslicence = models.CharField(max_length=255, blank=True, null=True)
# #     idcountrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='idcountrycode', blank=True, null=True)
# #     passportcountrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='passportcountrycode', blank=True, null=True)
# #     driverscountrycode = models.ForeignKey('Country', models.DO_NOTHING, db_column='driverscountrycode', blank=True, null=True)
# #     displayfirstname = models.CharField(max_length=255, blank=True, null=True)
# #     displaylastname = models.CharField(max_length=255, blank=True, null=True)
# #     displaymiddlename = models.CharField(max_length=255, blank=True, null=True)
# #     ccemail = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'contact'


# # class ContactType(models.Model):
# #     con_type_id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'contact_type'


# # class Contactdetail(models.Model):
# #     contactdetailid = models.AutoField(primary_key=True)
# #     fax = models.CharField(max_length=255, blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     phone = models.CharField(max_length=255, blank=True, null=True)
# #     mobile = models.CharField(max_length=255, blank=True, null=True)
# #     contacttype = models.CharField(max_length=255, blank=True, null=True)
# #     website = models.CharField(max_length=255, blank=True, null=True)
# #     addressid = models.ForeignKey(Addressdetail, models.DO_NOTHING, db_column='addressid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'contactdetail'


# # class Contactdetailstype(models.Model):
# #     type_id = models.IntegerField(primary_key=True)
# #     type = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'contactdetailstype'


# # class Contactmethod(models.Model):
# #     contactmethodid = models.IntegerField(primary_key=True)
# #     contactmethodname = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'contactmethod'


# # class Contactmethodmap(models.Model):
# #     memberid = models.BigIntegerField()
# #     contactmethodid = models.BigIntegerField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'contactmethodmap'
# #         unique_together = (('contactmethodid', 'memberid'),)


# # class Corporate(models.Model):
# #     corporateid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.BigIntegerField()
# #     triptype = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'corporate'


# # class Corporatediscount(models.Model):
# #     corporatemerchantid = models.BigIntegerField(primary_key=True)
# #     suppliermerchantid = models.BigIntegerField()
# #     percentage = models.DecimalField(max_digits=20, decimal_places=2)

# #     class Meta:
# #         managed = False
# #         db_table = 'corporatediscount'
# #         unique_together = (('corporatemerchantid', 'suppliermerchantid'),)


# # class Corporatemerchant(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     companyname = models.CharField(max_length=255, blank=True, null=True)
# #     corporatecode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'corporatemerchant'


# # class Corporateprogrammap(models.Model):
# #     merchantid = models.BigIntegerField(primary_key=True)
# #     programid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'corporateprogrammap'


# # class Cost(models.Model):
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     statementitem_id = models.BigIntegerField(blank=True, null=True)
# #     statementitemid = models.ForeignKey('Statementitem', models.DO_NOTHING, db_column='statementitemid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'cost'


# # class Costallocation(models.Model):
# #     ordernumber = models.CharField(max_length=255, blank=True, null=True)
# #     statementitem_id = models.BigIntegerField(blank=True, null=True)
# #     statementitemid = models.ForeignKey('Statementitem', models.DO_NOTHING, db_column='statementitemid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'costallocation'


# # class Costassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     cost = models.ForeignKey('Costassertioncost', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'costassertion'


# # class Costassertioncost(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     costcomponenttype = models.CharField(max_length=255, blank=True, null=True)
# #     parent = models.ForeignKey('self', models.DO_NOTHING, db_column='parent', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'costassertioncost'


# # class Costcentreassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     costcentre = models.CharField(max_length=255, blank=True, null=True)
# #     costcentrename = models.CharField(max_length=255, blank=True, null=True)
# #     domain = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'costcentreassertion'


# # class Costconstraint(models.Model):
# #     constraintid = models.ForeignKey(Constrainttable, models.DO_NOTHING, db_column='constraintid', primary_key=True)
# #     target = models.CharField(max_length=255, blank=True, null=True)
# #     matchtype = models.CharField(max_length=255, blank=True, null=True)
# #     cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     preferencelevel = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'costconstraint'


# # class Country(models.Model):
# #     country_code = models.CharField(primary_key=True, max_length=2)
# #     name = models.CharField(max_length=80)
# #     printable_name = models.CharField(max_length=80)
# #     iso3 = models.CharField(max_length=3, blank=True, null=True)
# #     numcode = models.CharField(max_length=4, blank=True, null=True)
# #     regional = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'country'


# # class Credentialslinkage(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     disabled = models.BooleanField()
# #     updatedat = models.DateTimeField(blank=True, null=True)
# #     company_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     credential = models.ForeignKey('Suppliercredential', models.DO_NOTHING)
# #     updateby_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'credentialslinkage'


# # class Currency(models.Model):
# #     code = models.CharField(primary_key=True, max_length=255)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'currency'


# # class Currencyprovisioning(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     boughtwithamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     boughtwithcurrency = models.CharField(max_length=255, blank=True, null=True)
# #     deliverydatetime = models.DateTimeField(blank=True, null=True)
# #     paymentmechanism = models.CharField(max_length=255, blank=True, null=True)
# #     purchasedatetime = models.DateTimeField(blank=True, null=True)
# #     requestedamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     requestedcurrency = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovider = models.CharField(max_length=255, blank=True, null=True)
# #     trip = models.ForeignKey('Trip', models.DO_NOTHING, blank=True, null=True)
# #     boughtwithpaymentmechanism = models.CharField(max_length=255, blank=True, null=True)
# #     city = models.CharField(max_length=255, blank=True, null=True)
# #     country = models.CharField(max_length=255, blank=True, null=True)
# #     postalcode = models.CharField(max_length=255, blank=True, null=True)
# #     province = models.CharField(max_length=255, blank=True, null=True)
# #     streetaddress = models.CharField(max_length=255, blank=True, null=True)
# #     suburb = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'currencyprovisioning'


# # class Cutmethod(models.Model):
# #     cuttype = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=20)

# #     class Meta:
# #         managed = False
# #         db_table = 'cutmethod'


# # class Cuts(models.Model):
# #     from_account = models.BigIntegerField()
# #     target_account = models.BigIntegerField()
# #     cut = models.DecimalField(max_digits=20, decimal_places=10)
# #     cuttype = models.IntegerField()
# #     id = models.BigIntegerField(primary_key=True)
# #     cutmethod = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'cuts'


# # class Cuttype(models.Model):
# #     type = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=20)

# #     class Meta:
# #         managed = False
# #         db_table = 'cuttype'


# # class Cuttypevalues(models.Model):
# #     cuttype = models.IntegerField()
# #     name = models.CharField(max_length=20)

# #     class Meta:
# #         managed = False
# #         db_table = 'cuttypevalues'


# # class Dailyrateassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     rate = models.ForeignKey(Costassertioncost, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'dailyrateassertion'


# # class Debitcredittype(models.Model):
# #     typeid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'debitcredittype'


# # class Defaultvouchertype(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     voucherowner = models.CharField(max_length=255, blank=True, null=True)
# #     vouchertype = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'defaultvouchertype'


# # class Delivery(models.Model):
# #     deliveryid = models.BigIntegerField(primary_key=True)
# #     deliverytypeid = models.IntegerField()
# #     eventid = models.BigIntegerField()
# #     status = models.IntegerField()
# #     branchid = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'delivery'


# # class Deliverytype(models.Model):
# #     deliverytypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'deliverytype'


# # class Demographics(models.Model):
# #     demographicid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'demographics'


# # class Demographicvalues(models.Model):
# #     demographicid = models.IntegerField(blank=True, null=True)
# #     value = models.CharField(max_length=50, blank=True, null=True)
# #     valueid = models.BigIntegerField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'demographicvalues'


# # class Department(models.Model):
# #     departmentid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=150)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     companyid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'department'


# # class Distance(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     unit = models.CharField(max_length=255, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     fightrouteid = models.ForeignKey('Flightroute', models.DO_NOTHING, db_column='fightrouteid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'distance'


# # class Distancecost(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     maxdistance = models.IntegerField(blank=True, null=True)
# #     mindistance = models.IntegerField(blank=True, null=True)
# #     unit = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'distancecost'


# # class Document(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     contenttype = models.CharField(max_length=255, blank=True, null=True)
# #     documenturi = models.CharField(max_length=255, blank=True, null=True)
# #     filename = models.CharField(max_length=255, blank=True, null=True)
# #     filesize = models.BigIntegerField()
# #     published = models.DateTimeField(blank=True, null=True)
# #     rank = models.IntegerField(blank=True, null=True)
# #     subjecturi = models.CharField(max_length=255, blank=True, null=True)
# #     documentdata = models.ForeignKey('Documentdataentity', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'document'


# # class Documentdataentity(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     data = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'documentdataentity'


# # class Driverslicence(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     expirydate = models.CharField(max_length=255, blank=True, null=True)
# #     licencenumber = models.CharField(max_length=255, blank=True, null=True)
# #     licencecountrycode = models.ForeignKey(Country, models.DO_NOTHING, db_column='licencecountrycode', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'driverslicence'


# # class Emailfailedbookings(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     emailaddress = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     receipientname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'emailfailedbookings'


# # class Emailmessagetorequester(models.Model):
# #     companyuri = models.CharField(primary_key=True, max_length=255)
# #     messagetorequester = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'emailmessagetorequester'


# # class Emailrequisitiontrips(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     emailaddress = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     receipientname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'emailrequisitiontrips'


# # class Emailtemplate(models.Model):
# #     templateid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=20)
# #     description = models.CharField(max_length=80, blank=True, null=True)
# #     template = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'emailtemplate'


# # class Emergencycontact(models.Model):
# #     emergencycontactid = models.BigIntegerField(primary_key=True)
# #     contactname = models.CharField(max_length=255, blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     relation = models.CharField(max_length=255, blank=True, null=True)
# #     telephone = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'emergencycontact'


# # class Employee(models.Model):
# #     employee_id = models.BigIntegerField(primary_key=True)
# #     member = models.ForeignKey('Members', models.DO_NOTHING)
# #     company = models.ForeignKey('Merchants', models.DO_NOTHING)
# #     staff_code = models.CharField(max_length=200, blank=True, null=True)
# #     department = models.CharField(max_length=50, blank=True, null=True)
# #     lob = models.CharField(max_length=50, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     departmentid = models.BigIntegerField(blank=True, null=True)
# #     lobid = models.ForeignKey('Lob', models.DO_NOTHING, db_column='lobid', blank=True, null=True)
# #     employmenttype = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'employee'


# # class Employeeband(models.Model):
# #     bandid = models.BigIntegerField(primary_key=True)
# #     bandcode = models.CharField(max_length=255, blank=True, null=True)
# #     companyid = models.BigIntegerField(blank=True, null=True)
# #     jobfunction = models.CharField(max_length=255, blank=True, null=True)
# #     jobposition = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'employeeband'


# # class Employeebandindex(models.Model):
# #     employee_id = models.BigIntegerField(primary_key=True)
# #     bandid = models.BigIntegerField(blank=True, null=True)
# #     employeeband_bandid = models.ForeignKey(Employeeband, models.DO_NOTHING, db_column='employeeband_bandid', unique=True, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'employeebandindex'


# # class Employeebandlookup(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     company_id = models.BigIntegerField(blank=True, null=True)
# #     type = models.IntegerField(blank=True, null=True)
# #     value = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'employeebandlookup'


# # class Ereserrortypes(models.Model):
# #     errorid = models.BigIntegerField(primary_key=True)
# #     ereserrorcode = models.CharField(max_length=50)
# #     reason = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'ereserrortypes'


# # class Ereshotel(models.Model):
# #     hotel_code = models.CharField(primary_key=True, max_length=20)
# #     name = models.CharField(max_length=100, blank=True, null=True)
# #     description = models.CharField(max_length=80, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ereshotel'


# # class Erespaymentdetails(models.Model):
# #     payment_details_id = models.BigIntegerField(primary_key=True)
# #     card_type = models.CharField(max_length=10)
# #     card_number = models.CharField(max_length=30)
# #     cvv_number = models.CharField(max_length=3)
# #     expiry_date = models.CharField(max_length=4)

# #     class Meta:
# #         managed = False
# #         db_table = 'erespaymentdetails'


# # class Eresratecodes(models.Model):
# #     rateplancode = models.CharField(primary_key=True, max_length=20)
# #     name = models.CharField(max_length=20, blank=True, null=True)
# #     description = models.CharField(max_length=80, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'eresratecodes'


# # class Eresroomcodes(models.Model):
# #     room_type_code = models.CharField(primary_key=True, max_length=20)
# #     name = models.CharField(max_length=20, blank=True, null=True)
# #     description = models.CharField(max_length=80, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'eresroomcodes'


# # class Eresroomtypecodes(models.Model):
# #     room_type_code = models.CharField(primary_key=True, max_length=10)
# #     name = models.CharField(max_length=30)
# #     hotel_code = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'eresroomtypecodes'
# #         unique_together = (('room_type_code', 'hotel_code'),)


# # class Error(models.Model):
# #     errorid = models.BigIntegerField(primary_key=True)
# #     errortypeid = models.BigIntegerField()
# #     exception = models.CharField(max_length=100, blank=True, null=True)
# #     exceptionmess = models.CharField(max_length=100, blank=True, null=True)
# #     message = models.CharField(max_length=100, blank=True, null=True)
# #     severityid = models.IntegerField()
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     actiontaken = models.CharField(max_length=300, blank=True, null=True)
# #     actiontimestamp = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'error'


# # class Errorseverity(models.Model):
# #     severityid = models.IntegerField(primary_key=True)
# #     severity = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'errorseverity'


# # class Errorslocal(models.Model):
# #     error_id = models.BigIntegerField(primary_key=True)
# #     type = models.IntegerField()
# #     timestamp = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'errorslocal'


# # class Errortable(models.Model):
# #     guid = models.BigIntegerField(primary_key=True)
# #     request = models.CharField(max_length=8000, blank=True, null=True)
# #     datetime = models.DateTimeField(blank=True, null=True)
# #     exceptionstring = models.CharField(max_length=8000, blank=True, null=True)
# #     extradetail_1 = models.CharField(max_length=8000, blank=True, null=True)
# #     extradetail_2 = models.CharField(max_length=8000, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'errortable'


# # class Errortype(models.Model):
# #     errorid = models.IntegerField(primary_key=True)
# #     errordescr = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'errortype'


# # class Europcarrentalmap(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='rentalid', blank=True, null=True)
# #     europcarstatementid = models.ForeignKey('Europcarstatement', models.DO_NOTHING, db_column='europcarstatementid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'europcarrentalmap'


# # class Europcarstatement(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     key = models.CharField(max_length=255, blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     transactiontype = models.CharField(max_length=255, blank=True, null=True)
# #     exceptiontype = models.CharField(max_length=255, blank=True, null=True)
# #     checkindate = models.DateTimeField(blank=True, null=True)
# #     checkoutdate = models.DateTimeField(blank=True, null=True)
# #     totalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     taxamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     rentalagreementno = models.CharField(max_length=255, blank=True, null=True)
# #     recordtype = models.CharField(max_length=255, blank=True, null=True)
# #     businessunitno = models.CharField(max_length=255, blank=True, null=True)
# #     checkoutbranch = models.CharField(max_length=255, blank=True, null=True)
# #     renter = models.CharField(max_length=255, blank=True, null=True)
# #     chargedvehiclegrp = models.CharField(max_length=255, blank=True, null=True)
# #     dayscharged = models.IntegerField(blank=True, null=True)
# #     kilometresdriven = models.IntegerField(blank=True, null=True)
# #     rentalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     fuelcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     cdwcharged = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     twcharged = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     paicharged = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     sundries = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'europcarstatement'


# # class Europcarvouchers(models.Model):
# #     carvoucherid = models.BigIntegerField(primary_key=True)
# #     carsupplier = models.CharField(max_length=255, blank=True, null=True)
# #     checkindate = models.DateField(blank=True, null=True)
# #     checkoutdate = models.DateField(blank=True, null=True)
# #     checkedinbyuser = models.CharField(max_length=255, blank=True, null=True)
# #     checkedoutbyuser = models.CharField(max_length=255, blank=True, null=True)
# #     status = models.BooleanField(blank=True, null=True)
# #     useddate = models.CharField(max_length=255, blank=True, null=True)
# #     vouchernumber = models.CharField(max_length=255, blank=True, null=True)
# #     vouchertype = models.ForeignKey(Carvouchertype, models.DO_NOTHING, db_column='vouchertype', blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'europcarvouchers'


# # class Europcarvouchersbackup(models.Model):
# #     carvoucherid = models.BigIntegerField(blank=True, null=True)
# #     carsupplier = models.CharField(max_length=255, blank=True, null=True)
# #     checkindate = models.DateField(blank=True, null=True)
# #     checkoutdate = models.DateField(blank=True, null=True)
# #     checkedinbyuser = models.CharField(max_length=255, blank=True, null=True)
# #     checkedoutbyuser = models.CharField(max_length=255, blank=True, null=True)
# #     status = models.BooleanField(blank=True, null=True)
# #     useddate = models.CharField(max_length=255, blank=True, null=True)
# #     vouchernumber = models.CharField(max_length=255, blank=True, null=True)
# #     vouchertype = models.CharField(max_length=255, blank=True, null=True)
# #     merchant_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'europcarvouchersbackup'


# # class Evaluatedbyspecificpersonassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     evaluator = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'evaluatedbyspecificpersonassertion'


# # class Event(models.Model):
# #     eventid = models.BigIntegerField(primary_key=True)
# #     adminid = models.BigIntegerField()
# #     timestamp = models.DateTimeField()
# #     eventtypeid = models.IntegerField()
# #     memberid = models.BigIntegerField()
# #     programid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'event'


# # class Eventnotificationsubscription(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     eventuri = models.CharField(max_length=255, blank=True, null=True)
# #     occurredat = models.DateTimeField(blank=True, null=True)
# #     client_merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'eventnotificationsubscription'


# # class Eventtype(models.Model):
# #     eventtypeid = models.IntegerField(primary_key=True)
# #     eventtypename = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'eventtype'


# # class Eventtypespercompany(models.Model):
# #     eventtypeid = models.BigIntegerField(primary_key=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING)
# #     event_type = models.CharField(max_length=255, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     created_by = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'eventtypespercompany'


# # class Externalmemberprofile(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     userid = models.CharField(max_length=255)
# #     externalsystemid = models.ForeignKey('Externalsystem', models.DO_NOTHING, db_column='externalsystemid')
# #     memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid')

# #     class Meta:
# #         managed = False
# #         db_table = 'externalmemberprofile'
# #         unique_together = (('externalsystemid', 'memberid'), ('externalsystemid', 'userid'),)


# # class Externalsystem(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=255)

# #     class Meta:
# #         managed = False
# #         db_table = 'externalsystem'


# # class Externalvehicleinvoicedetail(models.Model):
# #     invoicedetailid = models.BigIntegerField(primary_key=True)
# #     invoiceheaderid = models.BigIntegerField()
# #     supplier = models.CharField(max_length=30, blank=True, null=True)
# #     company = models.CharField(max_length=30, blank=True, null=True)
# #     referencenr = models.CharField(max_length=20, blank=True, null=True)
# #     ordernr = models.CharField(max_length=20, blank=True, null=True)
# #     costcontrol = models.CharField(max_length=10, blank=True, null=True)
# #     reservationnumber = models.CharField(max_length=30, blank=True, null=True)
# #     travelagencyname = models.CharField(max_length=30, blank=True, null=True)
# #     travelagentname = models.CharField(max_length=30, blank=True, null=True)
# #     rentalperioddays = models.BigIntegerField()
# #     bookedcargroup = models.CharField(max_length=5, blank=True, null=True)
# #     chargedcargroup = models.CharField(max_length=5, blank=True, null=True)
# #     distancedriven = models.BigIntegerField()
# #     ratecode = models.CharField(max_length=5, blank=True, null=True)
# #     startlocation = models.CharField(max_length=20, blank=True, null=True)
# #     startdatetime = models.DateTimeField(blank=True, null=True)
# #     endlocation = models.CharField(max_length=20, blank=True, null=True)
# #     enddatetime = models.DateTimeField(blank=True, null=True)
# #     timeandmileageamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     taxamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     fuelamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     discountamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     totalrentalamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     sundriestotal = models.DecimalField(max_digits=20, decimal_places=2)
# #     insurancetotal = models.DecimalField(max_digits=20, decimal_places=2)
# #     currencycode = models.CharField(max_length=5, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'externalvehicleinvoicedetail'


# # class Externalvehicleinvoiceheader(models.Model):
# #     invoiceheaderid = models.BigIntegerField(primary_key=True)
# #     invoicetype = models.CharField(max_length=10)
# #     filepacketid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'externalvehicleinvoiceheader'


# # class Externalvehicleinvoiceline(models.Model):
# #     lineid = models.BigIntegerField(primary_key=True)
# #     invoicedetailid = models.BigIntegerField()
# #     linecodeid = models.BigIntegerField()
# #     lineamount = models.DecimalField(max_digits=20, decimal_places=2)

# #     class Meta:
# #         managed = False
# #         db_table = 'externalvehicleinvoiceline'


# # class Externalvehicleinvoicelinecodes(models.Model):
# #     linecodeid = models.BigIntegerField(primary_key=True)
# #     linetype = models.CharField(max_length=1)
# #     description = models.CharField(max_length=25)

# #     class Meta:
# #         managed = False
# #         db_table = 'externalvehicleinvoicelinecodes'


# # class Externalvehicleinvoicemap(models.Model):
# #     rentalid = models.BigIntegerField(primary_key=True)
# #     invoicedetailid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'externalvehicleinvoicemap'
# #         unique_together = (('rentalid', 'invoicedetailid'),)


# # class Feature(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=-1, blank=True, null=True)
# #     description = models.CharField(max_length=-1, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'feature'


# # class Featureclient(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)
# #     featureclient = models.ForeignKey(Feature, models.DO_NOTHING)
# #     create_date = models.DateField(blank=True, null=True)
# #     start_date = models.DateField(blank=True, null=True)
# #     end_date = models.DateField(blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'featureclient'


# # class Filepollproperties(models.Model):
# #     propertyid = models.IntegerField(primary_key=True)
# #     propertyname = models.CharField(max_length=25)
# #     propertyvalue = models.CharField(max_length=25)

# #     class Meta:
# #         managed = False
# #         db_table = 'filepollproperties'


# # class Filter(models.Model):
# #     guid = models.BigIntegerField(primary_key=True)
# #     filter = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     select_index = models.IntegerField(blank=True, null=True)
# #     parent_guid = models.BigIntegerField(blank=True, null=True)
# #     escelationparent_guid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'filter'


# # class Flagtable(models.Model):
# #     flagid = models.IntegerField(primary_key=True)
# #     flagdescr = models.CharField(max_length=80)

# #     class Meta:
# #         managed = False
# #         db_table = 'flagtable'


# # class Flightcancel(models.Model):
# #     flightcancelid = models.BigIntegerField(primary_key=True)
# #     flightgrpid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     cancelfee = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightcancel'


# # class Flightchange(models.Model):
# #     flightchangeid = models.BigIntegerField(primary_key=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     airlineid = models.BigIntegerField(blank=True, null=True)
# #     changecost = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     reservationid = models.BigIntegerField(blank=True, null=True)
# #     flightgrpid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightchange'


# # class Flightfare(models.Model):
# #     flightgrpid = models.BigIntegerField(primary_key=True)
# #     travresid = models.ForeignKey('Travelreservation', models.DO_NOTHING, db_column='travresid', blank=True, null=True)
# #     ticketingairline = models.ForeignKey(Airlines, models.DO_NOTHING, db_column='ticketingairline', blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=30, blank=True, null=True)
# #     basefare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     airporttax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     vat = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     totalfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     publishedfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     status = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='status', blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     costreason = models.CharField(max_length=200, blank=True, null=True)
# #     passfname = models.CharField(max_length=100, blank=True, null=True)
# #     passsname = models.CharField(max_length=100, blank=True, null=True)
# #     ticketed = models.IntegerField(blank=True, null=True)
# #     triptravid = models.ForeignKey('Triptravellermap', models.DO_NOTHING, db_column='triptravid', blank=True, null=True)
# #     tickettimelimit = models.DateTimeField(blank=True, null=True)
# #     ticketeddate = models.DateTimeField(blank=True, null=True)
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid', blank=True, null=True)
# #     pricingsource = models.CharField(max_length=255, blank=True, null=True)
# #     vendorlocator = models.CharField(max_length=255, blank=True, null=True)
# #     farebasiscodes = models.CharField(max_length=255, blank=True, null=True)
# #     tickettype = models.CharField(max_length=255, blank=True, null=True)
# #     currency = models.ForeignKey(Currency, models.DO_NOTHING, db_column='currency', blank=True, null=True)
# #     bookingagent = models.ForeignKey('Travelagent', models.DO_NOTHING, db_column='bookingagent', blank=True, null=True)
# #     ticketingagent = models.ForeignKey('Travelagent', models.DO_NOTHING, db_column='ticketingagent', blank=True, null=True)
# #     cheapestfare = models.ForeignKey('self', models.DO_NOTHING, db_column='cheapestfare', blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     quoteid = models.ForeignKey('Quote', models.DO_NOTHING, db_column='quoteid', blank=True, null=True)
# #     invoiceuri = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Carbonemissionderivedvalues, models.DO_NOTHING, db_column='id', blank=True, null=True)
# #     tripglcodeid = models.ForeignKey('Tripglcode', models.DO_NOTHING, db_column='tripglcodeid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightfare'


# # class FlightfareQuote(models.Model):
# #     flightfare_flightgrpid = models.ForeignKey(Flightfare, models.DO_NOTHING, db_column='flightfare_flightgrpid')
# #     quotes_quoteid = models.ForeignKey('Quote', models.DO_NOTHING, db_column='quotes_quoteid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightfare_quote'


# # class Flightgrpinvmap(models.Model):
# #     flightgrpinvmapid = models.BigIntegerField(primary_key=True)
# #     flightgrpid = models.BigIntegerField(blank=True, null=True)
# #     invoiceid = models.BigIntegerField(blank=True, null=True)
# #     type = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightgrpinvmap'


# # class Flightitemdetail(models.Model):
# #     id = models.ForeignKey('Statementitemdetail', models.DO_NOTHING, db_column='id', primary_key=True)
# #     reservationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=255, blank=True, null=True)
# #     passengername = models.CharField(max_length=255, blank=True, null=True)
# #     ticketcode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightitemdetail'


# # class FlightitemdetailFlightfare(models.Model):
# #     flightitemdetail = models.ForeignKey(Flightitemdetail, models.DO_NOTHING)
# #     flightfare_flightgrpid = models.ForeignKey(Flightfare, models.DO_NOTHING, db_column='flightfare_flightgrpid')

# #     class Meta:
# #         managed = False
# #         db_table = 'flightitemdetail_flightfare'


# # class Flightrequest(models.Model):
# #     tripid = models.BigIntegerField()
# #     departurepoint = models.CharField(max_length=50, blank=True, null=True)
# #     arrivalpoint = models.CharField(max_length=50, blank=True, null=True)
# #     flightdate = models.DateTimeField(blank=True, null=True)
# #     maximumclass = models.CharField(max_length=50, blank=True, null=True)
# #     requestid = models.BigIntegerField(primary_key=True)
# #     departuretime = models.CharField(max_length=50, blank=True, null=True)
# #     arrivaltime = models.CharField(max_length=50, blank=True, null=True)
# #     flightnumber = models.CharField(max_length=50, blank=True, null=True)
# #     loyaltynumber = models.CharField(max_length=50, blank=True, null=True)
# #     billinginfo = models.CharField(max_length=50, blank=True, null=True)
# #     ticketprice = models.CharField(max_length=15, blank=True, null=True)
# #     airline_id = models.IntegerField(blank=True, null=True)
# #     flightdepartdatetime = models.DateTimeField(blank=True, null=True)
# #     flightreturndatetime = models.DateTimeField(blank=True, null=True)
# #     departuredatetime = models.DateTimeField(blank=True, null=True)
# #     arrivaldatetime = models.DateTimeField(blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     flightdeparturedatetime = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightrequest'


# # class Flightroute(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     startlocation = models.ForeignKey(Airport, models.DO_NOTHING, db_column='startlocation', blank=True, null=True)
# #     endlocation = models.ForeignKey(Airport, models.DO_NOTHING, db_column='endlocation', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightroute'


# # class Flightsector(models.Model):
# #     flight_id = models.BigIntegerField(primary_key=True)
# #     flight_number = models.CharField(max_length=30, blank=True, null=True)
# #     flight_date = models.DateTimeField(blank=True, null=True)
# #     dep_point = models.CharField(max_length=30, blank=True, null=True)
# #     arr_point = models.CharField(max_length=30, blank=True, null=True)
# #     class_field = models.ForeignKey(Airlineclasses, models.DO_NOTHING, db_column='class_id', blank=True, null=True)  # Field renamed because it was a Python reserved word.
# #     created = models.DateTimeField(blank=True, null=True)
# #     flightgrpid = models.ForeignKey(Flightfare, models.DO_NOTHING, db_column='flightgrpid', blank=True, null=True)
# #     duration = models.BigIntegerField(blank=True, null=True)
# #     flightarrivaldate = models.DateTimeField(blank=True, null=True)
# #     stops = models.IntegerField(blank=True, null=True)
# #     equipment = models.CharField(max_length=255, blank=True, null=True)
# #     operatingairlineid = models.ForeignKey(Airlines, models.DO_NOTHING, db_column='operatingairlineid', blank=True, null=True)
# #     marketingairlineid = models.ForeignKey(Airlines, models.DO_NOTHING, db_column='marketingairlineid', blank=True, null=True)
# #     std = models.CharField(max_length=255, blank=True, null=True)
# #     sta = models.CharField(max_length=255, blank=True, null=True)
# #     co2emission = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     mealid = models.ForeignKey('Suppliermeals', models.DO_NOTHING, db_column='mealid', blank=True, null=True)
# #     industryseatclass = models.CharField(max_length=255, blank=True, null=True)
# #     carbonemissionid = models.ForeignKey(Carbonemission, models.DO_NOTHING, db_column='carbonemissionid', blank=True, null=True)
# #     outsourcedairlineid = models.ForeignKey(Airlines, models.DO_NOTHING, db_column='outsourcedairlineid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightsector'


# # class Flightsectordistanceclassifier(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     unit = models.CharField(max_length=255, blank=True, null=True)
# #     defracarbondistancefactor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     radiativeforcingindexfactor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     classification = models.CharField(max_length=255, blank=True, null=True)
# #     startdistancerange = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     enddistancerange = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightsectordistanceclassifier'


# # class Flightstatusmap(models.Model):
# #     flightstatusid = models.BigIntegerField(primary_key=True)
# #     resstatusid = models.IntegerField()
# #     name = models.CharField(max_length=50)
# #     description = models.CharField(max_length=100, blank=True, null=True)
# #     pnrflag = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flightstatusmap'


# # class Flighttransactiontype(models.Model):
# #     flighttransactiontypeid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=20, blank=True, null=True)
# #     description = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flighttransactiontype'


# # class Flighttypeassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     flighttype = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'flighttypeassertion'


# # class Frequenttravellerprogs(models.Model):
# #     ftncode = models.CharField(max_length=3)
# #     partnername = models.CharField(max_length=100, blank=True, null=True)
# #     programname = models.CharField(max_length=100, blank=True, null=True)
# #     supplierid = models.ForeignKey('Members', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)
# #     programid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'frequenttravellerprogs'


# # class Galileocredentials(models.Model):
# #     agencyid = models.BigIntegerField(primary_key=True)
# #     pseudocitycode = models.CharField(max_length=30, blank=True, null=True)
# #     isocurrency = models.CharField(max_length=10, blank=True, null=True)
# #     requestorid = models.CharField(max_length=20, blank=True, null=True)
# #     requestortype = models.CharField(max_length=10, blank=True, null=True)
# #     providername = models.CharField(max_length=30, blank=True, null=True)
# #     providersystem = models.CharField(max_length=20, blank=True, null=True)
# #     provideruserid = models.CharField(max_length=30, blank=True, null=True)
# #     providerpassword = models.CharField(max_length=30, blank=True, null=True)
# #     psuedocitycode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'galileocredentials'


# # class Geoname(models.Model):
# #     geonameid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     asciiname = models.CharField(max_length=255, blank=True, null=True)
# #     alternatenames = models.CharField(max_length=10000, blank=True, null=True)
# #     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
# #     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
# #     featureclass = models.CharField(max_length=2, blank=True, null=True)
# #     featurecode = models.CharField(max_length=10, blank=True, null=True)
# #     countrycode = models.ForeignKey(Country, models.DO_NOTHING, db_column='countrycode', blank=True, null=True)
# #     cc2 = models.CharField(max_length=255, blank=True, null=True)
# #     admin1code = models.CharField(max_length=255, blank=True, null=True)
# #     admin2code = models.CharField(max_length=255, blank=True, null=True)
# #     admin3code = models.CharField(max_length=255, blank=True, null=True)
# #     admin4code = models.CharField(max_length=255, blank=True, null=True)
# #     population = models.BigIntegerField(blank=True, null=True)
# #     elevation = models.BigIntegerField(blank=True, null=True)
# #     dem = models.BigIntegerField(blank=True, null=True)
# #     timezone = models.CharField(max_length=255, blank=True, null=True)
# #     modificationdate = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'geoname'


# # class Geopointsofinterest(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     city = models.CharField(max_length=255, blank=True, null=True)
# #     companyid = models.BigIntegerField(blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     latitude = models.CharField(max_length=255, blank=True, null=True)
# #     longitude = models.CharField(max_length=255, blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     province = models.CharField(max_length=255, blank=True, null=True)
# #     country_country_code = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_country_code', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'geopointsofinterest'


# # class Glcodetype(models.Model):
# #     glcodetypeid = models.IntegerField(primary_key=True)
# #     amount = models.FloatField(blank=True, null=True)
# #     deleted = models.BooleanField(blank=True, null=True)
# #     merchant_id = models.BigIntegerField(blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'glcodetype'


# # class Googlemaplocator(models.Model):
# #     id = models.ForeignKey('Locator', models.DO_NOTHING, db_column='id', primary_key=True)
# #     url = models.TextField(blank=True, null=True)
# #     iframe = models.TextField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'googlemaplocator'


# # class Governedentity(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     governed_entity = models.ForeignKey('Policy', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'governedentity'


# # class Gpslocator(models.Model):
# #     id = models.ForeignKey('Locator', models.DO_NOTHING, db_column='id', primary_key=True)
# #     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
# #     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'gpslocator'


# # class GroupType(models.Model):
# #     grp_type_id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=30, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'group_type'


# # class Groupmap(models.Model):
# #     group_id = models.BigIntegerField(primary_key=True)
# #     memberid = models.BigIntegerField()
# #     grp_type_id = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'groupmap'


# # class Groupstate(models.Model):
# #     guid = models.BigIntegerField(primary_key=True)
# #     processstatus = models.IntegerField(blank=True, null=True)
# #     state_index = models.IntegerField(blank=True, null=True)
# #     group_guid = models.BigIntegerField(blank=True, null=True)
# #     parent_guid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'groupstate'


# # class Histtype(models.Model):
# #     histtypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=20, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'histtype'


# # class Hotel(models.Model):
# #     hotelid = models.AutoField(primary_key=True)
# #     hotelname = models.CharField(max_length=255, blank=True, null=True)
# #     hoteldescription = models.TextField(blank=True, null=True)
# #     rating = models.CharField(max_length=255, blank=True, null=True)
# #     contactdetailid = models.ForeignKey(Contactdetail, models.DO_NOTHING, db_column='contactdetailid', blank=True, null=True)
# #     regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid', blank=True, null=True)
# #     hotelchainid = models.ForeignKey('Hotelchain', models.DO_NOTHING, db_column='hotelchainid', blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     altsearchname = models.CharField(max_length=255, blank=True, null=True)
# #     hotelproconcode = models.CharField(max_length=15, blank=True, null=True)
# #     hotellocationcode = models.CharField(max_length=15, blank=True, null=True)
# #     preferredexception = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotel'


# # class Hotelcardmerchant(models.Model):
# #     issuer = models.CharField(max_length=255, blank=True, null=True)
# #     issuermerchantname = models.CharField(max_length=255, blank=True, null=True)
# #     hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotelid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelcardmerchant'


# # class Hotelchain(models.Model):
# #     hotelchainid = models.AutoField(primary_key=True)
# #     hotelchainname = models.CharField(max_length=255, blank=True, null=True)
# #     hotelchaindescription = models.CharField(max_length=255, blank=True, null=True)
# #     timecreated = models.DateTimeField(blank=True, null=True)
# #     hotelchaincode = models.CharField(max_length=255, blank=True, null=True)
# #     hotelchainuri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelchain'


# # class HotelchainBookingengineTable(models.Model):
# #     engineid = models.ForeignKey(Hotelchain, models.DO_NOTHING, db_column='engineid', primary_key=True)
# #     hotelchainid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='hotelchainid')

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelchain_bookingengine_table'
# #         unique_together = (('engineid', 'hotelchainid'),)


# # class Hoteldetails(models.Model):
# #     hoteldetailsid = models.BigIntegerField(primary_key=True)
# #     hotelcode = models.CharField(max_length=30)
# #     hotelname = models.CharField(max_length=60)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid')
# #     hotelmerchantid = models.BigIntegerField(blank=True, null=True)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     website = models.CharField(max_length=255, blank=True, null=True)
# #     starrating = models.CharField(max_length=255, blank=True, null=True)
# #     regionid = models.ForeignKey('Region', models.DO_NOTHING, db_column='regionid', blank=True, null=True)
# #     contactdetailid = models.ForeignKey(Contactdetail, models.DO_NOTHING, db_column='contactdetailid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hoteldetails'
# #         unique_together = (('hotelcode', 'merchantid'),)


# # class Hotelimages(models.Model):
# #     hotelimagesid = models.BigIntegerField(primary_key=True)
# #     hotelcode = models.CharField(max_length=255, blank=True, null=True)
# #     imagepath = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelimages'


# # class Hotelitemdetail(models.Model):
# #     id = models.ForeignKey('Statementitemdetail', models.DO_NOTHING, db_column='id', primary_key=True)
# #     reservationnumber = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelitemdetail'


# # class HotelitemdetailAccommodation(models.Model):
# #     hotelitemdetail = models.ForeignKey(Hotelitemdetail, models.DO_NOTHING)
# #     accommodations_bookingid = models.ForeignKey(Accommodation, models.DO_NOTHING, db_column='accommodations_bookingid')

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelitemdetail_accommodation'


# # class Hotelmerchantsupplier(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     merchantid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='merchantid', blank=True, null=True)
# #     hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotelid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'hotelmerchantsupplier'


# # class IdType(models.Model):
# #     id_type_id = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=25)

# #     class Meta:
# #         managed = False
# #         db_table = 'id_type'


# # class Imagedata(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     data = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'imagedata'


# # class Images(models.Model):
# #     imageid = models.BigIntegerField()
# #     memberid = models.BigIntegerField(primary_key=True)
# #     image = models.TextField(blank=True, null=True)
# #     thumbnail = models.TextField(blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)
# #     imagetypeid = models.IntegerField(blank=True, null=True)
# #     filename = models.CharField(max_length=100, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'images'


# # class Imagetype(models.Model):
# #     imagetypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'imagetype'


# # class Imperialcarrentalmap(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     imperialstatementid = models.ForeignKey('Imperialstatement', models.DO_NOTHING, db_column='imperialstatementid', blank=True, null=True)
# #     rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='rentalid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'imperialcarrentalmap'


# # class Imperialstatement(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     startdate = models.CharField(max_length=255, blank=True, null=True)
# #     starttime = models.CharField(max_length=255, blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     days = models.CharField(max_length=255, blank=True, null=True)
# #     endtime = models.CharField(max_length=255, blank=True, null=True)
# #     totalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     contractfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     enddate = models.CharField(max_length=255, blank=True, null=True)
# #     transtype = models.CharField(max_length=255, blank=True, null=True)
# #     airline = models.CharField(max_length=255, blank=True, null=True)
# #     travellername = models.CharField(max_length=255, blank=True, null=True)
# #     iatanumber = models.CharField(max_length=255, blank=True, null=True)
# #     airportsurcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     costcentre = models.CharField(max_length=255, blank=True, null=True)
# #     rentalagreementno = models.CharField(max_length=255, blank=True, null=True)
# #     extref = models.CharField(max_length=255, blank=True, null=True)
# #     tourismlevy = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     clientno = models.CharField(max_length=255, blank=True, null=True)
# #     clientname1 = models.CharField(max_length=255, blank=True, null=True)
# #     clientname2 = models.CharField(max_length=255, blank=True, null=True)
# #     lodgecardno = models.CharField(max_length=255, blank=True, null=True)
# #     outbranch = models.CharField(max_length=255, blank=True, null=True)
# #     frequentflyer = models.CharField(max_length=255, blank=True, null=True)
# #     chargedvehiclegrp = models.CharField(max_length=255, blank=True, null=True)
# #     actualvehiclegrp = models.CharField(max_length=255, blank=True, null=True)
# #     model = models.CharField(max_length=255, blank=True, null=True)
# #     kilometres = models.CharField(max_length=255, blank=True, null=True)
# #     rentalcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     distancecost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     discount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     damagerwaivercost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     theftwaivercost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     paicost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     tax = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     fuelcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     sundrycost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     transnumber = models.CharField(max_length=255, blank=True, null=True)
# #     paynumber = models.CharField(max_length=255, blank=True, null=True)
# #     paytype = models.CharField(max_length=255, blank=True, null=True)
# #     invoicedate = models.CharField(max_length=255, blank=True, null=True)
# #     netttrans = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     deliverycharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     additionaldrivercharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     onewaydropoffcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     theftordamagescharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     othercharges = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     profilegroupcode = models.CharField(max_length=255, blank=True, null=True)
# #     promotioncode = models.CharField(max_length=255, blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)
# #     rentercustomername = models.CharField(max_length=255, blank=True, null=True)
# #     ressourcename = models.CharField(max_length=255, blank=True, null=True)
# #     inbranch = models.CharField(max_length=255, blank=True, null=True)
# #     outregistrationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     inregistrationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     crossborderwaiver = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     stampdutywaiver = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     navigationunitcharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     bagaggeinsurance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     windscreentyrewaiver = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     adminfee = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     pricelistnumber = models.CharField(max_length=255, blank=True, null=True)
# #     tariffperiodcode = models.CharField(max_length=255, blank=True, null=True)
# #     co2emissionrate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     totalraco2 = models.FloatField(blank=True, null=True)
# #     rentercustomernumber = models.CharField(max_length=255, blank=True, null=True)
# #     crossbordercharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     stampdutycharge = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'imperialstatement'


# # class Interests(models.Model):
# #     interestid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'interests'


# # class Invoice(models.Model):
# #     invoiceid = models.BigIntegerField(primary_key=True)
# #     puraccountid = models.BigIntegerField(blank=True, null=True)
# #     meraccountid = models.BigIntegerField(blank=True, null=True)
# #     invoiceamount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     paymentmethodid = models.IntegerField(blank=True, null=True)
# #     invoicetypeid = models.IntegerField(blank=True, null=True)
# #     periodid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)
# #     ret_ref_no = models.CharField(max_length=50, blank=True, null=True)
# #     switchid = models.BigIntegerField(blank=True, null=True)
# #     statementid = models.BigIntegerField(blank=True, null=True)
# #     ccdetailsid = models.BigIntegerField(blank=True, null=True)
# #     matched = models.IntegerField(blank=True, null=True)
# #     paymentreferencenumber = models.CharField(max_length=255, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     paymentdate = models.DateField(blank=True, null=True)
# #     supplierinvoicenumber = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoice'


# # class InvoiceEntriesCar(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     entry_name = models.CharField(max_length=255, blank=True, null=True)
# #     entry_value = models.CharField(max_length=255, blank=True, null=True)
# #     voucher_type = models.CharField(max_length=255, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoice_entries_car'


# # class InvoiceEntriesHotel(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     entry_name = models.CharField(max_length=255, blank=True, null=True)
# #     entry_value = models.CharField(max_length=255, blank=True, null=True)
# #     voucher_type = models.CharField(max_length=255, blank=True, null=True)
# #     merchant = models.ForeignKey('Merchants', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoice_entries_hotel'


# # class InvoiceLineitems(models.Model):
# #     invoice_invoiceid = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='invoice_invoiceid')
# #     lineitems_lineitemid = models.ForeignKey('Lineitems', models.DO_NOTHING, db_column='lineitems_lineitemid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoice_lineitems'


# # class Invoicefile(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     file_name = models.CharField(max_length=255, blank=True, null=True)
# #     invoice = models.TextField(blank=True, null=True)  # This field type is a guess.
# #     accommodation = models.ForeignKey(Accommodation, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoicefile'


# # class Invoiceproductmap(models.Model):
# #     invoiceid = models.BigIntegerField(primary_key=True)
# #     productid = models.BigIntegerField()
# #     linevat = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     quantity = models.IntegerField(blank=True, null=True)
# #     unitpriceexclusive = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     linetotal = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     barcode = models.CharField(max_length=100, blank=True, null=True)
# #     lineno = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoiceproductmap'
# #         unique_together = (('invoiceid', 'productid'),)


# # class Invoicestatementmap(models.Model):
# #     invstatmapid = models.BigIntegerField(primary_key=True)
# #     invoiceid = models.BigIntegerField(blank=True, null=True)
# #     statementid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoicestatementmap'


# # class Invoicetype(models.Model):
# #     invoicetypeid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=20, blank=True, null=True)
# #     description = models.CharField(max_length=80, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'invoicetype'


# # class Item(models.Model):
# #     itemid = models.AutoField(primary_key=True)
# #     lobid = models.ForeignKey('Lob', models.DO_NOTHING, db_column='lobid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'item'


# # class Itinerary(models.Model):
# #     itinid = models.BigIntegerField(primary_key=True)
# #     itinordernumber = models.CharField(max_length=50, blank=True, null=True)
# #     created = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'itinerary'


# # class IveriInputLogg(models.Model):
# #     # id = models.AutoField()
# #     amount = models.CharField(max_length=255, blank=True, null=True)
# #     applicationid = models.CharField(max_length=255, blank=True, null=True)
# #     expirydate = models.CharField(max_length=255, blank=True, null=True)
# #     merchantreference = models.CharField(max_length=255, blank=True, null=True)
# #     merchanttrace = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iveri_input_log'


# # class IveriOutputLogg(models.Model):
# #     # id = models.AutoField()
# #     acquirer = models.CharField(max_length=255, blank=True, null=True)
# #     acquirerdate = models.CharField(max_length=255, blank=True, null=True)
# #     acquirerreference = models.CharField(max_length=255, blank=True, null=True)
# #     acquirertime = models.CharField(max_length=255, blank=True, null=True)
# #     authorisationcode = models.CharField(max_length=255, blank=True, null=True)
# #     merchantreference = models.CharField(max_length=255, blank=True, null=True)
# #     merchanttrace = models.CharField(max_length=255, blank=True, null=True)
# #     pan = models.CharField(max_length=255, blank=True, null=True)
# #     reconreference = models.CharField(max_length=255, blank=True, null=True)
# #     requestid = models.CharField(max_length=255, blank=True, null=True)
# #     resultcode = models.CharField(max_length=255, blank=True, null=True)
# #     resultdescription = models.CharField(max_length=255, blank=True, null=True)
# #     resultsource = models.CharField(max_length=255, blank=True, null=True)
# #     resultstatus = models.CharField(max_length=255, blank=True, null=True)
# #     transactionindex = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iveri_output_log'


# # class Iverihotelappids(models.Model):
# #     applicationid = models.CharField(max_length=255, blank=True, null=True)
# #     meansofbookinghotel = models.ForeignKey('Meansofbookinghotel', models.DO_NOTHING, db_column='meansofbookinghotel', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iverihotelappids'


# # class Iveriinputlog(models.Model):
# #     amount = models.CharField(max_length=255, blank=True, null=True)
# #     applicationid = models.CharField(max_length=255, blank=True, null=True)
# #     expirydate = models.CharField(max_length=255, blank=True, null=True)
# #     merchantreference = models.CharField(max_length=255, blank=True, null=True)
# #     merchanttrace = models.CharField(max_length=255, blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     userid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iveriinputlog'


# # class Iverioutputlog(models.Model):
# #     requestid = models.CharField(max_length=255, blank=True, null=True)
# #     resultstatus = models.CharField(max_length=255, blank=True, null=True)
# #     resultdescription = models.CharField(max_length=255, blank=True, null=True)
# #     resultcode = models.CharField(max_length=255, blank=True, null=True)
# #     resultsource = models.CharField(max_length=255, blank=True, null=True)
# #     merchantreference = models.CharField(max_length=255, blank=True, null=True)
# #     merchanttrace = models.CharField(max_length=255, blank=True, null=True)
# #     acquirer = models.CharField(max_length=255, blank=True, null=True)
# #     acquirerdate = models.CharField(max_length=255, blank=True, null=True)
# #     acquirertime = models.CharField(max_length=255, blank=True, null=True)
# #     acquirerreference = models.CharField(max_length=255, blank=True, null=True)
# #     authorisationcode = models.CharField(max_length=255, blank=True, null=True)
# #     pan = models.CharField(max_length=255, blank=True, null=True)
# #     reconreference = models.CharField(max_length=255, blank=True, null=True)
# #     transactionindex = models.CharField(max_length=255, blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     userid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iverioutputlog'


# # class Iveritransactionlog(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     iveriinputlogid = models.ForeignKey(Iveriinputlog, models.DO_NOTHING, db_column='iveriinputlogid', blank=True, null=True)
# #     iverioutputlogid = models.ForeignKey(Iverioutputlog, models.DO_NOTHING, db_column='iverioutputlogid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iveritransactionlog'


# # class IveritransactionlogInvoice(models.Model):
# #     iveritransactionlog = models.ForeignKey(Iveritransactionlog, models.DO_NOTHING)
# #     invoices_invoiceid = models.ForeignKey(Invoice, models.DO_NOTHING, db_column='invoices_invoiceid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'iveritransactionlog_invoice'


# # class Kaizerchiefsmembershippayments(models.Model):
# #     paymentid = models.BigIntegerField(primary_key=True)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     membershipfee = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     postage = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'kaizerchiefsmembershippayments'


# # class Kaizerchiefssupporter(models.Model):
# #     shopperid = models.BigIntegerField(primary_key=True)
# #     paymenttypeid = models.IntegerField()
# #     discoverymemberno = models.CharField(max_length=30, blank=True, null=True)
# #     discoverymembertype = models.CharField(max_length=30, blank=True, null=True)
# #     paidflag = models.IntegerField()
# #     autorenewflag = models.IntegerField()
# #     renewalperiodid = models.IntegerField()
# #     paymentcarddetailsid = models.BigIntegerField(blank=True, null=True)
# #     renewalpaymentcarddetailsid = models.BigIntegerField(blank=True, null=True)
# #     standardbankaccountflag = models.IntegerField(blank=True, null=True)
# #     deliverytypeid = models.IntegerField(blank=True, null=True)
# #     deliverybranchid = models.BigIntegerField(blank=True, null=True)
# #     cardmembershipid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'kaizerchiefssupporter'


# # class Kcpaymentamounts(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=10)

# #     class Meta:
# #         managed = False
# #         db_table = 'kcpaymentamounts'


# # class Kululataxcode(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     taxcode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'kululataxcode'


# # class Kululataxperiod(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     effectivebookingdate = models.DateField(blank=True, null=True)
# #     fromdate = models.DateField(blank=True, null=True)
# #     todate = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'kululataxperiod'


# # class Kululataxrate(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     taxamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     previoustaxamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     periodid = models.ForeignKey(Kululataxperiod, models.DO_NOTHING, db_column='periodid', blank=True, null=True)
# #     taxcodeid = models.ForeignKey(Kululataxcode, models.DO_NOTHING, db_column='taxcodeid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'kululataxrate'


# # class Level(models.Model):
# #     levelid = models.IntegerField(primary_key=True)
# #     levelname = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'level'


# # class Lineitems(models.Model):
# #     lineitemid = models.BigIntegerField(primary_key=True)
# #     invoiceid = models.BigIntegerField(blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     lineitemtypeid = models.ForeignKey('Lineitemtype', models.DO_NOTHING, db_column='lineitemtypeid', blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     lineitempaymentdate = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'lineitems'


# # class Lineitemtype(models.Model):
# #     lineitemtypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'lineitemtype'


# # class Lob(models.Model):
# #     lobid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=150, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     departmentid = models.BigIntegerField(blank=True, null=True)
# #     companyid = models.ForeignKey('Merchants', models.DO_NOTHING, db_column='companyid')
# #     datedisabled = models.CharField(max_length=255, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     approver = models.ForeignKey(Autoapprovalapproverconfig, models.DO_NOTHING, db_column='approver', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'lob'


# # class Location(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'location'


# # class LocationLocator(models.Model):
# #     location = models.ForeignKey(Location, models.DO_NOTHING)
# #     locators = models.ForeignKey('Locator', models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'location_locator'


# # class LocationRegionlocator(models.Model):
# #     location = models.ForeignKey(Location, models.DO_NOTHING)
# #     regions_uri = models.ForeignKey('Regionlocator', models.DO_NOTHING, db_column='regions_uri')
# #     regions_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'location_regionlocator'


# # class Locator(models.Model):
# #     id = models.BigAutoField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'locator'


# # class Loyaltyprogram(models.Model):
# #     loyaltyprogramid = models.AutoField(primary_key=True)
# #     supplierid = models.BigIntegerField(blank=True, null=True)
# #     ftncode = models.CharField(max_length=255, blank=True, null=True)
# #     partnername = models.CharField(max_length=255, blank=True, null=True)
# #     programname = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=250, blank=True, null=True)
# #     partneruri = models.CharField(max_length=255, blank=True, null=True)
# #     partneriatacode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'loyaltyprogram'


# # class Meansofbookinghotel(models.Model):
# #     mobid = models.AutoField(primary_key=True)
# #     hotelcode = models.CharField(max_length=255, blank=True, null=True)
# #     bookingengineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='bookingengineid', blank=True, null=True)
# #     hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotelid', blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'meansofbookinghotel'


# # class MemberGroup(models.Model):
# #     group_id = models.BigIntegerField(primary_key=True)
# #     memberid = models.BigIntegerField()
# #     group_name = models.CharField(max_length=30, blank=True, null=True)
# #     created = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'member_group'


# # class Memberdemographicmap(models.Model):
# #     memberid = models.BigIntegerField(primary_key=True)
# #     valueid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'memberdemographicmap'
# #         unique_together = (('memberid', 'valueid'),)


# # class Memberrfimap(models.Model):
# #     memberid = models.BigIntegerField(primary_key=True)
# #     valueid = models.BigIntegerField()
# #     rfiid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'memberrfimap'
# #         unique_together = (('memberid', 'valueid'),)




# class Membertype(models.Model):
#     membertypeid = models.IntegerField(primary_key=True)
#     description = models.CharField(max_length=20, blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'membertype'


# # class MerCategory(models.Model):
# #     cat_id = models.CharField(primary_key=True, max_length=18)
# #     created = models.CharField(max_length=18)
# #     merchant_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'mer_category'


# # class MerchantType(models.Model):
# #     merchanttypeid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=200)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchant_type'


# # class Merchantflightinvoicedownloadoptions(models.Model):
# #     merchantid = models.BigIntegerField(primary_key=True)
# #     reservationtype = models.CharField(max_length=255, blank=True, null=True)
# #     reportname = models.CharField(max_length=255, blank=True, null=True)
# #     batchreportname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantflightinvoicedownloadoptions'


# # class Merchantmap(models.Model):
# #     accountid = models.BigIntegerField(primary_key=True)
# #     defaultperc = models.DecimalField(max_digits=4, decimal_places=0, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantmap'


# # class Merchantpaymentrequest(models.Model):
# #     merchantpaymentrqid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.BigIntegerField()
# #     batchpaymentrqid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantpaymentrequest'


# # class Merchantpaymentrule(models.Model):
# #     frommerchantid = models.BigIntegerField(primary_key=True)
# #     tomerchantid = models.BigIntegerField()
# #     switchid = models.BigIntegerField()
# #     maxdays = models.IntegerField(blank=True, null=True)
# #     mindays = models.IntegerField(blank=True, null=True)
# #     maxbatchsize = models.IntegerField(blank=True, null=True)
# #     minbatchsize = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantpaymentrule'
# #         unique_together = (('frommerchantid', 'tomerchantid', 'switchid'),)


# # class Merchants(models.Model):
# #     merchant_id = models.BigIntegerField(primary_key=True)
# #     company_name = models.CharField(max_length=255, blank=True, null=True)
# #     trading_as = models.CharField(max_length=255, blank=True, null=True)
# #     store_name = models.CharField(max_length=255, blank=True, null=True)
# #     registration_number = models.CharField(max_length=50, blank=True, null=True)
# #     url = models.CharField(max_length=80, blank=True, null=True)
# #     receive_email = models.IntegerField(blank=True, null=True)
# #     receive_news = models.IntegerField(blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     bank_mer_id = models.CharField(max_length=20, blank=True, null=True)
# #     location_id = models.IntegerField(blank=True, null=True)
# #     member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     mer_type = models.ForeignKey(MerchantType, models.DO_NOTHING, blank=True, null=True)
# #     logourl = models.CharField(max_length=200, blank=True, null=True)
# #     vatnumber = models.CharField(max_length=255, blank=True, null=True)
# #     logourllarge = models.CharField(max_length=255, blank=True, null=True)
# #     autogenerateorder = models.IntegerField(blank=True, null=True)
# #     carsuperwaiver = models.BooleanField(blank=True, null=True)
# #     carwaivertype = models.CharField(max_length=255, blank=True, null=True)
# #     logourlsecondary = models.CharField(max_length=255, blank=True, null=True)
# #     autogenerateordernumberscenario = models.CharField(max_length=255, blank=True, null=True)
# #     allowtravellercalendar = models.BooleanField(blank=True, null=True)
# #     auto_email_itinerary_documents = models.IntegerField(blank=True, null=True)
# #     email_calendar_appointments = models.IntegerField(blank=True, null=True)
# #     personalassistantname = models.IntegerField(blank=True, null=True)
# #     purchaseorder = models.IntegerField(blank=True, null=True)
# #     projectnumber = models.IntegerField(blank=True, null=True)
# #     autovoucher = models.BooleanField(blank=True, null=True)
# #     autovoucher_email = models.CharField(max_length=255, blank=True, null=True)
# #     customer_no = models.CharField(max_length=255, blank=True, null=True)
# #     office_number = models.IntegerField(blank=True, null=True)
# #     agencypcc = models.CharField(max_length=255, blank=True, null=True)
# #     corporatecode = models.CharField(max_length=255, blank=True, null=True)
# #     viptravellerreason = models.BooleanField(blank=True, null=True)
# #     electronic_document_required = models.BooleanField(blank=True, null=True)
# #     pseudocitycode = models.CharField(max_length=255, blank=True, null=True)
# #     country_code = models.ForeignKey(Country, models.DO_NOTHING, db_column='country_code', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchants'


# # class MerchantsTravellerloyaltyprogram(models.Model):
# #     merchants_merchant = models.ForeignKey(Merchants, models.DO_NOTHING)
# #     affiliations_travellerloyaltyprogramid = models.ForeignKey('Travellerloyaltyprogram', models.DO_NOTHING, db_column='affiliations_travellerloyaltyprogramid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchants_travellerloyaltyprogram'


# # class Merchantssettings(models.Model):
# #     merchants_settings_id = models.BigIntegerField(primary_key=True)
# #     clientaccountnumber = models.CharField(max_length=255, blank=True, null=True)
# #     clientdebtornumber = models.CharField(max_length=255, blank=True, null=True)
# #     dvctype = models.CharField(max_length=255, blank=True, null=True)
# #     isactive = models.BooleanField(blank=True, null=True)
# #     merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)
# #     isdinersmember = models.BooleanField(blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     memberidentifier = models.CharField(max_length=255, blank=True, null=True)
# #     accountname = models.CharField(max_length=255, blank=True, null=True)
# #     addresslineone = models.CharField(max_length=255, blank=True, null=True)
# #     addresslinetwo = models.CharField(max_length=255, blank=True, null=True)
# #     city = models.CharField(max_length=255, blank=True, null=True)
# #     country = models.CharField(max_length=255, blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     postalcode = models.CharField(max_length=255, blank=True, null=True)
# #     registeredname = models.CharField(max_length=255, blank=True, null=True)
# #     registrationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     suburb = models.CharField(max_length=255, blank=True, null=True)
# #     taxnumber = models.CharField(max_length=255, blank=True, null=True)
# #     telephone = models.CharField(max_length=255, blank=True, null=True)
# #     tradename = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantssettings'


# # class Merchantswitchmap(models.Model):
# #     merchant_id = models.BigIntegerField(primary_key=True)
# #     switch_id = models.BigIntegerField()
# #     merchant_number = models.CharField(max_length=25)

# #     class Meta:
# #         managed = False
# #         db_table = 'merchantswitchmap'
# #         unique_together = (('merchant_id', 'switch_id'),)


# # class Messages(models.Model):
# #     messageid = models.BigIntegerField(primary_key=True)
# #     messagetext = models.CharField(max_length=3000, blank=True, null=True)
# #     messagetype = models.IntegerField(blank=True, null=True)
# #     description = models.CharField(max_length=100, blank=True, null=True)
# #     numfields = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'messages'


# # class Messagetypes(models.Model):
# #     typeid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'messagetypes'


# # class Missedsavingsassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'missedsavingsassertion'


# # class Missedsavingsreasons(models.Model):
# #     reasonid = models.BigIntegerField(primary_key=True)
# #     merchant = models.ForeignKey(Merchants, models.DO_NOTHING)
# #     missed_savings_reason = models.CharField(max_length=255, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     created_by = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'missedsavingsreasons'


# # class Missedsavingsviolation(models.Model):
# #     missedsavingsviolationid = models.BigIntegerField(primary_key=True)
# #     datetime = models.DateTimeField(blank=True, null=True)
# #     bookingconfirmation = models.CharField(max_length=255, blank=True, null=True)
# #     trip_trip = models.ForeignKey('Trip', models.DO_NOTHING, blank=True, null=True)
# #     violationreason = models.CharField(max_length=1024, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)
# #     violatedbyperson_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     additionalcomments = models.CharField(max_length=1024, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'missedsavingsviolation'


# # class NedbankDemoCostCentre(models.Model):
# #     id = models.CharField(primary_key=True, max_length=255)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'nedbank_demo_cost_centre'


# # class NedbankDemoStaff(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     birthdate = models.DateTimeField(blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     employmentpermanency = models.CharField(max_length=255, blank=True, null=True)
# #     familyname = models.CharField(max_length=255, blank=True, null=True)
# #     gender = models.CharField(max_length=255, blank=True, null=True)
# #     givenname = models.CharField(max_length=255, blank=True, null=True)
# #     middlename = models.CharField(max_length=255, blank=True, null=True)
# #     mobilephone_area = models.CharField(max_length=255, blank=True, null=True)
# #     mobilephone_country = models.CharField(max_length=255, blank=True, null=True)
# #     mobilephone_localnum = models.CharField(max_length=255, blank=True, null=True)
# #     title = models.CharField(max_length=255, blank=True, null=True)
# #     workphone_area = models.CharField(max_length=255, blank=True, null=True)
# #     workphone_country = models.CharField(max_length=255, blank=True, null=True)
# #     workphone_localnum = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'nedbank_demo_staff'


# # class Nightsbridgeallowances(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     allowancecode = models.CharField(max_length=255, blank=True, null=True)
# #     bbid = models.BigIntegerField(blank=True, null=True)
# #     hotelname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'nightsbridgeallowances'


# # class Nominatedapproversactivation(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     createuser = models.BigIntegerField(blank=True, null=True)
# #     enabled = models.BooleanField(blank=True, null=True)
# #     merchantid = models.ForeignKey(Merchants, models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'nominatedapproversactivation'


# # class Note(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     content = models.CharField(max_length=8192, blank=True, null=True)
# #     firstpublishedat = models.DateTimeField(blank=True, null=True)
# #     intent = models.CharField(max_length=255, blank=True, null=True)
# #     lastupdatedat = models.DateTimeField(blank=True, null=True)
# #     publisher = models.CharField(max_length=255, blank=True, null=True)
# #     subjecturi = models.CharField(max_length=255, blank=True, null=True)
# #     contexturi = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'note'


# # class Numberoftravellersonsameserviceassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     numberoftravellers = models.IntegerField(blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'numberoftravellersonsameserviceassertion'


# # class OdeActivityRecovery(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     actions = models.CharField(max_length=255, blank=True, null=True)
# #     activity_id = models.BigIntegerField(blank=True, null=True)
# #     channel = models.CharField(max_length=255, blank=True, null=True)
# #     date_time = models.DateTimeField(blank=True, null=True)
# #     details = models.TextField(blank=True, null=True)
# #     instance_id = models.BigIntegerField(blank=True, null=True)
# #     reason = models.CharField(max_length=255, blank=True, null=True)
# #     retries = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_activity_recovery'


# # class OdeCorrelationSet(models.Model):
# #     correlation_set_id = models.BigIntegerField(primary_key=True)
# #     correlation_key = models.CharField(max_length=255, blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     scope_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_correlation_set'


# # class OdeCorrelator(models.Model):
# #     correlator_id = models.BigIntegerField(primary_key=True)
# #     correlator_key = models.CharField(max_length=255, blank=True, null=True)
# #     proc_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_correlator'


# # class OdeCorsetProp(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     corrset_id = models.BigIntegerField(blank=True, null=True)
# #     prop_key = models.CharField(max_length=255, blank=True, null=True)
# #     prop_value = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_corset_prop'


# # class OdeEvent(models.Model):
# #     event_id = models.BigIntegerField(primary_key=True)
# #     detail = models.CharField(max_length=255, blank=True, null=True)
# #     data = models.BinaryField(blank=True, null=True)
# #     scope_id = models.BigIntegerField(blank=True, null=True)
# #     tstamp = models.DateTimeField(blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     instance_id = models.BigIntegerField(blank=True, null=True)
# #     process_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_event'


# # class OdeFault(models.Model):
# #     fault_id = models.BigIntegerField(primary_key=True)
# #     activity_id = models.IntegerField(blank=True, null=True)
# #     data = models.TextField(blank=True, null=True)
# #     message = models.CharField(max_length=4000, blank=True, null=True)
# #     line_number = models.IntegerField(blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_fault'


# # class OdeJob(models.Model):
# #     jobid = models.CharField(primary_key=True, max_length=64)
# #     ts = models.BigIntegerField()
# #     nodeid = models.CharField(max_length=64, blank=True, null=True)
# #     scheduled = models.IntegerField()
# #     transacted = models.IntegerField()
# #     details = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_job'


# # class OdeMessage(models.Model):
# #     message_id = models.BigIntegerField(primary_key=True)
# #     data = models.TextField(blank=True, null=True)
# #     header = models.TextField(blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     message_exchange_id = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_message'


# # class OdeMessageExchange(models.Model):
# #     message_exchange_id = models.CharField(primary_key=True, max_length=255)
# #     callee = models.CharField(max_length=255, blank=True, null=True)
# #     channel = models.CharField(max_length=255, blank=True, null=True)
# #     correlation_id = models.CharField(max_length=255, blank=True, null=True)
# #     correlation_keys = models.CharField(max_length=255, blank=True, null=True)
# #     correlation_status = models.CharField(max_length=255, blank=True, null=True)
# #     create_time = models.DateTimeField(blank=True, null=True)
# #     direction = models.IntegerField(blank=True, null=True)
# #     epr = models.TextField(blank=True, null=True)
# #     fault = models.CharField(max_length=255, blank=True, null=True)
# #     fault_explanation = models.CharField(max_length=255, blank=True, null=True)
# #     operation = models.CharField(max_length=255, blank=True, null=True)
# #     partner_link_model_id = models.IntegerField(blank=True, null=True)
# #     pattern = models.CharField(max_length=255, blank=True, null=True)
# #     piped_id = models.CharField(max_length=255, blank=True, null=True)
# #     port_type = models.CharField(max_length=255, blank=True, null=True)
# #     propagate_trans = models.BooleanField(blank=True, null=True)
# #     status = models.CharField(max_length=255, blank=True, null=True)
# #     subscriber_count = models.IntegerField(blank=True, null=True)
# #     process_instance_id = models.BigIntegerField(blank=True, null=True)
# #     corr_id = models.BigIntegerField(blank=True, null=True)
# #     partner_link_id = models.BigIntegerField(blank=True, null=True)
# #     process_id = models.BigIntegerField(blank=True, null=True)
# #     request_message_id = models.BigIntegerField(blank=True, null=True)
# #     response_message_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_message_exchange'


# # class OdeMessageRoute(models.Model):
# #     message_route_id = models.BigIntegerField(primary_key=True)
# #     correlation_key = models.CharField(max_length=255, blank=True, null=True)
# #     group_id = models.CharField(max_length=255, blank=True, null=True)
# #     route_index = models.IntegerField(blank=True, null=True)
# #     process_instance_id = models.IntegerField(blank=True, null=True)
# #     route_policy = models.CharField(max_length=16, blank=True, null=True)
# #     corr_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_message_route'


# # class OdeMexProp(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     mex_id = models.CharField(max_length=255, blank=True, null=True)
# #     prop_key = models.CharField(max_length=255, blank=True, null=True)
# #     prop_value = models.CharField(max_length=2000, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_mex_prop'


# # class OdePartnerLink(models.Model):
# #     partner_link_id = models.BigIntegerField(primary_key=True)
# #     my_epr = models.TextField(blank=True, null=True)
# #     my_role_name = models.CharField(max_length=255, blank=True, null=True)
# #     my_role_service_name = models.CharField(max_length=255, blank=True, null=True)
# #     my_session_id = models.CharField(max_length=255, blank=True, null=True)
# #     partner_epr = models.TextField(blank=True, null=True)
# #     partner_link_model_id = models.IntegerField(blank=True, null=True)
# #     partner_link_name = models.CharField(max_length=255, blank=True, null=True)
# #     partner_role_name = models.CharField(max_length=255, blank=True, null=True)
# #     partner_session_id = models.CharField(max_length=255, blank=True, null=True)
# #     scope_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_partner_link'


# # class OdeProcess(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     guid = models.CharField(max_length=255, blank=True, null=True)
# #     process_id = models.CharField(max_length=255, blank=True, null=True)
# #     process_type = models.CharField(max_length=255, blank=True, null=True)
# #     version = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_process'


# # class OdeProcessInstance(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     date_created = models.DateTimeField(blank=True, null=True)
# #     execution_state = models.BinaryField(blank=True, null=True)
# #     fault_id = models.BigIntegerField(blank=True, null=True)
# #     last_active_time = models.DateTimeField(blank=True, null=True)
# #     last_recovery_date = models.DateTimeField(blank=True, null=True)
# #     previous_state = models.SmallIntegerField(blank=True, null=True)
# #     sequence = models.BigIntegerField(blank=True, null=True)
# #     instance_state = models.SmallIntegerField(blank=True, null=True)
# #     instantiating_correlator_id = models.BigIntegerField(blank=True, null=True)
# #     process_id = models.BigIntegerField(blank=True, null=True)
# #     root_scope_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_process_instance'


# # class OdeSchemaVersion(models.Model):
# #     version = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_schema_version'


# # class OdeScope(models.Model):
# #     scope_id = models.BigIntegerField(primary_key=True)
# #     model_id = models.IntegerField(blank=True, null=True)
# #     scope_name = models.CharField(max_length=255, blank=True, null=True)
# #     scope_state = models.CharField(max_length=255, blank=True, null=True)
# #     parent_scope_id = models.BigIntegerField(blank=True, null=True)
# #     process_instance_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_scope'


# # class OdeXmlData(models.Model):
# #     xml_data_id = models.BigIntegerField(primary_key=True)
# #     data = models.TextField(blank=True, null=True)
# #     is_simple_type = models.BooleanField(blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     scope_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_xml_data'


# # class OdeXmlDataProp(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     xml_data_id = models.BigIntegerField(blank=True, null=True)
# #     prop_key = models.CharField(max_length=255, blank=True, null=True)
# #     prop_value = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'ode_xml_data_prop'


# # class Omtmpperson(models.Model):
# #     personid = models.BigIntegerField(primary_key=True)
# #     staff_code = models.CharField(max_length=-1, blank=True, null=True)
# #     id_number = models.CharField(max_length=-1, blank=True, null=True)
# #     email = models.CharField(max_length=-1, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'omtmpperson'


# # class OpenjpaSequenceTable(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     sequence_value = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'openjpa_sequence_table'


# # class Optionalworkflowstepsubscription(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     occurredat = models.DateTimeField(blank=True, null=True)
# #     optionalworkflowstep = models.CharField(max_length=255, blank=True, null=True)
# #     client_merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'optionalworkflowstepsubscription'


# # class Originalamexlineitem(models.Model):
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     reference = models.CharField(max_length=255, blank=True, null=True)
# #     controlaccount = models.CharField(max_length=255, blank=True, null=True)
# #     transtype = models.CharField(max_length=255, blank=True, null=True)
# #     transdate = models.CharField(max_length=255, blank=True, null=True)
# #     processdate = models.CharField(max_length=255, blank=True, null=True)
# #     accountname = models.CharField(max_length=255, blank=True, null=True)
# #     statementperiod = models.CharField(max_length=255, blank=True, null=True)
# #     accountnumber = models.CharField(max_length=255, blank=True, null=True)
# #     refnumber = models.CharField(max_length=255, blank=True, null=True)
# #     transamount = models.CharField(max_length=255, blank=True, null=True)
# #     statementitemid = models.ForeignKey('Statementitem', models.DO_NOTHING, db_column='statementitemid', blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)
# #     plasticnumber = models.CharField(max_length=-1, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'originalamexlineitem'


# # class Originaldinerslineitem(models.Model):
# #     referencenumber = models.CharField(max_length=255, blank=True, null=True)
# #     ordernumber = models.CharField(max_length=255, blank=True, null=True)
# #     cardnumber = models.CharField(max_length=255, blank=True, null=True)
# #     transtype = models.CharField(max_length=255, blank=True, null=True)
# #     transdate = models.CharField(max_length=255, blank=True, null=True)
# #     processdate = models.CharField(max_length=255, blank=True, null=True)
# #     supplier = models.CharField(max_length=255, blank=True, null=True)
# #     customername = models.CharField(max_length=255, blank=True, null=True)
# #     transamount = models.CharField(max_length=255, blank=True, null=True)
# #     debitorcredit = models.CharField(max_length=255, blank=True, null=True)
# #     statementid = models.ForeignKey('Statementheader', models.DO_NOTHING, db_column='statementid', blank=True, null=True)
# #     statementitemid = models.ForeignKey('Statementitem', models.DO_NOTHING, db_column='statementitemid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'originaldinerslineitem'


# # class Othergenericitems(models.Model):
# #     otheritemid = models.BigIntegerField(primary_key=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     otherreqid = models.BigIntegerField(blank=True, null=True)
# #     paidon = models.DateTimeField(blank=True, null=True)
# #     totalamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     vat = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     capturedby_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     tripid = models.ForeignKey('Trip', models.DO_NOTHING, db_column='tripid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'othergenericitems'


# # class Otheritems(models.Model):
# #     otheritemid = models.BigIntegerField(primary_key=True)
# #     otherreqid = models.BigIntegerField(blank=True, null=True)
# #     name = models.CharField(max_length=1000, blank=True, null=True)
# #     description = models.CharField(max_length=1000, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     vat = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     tripid = models.ForeignKey('Trip', models.DO_NOTHING, db_column='tripid', blank=True, null=True)
# #     startdate = models.DateTimeField(blank=True, null=True)
# #     enddate = models.DateTimeField(blank=True, null=True)
# #     trip = models.ForeignKey('Trip', models.DO_NOTHING, db_column='trip', blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     paidon = models.DateTimeField(blank=True, null=True)
# #     paymentmechanismowner = models.CharField(max_length=255, blank=True, null=True)
# #     totalamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     capturedby_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     paymentmechanismid = models.ForeignKey('Paymentmechanism', models.DO_NOTHING, db_column='paymentmechanismid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'otheritems'


# # class Otherrequest(models.Model):
# #     requestid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     description = models.CharField(max_length=100, blank=True, null=True)
# #     date = models.DateTimeField(blank=True, null=True)
# #     billinginfo = models.CharField(max_length=50, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
# #     special_requests = models.CharField(max_length=200, blank=True, null=True)
# #     other_information = models.CharField(max_length=200, blank=True, null=True)
# #     maxcost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
# #     specialrequests = models.CharField(max_length=255, blank=True, null=True)
# #     otherinformation = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'otherrequest'


# # class Packeterror(models.Model):
# #     xmlpacketid = models.BigIntegerField(primary_key=True)
# #     errortypeid = models.IntegerField()
# #     timestamp = models.DateTimeField()
# #     comment = models.CharField(max_length=250, blank=True, null=True)
# #     adminid = models.BigIntegerField(blank=True, null=True)
# #     actiontakenflag = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'packeterror'


# # class Packettype(models.Model):
# #     typeid = models.IntegerField(primary_key=True)
# #     typename = models.CharField(max_length=80)

# #     class Meta:
# #         managed = False
# #         db_table = 'packettype'


# # class Parking(models.Model):
# #     parkingid = models.BigIntegerField(primary_key=True)
# #     collectiondatetime = models.DateTimeField(blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     dropoffdatetime = models.DateTimeField(blank=True, null=True)
# #     facility = models.CharField(max_length=255, blank=True, null=True)
# #     licenseregistration = models.CharField(max_length=255, blank=True, null=True)
# #     manufacturer = models.CharField(max_length=255, blank=True, null=True)
# #     modelname = models.CharField(max_length=255, blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     operator = models.CharField(max_length=255, blank=True, null=True)
# #     parkingcost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     reservationnumber = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovider = models.CharField(max_length=255, blank=True, null=True)
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid', blank=True, null=True)
# #     status_resstatus = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='status_resstatus', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'parking'


# # class Parkingfacility(models.Model):
# #     facilityid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'parkingfacility'


# # class Parkinglicenseregistration(models.Model):
# #     registrationid = models.BigIntegerField(primary_key=True)
# #     licensingauthority = models.CharField(max_length=255, blank=True, null=True)
# #     vehicleregistration = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'parkinglicenseregistration'


# # class Passport(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     expirydate = models.CharField(max_length=255, blank=True, null=True)
# #     passportnumber = models.CharField(max_length=255, blank=True, null=True)
# #     passportcountrycode = models.ForeignKey(Country, models.DO_NOTHING, db_column='passportcountrycode', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'passport'


# # class Paymentcarddetails(models.Model):
# #     cardnumber = models.CharField(max_length=100)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     cardtype = models.IntegerField(blank=True, null=True)
# #     cvv = models.CharField(max_length=3)
# #     expiry = models.CharField(max_length=4)
# #     cardholdername = models.CharField(max_length=50, blank=True, null=True)
# #     paymentcarddetailsid = models.BigIntegerField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymentcarddetails'


# # class Paymentcardtype(models.Model):
# #     cardtypeid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymentcardtype'


# # class Paymentmechanism(models.Model):
# #     paymentmechanismid = models.BigIntegerField(primary_key=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     proconid = models.BigIntegerField(blank=True, null=True)
# #     code = models.CharField(max_length=20, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymentmechanism'


# # class Paymentmethod(models.Model):
# #     paymentmethodid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=20, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymentmethod'


# # class Paymentstatus(models.Model):
# #     statusid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=50)
# #     description = models.CharField(max_length=150)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymentstatus'


# # class Paymenttxmap(models.Model):
# #     merchantpaymentrqid = models.BigIntegerField(primary_key=True)
# #     transactionid = models.BigIntegerField()
# #     successflag = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'paymenttxmap'
# #         unique_together = (('merchantpaymentrqid', 'transactionid'),)


# # class Paymenttxstatus(models.Model):
# #     statusid = models.IntegerField(primary_key=True)
# #     status = models.CharField(max_length=100)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymenttxstatus'


# # class Paymenttype(models.Model):
# #     paymenttypeid = models.IntegerField(primary_key=True)
# #     paymenttypename = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'paymenttype'


# # class Period(models.Model):
# #     periodid = models.BigIntegerField(primary_key=True)
# #     periodstart = models.DateTimeField(blank=True, null=True)
# #     perioedend = models.DateTimeField(blank=True, null=True)
# #     periodend = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'period'


# # class Person(models.Model):
# #     personid = models.AutoField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     vip = models.ForeignKey('Viptraveller', models.DO_NOTHING, db_column='vip', blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     createdbyagent = models.CharField(max_length=255, blank=True, null=True)
# #     emergencycontact = models.ForeignKey(Emergencycontact, models.DO_NOTHING, db_column='emergencycontact', blank=True, null=True)
# #     approver = models.ForeignKey(Autoapprovalapproverconfig, models.DO_NOTHING, db_column='approver', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person'


# # class PersonAdditionalemail(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     additionalemails = models.ForeignKey(Additionalemail, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_additionalemail'
# #         unique_together = (('person_personid', 'additionalemails'),)


# # class PersonCarboncopyemail(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     ccemail = models.ForeignKey(Carboncopyemail, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_carboncopyemail'


# # class PersonContact(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid')
# #     personaldetails_contact = models.ForeignKey(Contact, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_contact'


# # class PersonDriverslicence(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     driverslicences = models.ForeignKey(Driverslicence, models.DO_NOTHING, unique=True)
# #     licence = models.ForeignKey(Driverslicence, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_driverslicence'
# #         unique_together = (('person_personid', 'driverslicences'),)


# # class PersonEmployee(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid')
# #     employmentdetails_employee = models.ForeignKey(Employee, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_employee'


# # class PersonFlightpreference(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     flighttype = models.CharField(max_length=255, blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     meal = models.CharField(max_length=255, blank=True, null=True)
# #     person_personid = models.BigIntegerField(blank=True, null=True)
# #     seatconfiguration = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_flightpreference'


# # class PersonLoyaltyprogram(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     person_personid = models.BigIntegerField(blank=True, null=True)
# #     program_name = models.CharField(max_length=255, blank=True, null=True)
# #     program_number = models.CharField(max_length=255, blank=True, null=True)
# #     programid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_loyaltyprogram'


# # class PersonPassport(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     passports = models.ForeignKey(Passport, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_passport'
# #         unique_together = (('person_personid', 'passports'),)


# # class PersonTravellerflightpreference(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid')
# #     flightpreferences_travellerflightpreferenceid = models.ForeignKey('Travellerflightpreference', models.DO_NOTHING, db_column='flightpreferences_travellerflightpreferenceid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_travellerflightpreference'


# # class PersonTravellerloyaltyprogram(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid')
# #     loyaltyprograms_travellerloyaltyprogramid = models.ForeignKey('Travellerloyaltyprogram', models.DO_NOTHING, db_column='loyaltyprograms_travellerloyaltyprogramid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_travellerloyaltyprogram'


# # class PersonVehicle(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     vehicles = models.ForeignKey('Vehicle', models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_vehicle'
# #         unique_together = (('person_personid', 'vehicles'),)


# # class PersonVisa(models.Model):
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', primary_key=True)
# #     visas = models.ForeignKey('Visa', models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'person_visa'
# #         unique_together = (('person_personid', 'visas'),)


# # class Picture(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     contenttype = models.CharField(max_length=255, blank=True, null=True)
# #     width = models.IntegerField()
# #     height = models.IntegerField()
# #     published = models.DateTimeField(blank=True, null=True)
# #     rank = models.IntegerField(blank=True, null=True)
# #     filesize = models.BigIntegerField()
# #     subjecturi = models.CharField(max_length=255, blank=True, null=True)
# #     pictureuri = models.CharField(max_length=255, blank=True, null=True)
# #     imagedata = models.ForeignKey(Imagedata, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'picture'


# # class Policy(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     active = models.BooleanField(blank=True, null=True)
# #     activationdate = models.DateTimeField(blank=True, null=True)
# #     policyuri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'policy'


# # class Policyviolationreasonspercompany(models.Model):
# #     reasonid = models.BigIntegerField(primary_key=True)
# #     merchant = models.ForeignKey(Merchants, models.DO_NOTHING)
# #     violation_reason = models.CharField(max_length=255, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     created_by = models.CharField(max_length=255, blank=True, null=True)
# #     updated = models.DateTimeField(blank=True, null=True)
# #     updated_by = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'policyviolationreasonspercompany'


# # class Preflang(models.Model):
# #     lang_code = models.CharField(primary_key=True, max_length=6)
# #     iso3 = models.CharField(max_length=10, blank=True, null=True)
# #     name = models.CharField(max_length=50, blank=True, null=True)
# #     supported = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'preflang'


# # class Processor(models.Model):
# #     guid = models.BigIntegerField(primary_key=True)
# #     processordescription = models.CharField(max_length=255, blank=True, null=True)
# #     xpathquery = models.CharField(max_length=255, blank=True, null=True)
# #     processorclassname = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'processor'


# # class Processqueue(models.Model):
# #     xmlpacketid = models.BigIntegerField(primary_key=True)
# #     timestamp = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'processqueue'


# # class Products(models.Model):
# #     productid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.BigIntegerField(blank=True, null=True)
# #     description = models.CharField(max_length=350, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'products'


# # class ProfileAudits(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     changed_by = models.CharField(max_length=255, blank=True, null=True)
# #     changed_on = models.DateTimeField(blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     field = models.CharField(max_length=255, blank=True, null=True)
# #     new_value = models.CharField(max_length=255, blank=True, null=True)
# #     old_value = models.CharField(max_length=255, blank=True, null=True)
# #     personid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'profile_audits'


# # class Profiledisable(models.Model):
# #     member_id = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'profiledisable'


# # class Profilefeature(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'profilefeature'


# # class Profiletype(models.Model):
# #     profiletypeid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=30, blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)
# #     roles = models.TextField(blank=True, null=True)  # This field type is a guess.

# #     class Meta:
# #         managed = False
# #         db_table = 'profiletype'


# # class Profileupdate(models.Model):
# #     member_id = models.BigIntegerField()
# #     staff_code = models.CharField(max_length=255, blank=True, null=True)
# #     employmenttype = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'profileupdate'


# # class Program(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=20, blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)
# #     member_id = models.BigIntegerField()
# #     memberid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'program'


# # class Programbranchmap(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     branchid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'programbranchmap'
# #         unique_together = (('programid', 'branchid'),)


# # class Programcuts(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     cutid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'programcuts'
# #         unique_together = (('programid', 'cutid'),)


# # class Programdemographicmap(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     demographicid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'programdemographicmap'
# #         unique_together = (('programid', 'demographicid'),)


# # class Programservicemap(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     serviceid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'programservicemap'
# #         unique_together = (('programid', 'serviceid'),)


# # class Programsourcemap(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     sourceid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'programsourcemap'
# #         unique_together = (('programid', 'sourceid'),)


# # class Province(models.Model):
# #     province_id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=30, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'province'


# # class Purchasecontrolconfirmation(models.Model):
# #     invoiceuri = models.CharField(max_length=255, blank=True, null=True)
# #     purchasecontrolidentifier = models.CharField(max_length=255, blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     xml = models.BinaryField(blank=True, null=True)
# #     id = models.ForeignKey('Purchasecontrolresult', models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'purchasecontrolconfirmation'


# # class Purchasecontrolexception(models.Model):
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey('Purchasecontrolresult', models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'purchasecontrolexception'


# # class Purchasecontrolresult(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     supplierreference = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'purchasecontrolresult'


# # class Purchasecontrolsupplier(models.Model):
# #     purchasecontrolsupplierid = models.BigIntegerField(primary_key=True)
# #     accountname = models.CharField(max_length=255, blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     uniformresourcelocator = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'purchasecontrolsupplier'


# # class Queuesetup(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     proc_queue_size = models.IntegerField()
# #     poll_interval = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'queuesetup'


# # class Quote(models.Model):
# #     quoteid = models.CharField(primary_key=True, max_length=255)
# #     expirydate = models.DateTimeField(blank=True, null=True)
# #     quoteresponse_quoteresponseid = models.ForeignKey('Quoteresponse', models.DO_NOTHING, db_column='quoteresponse_quoteresponseid', blank=True, null=True)
# #     message = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quote'


# # class QuoteTest(models.Model):
# #     quoteid = models.CharField(max_length=255)
# #     expirydate = models.DateTimeField(blank=True, null=True)
# #     quoteresponse_quoteresponseid = models.BigIntegerField(blank=True, null=True)
# #     message = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quote_test'


# # class Quoteresponse(models.Model):
# #     quoteresponseid = models.BigIntegerField(primary_key=True)
# #     message = models.BinaryField(blank=True, null=True)
# #     quoteresponseuri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quoteresponse'


# # class QuoteresponseBenchmark(models.Model):
# #     quoteresponse_quoteresponseid = models.ForeignKey(Quoteresponse, models.DO_NOTHING, db_column='quoteresponse_quoteresponseid')
# #     benchmark_quoteid = models.ForeignKey(Quote, models.DO_NOTHING, db_column='benchmark_quoteid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quoteresponse_benchmark'


# # class QuoteresponseCheapestfare(models.Model):
# #     quoteresponse_quoteresponseid = models.ForeignKey(Quoteresponse, models.DO_NOTHING, db_column='quoteresponse_quoteresponseid')
# #     cheapest_quoteid = models.ForeignKey(Quote, models.DO_NOTHING, db_column='cheapest_quoteid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quoteresponse_cheapestfare'


# # class QuoteresponseQuote(models.Model):
# #     quoteresponse_quoteresponseid = models.ForeignKey(Quoteresponse, models.DO_NOTHING, db_column='quoteresponse_quoteresponseid')
# #     benchmark_quoteid = models.ForeignKey(Quote, models.DO_NOTHING, db_column='benchmark_quoteid', unique=True, blank=True, null=True)
# #     cheapest_quoteid = models.ForeignKey(Quote, models.DO_NOTHING, db_column='cheapest_quoteid', unique=True, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'quoteresponse_quote'


# # class Railtransit(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     departuredatetime = models.DateTimeField(blank=True, null=True)
# #     goingto = models.CharField(max_length=255, blank=True, null=True)
# #     leavingfrom = models.CharField(max_length=255, blank=True, null=True)
# #     railclass = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovider = models.CharField(max_length=255, blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=255, blank=True, null=True)
# #     reservationid = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='reservationid', blank=True, null=True)
# #     status_resstatus = models.ForeignKey('Resstatustable', models.DO_NOTHING, db_column='status_resstatus', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'railtransit'


# # class Realmidentifiermapping(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     linkingguid = models.CharField(max_length=255, blank=True, null=True)
# #     roid = models.ForeignKey('Realmobject', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'realmidentifiermapping'


# # class Realmobject(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     realm = models.CharField(max_length=255, blank=True, null=True)
# #     roidid = models.CharField(max_length=255, blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'realmobject'


# # class Reconciliationaccountsupload(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     reportname = models.CharField(max_length=255, blank=True, null=True)
# #     merchant_merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconciliationaccountsupload'


# # class Reconciliationfiltereddata(models.Model):
# #     surname = models.CharField(max_length=255, blank=True, null=True)
# #     ordernumber = models.CharField(max_length=255, blank=True, null=True)
# #     firstname = models.CharField(max_length=255, blank=True, null=True)
# #     transamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     customerresid = models.CharField(max_length=255, blank=True, null=True)
# #     suppliername = models.CharField(max_length=255, blank=True, null=True)
# #     paymentdate = models.DateTimeField(blank=True, null=True)
# #     statementid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconciliationfiltereddata'


# # class Reconciliationstatementuploadproperties(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     issuer = models.CharField(max_length=255, blank=True, null=True)
# #     filepath = models.CharField(max_length=255, blank=True, null=True)
# #     dumppath = models.CharField(max_length=255, blank=True, null=True)
# #     reconciliationstatementname = models.CharField(max_length=255, blank=True, null=True)
# #     merchant_merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconciliationstatementuploadproperties'


# # class Reconcilliationaccomm(models.Model):
# #     invoiceid = models.BigIntegerField()
# #     reservationid = models.BigIntegerField(primary_key=True)
# #     invoiceamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     reservationnumber = models.CharField(max_length=40)
# #     hotelcode = models.CharField(max_length=40)
# #     roomtypecode = models.CharField(max_length=40, blank=True, null=True)
# #     occupants = models.IntegerField(blank=True, null=True)
# #     checkindate = models.DateTimeField(blank=True, null=True)
# #     checkoutdate = models.DateTimeField(blank=True, null=True)
# #     numberunits = models.IntegerField(blank=True, null=True)
# #     totalcost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     nonroomcost = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconcilliationaccomm'


# # class Reconcilliationcarhire(models.Model):
# #     invoiceid = models.BigIntegerField(primary_key=True)
# #     rentalid = models.BigIntegerField()
# #     supplierid = models.BigIntegerField()
# #     corporateid = models.BigIntegerField()
# #     reservationnumber = models.CharField(max_length=30)
# #     checkoutdate = models.DateTimeField(blank=True, null=True)
# #     terminationdate = models.DateTimeField(blank=True, null=True)
# #     checkoutlocation = models.CharField(max_length=50, blank=True, null=True)
# #     cargroupid = models.BigIntegerField(blank=True, null=True)
# #     billeddays = models.IntegerField(blank=True, null=True)
# #     billedkms = models.IntegerField(blank=True, null=True)
# #     name = models.CharField(max_length=20, blank=True, null=True)
# #     surname = models.CharField(max_length=20, blank=True, null=True)
# #     tnm = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     fuel = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     cdw = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     tlw = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     misc = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     airportcharge = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     oneway = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     contractfee = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     vat = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     invoiceamount = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     created = models.DateTimeField()
# #     rentaloffice = models.CharField(max_length=50, blank=True, null=True)
# #     reservationid = models.BigIntegerField(blank=True, null=True)
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconcilliationcarhire'


# # class Reconcilliationflights(models.Model):
# #     invoiceid = models.BigIntegerField()
# #     reservationid = models.BigIntegerField(primary_key=True)
# #     invoiceamount = models.DecimalField(max_digits=20, decimal_places=2)
# #     flightnumber = models.CharField(max_length=40, blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=40)
# #     flightdate = models.DateTimeField(blank=True, null=True)
# #     deppoint = models.CharField(max_length=10, blank=True, null=True)
# #     arrpoint = models.CharField(max_length=10, blank=True, null=True)
# #     classid = models.IntegerField(blank=True, null=True)
# #     passengernum = models.CharField(max_length=40, blank=True, null=True)
# #     loyaltynum = models.CharField(max_length=40, blank=True, null=True)
# #     farebasis = models.CharField(max_length=40, blank=True, null=True)
# #     commission = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField()
# #     airlineid = models.IntegerField()
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     segment = models.CharField(max_length=50, blank=True, null=True)
# #     std = models.CharField(max_length=50, blank=True, null=True)
# #     sta = models.CharField(max_length=50, blank=True, null=True)
# #     children = models.IntegerField(blank=True, null=True)
# #     legs = models.CharField(max_length=100, blank=True, null=True)
# #     ccnumber = models.CharField(max_length=200, blank=True, null=True)
# #     cctype = models.CharField(max_length=20, blank=True, null=True)
# #     ccholdername = models.CharField(max_length=30, blank=True, null=True)
# #     flighttransactiontypeid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reconcilliationflights'


# # class Region(models.Model):
# #     regionid = models.BigIntegerField(primary_key=True)
# #     regionname = models.CharField(max_length=255, blank=True, null=True)
# #     parentid = models.BigIntegerField(blank=True, null=True)
# #     countrycode = models.CharField(max_length=10, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'region'


# # class Regionalairports(models.Model):
# #     regionalairportsid = models.IntegerField(primary_key=True)
# #     deleted = models.BooleanField(blank=True, null=True)
# #     airportcode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'regionalairports'


# # class Regionlocator(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     id = models.BigIntegerField(blank=True, null=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'regionlocator'


# # class RegionlocatorGpslocator(models.Model):
# #     regionlocator_uri = models.ForeignKey(Regionlocator, models.DO_NOTHING, db_column='regionlocator_uri')
# #     gpslocators = models.ForeignKey(Gpslocator, models.DO_NOTHING)
# #     regionlocator_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'regionlocator_gpslocator'


# # class Registration(models.Model):
# #     registrationid = models.BigIntegerField(primary_key=True)
# #     sourceid = models.BigIntegerField(blank=True, null=True)
# #     declarationdate = models.DateTimeField(blank=True, null=True)
# #     eventid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'registration'


# # class Renewalperiod(models.Model):
# #     renewalperiodid = models.IntegerField(primary_key=True)
# #     startdate = models.DateTimeField()
# #     enddate = models.DateTimeField()

# #     class Meta:
# #         managed = False
# #         db_table = 'renewalperiod'


# # class ReportdefinitionSqltocsv(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     appendexternal = models.TextField(blank=True, null=True)
# #     description = models.CharField(max_length=512, blank=True, null=True)
# #     inputsql = models.TextField(blank=True, null=True)
# #     organisation = models.CharField(max_length=255, blank=True, null=True)
# #     role = models.CharField(max_length=255)

# #     class Meta:
# #         managed = False
# #         db_table = 'reportdefinition_sqltocsv'


# # class Requestforconsultantassistance(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     closedat = models.DateTimeField(blank=True, null=True)
# #     messagetoconsultant = models.CharField(max_length=2048, blank=True, null=True)
# #     requestedat = models.DateTimeField(blank=True, null=True)
# #     status = models.CharField(max_length=255, blank=True, null=True)
# #     agency_agencyid = models.ForeignKey('Travelagency', models.DO_NOTHING, db_column='agency_agencyid', blank=True, null=True)
# #     consultant_agentid = models.ForeignKey('Travelagent', models.DO_NOTHING, db_column='consultant_agentid', blank=True, null=True)
# #     requester_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='requester_personid', blank=True, null=True)
# #     trip_trip = models.ForeignKey('Trip', models.DO_NOTHING, blank=True, null=True)
# #     messagetorequester = models.CharField(max_length=2048, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'requestforconsultantassistance'


# # class Requestvo(models.Model):
# #     uid = models.CharField(primary_key=True, max_length=255)
# #     status = models.IntegerField(blank=True, null=True)
# #     responseset = models.BooleanField()
# #     tiernumber = models.IntegerField()
# #     requestreference = models.CharField(max_length=255, blank=True, null=True)
# #     approverinfo_guid = models.BigIntegerField(blank=True, null=True)
# #     groupstate_guid = models.ForeignKey(Groupstate, models.DO_NOTHING, db_column='groupstate_guid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'requestvo'


# # class Reservation(models.Model):
# #     reservationid = models.BigIntegerField(primary_key=True)
# #     trip_id = models.BigIntegerField()
# #     trav_agent_id = models.BigIntegerField(blank=True, null=True)
# #     created = models.DateTimeField()
# #     tableid = models.IntegerField(blank=True, null=True)
# #     reconcileflag = models.IntegerField(blank=True, null=True)
# #     groupid = models.BigIntegerField(blank=True, null=True)
# #     bookingengineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='bookingengineid', blank=True, null=True)
# #     travresid = models.BigIntegerField(blank=True, null=True)
# #     paymentstatus = models.ForeignKey(Paymentstatus, models.DO_NOTHING, db_column='paymentstatus', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reservation'


# # class Reservationloyalty(models.Model):
# #     reservationid = models.BigIntegerField(primary_key=True)
# #     loyaltynumber = models.CharField(max_length=80)

# #     class Meta:
# #         managed = False
# #         db_table = 'reservationloyalty'


# # class Resstatustable(models.Model):
# #     resstatus = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=30)
# #     type = models.CharField(max_length=15, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'resstatustable'


# # class Reversal(models.Model):
# #     reversalid = models.BigIntegerField(primary_key=True)
# #     timestamp = models.DateTimeField()
# #     invoiceid = models.BigIntegerField()
# #     authid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'reversal'


# # class Revinfo(models.Model):
# #     rev = models.IntegerField(primary_key=True)
# #     revtstmp = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'revinfo'


# # class Rewardsbreakageaccountmap(models.Model):
# #     rewardsprogid = models.BigIntegerField(primary_key=True)
# #     accountid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'rewardsbreakageaccountmap'


# # class Rewardsdetails(models.Model):
# #     accountid = models.BigIntegerField(primary_key=True)
# #     parentid = models.BigIntegerField(blank=True, null=True)
# #     balance = models.DecimalField(max_digits=20, decimal_places=10)
# #     statusid = models.IntegerField()
# #     toclear = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     branchid = models.IntegerField(blank=True, null=True)
# #     levelid = models.IntegerField(blank=True, null=True)
# #     rewardsprogramid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'rewardsdetails'


# # class Rewardsinvoice(models.Model):
# #     invoiceid = models.BigIntegerField(primary_key=True)
# #     cleared = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'rewardsinvoice'


# # class Rewardsprogram(models.Model):
# #     rewardsprogid = models.BigIntegerField(primary_key=True)
# #     programid = models.BigIntegerField()
# #     programname = models.CharField(max_length=50, blank=True, null=True)
# #     numberlevels = models.IntegerField()
# #     purchaserrebate = models.DecimalField(max_digits=20, decimal_places=10)
# #     vat = models.DecimalField(max_digits=20, decimal_places=10)
# #     conversionrate = models.DecimalField(max_digits=20, decimal_places=10, blank=True, null=True)
# #     member_id = models.BigIntegerField(blank=True, null=True)
# #     rewardsprogramid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'rewardsprogram'


# # class Rewardstransactions(models.Model):
# #     transactionid = models.BigIntegerField(primary_key=True)
# #     debitcredit = models.IntegerField(blank=True, null=True)
# #     accountid = models.BigIntegerField()
# #     amount = models.DecimalField(max_digits=20, decimal_places=2)
# #     cardnumber = models.CharField(max_length=20, blank=True, null=True)
# #     invoiceid = models.BigIntegerField()
# #     transactiontypeid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField(blank=True, null=True)
# #     level = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'rewardstransactions'


# # class Rfi(models.Model):
# #     rfiid = models.BigIntegerField(primary_key=True)
# #     rfitext = models.CharField(max_length=100)
# #     status = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'rfi'


# # class Rfiprogrammap(models.Model):
# #     programid = models.BigIntegerField(primary_key=True)
# #     rfiid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'rfiprogrammap'
# #         unique_together = (('programid', 'rfiid'),)


# # class Rfivalues(models.Model):
# #     rfiid = models.BigIntegerField()
# #     value = models.CharField(max_length=50)
# #     valueid = models.BigIntegerField(primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'rfivalues'


# # class Roleplayerpredicatevalueassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     predicate = models.CharField(max_length=255, blank=True, null=True)
# #     role = models.CharField(max_length=255, blank=True, null=True)
# #     value = models.CharField(max_length=255, blank=True, null=True)
# #     valueisregex = models.BooleanField(blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'roleplayerpredicatevalueassertion'


# # class Royalty(models.Model):
# #     royalty_id = models.IntegerField(primary_key=True)
# #     member_id = models.BigIntegerField()
# #     organisation = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     url = models.CharField(max_length=80, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'royalty'


# # class Seatclass(models.Model):
# #     seatclassid = models.AutoField(primary_key=True)
# #     providerspecificclass = models.CharField(max_length=255, blank=True, null=True)
# #     seatingclass = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'seatclass'


# # class Seatclassassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     industryseatclass = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'seatclassassertion'


# # class Seatclasscarbonemissionfactor(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     seatclass = models.CharField(max_length=255, blank=True, null=True)
# #     factor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     distanceclassifierid = models.ForeignKey(Flightsectordistanceclassifier, models.DO_NOTHING, db_column='distanceclassifierid', blank=True, null=True)
# #     flightdistanceclassification = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'seatclasscarbonemissionfactor'


# # class Seatconfiguration(models.Model):
# #     seatconfigurationid = models.AutoField(primary_key=True)
# #     relativeseatposition = models.CharField(max_length=255, blank=True, null=True)
# #     seatclassid = models.ForeignKey(Seatclass, models.DO_NOTHING, db_column='seatclassid', blank=True, null=True)
# #     seatnumerid = models.ForeignKey('Seatnumber', models.DO_NOTHING, db_column='seatnumerid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'seatconfiguration'


# # class Seatnumber(models.Model):
# #     seatnumerid = models.AutoField(primary_key=True)
# #     column = models.CharField(max_length=255, blank=True, null=True)
# #     row = models.CharField(max_length=255, blank=True, null=True)
# #     rowno = models.CharField(max_length=255, blank=True, null=True)
# #     columnno = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'seatnumber'


# # class Selectedquoteuris(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     selectedquoteuris = models.CharField(max_length=255, blank=True, null=True)
# #     selectedquotes = models.ForeignKey(Approvalrequest, models.DO_NOTHING, db_column='selectedquotes', blank=True, null=True)
# #     triprequirements_uri = models.ForeignKey('Triprequirements', models.DO_NOTHING, db_column='triprequirements_uri', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'selectedquoteuris'


# # class Sentsms(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     cellnumber = models.CharField(max_length=30)
# #     fromaccountid = models.BigIntegerField(blank=True, null=True)
# #     fromname = models.BigIntegerField(blank=True, null=True)
# #     messageid = models.BigIntegerField(blank=True, null=True)
# #     timestamp = models.DateTimeField()
# #     errorid = models.BigIntegerField(blank=True, null=True)
# #     batchid = models.BigIntegerField(blank=True, null=True)
# #     provider = models.BigIntegerField()
# #     provmessageid = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'sentsms'


# # class Service(models.Model):
# #     serviceid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=60)
# #     bean = models.CharField(max_length=60, blank=True, null=True)
# #     beanjndiname = models.CharField(max_length=80, blank=True, null=True)
# #     id = models.BigIntegerField(blank=True, null=True)
# #     location_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'service'


# # class Servicecancellation(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     invoiceuri = models.CharField(max_length=255, blank=True, null=True)
# #     reasonforchange = models.CharField(max_length=255, blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     cancelservice = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicecancellation'


# # class Servicecommencementdayofweekassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     servicecommencementdayofweek = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicecommencementdayofweekassertion'


# # class Servicecommencementnoticeperiodassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     noticeperiod = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'servicecommencementnoticeperiodassertion'


# # class Servicecommencementtimeofdayassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     servicecommencementtime = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicecommencementtimeofdayassertion'


# # class Serviceenddayofweekassertion(models.Model):
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     serviceenddayofweek = models.CharField(max_length=255, blank=True, null=True)
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'serviceenddayofweekassertion'


# # class Servicemapper(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     id = models.BigIntegerField(blank=True, null=True)
# #     servicetype = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicemapper'


# # class Serviceprovider(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     locationid = models.ForeignKey(Location, models.DO_NOTHING, db_column='locationid', blank=True, null=True)
# #     dtype = models.CharField(max_length=31, blank=True, null=True)
# #     hotelid = models.ForeignKey(Hotel, models.DO_NOTHING, db_column='hotelid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'serviceprovider'


# # class Serviceprovideridentityassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     serviceprovideruri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'serviceprovideridentityassertion'


# # class Serviceproviderindustryidentifierassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     serviceproviderschema = models.CharField(max_length=255, blank=True, null=True)
# #     serviceproviderindustrycode = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'serviceproviderindustryidentifierassertion'


# # class Serviceprovidertmp(models.Model):
# #     id = models.BigIntegerField(blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     locationid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'serviceprovidertmp'


# # class Servicetypeassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     servicetype = models.CharField(max_length=255, blank=True, null=True)
# #     servicetypenamespace = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicetypeassertion'


# # class Servicevouchertype(models.Model):
# #     vouchertypeid = models.AutoField(primary_key=True)
# #     vouchercode = models.CharField(max_length=255, blank=True, null=True)
# #     voucherdescription = models.CharField(max_length=100, blank=True, null=True)
# #     voucherservicetype = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'servicevouchertype'


# # class Shopper(models.Model):
# #     shopper_id = models.BigIntegerField(primary_key=True)
# #     member_id = models.BigIntegerField()
# #     id_number = models.CharField(max_length=40, blank=True, null=True)
# #     birth_date = models.DateTimeField(blank=True, null=True)
# #     receive_email = models.IntegerField(blank=True, null=True)
# #     receive_news = models.IntegerField(blank=True, null=True)
# #     created = models.DateTimeField()
# #     last_updated = models.DateTimeField(blank=True, null=True)
# #     id_type_id = models.IntegerField(blank=True, null=True)
# #     passport = models.CharField(max_length=30, blank=True, null=True)
# #     shopperid = models.BigIntegerField(blank=True, null=True)
# #     memberid = models.BigIntegerField(blank=True, null=True)
# #     idnumber = models.CharField(max_length=255, blank=True, null=True)
# #     id_type = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'shopper'


# # class Shortenedurl(models.Model):
# #     id = models.CharField(primary_key=True, max_length=255)
# #     fullurl = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'shortenedurl'


# # class Singlesignoncallback(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     callbackendpointurl = models.CharField(max_length=255)
# #     incomingreferrerpattern = models.CharField(max_length=255)
# #     externalsystemid = models.ForeignKey(Externalsystem, models.DO_NOTHING, db_column='externalsystemid')

# #     class Meta:
# #         managed = False
# #         db_table = 'singlesignoncallback'


# # class Source(models.Model):
# #     sourceid = models.BigIntegerField(primary_key=True)
# #     sourcename = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'source'


# # class Statement(models.Model):
# #     statementheaderid = models.BigIntegerField(primary_key=True)
# #     statementtype = models.CharField(max_length=10)
# #     filepacketid = models.BigIntegerField(blank=True, null=True)
# #     periodstart = models.DateField(blank=True, null=True)
# #     periodend = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statement'


# # class Statementairline(models.Model):
# #     statementairlineid = models.BigIntegerField(primary_key=True)
# #     airline = models.CharField(max_length=50, blank=True, null=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     passengername = models.CharField(max_length=50, blank=True, null=True)
# #     ticketnr = models.CharField(max_length=20, blank=True, null=True)
# #     ticketcode = models.CharField(max_length=10, blank=True, null=True)
# #     statementid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'statementairline'


# # class Statementdetail(models.Model):
# #     statementid = models.BigIntegerField(primary_key=True)
# #     statementheaderid = models.BigIntegerField()
# #     accountname = models.CharField(max_length=80, blank=True, null=True)
# #     accountnr = models.CharField(max_length=30, blank=True, null=True)
# #     controlaccount = models.CharField(max_length=30, blank=True, null=True)
# #     plasticnr = models.CharField(max_length=200, blank=True, null=True)
# #     transdate = models.DateField(blank=True, null=True)
# #     processdate = models.DateField(blank=True, null=True)
# #     referencenr = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     ordernr = models.CharField(max_length=25, blank=True, null=True)
# #     amount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     matched = models.IntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statementdetail'


# # class Statementheader(models.Model):
# #     issuer = models.CharField(max_length=255, blank=True, null=True)
# #     brand = models.CharField(max_length=255, blank=True, null=True)
# #     period = models.ForeignKey('Statementperiod', models.DO_NOTHING, blank=True, null=True)
# #     ownerid = models.ForeignKey(Merchants, models.DO_NOTHING, db_column='ownerid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statementheader'


# # class Statementitem(models.Model):
# #     processdate = models.DateField(blank=True, null=True)
# #     transactiondate = models.DateField(blank=True, null=True)
# #     statementid = models.ForeignKey(Statementheader, models.DO_NOTHING, db_column='statementid', blank=True, null=True)
# #     bankaccountid = models.ForeignKey(Bankaccount, models.DO_NOTHING, db_column='bankaccountid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statementitem'


# # class Statementitemdetail(models.Model):
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     statementitemid = models.ForeignKey(Statementitem, models.DO_NOTHING, db_column='statementitemid', blank=True, null=True)
# #     supplierid = models.ForeignKey('Supplier', models.DO_NOTHING, db_column='supplierid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statementitemdetail'


# # class Statementperiod(models.Model):
# #     startdate = models.DateField(blank=True, null=True)
# #     enddate = models.DateField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'statementperiod'


# # class Status(models.Model):
# #     statusid = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=20, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'status'


# # class StoreDu(models.Model):
# #     name = models.CharField(primary_key=True, max_length=255)
# #     deploydt = models.DateTimeField(blank=True, null=True)
# #     deployer = models.CharField(max_length=255, blank=True, null=True)
# #     dir = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'store_du'


# # class StoreProcToProp(models.Model):
# #     processconfdaoimpl_pid = models.CharField(max_length=255, blank=True, null=True)
# #     element_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'store_proc_to_prop'


# # class StoreProcess(models.Model):
# #     pid = models.CharField(primary_key=True, max_length=255)
# #     state = models.CharField(max_length=255, blank=True, null=True)
# #     type = models.CharField(max_length=255, blank=True, null=True)
# #     version = models.BigIntegerField(blank=True, null=True)
# #     du = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'store_process'


# # class StoreProcessProp(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     prop_key = models.CharField(max_length=255, blank=True, null=True)
# #     prop_val = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'store_process_prop'


# # class StoreVersions(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     version = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'store_versions'


# # class Storedcard(models.Model):
# #     storedcarduri = models.CharField(primary_key=True, max_length=255)
# #     owneruri = models.CharField(max_length=255, blank=True, null=True)
# #     carddetailid = models.ForeignKey(Carddetail, models.DO_NOTHING, db_column='carddetailid', blank=True, null=True)
# #     cardvaultid = models.ForeignKey(Cardvault, models.DO_NOTHING, db_column='cardvaultid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'storedcard'


# # class Supplier(models.Model):
# #     name = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplier'


# # class Supplierapplicationid(models.Model):
# #     supplierapplicationid = models.BigIntegerField(primary_key=True)
# #     supplierid = models.BigIntegerField()
# #     applicationid = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierapplicationid'


# # class Supplierbookingconfirmation(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     supplierreference = models.CharField(max_length=255, blank=True, null=True)
# #     logincredentialuri = models.CharField(max_length=255, blank=True, null=True)
# #     supplier = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='supplier', blank=True, null=True)
# #     invoiceuri = models.ForeignKey('Supplierinvoice', models.DO_NOTHING, db_column='invoiceuri', blank=True, null=True)
# #     bookingconfirmationxml = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation'


# # class SupplierbookingconfirmationAccommodation(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     hotels_bookingid = models.ForeignKey(Accommodation, models.DO_NOTHING, db_column='hotels_bookingid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_accommodation'


# # class SupplierbookingconfirmationBustransit(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     buses = models.ForeignKey(Bustransit, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_bustransit'


# # class SupplierbookingconfirmationCarrental(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     cars_rentalid = models.ForeignKey(Carrental, models.DO_NOTHING, db_column='cars_rentalid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_carrental'


# # class SupplierbookingconfirmationFlightfare(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     flights_flightgrpid = models.ForeignKey(Flightfare, models.DO_NOTHING, db_column='flights_flightgrpid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_flightfare'


# # class SupplierbookingconfirmationOtheritems(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     otheritems_otheritemid = models.ForeignKey(Otheritems, models.DO_NOTHING, db_column='otheritems_otheritemid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_otheritems'


# # class SupplierbookingconfirmationQuote(models.Model):
# #     supplierbookingconfirmation_uri = models.ForeignKey(Supplierbookingconfirmation, models.DO_NOTHING, db_column='supplierbookingconfirmation_uri')
# #     quotes_quoteid = models.ForeignKey(Quote, models.DO_NOTHING, db_column='quotes_quoteid', unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierbookingconfirmation_quote'


# # class Suppliercredential(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     createddate = models.DateTimeField(blank=True, null=True)
# #     data = models.BinaryField(blank=True, null=True)
# #     description = models.CharField(max_length=255, blank=True, null=True)
# #     disabled = models.BooleanField()
# #     ratetype = models.CharField(max_length=255, blank=True, null=True)
# #     updateddate = models.DateTimeField(blank=True, null=True)
# #     owner_merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)
# #     supplier_engineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='supplier_engineid', blank=True, null=True)
# #     updatedby_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'suppliercredential'


# # class Suppliercredentialalias(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     credential = models.ForeignKey(Suppliercredential, models.DO_NOTHING)

# #     class Meta:
# #         managed = False
# #         db_table = 'suppliercredentialalias'


# # class Supplierinvoice(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     settleby = models.DateTimeField(blank=True, null=True)
# #     settlementstatus = models.CharField(max_length=255, blank=True, null=True)
# #     trip_id = models.BigIntegerField(blank=True, null=True)
# #     supplierinvoicenumber = models.CharField(max_length=255, blank=True, null=True)
# #     source_engineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='source_engineid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierinvoice'


# # class SupplierinvoiceBookingengine(models.Model):
# #     supplierinvoice_uri = models.ForeignKey(Supplierinvoice, models.DO_NOTHING, db_column='supplierinvoice_uri')
# #     settlevia_engineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='settlevia_engineid')

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierinvoice_bookingengine'


# # class SupplierinvoicePaymentmechanism(models.Model):
# #     supplierinvoice_uri = models.ForeignKey(Supplierinvoice, models.DO_NOTHING, db_column='supplierinvoice_uri')
# #     settlementmechanism_paymentmechanismid = models.ForeignKey(Paymentmechanism, models.DO_NOTHING, db_column='settlementmechanism_paymentmechanismid')

# #     class Meta:
# #         managed = False
# #         db_table = 'supplierinvoice_paymentmechanism'


# # class Suppliermeals(models.Model):
# #     mealid = models.AutoField(primary_key=True)
# #     mealname = models.CharField(max_length=255, blank=True, null=True)
# #     mealcode = models.CharField(max_length=255, blank=True, null=True)
# #     engineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='engineid', blank=True, null=True)
# #     uri = models.CharField(max_length=255, blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'suppliermeals'


# # class Suppliertype(models.Model):
# #     suppliertypeid = models.BigIntegerField(primary_key=True)
# #     suppliertypedescription = models.CharField(max_length=200)

# #     class Meta:
# #         managed = False
# #         db_table = 'suppliertype'


# # class Supportcontact(models.Model):
# #     id = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     operatinghours = models.CharField(max_length=255, blank=True, null=True)
# #     contactdetail_contactdetailid = models.ForeignKey(Contactdetail, models.DO_NOTHING, db_column='contactdetail_contactdetailid', blank=True, null=True)
# #     merchants_merchant = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)
# #     role_admin_type = models.ForeignKey(AdminType, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supportcontact'


# # class Supportmessage(models.Model):
# #     messageid = models.AutoField(primary_key=True)
# #     message = models.CharField(max_length=255, blank=True, null=True)
# #     merchantid = models.ForeignKey(Merchants, models.DO_NOTHING, db_column='merchantid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'supportmessage'


# # class Switch(models.Model):
# #     switchid = models.BigIntegerField(primary_key=True)
# #     name = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'switch'


# # class Switcharchive(models.Model):
# #     xmlpacketid = models.BigIntegerField(primary_key=True)
# #     switchid = models.IntegerField()
# #     xmlblob = models.TextField()
# #     timestamp = models.DateTimeField()
# #     flag = models.IntegerField()
# #     typeid = models.IntegerField(blank=True, null=True)
# #     ret_ref_no = models.CharField(max_length=50, blank=True, null=True)
# #     file_name = models.CharField(max_length=150, blank=True, null=True)
# #     invoiceid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'switcharchive'


# # class Switchcuts(models.Model):
# #     switchid = models.BigIntegerField(primary_key=True)
# #     cutid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'switchcuts'
# #         unique_together = (('switchid', 'cutid'),)


# # class Switchmainqueue(models.Model):
# #     xmlpacketid = models.BigIntegerField(primary_key=True)
# #     switchid = models.IntegerField()
# #     xmlblob = models.TextField()
# #     timestamp = models.DateTimeField()
# #     flag = models.IntegerField()
# #     packettype = models.IntegerField(blank=True, null=True)
# #     ret_ref_no = models.CharField(max_length=50, blank=True, null=True)
# #     file_name = models.CharField(max_length=150, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'switchmainqueue'


# # class Switchnames(models.Model):
# #     switchid = models.IntegerField(primary_key=True)
# #     switchname = models.CharField(max_length=80)

# #     class Meta:
# #         managed = False
# #         db_table = 'switchnames'


# # class Switchxmlservice(models.Model):
# #     switchid = models.IntegerField(primary_key=True)
# #     typeid = models.IntegerField()
# #     name = models.CharField(max_length=50)
# #     package = models.CharField(max_length=50)
# #     classname = models.CharField(max_length=40)

# #     class Meta:
# #         managed = False
# #         db_table = 'switchxmlservice'
# #         unique_together = (('switchid', 'typeid'),)


# # class T20081108131224Exception(models.Model):
# #     flightgrpid = models.BigIntegerField()
# #     travresid = models.BigIntegerField(blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     ticketingairline = models.BigIntegerField(blank=True, null=True)
# #     ticketnumber = models.CharField(max_length=30, blank=True, null=True)
# #     basefare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     airporttax = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     vat = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     totalfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     publishedfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     savings = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     status = models.IntegerField(blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     costreason = models.CharField(max_length=200, blank=True, null=True)
# #     passfname = models.CharField(max_length=100, blank=True, null=True)
# #     passsname = models.CharField(max_length=100, blank=True, null=True)
# #     ticketed = models.IntegerField(blank=True, null=True)
# #     oldflightgroupid = models.BigIntegerField(blank=True, null=True)
# #     collectionid = models.BigIntegerField(blank=True, null=True)
# #     triptravid = models.BigIntegerField(blank=True, null=True)
# #     cheapestavailfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     bookedontl = models.IntegerField(blank=True, null=True)
# #     tickettimelimit = models.DateTimeField(blank=True, null=True)
# #     ticketeddate = models.DateTimeField(blank=True, null=True)
# #     reservationid = models.BigIntegerField(blank=True, null=True)
# #     pricingsource = models.CharField(max_length=255, blank=True, null=True)
# #     vendorlocator = models.CharField(max_length=255, blank=True, null=True)
# #     farebasiscodes = models.CharField(max_length=255, blank=True, null=True)
# #     tickettype = models.CharField(max_length=255, blank=True, null=True)
# #     currency = models.CharField(max_length=255, blank=True, null=True)
# #     bookingagent = models.BigIntegerField(blank=True, null=True)
# #     ticketingagent = models.BigIntegerField(blank=True, null=True)
# #     cheapestfare = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 't20081108_131224_exception'


# # class Tableid(models.Model):
# #     tableid = models.IntegerField(primary_key=True)
# #     tablename = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tableid'


# # class Taenginelogin(models.Model):
# #     travelagencyid = models.BigIntegerField(primary_key=True)
# #     bookingengineid = models.BigIntegerField()
# #     username = models.CharField(max_length=80, blank=True, null=True)
# #     password = models.CharField(max_length=80, blank=True, null=True)
# #     loginid = models.CharField(max_length=80, blank=True, null=True)
# #     loginpassword = models.CharField(max_length=80, blank=True, null=True)
# #     other = models.CharField(max_length=80, blank=True, null=True)
# #     corporateid = models.CharField(max_length=80, blank=True, null=True)
# #     companyid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'taenginelogin'
# #         unique_together = (('travelagencyid', 'bookingengineid', 'companyid'),)


# # class Tag(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     firstpublishedat = models.DateTimeField(blank=True, null=True)
# #     lastupdatedat = models.DateTimeField(blank=True, null=True)
# #     subjecturi = models.CharField(max_length=255, blank=True, null=True)
# #     tagger = models.CharField(max_length=255, blank=True, null=True)
# #     value = models.CharField(max_length=255, blank=True, null=True)
# #     tagdefinition_predicateuri = models.ForeignKey('Tagdefinition', models.DO_NOTHING, db_column='tagdefinition_predicateuri', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tag'


# # class Tagdefinition(models.Model):
# #     predicateuri = models.CharField(primary_key=True, max_length=255)
# #     disabled = models.BooleanField()
# #     domainuri = models.CharField(max_length=255, blank=True, null=True)
# #     organisationuri = models.CharField(max_length=255, blank=True, null=True)
# #     valueconstraint = models.CharField(max_length=2048, blank=True, null=True)
# #     valueconstrainttype = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tagdefinition'


# # class TagdefinitionAdminType(models.Model):
# #     tagdefinition_predicateuri = models.ForeignKey(Tagdefinition, models.DO_NOTHING, db_column='tagdefinition_predicateuri', primary_key=True)
# #     visibleto_admin_type = models.ForeignKey(AdminType, models.DO_NOTHING, unique=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tagdefinition_admin_type'
# #         unique_together = (('tagdefinition_predicateuri', 'visibleto_admin_type'),)


# # class Telephone(models.Model):
# #     telephone_id = models.BigIntegerField(primary_key=True)
# #     memeber_id = models.BigIntegerField()
# #     type_id = models.IntegerField()
# #     code = models.CharField(max_length=10, blank=True, null=True)
# #     number = models.CharField(max_length=20)
# #     member_id = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'telephone'


# # class Tempo(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     hotelname = models.CharField(max_length=100, blank=True, null=True)
# #     address = models.CharField(max_length=255, blank=True, null=True)
# #     city = models.CharField(max_length=100, blank=True, null=True)
# #     province = models.CharField(max_length=100, blank=True, null=True)
# #     latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
# #     longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
# #     uri = models.CharField(max_length=256, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tempo'


# # class Tempprotea(models.Model):
# #     hotelname = models.CharField(max_length=255)
# #     code = models.CharField(max_length=30)

# #     class Meta:
# #         managed = False
# #         db_table = 'tempprotea'


# # class Temptable(models.Model):
# #     col1 = models.CharField(max_length=50, blank=True, null=True)
# #     col2 = models.CharField(max_length=50, blank=True, null=True)
# #     col3 = models.CharField(max_length=50, blank=True, null=True)
# #     col4 = models.CharField(max_length=50, blank=True, null=True)
# #     col5 = models.CharField(max_length=50, blank=True, null=True)
# #     col6 = models.CharField(max_length=50, blank=True, null=True)
# #     col7 = models.CharField(max_length=50, blank=True, null=True)
# #     col8 = models.CharField(max_length=50, blank=True, null=True)
# #     col9 = models.CharField(max_length=50, blank=True, null=True)
# #     col10 = models.CharField(max_length=50, blank=True, null=True)
# #     col11 = models.CharField(max_length=50, blank=True, null=True)
# #     col12 = models.CharField(max_length=50, blank=True, null=True)
# #     col13 = models.CharField(max_length=50, blank=True, null=True)
# #     col14 = models.CharField(max_length=80, blank=True, null=True)
# #     col15 = models.CharField(max_length=80, blank=True, null=True)
# #     col16 = models.CharField(max_length=80, blank=True, null=True)
# #     col17 = models.CharField(max_length=80, blank=True, null=True)
# #     col18 = models.CharField(max_length=80, blank=True, null=True)
# #     col19 = models.CharField(max_length=80, blank=True, null=True)
# #     col20 = models.CharField(max_length=80, blank=True, null=True)
# #     col21 = models.CharField(max_length=80, blank=True, null=True)
# #     col22 = models.CharField(max_length=80, blank=True, null=True)
# #     col23 = models.CharField(max_length=80, blank=True, null=True)
# #     col24 = models.CharField(max_length=80, blank=True, null=True)
# #     col25 = models.CharField(max_length=80, blank=True, null=True)
# #     col26 = models.CharField(max_length=80, blank=True, null=True)
# #     col27 = models.CharField(max_length=80, blank=True, null=True)
# #     col28 = models.CharField(max_length=80, blank=True, null=True)
# #     col29 = models.CharField(max_length=80, blank=True, null=True)
# #     col30 = models.CharField(max_length=80, blank=True, null=True)
# #     col31 = models.CharField(max_length=80, blank=True, null=True)
# #     col32 = models.CharField(max_length=80, blank=True, null=True)
# #     col33 = models.CharField(max_length=80, blank=True, null=True)
# #     col34 = models.CharField(max_length=80, blank=True, null=True)
# #     col35 = models.CharField(max_length=80, blank=True, null=True)
# #     col36 = models.CharField(max_length=80, blank=True, null=True)
# #     col37 = models.CharField(max_length=80, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'temptable'


# # class Timers(models.Model):
# #     timerid = models.CharField(primary_key=True, max_length=80)
# #     targetid = models.CharField(max_length=250)
# #     initialdate = models.DateTimeField()
# #     timerinterval = models.BigIntegerField(blank=True, null=True)
# #     instancepk = models.BinaryField(blank=True, null=True)
# #     info = models.BinaryField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'timers'
# #         unique_together = (('timerid', 'targetid'),)


# # class Title(models.Model):
# #     title_id = models.IntegerField(primary_key=True)
# #     title_name = models.CharField(max_length=30, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'title'


# # class Tlevent(models.Model):
# #     eventid = models.AutoField(primary_key=True)
# #     message = models.CharField(max_length=3000, blank=True, null=True)
# #     timestamp = models.CharField(max_length=255, blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     eventtypeid = models.CharField(max_length=255, blank=True, null=True)
# #     xmlsent = models.TextField(blank=True, null=True)
# #     xmlreceived = models.TextField(blank=True, null=True)
# #     memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid', blank=True, null=True)
# #     occurred_at = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tlevent'


# # class Tleventtype(models.Model):
# #     eventtypeid = models.CharField(primary_key=True, max_length=20)
# #     description = models.CharField(max_length=150, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tleventtype'


# # class Tmpompstaffcode(models.Model):
# #     member_id = models.BigIntegerField()
# #     staff_code = models.CharField(max_length=200, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tmpompstaffcode'


# # class Tmppaymentrefs(models.Model):
# #     flightgrpid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tmppaymentrefs'


# # class Tmpprofiledisableomp(models.Model):
# #     member_id = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'tmpprofiledisableomp'


# # class Tmpremoveflights(models.Model):
# #     flightgrpid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tmpremoveflights'


# # class Tradertrespcodes(models.Model):
# #     code = models.IntegerField(primary_key=True)
# #     description = models.CharField(max_length=50)

# #     class Meta:
# #         managed = False
# #         db_table = 'tradertrespcodes'


# # class Transactiontype(models.Model):
# #     transactiontypeid = models.BigIntegerField(primary_key=True)
# #     description = models.CharField(max_length=20, blank=True, null=True)
# #     escription = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'transactiontype'


# # class Travelagency(models.Model):
# #     agencyid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.ForeignKey(Merchants, models.DO_NOTHING, db_column='merchantid')
# #     iatanumber = models.CharField(max_length=100, blank=True, null=True)
# #     agencytype = models.ForeignKey(Agencytype, models.DO_NOTHING, db_column='agencytype', blank=True, null=True)
# #     iscreatepnr = models.IntegerField(blank=True, null=True)
# #     iscreatepassive = models.IntegerField(blank=True, null=True)
# #     iscreatetriponpnrfail = models.IntegerField(blank=True, null=True)
# #     accessflightsmodule = models.BooleanField(blank=True, null=True)
# #     agencyname = models.CharField(max_length=255, blank=True, null=True)
# #     agencypcc = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travelagency'


# # class Travelagencybranch(models.Model):
# #     branchid = models.BigIntegerField(primary_key=True)
# #     branchname = models.CharField(max_length=70)
# #     agencyid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'travelagencybranch'


# # class Travelagent(models.Model):
# #     agentid = models.BigIntegerField(primary_key=True)
# #     travelagencyid = models.ForeignKey(Travelagency, models.DO_NOTHING, db_column='travelagencyid')
# #     memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid')
# #     branchid = models.BigIntegerField(blank=True, null=True)
# #     accessflightsmodule = models.BooleanField(blank=True, null=True)
# #     agentdefaultcompany = models.BigIntegerField(blank=True, null=True)
# #     bot = models.BooleanField(blank=True, null=True)
# #     salesmannumber = models.CharField(max_length=4, blank=True, null=True)
# #     agentidsabre = models.CharField(max_length=255, blank=True, null=True)
# #     consultantcode = models.CharField(max_length=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travelagent'


# # class Travellercalendarinfo(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     calendarguid = models.CharField(max_length=255, blank=True, null=True)
# #     person_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='person_personid', blank=True, null=True)
# #     disabled = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travellercalendarinfo'


# # class Travellerflightpreference(models.Model):
# #     travellerflightpreferenceid = models.AutoField(primary_key=True)
# #     flighttype = models.CharField(max_length=255, blank=True, null=True)
# #     mealid = models.ForeignKey(Suppliermeals, models.DO_NOTHING, db_column='mealid', blank=True, null=True)
# #     seatconfigurationid = models.ForeignKey(Seatconfiguration, models.DO_NOTHING, db_column='seatconfigurationid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travellerflightpreference'


# # class Travelleridentityassertion(models.Model):
# #     id = models.ForeignKey(Assertion, models.DO_NOTHING, db_column='id', primary_key=True)
# #     match = models.CharField(max_length=255, blank=True, null=True)
# #     travelleruri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travelleridentityassertion'


# # class Travellerloyaltyprogram(models.Model):
# #     travellerloyaltyprogramid = models.AutoField(primary_key=True)
# #     programnumber = models.CharField(max_length=255, blank=True, null=True)
# #     loyaltyprogramid = models.ForeignKey(Loyaltyprogram, models.DO_NOTHING, db_column='loyaltyprogramid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travellerloyaltyprogram'


# # class Travellerprofile(models.Model):
# #     travellerprofileid = models.BigIntegerField(primary_key=True)
# #     memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid')
# #     preferredmeal = models.CharField(max_length=30)
# #     preferredseat = models.CharField(max_length=20)
# #     flighttype = models.CharField(max_length=20)
# #     seatconfigurationid = models.ForeignKey(Seatconfiguration, models.DO_NOTHING, db_column='seatconfigurationid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travellerprofile'


# # class Travellerprofilelinkage(models.Model):
# #     travellerprofilelinkageid = models.BigIntegerField(primary_key=True)
# #     memberid = models.ForeignKey('Members', models.DO_NOTHING, db_column='memberid')
# #     ftncode = models.CharField(max_length=10)
# #     ftnnumber = models.CharField(max_length=50)
# #     travellerprofileid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'travellerprofilelinkage'


# # class Travelreservation(models.Model):
# #     travresid = models.BigIntegerField(primary_key=True)
# #     pnr = models.CharField(max_length=50, blank=True, null=True)
# #     bookingengineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='bookingengineid')
# #     created = models.DateTimeField()
# #     bookingchannel = models.ForeignKey(Bookingchannel, models.DO_NOTHING, db_column='bookingchannel', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'travelreservation'


# # class Travelsupplier(models.Model):
# #     travelsupplierid = models.BigIntegerField(primary_key=True)
# #     merchantid = models.BigIntegerField()
# #     suppliertypeid = models.IntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'travelsupplier'
# #         unique_together = (('travelsupplierid', 'merchantid'),)


# # class Trip(models.Model):
# #     trip_id = models.BigIntegerField(primary_key=True)
# #     start_date = models.DateTimeField(blank=True, null=True)
# #     end_date = models.DateTimeField(blank=True, null=True)
# #     travel_order_num = models.CharField(max_length=50, blank=True, null=True)
# #     created = models.DateTimeField()
# #     employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
# #     manager = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
# #     company = models.ForeignKey(Merchants, models.DO_NOTHING, blank=True, null=True)
# #     trip_reason = models.CharField(max_length=800, blank=True, null=True)
# #     trip_info = models.CharField(max_length=800, blank=True, null=True)
# #     trip_instructions = models.CharField(max_length=800, blank=True, null=True)
# #     booker = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
# #     agency = models.ForeignKey(Travelagency, models.DO_NOTHING, blank=True, null=True)
# #     agent = models.ForeignKey(Travelagent, models.DO_NOTHING, blank=True, null=True)
# #     xmlpacketid = models.BigIntegerField(blank=True, null=True)
# #     itinid = models.BigIntegerField(blank=True, null=True)
# #     status = models.ForeignKey('Tripstatus', models.DO_NOTHING, db_column='status', blank=True, null=True)
# #     reqcreationdate = models.DateTimeField(blank=True, null=True)
# #     triptravresid = models.BigIntegerField(blank=True, null=True)
# #     start_date_formatted = models.CharField(max_length=255, blank=True, null=True)
# #     end_date_formatted = models.CharField(max_length=255, blank=True, null=True)
# #     workstatusid = models.ForeignKey('Workstatus', models.DO_NOTHING, db_column='workstatusid', blank=True, null=True)
# #     eventtypes = models.CharField(max_length=255, blank=True, null=True)
# #     itemid = models.ForeignKey(Item, models.DO_NOTHING, db_column='itemid', blank=True, null=True)
# #     recoverablecost = models.BooleanField(blank=True, null=True)
# #     approvalreference = models.CharField(max_length=255, blank=True, null=True)
# #     projectnumber = models.CharField(max_length=255, blank=True, null=True)
# #     requestlastmodified = models.DateTimeField(blank=True, null=True)
# #     requester_personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='requester_personid', blank=True, null=True)
# #     requestername = models.CharField(max_length=255, blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     boundtorequirements = models.BooleanField(blank=True, null=True)
# #     crossborder = models.BooleanField(blank=True, null=True)
# #     lastassigneddate = models.DateTimeField(blank=True, null=True)
# #     lastcompleteddate = models.DateTimeField(blank=True, null=True)
# #     slaexpiry = models.DateTimeField(blank=True, null=True)
# #     purchaseorder = models.CharField(max_length=255, blank=True, null=True)
# #     corporatemerchant = models.ForeignKey(Corporatemerchant, models.DO_NOTHING, blank=True, null=True)
# #     account_number = models.CharField(max_length=50, blank=True, null=True)
# #     objective = models.CharField(max_length=50, blank=True, null=True)
# #     requisition_form_trip = models.BooleanField(blank=True, null=True)
# #     responsibility = models.CharField(max_length=50, blank=True, null=True)
# #     flightchangerequired = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'trip'
# #         unique_together = (('trip_id', 'created'),)


# # class TripApproverSnapshot(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     employeruri = models.CharField(max_length=255, blank=True, null=True)
# #     firstname = models.CharField(max_length=255, blank=True, null=True)
# #     lastname = models.CharField(max_length=255, blank=True, null=True)
# #     staffcode = models.CharField(max_length=255, blank=True, null=True)
# #     member_member = models.ForeignKey('Members', models.DO_NOTHING, blank=True, null=True)
# #     trip = models.ForeignKey(Trip, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'trip_approver_snapshot'


# # class Tripcollision(models.Model):
# #     tripcollisionid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     errorid = models.BigIntegerField()
# #     tripcollsionid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripcollision'


# # class Tripcollisionmap(models.Model):
# #     tripid = models.BigIntegerField(primary_key=True)
# #     tripcollisionid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'tripcollisionmap'
# #         unique_together = (('tripid', 'tripcollisionid'),)


# # class Tripcostlimit(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     lastupdatedat = models.DateTimeField(blank=True, null=True)
# #     trip_trip = models.ForeignKey(Trip, models.DO_NOTHING, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripcostlimit'


# # class Tripfee(models.Model):
# #     tripfeeid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     tripfeetype = models.ForeignKey('Tripfeetype', models.DO_NOTHING, db_column='tripfeetype', blank=True, null=True)
# #     feeamount = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     feeamountvat = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripfee'


# # class Tripfeequote(models.Model):
# #     tripfeequoteid = models.BigIntegerField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     feeamount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     feeamountvat = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     tripfeetype = models.ForeignKey('Tripfeetype', models.DO_NOTHING, db_column='tripfeetype', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripfeequote'


# # class Tripfeetype(models.Model):
# #     tripfeetypeid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=250, blank=True, null=True)
# #     description = models.CharField(max_length=250, blank=True, null=True)
# #     merchant_id = models.BigIntegerField(blank=True, null=True)
# #     amount = models.FloatField(blank=True, null=True)
# #     deleted = models.BooleanField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripfeetype'


# # class Tripglcode(models.Model):
# #     tripglcodeid = models.BigIntegerField(primary_key=True)
# #     amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     amountvat = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     glcodetypeid = models.ForeignKey(Glcodetype, models.DO_NOTHING, db_column='glcodetypeid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripglcode'


# # class Tripitinerarydestinationsubscription(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     created = models.DateTimeField(blank=True, null=True)
# #     itinerarydestination = models.CharField(max_length=255, blank=True, null=True)
# #     lastupdated = models.DateTimeField(blank=True, null=True)
# #     trip_id = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'tripitinerarydestinationsubscription'


# # class Triplob(models.Model):
# #     triplobid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     lobid = models.BigIntegerField()

# #     class Meta:
# #         managed = False
# #         db_table = 'triplob'


# # class Tripnotes(models.Model):
# #     noteid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField()
# #     note = models.CharField(max_length=1000, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripnotes'


# # class Triprequirements(models.Model):
# #     uri = models.CharField(primary_key=True, max_length=255)
# #     corporatetravelrequest = models.BinaryField(blank=True, null=True)
# #     quoteresponseuri = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'triprequirements'


# # class Triprequirementsmapping(models.Model):
# #     tripid = models.BigIntegerField(primary_key=True)
# #     corporatetravelrequesturi = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'triprequirementsmapping'


# # class Tripservicefees(models.Model):
# #     merchantid = models.BigIntegerField(primary_key=True)
# #     domesticservicefee = models.DecimalField(max_digits=12, decimal_places=2)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripservicefees'


# # class Tripstatus(models.Model):
# #     statusid = models.IntegerField(primary_key=True)
# #     name = models.CharField(max_length=50, blank=True, null=True)
# #     description = models.CharField(max_length=50, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'tripstatus'


# # class Triptravellermap(models.Model):
# #     triptravid = models.BigIntegerField(primary_key=True)
# #     tripid = models.BigIntegerField(blank=True, null=True)
# #     employeeid = models.BigIntegerField(blank=True, null=True)
# #     primarytraveller = models.BooleanField(blank=True, null=True)
# #     type = models.CharField(max_length=1, blank=True, null=True)
# #     personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='personid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'triptravellermap'


# # class Triptravellermapaccomodationlink(models.Model):
# #     triptravid = models.BigIntegerField(primary_key=True)
# #     bookingid = models.BigIntegerField()
# #     travelerfare = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
# #     travellerfare = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'triptravellermapaccomodationlink'
# #         unique_together = (('triptravid', 'bookingid'),)


# # class Vehicle(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     color = models.CharField(max_length=255, blank=True, null=True)
# #     manufacturer = models.CharField(max_length=255, blank=True, null=True)
# #     modelname = models.CharField(max_length=255, blank=True, null=True)
# #     licenseregistration_registrationid = models.ForeignKey('Vehiclelicenseregistration', models.DO_NOTHING, db_column='licenseregistration_registrationid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'vehicle'


# # class Vehiclehiresupplieridentifier(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     createat = models.DateTimeField(blank=True, null=True)
# #     suppliercode = models.CharField(max_length=255, blank=True, null=True)
# #     bookingengineid = models.ForeignKey(Bookingengine, models.DO_NOTHING, db_column='bookingengineid', blank=True, null=True)
# #     vehiclehiredepotid = models.ForeignKey(Avislocation, models.DO_NOTHING, db_column='vehiclehiredepotid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'vehiclehiresupplieridentifier'


# # class Vehiclelicenseregistration(models.Model):
# #     registrationid = models.BigIntegerField(primary_key=True)
# #     licensingauthority = models.CharField(max_length=255, blank=True, null=True)
# #     vehicleregistration = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'vehiclelicenseregistration'


# # class Viptraveller(models.Model):
# #     vipid = models.BigIntegerField(primary_key=True)
# #     reason = models.CharField(max_length=255, blank=True, null=True)
# #     actionedperson = models.BigIntegerField(blank=True, null=True)
# #     vipstatus = models.BooleanField()
# #     actioneddate = models.DateTimeField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'viptraveller'


# # class Virtualcard(models.Model):
# #     id = models.BigAutoField(primary_key=True)
# #     carddetailid = models.ForeignKey(Carddetail, models.DO_NOTHING, db_column='carddetailid', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'virtualcard'


# # class Visa(models.Model):
# #     id = models.BigIntegerField(primary_key=True)
# #     expirydate = models.CharField(max_length=255, blank=True, null=True)
# #     visanumber = models.CharField(max_length=255, blank=True, null=True)
# #     visacountrycode = models.ForeignKey(Country, models.DO_NOTHING, db_column='visacountrycode', blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'visa'


# # class Voucherdetails(models.Model):
# #     merchantid = models.BigIntegerField(primary_key=True)
# #     city = models.CharField(max_length=255, blank=True, null=True)
# #     email = models.CharField(max_length=255, blank=True, null=True)
# #     specialinstructions = models.CharField(max_length=255, blank=True, null=True)
# #     vatnumber = models.CharField(max_length=255, blank=True, null=True)
# #     faxnumber = models.CharField(max_length=255, blank=True, null=True)
# #     address1 = models.CharField(max_length=255, blank=True, null=True)
# #     address2 = models.CharField(max_length=255, blank=True, null=True)
# #     telephone = models.CharField(max_length=255, blank=True, null=True)
# #     invoicedetails = models.CharField(max_length=255, blank=True, null=True)
# #     invoiceemail = models.CharField(max_length=255, blank=True, null=True)
# #     invoicefax = models.CharField(max_length=255, blank=True, null=True)
# #     invoicepostaldetails = models.CharField(max_length=255, blank=True, null=True)
# #     invoiceaddress = models.CharField(max_length=255, blank=True, null=True)
# #     afterhourscompany = models.CharField(max_length=255, blank=True, null=True)
# #     afterhoursemail = models.CharField(max_length=255, blank=True, null=True)
# #     afterhourstelephone = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'voucherdetails'


# # class Waittimeout(models.Model):
# #     guid = models.BigIntegerField(primary_key=True)
# #     waittype = models.CharField(max_length=255, blank=True, null=True)
# #     waittimeout = models.CharField(max_length=255, blank=True, null=True)
# #     group_guid = models.BigIntegerField(blank=True, null=True)
# #     approver_guid = models.BigIntegerField(blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'waittimeout'


# # class Workstatus(models.Model):
# #     workstatusid = models.BigIntegerField(primary_key=True)
# #     action = models.CharField(max_length=255, blank=True, null=True)
# #     workstatusactionname = models.CharField(max_length=255, blank=True, null=True)
# #     urlworkstatusaction = models.CharField(max_length=255, blank=True, null=True)

# #     class Meta:
# #         managed = False
# #         db_table = 'workstatus'


# # class Xmlpacket(models.Model):
# #     xmlpacketid = models.BigIntegerField(primary_key=True)
# #     timestamp = models.DateTimeField()
# #     xmlpacketdata = models.CharField(max_length=3000)

# #     class Meta:
# #         managed = False
# #         db_table = 'xmlpacket'
