# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    group = models.ForeignKey('AccountGroup', models.DO_NOTHING, blank=True, null=True)
    root_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    code = models.CharField(max_length=64)
    account_type = models.CharField(max_length=-1)
    internal_group = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    deprecated = models.BooleanField(blank=True, null=True)
    include_initial_balance = models.BooleanField(blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    is_off_balance = models.BooleanField(blank=True, null=True)
    non_trade = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'
        unique_together = (('code', 'company'),)


class AccountAccountAccountJournalRel(models.Model):
    account_account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey('AccountJournal', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_journal_rel'
        unique_together = (('account_account', 'account_journal'),)


class AccountAccountAccountTag(models.Model):
    account_account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey('AccountAccountTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_account_tag'
        unique_together = (('account_account', 'account_account_tag'),)


class AccountAccountTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    applicability = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    tax_negate = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_tag'


class AccountAccountTagAccountMoveLineRel(models.Model):
    account_move_line = models.OneToOneField('AccountMoveLine', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_move_line_rel'
        unique_together = (('account_move_line', 'account_account_tag'),)


class AccountAccountTagAccountTaxRepartitionLineRel(models.Model):
    account_tax_repartition_line = models.OneToOneField('AccountTaxRepartitionLine', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_account_tax_repartition_line_rel'
        unique_together = (('account_tax_repartition_line', 'account_account_tag'),)


class AccountAccountTagProductTemplateRel(models.Model):
    product_template = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tag_product_template_rel'
        unique_together = (('product_template', 'account_account_tag'),)


class AccountAccountTaxDefaultRel(models.Model):
    account = models.OneToOneField(AccountAccount, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_tax_default_rel'
        unique_together = (('account', 'tax'),)


class AccountAccountTemplate(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey('AccountChartTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    code = models.CharField(max_length=64)
    account_type = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    reconcile = models.BooleanField(blank=True, null=True)
    nocreate = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account_template'


class AccountAccountTemplateAccountTag(models.Model):
    account_account_template = models.OneToOneField(AccountAccountTemplate, models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_account_tag'
        unique_together = (('account_account_template', 'account_account_tag'),)


class AccountAccountTemplateTaxRel(models.Model):
    account = models.OneToOneField(AccountAccountTemplate, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_account_template_tax_rel'
        unique_together = (('account', 'tax'),)


class AccountAccruedOrdersWizard(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date = models.DateField()
    reversal_date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_accrued_orders_wizard'


class AccountAnalyticAccount(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING)
    root_plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    code = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_account'


class AccountAnalyticApplicability(models.Model):
    analytic_plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    business_domain = models.CharField(max_length=-1)
    applicability = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    account_prefix = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_applicability'


class AccountAnalyticDistributionModel(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    analytic_distribution = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_categ = models.ForeignKey('ProductCategory', models.DO_NOTHING, blank=True, null=True)
    account_prefix = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_distribution_model'


class AccountAnalyticLine(models.Model):
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey('AccountAnalyticPlan', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    category = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    unit_amount = models.FloatField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    general_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING, blank=True, null=True)
    code = models.CharField(max_length=8, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    so_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, db_column='so_line', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_line'


class AccountAnalyticPlan(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    default_applicability = models.CharField(max_length=-1)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_analytic_plan'


class AccountAutomaticEntryWizard(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    action = models.CharField(max_length=-1)
    account_type = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard'


class AccountAutomaticEntryWizardAccountMoveLineRel(models.Model):
    account_automatic_entry_wizard = models.OneToOneField(AccountAutomaticEntryWizard, models.DO_NOTHING, primary_key=True)
    account_move_line = models.ForeignKey('AccountMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_automatic_entry_wizard_account_move_line_rel'
        unique_together = (('account_automatic_entry_wizard', 'account_move_line'),)


class AccountBankStatement(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey('AccountJournal', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    first_line_index = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    balance_start = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance_end_real = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_complete = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement'


class AccountBankStatementIrAttachmentRel(models.Model):
    account_bank_statement = models.OneToOneField(AccountBankStatement, models.DO_NOTHING, primary_key=True)
    ir_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_ir_attachment_rel'
        unique_together = (('account_bank_statement', 'ir_attachment'),)


class AccountBankStatementLine(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    foreign_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    account_number = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    payment_ref = models.CharField(max_length=-1, blank=True, null=True)
    internal_index = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_reconciled = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount_residual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_bank_statement_line'


class AccountCashRounding(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    strategy = models.CharField(max_length=-1)
    rounding_method = models.CharField(max_length=-1)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    rounding = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_cash_rounding'


class AccountChartTemplate(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    code_digits = models.IntegerField()
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    income_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_debit_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_credit_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    default_pos_receivable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_journal_early_pay_discount_loss_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    account_journal_early_pay_discount_gain_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_receivable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_payable = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_expense = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_account_income = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_tax_payable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_tax_receivable_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_advance_tax_payment_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    property_cash_basis_base_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    bank_account_code_prefix = models.CharField(max_length=-1)
    cash_account_code_prefix = models.CharField(max_length=-1)
    transfer_account_code_prefix = models.CharField(max_length=-1)
    visible = models.BooleanField(blank=True, null=True)
    use_anglo_saxon = models.BooleanField(blank=True, null=True)
    use_storno_accounting = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    spoken_languages = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_chart_template'


class AccountEdiDocument(models.Model):
    move = models.ForeignKey('AccountMove', models.DO_NOTHING)
    edi_format = models.ForeignKey('AccountEdiFormat', models.DO_NOTHING)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    blocking_level = models.CharField(max_length=-1, blank=True, null=True)
    error = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_document'
        unique_together = (('edi_format', 'move'),)


class AccountEdiFormat(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_edi_format'


class AccountEdiFormatAccountJournalRel(models.Model):
    account_journal = models.OneToOneField('AccountJournal', models.DO_NOTHING, primary_key=True)
    account_edi_format = models.ForeignKey(AccountEdiFormat, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_edi_format_account_journal_rel'
        unique_together = (('account_journal', 'account_edi_format'),)


class AccountFinancialYearOp(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_financial_year_op'


class AccountFiscalPosition(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    zip_from = models.CharField(max_length=-1, blank=True, null=True)
    zip_to = models.CharField(max_length=-1, blank=True, null=True)
    foreign_vat = models.CharField(max_length=-1, blank=True, null=True)
    note = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position'


class AccountFiscalPositionAccount(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    account_src = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account'
        unique_together = (('position', 'account_src', 'account_dest'),)


class AccountFiscalPositionAccountTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    account_src = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    account_dest = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_account_template'


class AccountFiscalPositionResCountryStateRel(models.Model):
    account_fiscal_position = models.OneToOneField(AccountFiscalPosition, models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_res_country_state_rel'
        unique_together = (('account_fiscal_position', 'res_country_state'),)


class AccountFiscalPositionTax(models.Model):
    position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    tax_src = models.ForeignKey('AccountTax', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax'
        unique_together = (('position', 'tax_src', 'tax_dest'),)


class AccountFiscalPositionTaxTemplate(models.Model):
    position = models.ForeignKey('AccountFiscalPositionTemplate', models.DO_NOTHING)
    tax_src = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)
    tax_dest = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_tax_template'


class AccountFiscalPositionTemplate(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    country_group = models.ForeignKey('ResCountryGroup', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    zip_from = models.CharField(max_length=-1, blank=True, null=True)
    zip_to = models.CharField(max_length=-1, blank=True, null=True)
    note = models.JSONField(blank=True, null=True)
    auto_apply = models.BooleanField(blank=True, null=True)
    vat_required = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template'


class AccountFiscalPositionTemplateResCountryStateRel(models.Model):
    account_fiscal_position_template = models.OneToOneField(AccountFiscalPositionTemplate, models.DO_NOTHING, primary_key=True)
    res_country_state = models.ForeignKey('ResCountryState', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_fiscal_position_template_res_country_state_rel'
        unique_together = (('account_fiscal_position_template', 'res_country_state'),)


class AccountFullReconcile(models.Model):
    exchange_move = models.ForeignKey('AccountMove', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_full_reconcile'


class AccountGroup(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    code_prefix_start = models.CharField(max_length=-1, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group'


class AccountGroupTemplate(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    code_prefix_start = models.CharField(max_length=-1, blank=True, null=True)
    code_prefix_end = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_group_template'


class AccountIncoterms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(max_length=3)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_incoterms'


class AccountInvoiceSend(models.Model):
    composer = models.ForeignKey('MailComposeMessage', models.DO_NOTHING)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    is_email = models.BooleanField(blank=True, null=True)
    is_print = models.BooleanField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    snailmail_is_letter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_invoice_send'


class AccountInvoiceTransactionRel(models.Model):
    invoice = models.OneToOneField('AccountMove', models.DO_NOTHING, primary_key=True)
    transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_invoice_transaction_rel'
        unique_together = (('invoice', 'transaction'),)


class AccountJournal(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    default_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    profit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    sale_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    sale_activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True)
    secure_sequence = models.ForeignKey('IrSequence', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    name = models.JSONField()
    code = models.CharField(max_length=5)
    type = models.CharField(max_length=-1)
    invoice_reference_type = models.CharField(max_length=-1)
    invoice_reference_model = models.CharField(max_length=-1)
    bank_statements_source = models.CharField(max_length=-1, blank=True, null=True)
    sequence_override_regex = models.TextField(blank=True, null=True)
    sale_activity_note = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    restrict_mode_hash_table = models.BooleanField(blank=True, null=True)
    refund_sequence = models.BooleanField(blank=True, null=True)
    payment_sequence = models.BooleanField(blank=True, null=True)
    show_on_dashboard = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal'
        unique_together = (('company', 'code'),)


class AccountJournalAccountJournalGroupRel(models.Model):
    account_journal_group = models.OneToOneField('AccountJournalGroup', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_journal_group_rel'
        unique_together = (('account_journal_group', 'account_journal'),)


class AccountJournalAccountReconcileModelRel(models.Model):
    account_reconcile_model = models.OneToOneField('AccountReconcileModel', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_rel'
        unique_together = (('account_reconcile_model', 'account_journal'),)


class AccountJournalAccountReconcileModelTemplateRel(models.Model):
    account_reconcile_model_template = models.OneToOneField('AccountReconcileModelTemplate', models.DO_NOTHING, primary_key=True)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_journal_account_reconcile_model_template_rel'
        unique_together = (('account_reconcile_model_template', 'account_journal'),)


class AccountJournalGroup(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_journal_group'
        unique_together = (('company', 'name'),)


class AccountMove(models.Model):
    sequence_number = models.IntegerField(blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_rec = models.ForeignKey('AccountPartialReconcile', models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_origin_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    auto_post_origin = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    secure_sequence_number = models.IntegerField(blank=True, null=True)
    invoice_payment_term = models.ForeignKey('AccountPaymentTerm', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    commercial_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner_shipping = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    reversed_entry = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    invoice_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    invoice_incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True)
    invoice_cash_rounding = models.ForeignKey(AccountCashRounding, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sequence_prefix = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1)
    move_type = models.CharField(max_length=-1)
    auto_post = models.CharField(max_length=-1)
    inalterable_hash = models.CharField(max_length=-1, blank=True, null=True)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    qr_code_method = models.CharField(max_length=-1, blank=True, null=True)
    payment_state = models.CharField(max_length=-1, blank=True, null=True)
    invoice_source_email = models.CharField(max_length=-1, blank=True, null=True)
    invoice_partner_display_name = models.CharField(max_length=-1, blank=True, null=True)
    invoice_origin = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    auto_post_until = models.DateField(blank=True, null=True)
    invoice_date = models.DateField(blank=True, null=True)
    invoice_date_due = models.DateField(blank=True, null=True)
    narration = models.TextField(blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total_in_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quick_edit_total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_storno = models.BooleanField(blank=True, null=True)
    always_tax_exigible = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    posted_before = models.BooleanField(blank=True, null=True)
    is_move_sent = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    edi_state = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_replace_invoice = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    l10n_id_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    l10n_id_tax_number = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_kode_transaksi = models.CharField(max_length=-1, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey('CrmTeam', models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move'
        unique_together = (('name', 'journal'),)


class AccountMoveAccountInvoiceSendRel(models.Model):
    account_invoice_send = models.OneToOneField(AccountInvoiceSend, models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_invoice_send_rel'
        unique_together = (('account_invoice_send', 'account_move'),)


class AccountMoveAccountResequenceWizardRel(models.Model):
    account_resequence_wizard = models.OneToOneField('AccountResequenceWizard', models.DO_NOTHING, primary_key=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_account_resequence_wizard_rel'
        unique_together = (('account_resequence_wizard', 'account_move'),)


class AccountMoveLine(models.Model):
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    company_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    reconcile_model = models.ForeignKey('AccountReconcileModel', models.DO_NOTHING, blank=True, null=True)
    payment = models.ForeignKey('AccountPayment', models.DO_NOTHING, blank=True, null=True)
    statement_line = models.ForeignKey(AccountBankStatementLine, models.DO_NOTHING, blank=True, null=True)
    statement = models.ForeignKey(AccountBankStatement, models.DO_NOTHING, blank=True, null=True)
    group_tax = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    tax_line = models.ForeignKey('AccountTax', models.DO_NOTHING, blank=True, null=True)
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING, blank=True, null=True)
    tax_repartition_line = models.ForeignKey('AccountTaxRepartitionLine', models.DO_NOTHING, blank=True, null=True)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    account_root_id = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move_name = models.CharField(max_length=-1, blank=True, null=True)
    parent_state = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    tax_audit = models.CharField(max_length=-1, blank=True, null=True)
    matching_number = models.CharField(max_length=-1, blank=True, null=True)
    display_type = models.CharField(max_length=-1)
    date = models.DateField(blank=True, null=True)
    date_maturity = models.DateField(blank=True, null=True)
    discount_date = models.DateField(blank=True, null=True)
    analytic_distribution = models.JSONField(blank=True, null=True)
    debit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_base_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    discount_balance = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    tax_tag_invert = models.BooleanField(blank=True, null=True)
    reconciled = models.BooleanField(blank=True, null=True)
    blocked = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    discount_percentage = models.FloatField(blank=True, null=True)
    expense = models.ForeignKey('HrExpense', models.DO_NOTHING, blank=True, null=True)
    is_downpayment = models.BooleanField(blank=True, null=True)
    vehicle = models.ForeignKey('FleetVehicle', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_line'


class AccountMoveLineAccountTaxRel(models.Model):
    account_move_line = models.OneToOneField(AccountMoveLine, models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_line_account_tax_rel'
        unique_together = (('account_move_line', 'account_tax'),)


class AccountMoveReversal(models.Model):
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date_mode = models.CharField(max_length=-1)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    refund_method = models.CharField(max_length=-1)
    date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_move_reversal'


class AccountMoveReversalMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, models.DO_NOTHING, primary_key=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_move'
        unique_together = (('reversal', 'move'),)


class AccountMoveReversalNewMove(models.Model):
    reversal = models.OneToOneField(AccountMoveReversal, models.DO_NOTHING, primary_key=True)
    new_move = models.ForeignKey(AccountMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_move_reversal_new_move'
        unique_together = (('reversal', 'new_move'),)


class AccountPartialReconcile(models.Model):
    debit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    credit_move = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)
    full_reconcile = models.ForeignKey(AccountFullReconcile, models.DO_NOTHING, blank=True, null=True)
    exchange_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    debit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    credit_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    max_date = models.DateField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    debit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    credit_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_partial_reconcile'


class AccountPayment(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(AccountMove, models.DO_NOTHING)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    paired_internal_transfer_payment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    payment_method_line = models.ForeignKey('AccountPaymentMethodLine', models.DO_NOTHING, blank=True, null=True)
    payment_method = models.ForeignKey('AccountPaymentMethod', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    outstanding_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    destination_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    destination_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    payment_type = models.CharField(max_length=-1)
    partner_type = models.CharField(max_length=-1)
    payment_reference = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_company_currency_signed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_reconciled = models.BooleanField(blank=True, null=True)
    is_matched = models.BooleanField(blank=True, null=True)
    is_internal_transfer = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_transaction = models.ForeignKey('PaymentTransaction', models.DO_NOTHING, blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)
    source_payment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment'


class AccountPaymentAccountBankStatementLineRel(models.Model):
    account_bank_statement_line = models.OneToOneField(AccountBankStatementLine, models.DO_NOTHING, primary_key=True)
    account_payment = models.ForeignKey(AccountPayment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_account_bank_statement_line_rel'
        unique_together = (('account_bank_statement_line', 'account_payment'),)


class AccountPaymentMethod(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(max_length=-1)
    payment_type = models.CharField(max_length=-1)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method'
        unique_together = (('code', 'payment_type'),)


class AccountPaymentMethodLine(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    payment_method = models.ForeignKey(AccountPaymentMethod, models.DO_NOTHING)
    payment_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_provider = models.ForeignKey('PaymentProvider', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_method_line'


class AccountPaymentRegister(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    source_currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    payment_method_line = models.ForeignKey(AccountPaymentMethodLine, models.DO_NOTHING, blank=True, null=True)
    writeoff_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    communication = models.CharField(max_length=-1, blank=True, null=True)
    payment_type = models.CharField(max_length=-1, blank=True, null=True)
    partner_type = models.CharField(max_length=-1, blank=True, null=True)
    payment_difference_handling = models.CharField(max_length=-1, blank=True, null=True)
    writeoff_label = models.CharField(max_length=-1, blank=True, null=True)
    payment_date = models.DateField()
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    source_amount_currency = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    group_payment = models.BooleanField(blank=True, null=True)
    can_edit_wizard = models.BooleanField(blank=True, null=True)
    can_group_payments = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment_token = models.ForeignKey('PaymentToken', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_register'


class AccountPaymentRegisterMoveLineRel(models.Model):
    wizard = models.OneToOneField(AccountPaymentRegister, models.DO_NOTHING, primary_key=True)
    line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_payment_register_move_line_rel'
        unique_together = (('wizard', 'line'),)


class AccountPaymentTerm(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    note = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    display_on_invoice = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term'


class AccountPaymentTermLine(models.Model):
    months = models.IntegerField()
    days = models.IntegerField()
    days_after = models.IntegerField(blank=True, null=True)
    discount_days = models.IntegerField(blank=True, null=True)
    payment = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1)
    value_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    end_month = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    discount_percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_payment_term_line'


class AccountReconcileModel(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    past_months_limit = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    rule_type = models.CharField(max_length=-1)
    matching_order = models.CharField(max_length=-1)
    match_nature = models.CharField(max_length=-1)
    match_amount = models.CharField(max_length=-1, blank=True, null=True)
    match_label = models.CharField(max_length=-1, blank=True, null=True)
    match_label_param = models.CharField(max_length=-1, blank=True, null=True)
    match_note = models.CharField(max_length=-1, blank=True, null=True)
    match_note_param = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=-1, blank=True, null=True)
    payment_tolerance_type = models.CharField(max_length=-1)
    decimal_separator = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    allow_payment_tolerance = models.BooleanField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    payment_tolerance_param = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model'
        unique_together = (('name', 'company'),)


class AccountReconcileModelLine(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    amount_string = models.CharField(max_length=-1)
    analytic_distribution = models.JSONField(blank=True, null=True)
    force_tax_included = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line'


class AccountReconcileModelLineAccountTaxRel(models.Model):
    account_reconcile_model_line = models.OneToOneField(AccountReconcileModelLine, models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey('AccountTax', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_account_tax_rel'
        unique_together = (('account_reconcile_model_line', 'account_tax'),)


class AccountReconcileModelLineTemplate(models.Model):
    model = models.ForeignKey('AccountReconcileModelTemplate', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    amount_string = models.CharField(max_length=-1, blank=True, null=True)
    force_tax_included = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template'


class AccountReconcileModelLineTemplateAccountTaxTemplateRel(models.Model):
    account_reconcile_model_line_template = models.OneToOneField(AccountReconcileModelLineTemplate, models.DO_NOTHING, primary_key=True)
    account_tax_template = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_line_template_account_tax_template_rel'
        unique_together = (('account_reconcile_model_line_template', 'account_tax_template'),)


class AccountReconcileModelPartnerMapping(models.Model):
    model = models.ForeignKey(AccountReconcileModel, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    payment_ref_regex = models.CharField(max_length=-1, blank=True, null=True)
    narration_regex = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_partner_mapping'


class AccountReconcileModelResPartnerCategoryRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_category_rel'
        unique_together = (('account_reconcile_model', 'res_partner_category'),)


class AccountReconcileModelResPartnerRel(models.Model):
    account_reconcile_model = models.OneToOneField(AccountReconcileModel, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_res_partner_rel'
        unique_together = (('account_reconcile_model', 'res_partner'),)


class AccountReconcileModelTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    rule_type = models.CharField(max_length=-1)
    matching_order = models.CharField(max_length=-1, blank=True, null=True)
    match_nature = models.CharField(max_length=-1)
    match_amount = models.CharField(max_length=-1, blank=True, null=True)
    match_label = models.CharField(max_length=-1, blank=True, null=True)
    match_label_param = models.CharField(max_length=-1, blank=True, null=True)
    match_note = models.CharField(max_length=-1, blank=True, null=True)
    match_note_param = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type = models.CharField(max_length=-1, blank=True, null=True)
    match_transaction_type_param = models.CharField(max_length=-1, blank=True, null=True)
    payment_tolerance_type = models.CharField(max_length=-1)
    decimal_separator = models.CharField(max_length=-1, blank=True, null=True)
    auto_reconcile = models.BooleanField(blank=True, null=True)
    to_check = models.BooleanField(blank=True, null=True)
    match_text_location_label = models.BooleanField(blank=True, null=True)
    match_text_location_note = models.BooleanField(blank=True, null=True)
    match_text_location_reference = models.BooleanField(blank=True, null=True)
    match_same_currency = models.BooleanField(blank=True, null=True)
    allow_payment_tolerance = models.BooleanField(blank=True, null=True)
    match_partner = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    match_amount_min = models.FloatField(blank=True, null=True)
    match_amount_max = models.FloatField(blank=True, null=True)
    payment_tolerance_param = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template'


class AccountReconcileModelTemplateResPartnerCategoryRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_category_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner_category'),)


class AccountReconcileModelTemplateResPartnerRel(models.Model):
    account_reconcile_model_template = models.OneToOneField(AccountReconcileModelTemplate, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_reconcile_model_template_res_partner_rel'
        unique_together = (('account_reconcile_model_template', 'res_partner'),)


class AccountReport(models.Model):
    root_report = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    load_more_limit = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    availability_condition = models.CharField(max_length=-1, blank=True, null=True)
    default_opening_date_filter = models.CharField(max_length=-1, blank=True, null=True)
    filter_multi_company = models.CharField(max_length=-1, blank=True, null=True)
    filter_hierarchy = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    only_tax_exigible = models.BooleanField(blank=True, null=True)
    search_bar = models.BooleanField(blank=True, null=True)
    filter_date_range = models.BooleanField(blank=True, null=True)
    filter_show_draft = models.BooleanField(blank=True, null=True)
    filter_unreconciled = models.BooleanField(blank=True, null=True)
    filter_unfold_all = models.BooleanField(blank=True, null=True)
    filter_period_comparison = models.BooleanField(blank=True, null=True)
    filter_growth_comparison = models.BooleanField(blank=True, null=True)
    filter_journals = models.BooleanField(blank=True, null=True)
    filter_analytic = models.BooleanField(blank=True, null=True)
    filter_account_type = models.BooleanField(blank=True, null=True)
    filter_partner = models.BooleanField(blank=True, null=True)
    filter_fiscal_position = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report'


class AccountReportColumn(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    report = models.ForeignKey(AccountReport, models.DO_NOTHING, blank=True, null=True)
    custom_audit_action = models.ForeignKey('IrActWindow', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    expression_label = models.CharField(max_length=-1)
    figure_type = models.CharField(max_length=-1)
    name = models.JSONField()
    sortable = models.BooleanField(blank=True, null=True)
    blank_if_zero = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report_column'


class AccountReportExpression(models.Model):
    report_line = models.ForeignKey('AccountReportLine', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    label = models.CharField(max_length=-1)
    engine = models.CharField(max_length=-1)
    formula = models.CharField(max_length=-1)
    subformula = models.CharField(max_length=-1, blank=True, null=True)
    date_scope = models.CharField(max_length=-1)
    figure_type = models.CharField(max_length=-1, blank=True, null=True)
    carryover_target = models.CharField(max_length=-1, blank=True, null=True)
    green_on_positive = models.BooleanField(blank=True, null=True)
    blank_if_zero = models.BooleanField(blank=True, null=True)
    auditable = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report_expression'


class AccountReportExternalValue(models.Model):
    target_report_expression = models.ForeignKey(AccountReportExpression, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    foreign_vat_fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    carryover_origin_report_line = models.ForeignKey('AccountReportLine', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    carryover_origin_expression_label = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_report_external_value'


class AccountReportLine(models.Model):
    report = models.ForeignKey(AccountReport, models.DO_NOTHING)
    hierarchy_level = models.IntegerField()
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    groupby = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    name = models.JSONField()
    foldable = models.BooleanField(blank=True, null=True)
    print_on_new_page = models.BooleanField(blank=True, null=True)
    hide_if_zero = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_report_line'


class AccountResequenceWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    first_name = models.CharField(max_length=-1)
    ordering = models.CharField(max_length=-1)
    first_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_resequence_wizard'


class AccountSetupBankManualConfig(models.Model):
    res_partner_bank = models.ForeignKey('ResPartnerBank', models.DO_NOTHING)
    num_journals_without_account = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    new_journal_name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_setup_bank_manual_config'


class AccountTax(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sequence = models.IntegerField()
    tax_group = models.ForeignKey('AccountTaxGroup', models.DO_NOTHING)
    cash_basis_transition_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    tax_scope = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    description = models.JSONField(blank=True, null=True)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    is_base_affected = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    real_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax'
        unique_together = (('name', 'company', 'type_tax_use', 'tax_scope'),)


class AccountTaxFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTax, models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTaxGroup(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    preceding_subtotal = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_group'


class AccountTaxHrExpenseSplitRel(models.Model):
    hr_expense_split = models.OneToOneField('HrExpenseSplit', models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_hr_expense_split_rel'
        unique_together = (('hr_expense_split', 'account_tax'),)


class AccountTaxRepTemplateMinus(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate', models.DO_NOTHING, primary_key=True)
    account_report_expression = models.ForeignKey(AccountReportExpression, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_rep_template_minus'
        unique_together = (('account_tax_repartition_line_template', 'account_report_expression'),)


class AccountTaxRepTemplatePlus(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate', models.DO_NOTHING, primary_key=True)
    account_report_expression = models.ForeignKey(AccountReportExpression, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_rep_template_plus'
        unique_together = (('account_tax_repartition_line_template', 'account_report_expression'),)


class AccountTaxRepartitionFinancialTags(models.Model):
    account_tax_repartition_line_template = models.OneToOneField('AccountTaxRepartitionLineTemplate', models.DO_NOTHING, primary_key=True)
    account_account_tag = models.ForeignKey(AccountAccountTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_financial_tags'
        unique_together = (('account_tax_repartition_line_template', 'account_account_tag'),)


class AccountTaxRepartitionLine(models.Model):
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    repartition_type = models.CharField(max_length=-1)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    factor_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line'


class AccountTaxRepartitionLineTemplate(models.Model):
    account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    invoice_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    refund_tax = models.ForeignKey('AccountTaxTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    repartition_type = models.CharField(max_length=-1)
    use_in_tax_closing = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    factor_percent = models.FloatField()

    class Meta:
        managed = False
        db_table = 'account_tax_repartition_line_template'


class AccountTaxSaleAdvancePaymentInvRel(models.Model):
    sale_advance_payment_inv = models.OneToOneField('SaleAdvancePaymentInv', models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_advance_payment_inv_rel'
        unique_together = (('sale_advance_payment_inv', 'account_tax'),)


class AccountTaxSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', models.DO_NOTHING, primary_key=True)
    account_tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tax_sale_order_line_rel'
        unique_together = (('sale_order_line', 'account_tax'),)


class AccountTaxTemplate(models.Model):
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING)
    sequence = models.IntegerField()
    tax_group = models.ForeignKey(AccountTaxGroup, models.DO_NOTHING, blank=True, null=True)
    cash_basis_transition_account = models.ForeignKey(AccountAccountTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    type_tax_use = models.CharField(max_length=-1)
    tax_scope = models.CharField(max_length=-1, blank=True, null=True)
    amount_type = models.CharField(max_length=-1)
    description = models.JSONField(blank=True, null=True)
    tax_exigibility = models.CharField(max_length=-1, blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    price_include = models.BooleanField(blank=True, null=True)
    include_base_amount = models.BooleanField(blank=True, null=True)
    is_base_affected = models.BooleanField(blank=True, null=True)
    analytic = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tax_template'
        unique_together = (('name', 'type_tax_use', 'tax_scope', 'chart_template'),)


class AccountTaxTemplateFiliationRel(models.Model):
    parent_tax = models.OneToOneField(AccountTaxTemplate, models.DO_NOTHING, db_column='parent_tax', primary_key=True)
    child_tax = models.ForeignKey(AccountTaxTemplate, models.DO_NOTHING, db_column='child_tax')

    class Meta:
        managed = False
        db_table = 'account_tax_template_filiation_rel'
        unique_together = (('parent_tax', 'child_tax'),)


class AccountTourUploadBill(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    selection = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill'


class AccountTourUploadBillEmailConfirm(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_alias = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill_email_confirm'


class AccountTourUploadBillIrAttachmentsRel(models.Model):
    account_tour_upload_bill = models.OneToOneField(AccountTourUploadBill, models.DO_NOTHING, primary_key=True)
    ir_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_tour_upload_bill_ir_attachments_rel'
        unique_together = (('account_tour_upload_bill', 'ir_attachment'),)


class AccountUnreconcile(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_unreconcile'


class ApplicantGetRefuseReason(models.Model):
    refuse_reason = models.ForeignKey('HrApplicantRefuseReason', models.DO_NOTHING)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_get_refuse_reason'


class ApplicantGetRefuseReasonHrApplicantRel(models.Model):
    applicant_get_refuse_reason = models.OneToOneField(ApplicantGetRefuseReason, models.DO_NOTHING, primary_key=True)
    hr_applicant = models.ForeignKey('HrApplicant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'applicant_get_refuse_reason_hr_applicant_rel'
        unique_together = (('applicant_get_refuse_reason', 'hr_applicant'),)


class ApplicantSendMail(models.Model):
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'applicant_send_mail'


class ApplicantSendMailHrApplicantRel(models.Model):
    applicant_send_mail = models.OneToOneField(ApplicantSendMail, models.DO_NOTHING, primary_key=True)
    hr_applicant = models.ForeignKey('HrApplicant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'applicant_send_mail_hr_applicant_rel'
        unique_together = (('applicant_send_mail', 'hr_applicant'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthTotpDevice(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    scope = models.CharField(max_length=-1, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_device'


class AuthTotpWizard(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    secret = models.CharField(max_length=-1)
    url = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(max_length=7, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    qrcode = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_totp_wizard'


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BadgeUnlockedDefinitionRel(models.Model):
    gamification_badge = models.OneToOneField('GamificationBadge', models.DO_NOTHING, primary_key=True)
    gamification_goal_definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'badge_unlocked_definition_rel'
        unique_together = (('gamification_badge', 'gamification_goal_definition'),)


class BarcodeNomenclature(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=32)
    upc_ean_conv = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    gs1_separator_fnc1 = models.CharField(max_length=-1, blank=True, null=True)
    is_gs1_nomenclature = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_nomenclature'


class BarcodeRule(models.Model):
    barcode_nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=32)
    encoding = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    pattern = models.CharField(max_length=-1)
    alias = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    associated_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    gs1_content_type = models.CharField(max_length=-1, blank=True, null=True)
    gs1_decimal_usage = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'barcode_rule'


class BaseDocumentLayout(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    report_layout = models.ForeignKey('ReportLayout', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_document_layout'


class BaseEnableProfilingWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    duration = models.CharField(max_length=-1, blank=True, null=True)
    expiration = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_enable_profiling_wizard'


class BaseImportImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    file_name = models.CharField(max_length=-1, blank=True, null=True)
    file_type = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    file = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_import'


class BaseImportMapping(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    column_name = models.CharField(max_length=-1, blank=True, null=True)
    field_name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_mapping'


class BaseImportTestsModelsChar(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char'


class BaseImportTestsModelsCharNoreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_noreadonly'


class BaseImportTestsModelsCharReadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_readonly'


class BaseImportTestsModelsCharRequired(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_required'


class BaseImportTestsModelsCharStates(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_states'


class BaseImportTestsModelsCharStillreadonly(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_char_stillreadonly'


class BaseImportTestsModelsComplex(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    c = models.CharField(max_length=-1, blank=True, null=True)
    d = models.DateField(blank=True, null=True)
    m = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    dt = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    f = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_complex'


class BaseImportTestsModelsFloat(models.Model):
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value2 = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_float'


class BaseImportTestsModelsM2O(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORelated', models.DO_NOTHING, db_column='value', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o'


class BaseImportTestsModelsM2ORelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_related'


class BaseImportTestsModelsM2ORequired(models.Model):
    value = models.ForeignKey('BaseImportTestsModelsM2ORequiredRelated', models.DO_NOTHING, db_column='value')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required'


class BaseImportTestsModelsM2ORequiredRelated(models.Model):
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_m2o_required_related'


class BaseImportTestsModelsO2M(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m'


class BaseImportTestsModelsO2MChild(models.Model):
    parent = models.ForeignKey(BaseImportTestsModelsO2M, models.DO_NOTHING, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_o2m_child'


class BaseImportTestsModelsPreview(models.Model):
    somevalue = models.IntegerField()
    othervalue = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_import_tests_models_preview'


class BaseLanguageExport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1)
    format = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_export'


class BaseLanguageImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=6)
    filename = models.CharField(max_length=-1)
    overwrite = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    data = models.BinaryField()

    class Meta:
        managed = False
        db_table = 'base_language_import'


class BaseLanguageInstall(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    overwrite = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_language_install'


class BaseModuleInstallRequest(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_install_request'


class BaseModuleInstallReview(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_install_review'


class BaseModuleUninstall(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    show_all = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_uninstall'


class BaseModuleUpdate(models.Model):
    updated = models.IntegerField(blank=True, null=True)
    added = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_update'


class BaseModuleUpgrade(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    module_info = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_module_upgrade'


class BasePartnerMergeAutomaticWizard(models.Model):
    number_group = models.IntegerField(blank=True, null=True)
    current_line = models.ForeignKey('BasePartnerMergeLine', models.DO_NOTHING, blank=True, null=True)
    dst_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    maximum_group = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    group_by_email = models.BooleanField(blank=True, null=True)
    group_by_name = models.BooleanField(blank=True, null=True)
    group_by_is_company = models.BooleanField(blank=True, null=True)
    group_by_vat = models.BooleanField(blank=True, null=True)
    group_by_parent_id = models.BooleanField(blank=True, null=True)
    exclude_contact = models.BooleanField(blank=True, null=True)
    exclude_journal_item = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard'


class BasePartnerMergeAutomaticWizardResPartnerRel(models.Model):
    base_partner_merge_automatic_wizard = models.OneToOneField(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_automatic_wizard_res_partner_rel'
        unique_together = (('base_partner_merge_automatic_wizard', 'res_partner'),)


class BasePartnerMergeLine(models.Model):
    wizard = models.ForeignKey(BasePartnerMergeAutomaticWizard, models.DO_NOTHING, blank=True, null=True)
    min_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    aggr_ids = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'base_partner_merge_line'


class BusBus(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    channel = models.CharField(max_length=-1, blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_bus'


class BusPresence(models.Model):
    user = models.OneToOneField('ResUsers', models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=-1, blank=True, null=True)
    last_poll = models.DateTimeField(blank=True, null=True)
    last_presence = models.DateTimeField(blank=True, null=True)
    guest = models.OneToOneField('MailGuest', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bus_presence'


class CalendarAlarm(models.Model):
    duration = models.IntegerField()
    duration_minutes = models.IntegerField(blank=True, null=True)
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    alarm_type = models.CharField(max_length=-1)
    interval = models.CharField(max_length=-1)
    name = models.JSONField()
    body = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_alarm'


class CalendarAlarmCalendarEventRel(models.Model):
    calendar_event = models.OneToOneField('CalendarEvent', models.DO_NOTHING, primary_key=True)
    calendar_alarm = models.ForeignKey(CalendarAlarm, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_alarm_calendar_event_rel'
        unique_together = (('calendar_event', 'calendar_alarm'),)


class CalendarAttendee(models.Model):
    event = models.ForeignKey('CalendarEvent', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    common_name = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    availability = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_attendee'


class CalendarEvent(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    videocall_channel = models.ForeignKey('MailChannel', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    res_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    recurrence = models.ForeignKey('CalendarRecurrence', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    location = models.CharField(max_length=-1, blank=True, null=True)
    videocall_location = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    privacy = models.CharField(max_length=-1)
    show_as = models.CharField(max_length=-1)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    start_date = models.DateField(blank=True, null=True)
    stop_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    allday = models.BooleanField(blank=True, null=True)
    recurrency = models.BooleanField(blank=True, null=True)
    follow_recurrence = models.BooleanField(blank=True, null=True)
    start = models.DateTimeField()
    stop = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    applicant = models.ForeignKey('HrApplicant', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event'


class CalendarEventResPartnerRel(models.Model):
    res_partner = models.OneToOneField('ResPartner', models.DO_NOTHING, primary_key=True)
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'calendar_event_res_partner_rel'
        unique_together = (('res_partner', 'calendar_event'),)


class CalendarEventType(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_event_type'


class CalendarFilters(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    partner_checked = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_filters'
        unique_together = (('user', 'partner'),)


class CalendarProviderConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    external_calendar_provider = models.CharField(max_length=-1, blank=True, null=True)
    cal_client_id = models.CharField(max_length=-1, blank=True, null=True)
    cal_client_secret = models.CharField(max_length=-1, blank=True, null=True)
    microsoft_outlook_client_identifier = models.CharField(max_length=-1, blank=True, null=True)
    microsoft_outlook_client_secret = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_provider_config'


class CalendarRecurrence(models.Model):
    base_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)
    interval = models.IntegerField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    day = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    event_tz = models.CharField(max_length=-1, blank=True, null=True)
    rrule = models.CharField(max_length=-1, blank=True, null=True)
    rrule_type = models.CharField(max_length=-1, blank=True, null=True)
    end_type = models.CharField(max_length=-1, blank=True, null=True)
    month_by = models.CharField(max_length=-1, blank=True, null=True)
    weekday = models.CharField(max_length=-1, blank=True, null=True)
    byday = models.CharField(max_length=-1, blank=True, null=True)
    until = models.DateField(blank=True, null=True)
    mon = models.BooleanField(blank=True, null=True)
    tue = models.BooleanField(blank=True, null=True)
    wed = models.BooleanField(blank=True, null=True)
    thu = models.BooleanField(blank=True, null=True)
    fri = models.BooleanField(blank=True, null=True)
    sat = models.BooleanField(blank=True, null=True)
    sun = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'calendar_recurrence'


class ChangePasswordOwn(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    new_password = models.CharField(max_length=-1, blank=True, null=True)
    confirm_password = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_own'


class ChangePasswordUser(models.Model):
    wizard = models.ForeignKey('ChangePasswordWizard', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    user_login = models.CharField(max_length=-1, blank=True, null=True)
    new_passwd = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_user'


class ChangePasswordWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_password_wizard'


class ChangeProductionQty(models.Model):
    mo = models.ForeignKey('MrpProduction', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'change_production_qty'


class ConfirmStockSms(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'confirm_stock_sms'


class CrmTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_tag'


class CrmTeam(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_quotations = models.BooleanField(blank=True, null=True)
    invoiced_target = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team'


class CrmTeamMember(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    crm_team = models.ForeignKey(CrmTeam, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'crm_team_member'


class DecimalPrecision(models.Model):
    digits = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'decimal_precision'


class DigestDigest(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    periodicity = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    next_run_date = models.DateField(blank=True, null=True)
    name = models.JSONField()
    kpi_res_users_connected = models.BooleanField(blank=True, null=True)
    kpi_mail_message_total = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    kpi_account_total_revenue = models.BooleanField(blank=True, null=True)
    kpi_project_task_opened = models.BooleanField(blank=True, null=True)
    kpi_all_sale_total = models.BooleanField(blank=True, null=True)
    kpi_hr_recruitment_new_colleagues = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_digest'


class DigestDigestResUsersRel(models.Model):
    digest_digest = models.OneToOneField(DigestDigest, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_digest_res_users_rel'
        unique_together = (('digest_digest', 'res_users'),)


class DigestTip(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    tip_description = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'digest_tip'


class DigestTipResUsersRel(models.Model):
    digest_tip = models.OneToOneField(DigestTip, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'digest_tip_res_users_rel'
        unique_together = (('digest_tip', 'res_users'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EmailTemplateAttachmentRel(models.Model):
    email_template = models.OneToOneField('MailTemplate', models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'email_template_attachment_rel'
        unique_together = (('email_template', 'attachment'),)


class EmployeeCategoryRel(models.Model):
    emp = models.OneToOneField('HrEmployee', models.DO_NOTHING, primary_key=True)
    category = models.ForeignKey('HrEmployeeCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_category_rel'
        unique_together = (('emp', 'category'),)


class ExpenseTax(models.Model):
    expense = models.OneToOneField('HrExpense', models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'expense_tax'
        unique_together = (('expense', 'tax'),)


class FetchmailServer(models.Model):
    port = models.IntegerField(blank=True, null=True)
    object = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    server = models.CharField(max_length=-1, blank=True, null=True)
    server_type = models.CharField(max_length=-1)
    user = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    script = models.CharField(max_length=-1, blank=True, null=True)
    configuration = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    is_ssl = models.BooleanField(blank=True, null=True)
    attach = models.BooleanField(blank=True, null=True)
    original = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    google_gmail_access_token_expiration = models.IntegerField(blank=True, null=True)
    google_gmail_authorization_code = models.CharField(max_length=-1, blank=True, null=True)
    google_gmail_refresh_token = models.CharField(max_length=-1, blank=True, null=True)
    google_gmail_access_token = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fetchmail_server'


class FleetServiceType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    category = models.CharField(max_length=-1)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_service_type'


class FleetServiceTypeFleetVehicleLogContractRel(models.Model):
    fleet_vehicle_log_contract = models.OneToOneField('FleetVehicleLogContract', models.DO_NOTHING, primary_key=True)
    fleet_service_type = models.ForeignKey(FleetServiceType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fleet_service_type_fleet_vehicle_log_contract_rel'
        unique_together = (('fleet_vehicle_log_contract', 'fleet_service_type'),)


class FleetVehicle(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    driver = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    future_driver = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey('FleetVehicleModel', models.DO_NOTHING)
    brand = models.ForeignKey('FleetVehicleModelBrand', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('FleetVehicleState', models.DO_NOTHING, blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey('FleetVehicleModelCategory', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    license_plate = models.CharField(max_length=-1, blank=True, null=True)
    vin_sn = models.CharField(max_length=-1, blank=True, null=True)
    color = models.CharField(max_length=-1, blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    model_year = models.CharField(max_length=-1, blank=True, null=True)
    odometer_unit = models.CharField(max_length=-1)
    transmission = models.CharField(max_length=-1, blank=True, null=True)
    fuel_type = models.CharField(max_length=-1, blank=True, null=True)
    co2_standard = models.CharField(max_length=-1, blank=True, null=True)
    frame_type = models.CharField(max_length=-1, blank=True, null=True)
    next_assignation_date = models.DateField(blank=True, null=True)
    acquisition_date = models.DateField(blank=True, null=True)
    write_off_date = models.DateField(blank=True, null=True)
    first_contract_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    trailer_hook = models.BooleanField(blank=True, null=True)
    plan_to_change_car = models.BooleanField(blank=True, null=True)
    plan_to_change_bike = models.BooleanField(blank=True, null=True)
    electric_assistance = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    horsepower_tax = models.FloatField(blank=True, null=True)
    co2 = models.FloatField(blank=True, null=True)
    car_value = models.FloatField(blank=True, null=True)
    net_car_value = models.FloatField(blank=True, null=True)
    residual_value = models.FloatField(blank=True, null=True)
    frame_size = models.FloatField(blank=True, null=True)
    driver_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    future_driver_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    mobility_card = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle'


class FleetVehicleAssignationLog(models.Model):
    vehicle = models.ForeignKey(FleetVehicle, models.DO_NOTHING)
    driver = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    driver_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_assignation_log'


class FleetVehicleLogContract(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey(FleetVehicle, models.DO_NOTHING)
    cost_subtype = models.ForeignKey(FleetServiceType, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    insurer = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    ins_ref = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    cost_frequency = models.CharField(max_length=-1)
    date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    cost_generated = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_log_contract'


class FleetVehicleLogServices(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    vehicle = models.ForeignKey(FleetVehicle, models.DO_NOTHING)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    odometer = models.ForeignKey('FleetVehicleOdometer', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    purchaser = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    vendor = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    service_type = models.ForeignKey(FleetServiceType, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    inv_ref = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    purchaser_employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_log_services'


class FleetVehicleModel(models.Model):
    brand = models.ForeignKey('FleetVehicleModelBrand', models.DO_NOTHING)
    category = models.ForeignKey('FleetVehicleModelCategory', models.DO_NOTHING, blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    seats = models.IntegerField(blank=True, null=True)
    doors = models.IntegerField(blank=True, null=True)
    power = models.IntegerField(blank=True, null=True)
    horsepower = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    vehicle_type = models.CharField(max_length=-1)
    transmission = models.CharField(max_length=-1, blank=True, null=True)
    color = models.CharField(max_length=-1, blank=True, null=True)
    co2_standard = models.CharField(max_length=-1, blank=True, null=True)
    default_fuel_type = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    trailer_hook = models.BooleanField(blank=True, null=True)
    electric_assistance = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    default_co2 = models.FloatField(blank=True, null=True)
    horsepower_tax = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_model'


class FleetVehicleModelBrand(models.Model):
    model_count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_model_brand'


class FleetVehicleModelCategory(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_model_category'


class FleetVehicleModelVendors(models.Model):
    model = models.OneToOneField(FleetVehicleModel, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_model_vendors'
        unique_together = (('model', 'partner'),)


class FleetVehicleOdometer(models.Model):
    vehicle = models.ForeignKey(FleetVehicle, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_odometer'


class FleetVehicleState(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_state'


class FleetVehicleTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_tag'


class FleetVehicleVehicleTagRel(models.Model):
    vehicle_tag = models.OneToOneField(FleetVehicle, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(FleetVehicleTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'fleet_vehicle_vehicle_tag_rel'
        unique_together = (('vehicle_tag', 'tag'),)


class GamificationBadge(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    rule_max_number = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    level = models.CharField(max_length=-1, blank=True, null=True)
    rule_auth = models.CharField(max_length=-1)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    rule_max = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_badge'


class GamificationBadgeRuleBadgeRel(models.Model):
    badge1 = models.OneToOneField(GamificationBadge, models.DO_NOTHING, primary_key=True)
    badge2 = models.ForeignKey(GamificationBadge, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gamification_badge_rule_badge_rel'
        unique_together = (('badge1', 'badge2'),)


class GamificationBadgeUser(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    sender = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    badge = models.ForeignKey(GamificationBadge, models.DO_NOTHING)
    challenge = models.ForeignKey('GamificationChallenge', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    level = models.CharField(max_length=-1, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_badge_user'


class GamificationBadgeUserWizard(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    badge = models.ForeignKey(GamificationBadge, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gamification_badge_user_wizard'


class GamificationChallenge(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    reward = models.ForeignKey(GamificationBadge, models.DO_NOTHING, blank=True, null=True)
    reward_first = models.ForeignKey(GamificationBadge, models.DO_NOTHING, blank=True, null=True)
    reward_second = models.ForeignKey(GamificationBadge, models.DO_NOTHING, blank=True, null=True)
    reward_third = models.ForeignKey(GamificationBadge, models.DO_NOTHING, blank=True, null=True)
    report_message_group = models.ForeignKey('MailChannel', models.DO_NOTHING, blank=True, null=True)
    report_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)
    remind_update_delay = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    user_domain = models.CharField(max_length=-1, blank=True, null=True)
    period = models.CharField(max_length=-1)
    visibility_mode = models.CharField(max_length=-1)
    report_message_frequency = models.CharField(max_length=-1)
    challenge_category = models.CharField(max_length=-1)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    last_report_date = models.DateField(blank=True, null=True)
    next_report_date = models.DateField(blank=True, null=True)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    reward_failure = models.BooleanField(blank=True, null=True)
    reward_realtime = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_challenge'


class GamificationChallengeLine(models.Model):
    challenge = models.ForeignKey(GamificationChallenge, models.DO_NOTHING)
    definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_goal = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gamification_challenge_line'


class GamificationChallengeUsersRel(models.Model):
    gamification_challenge = models.OneToOneField(GamificationChallenge, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gamification_challenge_users_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class GamificationGoal(models.Model):
    definition = models.ForeignKey('GamificationGoalDefinition', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    line = models.ForeignKey(GamificationChallengeLine, models.DO_NOTHING, blank=True, null=True)
    challenge = models.ForeignKey(GamificationChallenge, models.DO_NOTHING, blank=True, null=True)
    remind_update_delay = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    last_update = models.DateField(blank=True, null=True)
    to_update = models.BooleanField(blank=True, null=True)
    closed = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target_goal = models.FloatField()
    current = models.FloatField()

    class Meta:
        managed = False
        db_table = 'gamification_goal'


class GamificationGoalDefinition(models.Model):
    model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    field_date = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    batch_distinctive_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, db_column='batch_distinctive_field', blank=True, null=True)
    action = models.ForeignKey('IrActWindow', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    computation_mode = models.CharField(max_length=-1)
    display_mode = models.CharField(max_length=-1)
    domain = models.CharField(max_length=-1)
    batch_user_expression = models.CharField(max_length=-1, blank=True, null=True)
    condition = models.CharField(max_length=-1)
    res_id_field = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    suffix = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    compute_code = models.TextField(blank=True, null=True)
    monetary = models.BooleanField(blank=True, null=True)
    batch_mode = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_goal_definition'


class GamificationGoalWizard(models.Model):
    goal = models.ForeignKey(GamificationGoal, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    current = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_goal_wizard'


class GamificationInvitedUserIdsRel(models.Model):
    gamification_challenge = models.OneToOneField(GamificationChallenge, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'gamification_invited_user_ids_rel'
        unique_together = (('gamification_challenge', 'res_users'),)


class GamificationKarmaRank(models.Model):
    karma_min = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    description_motivational = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_karma_rank'


class GamificationKarmaTracking(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    old_value = models.IntegerField()
    new_value = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    tracking_date = models.DateField(blank=True, null=True)
    consolidated = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gamification_karma_tracking'


class HrApplicant(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('HrRecruitmentStage', models.DO_NOTHING, blank=True, null=True)
    last_stage = models.ForeignKey('HrRecruitmentStage', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    type = models.ForeignKey('HrRecruitmentDegree', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    emp = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    refuse_reason = models.ForeignKey('HrApplicantRefuseReason', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    email_from = models.CharField(max_length=128, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    salary_proposed_extra = models.CharField(max_length=-1, blank=True, null=True)
    salary_expected_extra = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    partner_phone = models.CharField(max_length=32, blank=True, null=True)
    partner_mobile = models.CharField(max_length=32, blank=True, null=True)
    kanban_state = models.CharField(max_length=-1)
    linkedin_profile = models.CharField(max_length=-1, blank=True, null=True)
    availability = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    date_open = models.DateTimeField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    probability = models.FloatField(blank=True, null=True)
    salary_proposed = models.FloatField(blank=True, null=True)
    salary_expected = models.FloatField(blank=True, null=True)
    delay_close = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant'


class HrApplicantCategory(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant_category'


class HrApplicantHrApplicantCategoryRel(models.Model):
    hr_applicant = models.OneToOneField(HrApplicant, models.DO_NOTHING, primary_key=True)
    hr_applicant_category = models.ForeignKey(HrApplicantCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_applicant_hr_applicant_category_rel'
        unique_together = (('hr_applicant', 'hr_applicant_category'),)


class HrApplicantHrSkillRel(models.Model):
    hr_applicant = models.OneToOneField(HrApplicant, models.DO_NOTHING, primary_key=True)
    hr_skill = models.ForeignKey('HrSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_applicant_hr_skill_rel'
        unique_together = (('hr_applicant', 'hr_skill'),)


class HrApplicantRefuseReason(models.Model):
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant_refuse_reason'


class HrApplicantResUsersInterviewersRel(models.Model):
    hr_applicant = models.OneToOneField(HrApplicant, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_applicant_res_users_interviewers_rel'
        unique_together = (('hr_applicant', 'res_users'),)


class HrApplicantSkill(models.Model):
    applicant = models.ForeignKey(HrApplicant, models.DO_NOTHING)
    skill = models.ForeignKey('HrSkill', models.DO_NOTHING)
    skill_level = models.ForeignKey('HrSkillLevel', models.DO_NOTHING)
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_applicant_skill'
        unique_together = (('applicant', 'skill'),)


class HrAttendance(models.Model):
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    worked_hours = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendance'


class HrAttendanceOvertime(models.Model):
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    adjustment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField()
    duration_real = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendance_overtime'
        unique_together = (('employee', 'date'),)


class HrContract(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    structure_type = models.ForeignKey('HrPayrollStructureType', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey('HrDepartment', models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    contract_type = models.ForeignKey('HrContractType', models.DO_NOTHING, blank=True, null=True)
    hr_responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    kanban_state = models.CharField(max_length=-1, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    trial_date_end = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    wage = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_contract'


class HrContractType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_contract_type'


class HrDepartment(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey('HrEmployee', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    master_department = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_department'


class HrDepartmentHrLeaveStressDayRel(models.Model):
    hr_leave_stress_day = models.OneToOneField('HrLeaveStressDay', models.DO_NOTHING, primary_key=True)
    hr_department = models.ForeignKey(HrDepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_department_hr_leave_stress_day_rel'
        unique_together = (('hr_leave_stress_day', 'hr_department'),)


class HrDepartmentMailChannelRel(models.Model):
    mail_channel = models.OneToOneField('MailChannel', models.DO_NOTHING, primary_key=True)
    hr_department = models.ForeignKey(HrDepartment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_department_mail_channel_rel'
        unique_together = (('mail_channel', 'hr_department'),)


class HrDepartureReason(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_departure_reason'


class HrDepartureWizard(models.Model):
    departure_reason = models.ForeignKey(HrDepartureReason, models.DO_NOTHING)
    employee = models.ForeignKey('HrEmployee', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    departure_date = models.DateField()
    departure_description = models.TextField(blank=True, null=True)
    archive_private_address = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    set_date_end = models.BooleanField(blank=True, null=True)
    cancel_leaves = models.BooleanField(blank=True, null=True)
    archive_allocation = models.BooleanField(blank=True, null=True)
    release_campany_car = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_departure_wizard'


class HrEmployee(models.Model):
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    job = models.ForeignKey('HrJob', models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    work_contact = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    work_location = models.ForeignKey('HrWorkLocation', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    coach = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    address_home = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    children = models.IntegerField(blank=True, null=True)
    country_of_birth = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country_of_birth', blank=True, null=True)
    bank_account = models.ForeignKey('ResPartnerBank', models.DO_NOTHING, blank=True, null=True)
    km_home_work = models.IntegerField(blank=True, null=True)
    departure_reason = models.ForeignKey(HrDepartureReason, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    job_title = models.CharField(max_length=-1, blank=True, null=True)
    work_phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile_phone = models.CharField(max_length=-1, blank=True, null=True)
    work_email = models.CharField(max_length=-1, blank=True, null=True)
    employee_type = models.CharField(max_length=-1)
    gender = models.CharField(max_length=-1, blank=True, null=True)
    marital = models.CharField(max_length=-1, blank=True, null=True)
    spouse_complete_name = models.CharField(max_length=-1, blank=True, null=True)
    place_of_birth = models.CharField(max_length=-1, blank=True, null=True)
    ssnid = models.CharField(max_length=-1, blank=True, null=True)
    sinid = models.CharField(max_length=-1, blank=True, null=True)
    identification_id = models.CharField(max_length=-1, blank=True, null=True)
    passport_id = models.CharField(max_length=-1, blank=True, null=True)
    permit_no = models.CharField(max_length=-1, blank=True, null=True)
    visa_no = models.CharField(max_length=-1, blank=True, null=True)
    certificate = models.CharField(max_length=-1, blank=True, null=True)
    study_field = models.CharField(max_length=-1, blank=True, null=True)
    study_school = models.CharField(max_length=-1, blank=True, null=True)
    emergency_contact = models.CharField(max_length=-1, blank=True, null=True)
    emergency_phone = models.CharField(max_length=-1, blank=True, null=True)
    barcode = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    pin = models.CharField(max_length=-1, blank=True, null=True)
    spouse_birthdate = models.DateField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    visa_expire = models.DateField(blank=True, null=True)
    work_permit_expiration_date = models.DateField(blank=True, null=True)
    departure_date = models.DateField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    departure_description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    work_permit_scheduled_activity = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    contract = models.ForeignKey(HrContract, models.DO_NOTHING, blank=True, null=True)
    vehicle = models.CharField(max_length=-1, blank=True, null=True)
    first_contract_date = models.DateField(blank=True, null=True)
    contract_warning = models.BooleanField(blank=True, null=True)
    expense_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    leave_manager = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    mobility_card = models.CharField(max_length=-1, blank=True, null=True)
    last_attendance = models.ForeignKey(HrAttendance, models.DO_NOTHING, blank=True, null=True)
    last_check_in = models.DateTimeField(blank=True, null=True)
    last_check_out = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee'
        unique_together = (('user', 'company'),)


class HrEmployeeCategory(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_category'


class HrEmployeeHrLeaveAllocationRel(models.Model):
    hr_leave_allocation = models.OneToOneField('HrLeaveAllocation', models.DO_NOTHING, primary_key=True)
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_leave_allocation_rel'
        unique_together = (('hr_leave_allocation', 'hr_employee'),)


class HrEmployeeHrLeaveRel(models.Model):
    hr_leave = models.OneToOneField('HrLeave', models.DO_NOTHING, primary_key=True)
    hr_employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_leave_rel'
        unique_together = (('hr_leave', 'hr_employee'),)


class HrEmployeeHrPlanWizardRel(models.Model):
    employee = models.OneToOneField('HrPlanWizard', models.DO_NOTHING, primary_key=True)
    plan_wizard = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_plan_wizard_rel'
        unique_together = (('employee', 'plan_wizard'),)


class HrEmployeeHrSkillRel(models.Model):
    hr_employee = models.OneToOneField(HrEmployee, models.DO_NOTHING, primary_key=True)
    hr_skill = models.ForeignKey('HrSkill', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_employee_hr_skill_rel'
        unique_together = (('hr_employee', 'hr_skill'),)


class HrEmployeeSkill(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    skill = models.ForeignKey('HrSkill', models.DO_NOTHING)
    skill_level = models.ForeignKey('HrSkillLevel', models.DO_NOTHING)
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_skill'
        unique_together = (('employee', 'skill'),)


class HrEmployeeSkillLog(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    skill = models.ForeignKey('HrSkill', models.DO_NOTHING)
    skill_level = models.ForeignKey('HrSkillLevel', models.DO_NOTHING)
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING)
    level_progress = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_employee_skill_log'
        unique_together = (('employee', 'department', 'skill', 'date'),)


class HrExpense(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    payment_mode = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)
    analytic_distribution = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax_company = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_amount_company = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_refused = models.BooleanField(blank=True, null=True)
    sample = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense'


class HrExpenseApproveDuplicate(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate'


class HrExpenseApproveDuplicateHrExpenseSheetRel(models.Model):
    hr_expense_approve_duplicate = models.OneToOneField(HrExpenseApproveDuplicate, models.DO_NOTHING, primary_key=True)
    hr_expense_sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_approve_duplicate_hr_expense_sheet_rel'
        unique_together = (('hr_expense_approve_duplicate', 'hr_expense_sheet'),)


class HrExpenseHrExpenseApproveDuplicateRel(models.Model):
    hr_expense_approve_duplicate = models.OneToOneField(HrExpenseApproveDuplicate, models.DO_NOTHING, primary_key=True)
    hr_expense = models.ForeignKey(HrExpense, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_hr_expense_approve_duplicate_rel'
        unique_together = (('hr_expense_approve_duplicate', 'hr_expense'),)


class HrExpenseHrExpenseRefuseWizardRel(models.Model):
    hr_expense_refuse_wizard = models.OneToOneField('HrExpenseRefuseWizard', models.DO_NOTHING, primary_key=True)
    hr_expense = models.ForeignKey(HrExpense, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_expense_hr_expense_refuse_wizard_rel'
        unique_together = (('hr_expense_refuse_wizard', 'hr_expense'),)


class HrExpenseRefuseWizard(models.Model):
    hr_expense_sheet = models.ForeignKey('HrExpenseSheet', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    reason = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_refuse_wizard'


class HrExpenseSheet(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    bank_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    payment_state = models.CharField(max_length=-1, blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    total_amount_taxes = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_residual = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_sheet'


class HrExpenseSplit(models.Model):
    wizard = models.ForeignKey('HrExpenseSplitWizard', models.DO_NOTHING, blank=True, null=True)
    expense = models.ForeignKey(HrExpense, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    analytic_distribution = models.JSONField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_has_cost = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_split'


class HrExpenseSplitWizard(models.Model):
    expense = models.ForeignKey(HrExpense, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_expense_split_wizard'


class HrHolidaysCancelLeave(models.Model):
    leave = models.ForeignKey('HrLeave', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    reason = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_cancel_leave'


class HrHolidaysSummaryEmployee(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    holiday_type = models.CharField(max_length=-1)
    date_from = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holidays_summary_employee'


class HrJob(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    expected_employees = models.IntegerField(blank=True, null=True)
    no_of_employee = models.IntegerField(blank=True, null=True)
    no_of_recruitment = models.IntegerField(blank=True, null=True)
    no_of_hired_employee = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    contract_type = models.ForeignKey(HrContractType, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    description = models.TextField(blank=True, null=True)
    requirements = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    hr_responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_job'
        unique_together = (('name', 'company', 'department'),)


class HrJobExtendedInterviewerResUsers(models.Model):
    hr_job = models.OneToOneField(HrJob, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_job_extended_interviewer_res_users'
        unique_together = (('hr_job', 'res_users'),)


class HrJobHrRecruitmentStageRel(models.Model):
    hr_recruitment_stage = models.OneToOneField('HrRecruitmentStage', models.DO_NOTHING, primary_key=True)
    hr_job = models.ForeignKey(HrJob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_job_hr_recruitment_stage_rel'
        unique_together = (('hr_recruitment_stage', 'hr_job'),)


class HrJobResUsersRel(models.Model):
    hr_job = models.OneToOneField(HrJob, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'hr_job_res_users_rel'
        unique_together = (('hr_job', 'res_users'),)


class HrLeave(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    holiday_status = models.ForeignKey('HrLeaveType', models.DO_NOTHING)
    holiday_allocation = models.ForeignKey('HrLeaveAllocation', models.DO_NOTHING, blank=True, null=True)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    employee_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    meeting = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(HrEmployeeCategory, models.DO_NOTHING, blank=True, null=True)
    mode_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    first_approver = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    second_approver = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    private_name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    duration_display = models.CharField(max_length=-1, blank=True, null=True)
    holiday_type = models.CharField(max_length=-1)
    request_hour_from = models.CharField(max_length=-1, blank=True, null=True)
    request_hour_to = models.CharField(max_length=-1, blank=True, null=True)
    request_date_from_period = models.CharField(max_length=-1, blank=True, null=True)
    request_date_from = models.DateField(blank=True, null=True)
    request_date_to = models.DateField(blank=True, null=True)
    report_note = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    multi_employee = models.BooleanField(blank=True, null=True)
    request_unit_half = models.BooleanField(blank=True, null=True)
    request_unit_hours = models.BooleanField(blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    overtime = models.ForeignKey(HrAttendanceOvertime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave'


class HrLeaveAccrualLevel(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    accrual_plan = models.ForeignKey('HrLeaveAccrualPlan', models.DO_NOTHING)
    start_count = models.IntegerField(blank=True, null=True)
    first_day = models.IntegerField(blank=True, null=True)
    second_day = models.IntegerField(blank=True, null=True)
    first_month_day = models.IntegerField(blank=True, null=True)
    second_month_day = models.IntegerField(blank=True, null=True)
    yearly_day = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    postpone_max_days = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    start_type = models.CharField(max_length=-1)
    added_value_type = models.CharField(max_length=-1)
    frequency = models.CharField(max_length=-1)
    week_day = models.CharField(max_length=-1)
    first_month = models.CharField(max_length=-1, blank=True, null=True)
    second_month = models.CharField(max_length=-1, blank=True, null=True)
    yearly_month = models.CharField(max_length=-1, blank=True, null=True)
    action_with_unused_accruals = models.CharField(max_length=-1)
    is_based_on_worked_time = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    added_value = models.FloatField()
    maximum_leave = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_accrual_level'


class HrLeaveAccrualPlan(models.Model):
    time_off_type = models.ForeignKey('HrLeaveType', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    transition_mode = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_accrual_plan'


class HrLeaveAllocation(models.Model):
    message_main_attachment = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    holiday_status = models.ForeignKey('HrLeaveType', models.DO_NOTHING)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    employee_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    manager = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    approver = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    mode_company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(HrEmployeeCategory, models.DO_NOTHING, blank=True, null=True)
    accrual_plan = models.ForeignKey(HrLeaveAccrualPlan, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    private_name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    holiday_type = models.CharField(max_length=-1)
    allocation_type = models.CharField(max_length=-1)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    lastcall = models.DateField(blank=True, null=True)
    nextcall = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    multi_employee = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    number_of_days = models.FloatField(blank=True, null=True)
    overtime = models.ForeignKey(HrAttendanceOvertime, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_allocation'


class HrLeaveStressDay(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    start_date = models.DateField()
    end_date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_stress_day'


class HrLeaveType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    icon = models.ForeignKey('IrAttachment', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    leave_notif_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    allocation_notif_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    color_name = models.CharField(max_length=-1)
    leave_validation_type = models.CharField(max_length=-1, blank=True, null=True)
    requires_allocation = models.CharField(max_length=-1)
    employee_requests = models.CharField(max_length=-1)
    allocation_validation_type = models.CharField(max_length=-1, blank=True, null=True)
    time_type = models.CharField(max_length=-1, blank=True, null=True)
    request_unit = models.CharField(max_length=-1)
    name = models.JSONField()
    create_calendar_meeting = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    unpaid = models.BooleanField(blank=True, null=True)
    support_document = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    overtime_deductible = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_leave_type'


class HrPayrollStructureType(models.Model):
    default_resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_payroll_structure_type'


class HrPlan(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan'


class HrPlanActivityType(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    responsible = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    plan = models.ForeignKey(HrPlan, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    responsible_0 = models.CharField(db_column='responsible', max_length=-1)  # Field renamed because of name conflict.
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan_activity_type'


class HrPlanWizard(models.Model):
    plan = models.ForeignKey(HrPlan, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_plan_wizard'


class HrRecruitmentDegree(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_recruitment_degree'


class HrRecruitmentSource(models.Model):
    source = models.ForeignKey('UtmSource', models.DO_NOTHING)
    job = models.ForeignKey(HrJob, models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey('MailAlias', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_recruitment_source'


class HrRecruitmentStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    legend_blocked = models.JSONField()
    legend_done = models.JSONField()
    legend_normal = models.JSONField()
    requirements = models.TextField(blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    hired_stage = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_recruitment_stage'


class HrResumeLine(models.Model):
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING)
    line_type = models.ForeignKey('HrResumeLineType', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    date_start = models.DateField()
    date_end = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_resume_line'


class HrResumeLineType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_resume_line_type'


class HrSkill(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_skill'


class HrSkillLevel(models.Model):
    skill_type = models.ForeignKey('HrSkillType', models.DO_NOTHING, blank=True, null=True)
    level_progress = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    default_level = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_skill_level'


class HrSkillType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_skill_type'


class HrWorkLocation(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    location_number = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_work_location'


class IapAccount(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    service_name = models.CharField(max_length=-1, blank=True, null=True)
    account_token = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'iap_account'


class IapAccountResCompanyRel(models.Model):
    iap_account = models.OneToOneField(IapAccount, models.DO_NOTHING, primary_key=True)
    res_company = models.ForeignKey('ResCompany', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'iap_account_res_company_rel'
        unique_together = (('iap_account', 'res_company'),)


class IrActClient(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tag = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    params_store = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_client'


class IrActReportXml(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    paperformat = models.ForeignKey('ReportPaperformat', models.DO_NOTHING, blank=True, null=True)
    model = models.CharField(max_length=-1)
    report_type = models.CharField(max_length=-1)
    report_name = models.CharField(max_length=-1)
    report_file = models.CharField(max_length=-1, blank=True, null=True)
    attachment = models.CharField(max_length=-1, blank=True, null=True)
    print_report_name = models.JSONField(blank=True, null=True)
    multi = models.BooleanField(blank=True, null=True)
    attachment_use = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_report_xml'


class IrActServer(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    model = models.ForeignKey('IrModel', models.DO_NOTHING)
    crud_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    link_field = models.ForeignKey('IrModelFields', models.DO_NOTHING, blank=True, null=True)
    usage = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    model_name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.TextField(blank=True, null=True)
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    activity_date_deadline_range = models.IntegerField(blank=True, null=True)
    activity_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    mail_post_method = models.CharField(max_length=-1, blank=True, null=True)
    activity_summary = models.CharField(max_length=-1, blank=True, null=True)
    activity_date_deadline_range_type = models.CharField(max_length=-1, blank=True, null=True)
    activity_user_type = models.CharField(max_length=-1, blank=True, null=True)
    activity_user_field_name = models.CharField(max_length=-1, blank=True, null=True)
    activity_note = models.TextField(blank=True, null=True)
    mail_post_autofollow = models.BooleanField(blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    sms_method = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_server'


class IrActServerGroupRel(models.Model):
    act = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_server_group_rel'
        unique_together = (('act', 'gid'),)


class IrActServerResPartnerRel(models.Model):
    ir_act_server = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_act_server_res_partner_rel'
        unique_together = (('ir_act_server', 'res_partner'),)


class IrActUrl(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    target = models.CharField(max_length=-1)
    url = models.TextField()

    class Meta:
        managed = False
        db_table = 'ir_act_url'


class IrActWindow(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    limit = models.IntegerField(blank=True, null=True)
    search_view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    context = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    usage = models.CharField(max_length=-1, blank=True, null=True)
    filter = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window'


class IrActWindowGroupRel(models.Model):
    act = models.OneToOneField(IrActWindow, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_act_window_group_rel'
        unique_together = (('act', 'gid'),)


class IrActWindowView(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    view = models.ForeignKey('IrUiView', models.DO_NOTHING, blank=True, null=True)
    act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    view_mode = models.CharField(max_length=-1)
    multi = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_act_window_view'
        unique_together = (('act_window', 'view_mode'),)


class IrActions(models.Model):
    binding_model = models.ForeignKey('IrModel', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    binding_type = models.CharField(max_length=-1)
    binding_view_types = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions'


class IrActionsTodo(models.Model):
    action_id = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_actions_todo'


class IrAsset(models.Model):
    sequence = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    bundle = models.CharField(max_length=-1)
    directive = models.CharField(max_length=-1, blank=True, null=True)
    path = models.CharField(max_length=-1)
    target = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_asset'


class IrAttachment(models.Model):
    res_id = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    res_field = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    url = models.CharField(max_length=1024, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    store_fname = models.CharField(max_length=-1, blank=True, null=True)
    checksum = models.CharField(max_length=40, blank=True, null=True)
    mimetype = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    index_content = models.TextField(blank=True, null=True)
    public = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    db_datas = models.BinaryField(blank=True, null=True)
    original = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_attachment'


class IrConfigParameter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    key = models.CharField(unique=True, max_length=-1)
    value = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_config_parameter'


class IrCron(models.Model):
    ir_actions_server = models.ForeignKey(IrActServer, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    interval_number = models.IntegerField(blank=True, null=True)
    numbercall = models.IntegerField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    interval_type = models.CharField(max_length=-1, blank=True, null=True)
    cron_name = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    doall = models.BooleanField(blank=True, null=True)
    nextcall = models.DateTimeField()
    lastcall = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron'


class IrCronTrigger(models.Model):
    cron = models.ForeignKey(IrCron, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    call_at = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_cron_trigger'


class IrDefault(models.Model):
    field = models.ForeignKey('IrModelFields', models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    condition = models.CharField(max_length=-1, blank=True, null=True)
    json_value = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_default'


class IrDemo(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo'


class IrDemoFailure(models.Model):
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING)
    wizard = models.ForeignKey('IrDemoFailureWizard', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    error = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure'


class IrDemoFailureWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_demo_failure_wizard'


class IrExports(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    resource = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports'


class IrExportsLine(models.Model):
    export = models.ForeignKey(IrExports, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_exports_line'


class IrFilters(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    model_id = models.CharField(max_length=-1)
    domain = models.TextField()
    context = models.TextField()
    sort = models.TextField()
    is_default = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_filters'
        unique_together = (('model_id', 'user', 'action_id', 'name'),)


class IrLogging(models.Model):
    create_uid = models.IntegerField(blank=True, null=True)
    write_uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1)
    dbname = models.CharField(max_length=-1, blank=True, null=True)
    level = models.CharField(max_length=-1, blank=True, null=True)
    path = models.CharField(max_length=-1)
    func = models.CharField(max_length=-1)
    line = models.CharField(max_length=-1)
    message = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_logging'


class IrMailServer(models.Model):
    smtp_port = models.IntegerField()
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    from_filter = models.CharField(max_length=-1, blank=True, null=True)
    smtp_host = models.CharField(max_length=-1)
    smtp_authentication = models.CharField(max_length=-1)
    smtp_user = models.CharField(max_length=-1, blank=True, null=True)
    smtp_pass = models.CharField(max_length=-1, blank=True, null=True)
    smtp_encryption = models.CharField(max_length=-1)
    smtp_debug = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    smtp_ssl_certificate = models.BinaryField(blank=True, null=True)
    smtp_ssl_private_key = models.BinaryField(blank=True, null=True)
    google_gmail_access_token_expiration = models.IntegerField(blank=True, null=True)
    google_gmail_authorization_code = models.CharField(max_length=-1, blank=True, null=True)
    google_gmail_refresh_token = models.CharField(max_length=-1, blank=True, null=True)
    google_gmail_access_token = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_mail_server'


class IrModel(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    model = models.CharField(unique=True, max_length=-1)
    order = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    info = models.TextField(blank=True, null=True)
    transient = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    is_mail_thread = models.BooleanField(blank=True, null=True)
    is_mail_activity = models.BooleanField(blank=True, null=True)
    is_mail_blacklist = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model'


class IrModelAccess(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_access'


class IrModelConstraint(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    definition = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=1)
    message = models.JSONField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_constraint'
        unique_together = (('name', 'module'),)


class IrModelData(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    noupdate = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=-1)
    module = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'ir_model_data'
        unique_together = (('module', 'name'),)


class IrModelFields(models.Model):
    relation_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    related_field = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1)  # Field renamed because of name conflict.
    relation = models.CharField(max_length=-1, blank=True, null=True)
    relation_field_0 = models.CharField(db_column='relation_field', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    ttype = models.CharField(max_length=-1)
    related = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1)
    on_delete = models.CharField(max_length=-1, blank=True, null=True)
    domain = models.CharField(max_length=-1, blank=True, null=True)
    relation_table = models.CharField(max_length=-1, blank=True, null=True)
    column1 = models.CharField(max_length=-1, blank=True, null=True)
    column2 = models.CharField(max_length=-1, blank=True, null=True)
    depends = models.CharField(max_length=-1, blank=True, null=True)
    field_description = models.JSONField()
    help = models.JSONField(blank=True, null=True)
    compute = models.TextField(blank=True, null=True)
    copied = models.BooleanField(blank=True, null=True)
    required = models.BooleanField(blank=True, null=True)
    readonly = models.BooleanField(blank=True, null=True)
    index = models.BooleanField(blank=True, null=True)
    translate = models.BooleanField(blank=True, null=True)
    group_expand = models.BooleanField(blank=True, null=True)
    selectable = models.BooleanField(blank=True, null=True)
    store = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    tracking = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields'
        unique_together = (('model_0', 'name'),)


class IrModelFieldsGroupRel(models.Model):
    field = models.OneToOneField(IrModelFields, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_group_rel'
        unique_together = (('field', 'group'),)


class IrModelFieldsSelection(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value = models.CharField(max_length=-1)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_fields_selection'
        unique_together = (('field', 'value'),)


class IrModelRelation(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, db_column='model')
    module = models.ForeignKey('IrModuleModule', models.DO_NOTHING, db_column='module')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_model_relation'


class IrModuleCategory(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    name = models.JSONField()
    sequence = models.IntegerField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    visible = models.BooleanField(blank=True, null=True)
    exclusive = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_category'


class IrModuleModule(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.JSONField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    author = models.CharField(max_length=-1, blank=True, null=True)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=16, blank=True, null=True)
    latest_version = models.CharField(max_length=-1, blank=True, null=True)
    shortdesc = models.JSONField(blank=True, null=True)
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    application = models.BooleanField(blank=True, null=True)
    demo = models.BooleanField(blank=True, null=True)
    web = models.BooleanField(blank=True, null=True)
    license = models.CharField(max_length=32, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    auto_install = models.BooleanField(blank=True, null=True)
    to_buy = models.BooleanField(blank=True, null=True)
    maintainer = models.CharField(max_length=-1, blank=True, null=True)
    published_version = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)
    contributors = models.TextField(blank=True, null=True)
    menus_by_module = models.TextField(blank=True, null=True)
    reports_by_module = models.TextField(blank=True, null=True)
    views_by_module = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module'


class IrModuleModuleDependency(models.Model):
    name = models.CharField(max_length=-1, blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    auto_install_required = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_dependency'


class IrModuleModuleExclusion(models.Model):
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_module_module_exclusion'


class IrProfile(models.Model):
    sql_count = models.IntegerField(blank=True, null=True)
    entry_count = models.IntegerField(blank=True, null=True)
    session = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    init_stack_trace = models.TextField(blank=True, null=True)
    sql = models.TextField(blank=True, null=True)
    traces_async = models.TextField(blank=True, null=True)
    traces_sync = models.TextField(blank=True, null=True)
    qweb = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_profile'


class IrProperty(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    fields = models.ForeignKey(IrModelFields, models.DO_NOTHING)
    value_integer = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    res_id = models.CharField(max_length=-1, blank=True, null=True)
    value_reference = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    value_text = models.TextField(blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_float = models.FloatField(blank=True, null=True)
    value_binary = models.BinaryField(blank=True, null=True)

    # A unique constraint could not be introspected.
    class Meta:
        managed = False
        db_table = 'ir_property'


class IrRule(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    domain_force = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    perm_read = models.BooleanField(blank=True, null=True)
    perm_write = models.BooleanField(blank=True, null=True)
    perm_create = models.BooleanField(blank=True, null=True)
    perm_unlink = models.BooleanField(blank=True, null=True)
    global_field = models.BooleanField(db_column='global', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_rule'


class IrSequence(models.Model):
    number_next = models.IntegerField()
    number_increment = models.IntegerField()
    padding = models.IntegerField()
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1, blank=True, null=True)
    implementation = models.CharField(max_length=-1)
    prefix = models.CharField(max_length=-1, blank=True, null=True)
    suffix = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_date_range = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence'


class IrSequenceDateRange(models.Model):
    sequence = models.ForeignKey(IrSequence, models.DO_NOTHING)
    number_next = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    date_from = models.DateField()
    date_to = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_sequence_date_range'


class IrServerObjectLines(models.Model):
    server = models.ForeignKey(IrActServer, models.DO_NOTHING, blank=True, null=True)
    col1 = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='col1')
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    evaluation_type = models.CharField(max_length=-1)
    value = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_server_object_lines'


class IrUiMenu(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    web_icon = models.CharField(max_length=-1, blank=True, null=True)
    action = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_menu'


class IrUiMenuGroupRel(models.Model):
    menu = models.OneToOneField(IrUiMenu, models.DO_NOTHING, primary_key=True)
    gid = models.ForeignKey('ResGroups', models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'ir_ui_menu_group_rel'
        unique_together = (('menu', 'gid'),)


class IrUiView(models.Model):
    priority = models.IntegerField()
    inherit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    model = models.CharField(max_length=-1, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    arch_fs = models.CharField(max_length=-1, blank=True, null=True)
    field_parent = models.CharField(max_length=-1, blank=True, null=True)
    mode = models.CharField(max_length=-1)
    arch_db = models.JSONField(blank=True, null=True)
    arch_prev = models.TextField(blank=True, null=True)
    arch_updated = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    customize_show = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view'


class IrUiViewCustom(models.Model):
    ref = models.ForeignKey(IrUiView, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    arch = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_custom'


class IrUiViewGroupRel(models.Model):
    view = models.OneToOneField(IrUiView, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ir_ui_view_group_rel'
        unique_together = (('view', 'group'),)


class JobFavoriteUserRel(models.Model):
    job = models.OneToOneField(HrJob, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_favorite_user_rel'
        unique_together = (('job', 'user'),)


class JournalAccountControlRel(models.Model):
    journal = models.OneToOneField(AccountJournal, models.DO_NOTHING, primary_key=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'journal_account_control_rel'
        unique_together = (('journal', 'account'),)


class L10NIdEfakturEfakturRange(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    available = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    max = models.CharField(max_length=-1, blank=True, null=True)
    min = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l10n_id_efaktur_efaktur_range'


class LinkTracker(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    url = models.CharField(max_length=-1)
    title = models.CharField(max_length=-1, blank=True, null=True)
    label = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker'


class LinkTrackerClick(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    ip = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mailing_trace = models.ForeignKey('MailingTrace', models.DO_NOTHING, blank=True, null=True)
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker_click'


class LinkTrackerCode(models.Model):
    link = models.ForeignKey(LinkTracker, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'link_tracker_code'


class LotLabelLayout(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    label_quantity = models.CharField(max_length=-1)
    print_format = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lot_label_layout'


class LotLabelLayoutStockPickingRel(models.Model):
    lot_label_layout = models.OneToOneField(LotLabelLayout, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'lot_label_layout_stock_picking_rel'
        unique_together = (('lot_label_layout', 'stock_picking'),)


class MailActivity(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    res_id = models.IntegerField(blank=True, null=True)
    activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    request_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    recommended_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    previous_activity_type = models.ForeignKey('MailActivityType', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    summary = models.CharField(max_length=-1, blank=True, null=True)
    date_deadline = models.DateField()
    note = models.TextField(blank=True, null=True)
    automated = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    calendar_event = models.ForeignKey(CalendarEvent, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity'


class MailActivityRel(models.Model):
    activity = models.OneToOneField('MailActivityType', models.DO_NOTHING, primary_key=True)
    recommended = models.ForeignKey('MailActivityType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_rel'
        unique_together = (('activity', 'recommended'),)


class MailActivityType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    delay_count = models.IntegerField(blank=True, null=True)
    triggered_next_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    default_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    delay_unit = models.CharField(max_length=-1)
    delay_from = models.CharField(max_length=-1)
    icon = models.CharField(max_length=-1, blank=True, null=True)
    decoration_type = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    chaining_type = models.CharField(max_length=-1)
    category = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    summary = models.JSONField(blank=True, null=True)
    default_note = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_activity_type'


class MailActivityTypeMailTemplateRel(models.Model):
    mail_activity_type = models.OneToOneField(MailActivityType, models.DO_NOTHING, primary_key=True)
    mail_template = models.ForeignKey('MailTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_activity_type_mail_template_rel'
        unique_together = (('mail_activity_type', 'mail_template'),)


class MailAlias(models.Model):
    alias_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    alias_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    alias_force_thread_id = models.IntegerField(blank=True, null=True)
    alias_parent_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    alias_parent_thread_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    alias_name = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    alias_contact = models.CharField(max_length=-1)
    alias_bounced_content = models.JSONField(blank=True, null=True)
    alias_defaults = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_alias'


class MailBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist'


class MailBlacklistRemove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=-1)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_blacklist_remove'


class MailChannel(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    group_public = models.ForeignKey('ResGroups', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    channel_type = models.CharField(max_length=-1)
    default_display_mode = models.CharField(max_length=-1, blank=True, null=True)
    uuid = models.CharField(unique=True, max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel'


class MailChannelMember(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey('MailGuest', models.DO_NOTHING, blank=True, null=True)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING)
    fetched_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    seen_message = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    rtc_inviting_session = models.ForeignKey('MailChannelRtcSession', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    custom_channel_name = models.CharField(max_length=-1, blank=True, null=True)
    fold_state = models.CharField(max_length=-1, blank=True, null=True)
    is_minimized = models.BooleanField(blank=True, null=True)
    is_pinned = models.BooleanField(blank=True, null=True)
    last_interest_dt = models.DateTimeField(blank=True, null=True)
    last_seen_dt = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_member'
        unique_together = (('channel', 'guest'), ('channel', 'partner'),)


class MailChannelResGroupsRel(models.Model):
    mail_channel = models.OneToOneField(MailChannel, models.DO_NOTHING, primary_key=True)
    res_groups = models.ForeignKey('ResGroups', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_channel_res_groups_rel'
        unique_together = (('mail_channel', 'res_groups'),)


class MailChannelRtcSession(models.Model):
    channel_member = models.OneToOneField(MailChannelMember, models.DO_NOTHING)
    channel = models.ForeignKey(MailChannel, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    is_screen_sharing_on = models.BooleanField(blank=True, null=True)
    is_camera_on = models.BooleanField(blank=True, null=True)
    is_muted = models.BooleanField(blank=True, null=True)
    is_deaf = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_channel_rtc_session'


class MailComposeMessage(models.Model):
    template = models.ForeignKey('MailTemplate', models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('MailMessage', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    email_layout_xmlid = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    composition_mode = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    message_type = models.CharField(max_length=-1)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    active_domain = models.TextField(blank=True, null=True)
    email_add_signature = models.BooleanField(blank=True, null=True)
    use_active_domain = models.BooleanField(blank=True, null=True)
    is_log = models.BooleanField(blank=True, null=True)
    notify = models.BooleanField(blank=True, null=True)
    reply_to_force_new = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    auto_delete_message = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mass_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    mass_mailing_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_compose_message'


class MailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class MailComposeMessageMailingListRel(models.Model):
    mail_compose_message = models.OneToOneField(MailComposeMessage, models.DO_NOTHING, primary_key=True)
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_mailing_list_rel'
        unique_together = (('mail_compose_message', 'mailing_list'),)


class MailComposeMessageResPartnerRel(models.Model):
    wizard = models.OneToOneField(MailComposeMessage, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_compose_message_res_partner_rel'
        unique_together = (('wizard', 'partner'),)


class MailFollowers(models.Model):
    res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    res_model = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mail_followers'
        unique_together = (('res_model', 'res_id', 'partner'),)


class MailFollowersMailMessageSubtypeRel(models.Model):
    mail_followers = models.OneToOneField(MailFollowers, models.DO_NOTHING, primary_key=True)
    mail_message_subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_followers_mail_message_subtype_rel'
        unique_together = (('mail_followers', 'mail_message_subtype'),)


class MailGatewayAllowed(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    email_normalized = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_gateway_allowed'


class MailGuest(models.Model):
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    access_token = models.CharField(max_length=-1)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    timezone = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_guest'


class MailIceServer(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    server_type = models.CharField(max_length=-1)
    uri = models.CharField(max_length=-1)
    username = models.CharField(max_length=-1, blank=True, null=True)
    credential = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_ice_server'


class MailLinkPreview(models.Model):
    message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    source_url = models.CharField(max_length=-1)
    og_type = models.CharField(max_length=-1, blank=True, null=True)
    og_title = models.CharField(max_length=-1, blank=True, null=True)
    og_image = models.CharField(max_length=-1, blank=True, null=True)
    og_mimetype = models.CharField(max_length=-1, blank=True, null=True)
    image_mimetype = models.CharField(max_length=-1, blank=True, null=True)
    og_description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_link_preview'


class MailMail(models.Model):
    mail_message = models.ForeignKey('MailMessage', models.DO_NOTHING)
    fetchmail_server = models.ForeignKey(FetchmailServer, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    failure_type = models.CharField(max_length=-1, blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    references = models.TextField(blank=True, null=True)
    headers = models.TextField(blank=True, null=True)
    email_to = models.TextField(blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    is_notification = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    to_delete = models.BooleanField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_mail'


class MailMailResPartnerRel(models.Model):
    mail_mail = models.OneToOneField(MailMail, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mail_res_partner_rel'
        unique_together = (('mail_mail', 'res_partner'),)


class MailMassMailingListRel(models.Model):
    mailing_list = models.OneToOneField('MailingList', models.DO_NOTHING, primary_key=True)
    mailing_mailing = models.ForeignKey('MailingMailing', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_mass_mailing_list_rel'
        unique_together = (('mailing_list', 'mailing_mailing'),)


class MailMessage(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    subtype = models.ForeignKey('MailMessageSubtype', models.DO_NOTHING, blank=True, null=True)
    mail_activity_type = models.ForeignKey(MailActivityType, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    author_guest = models.ForeignKey(MailGuest, models.DO_NOTHING, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    record_name = models.CharField(max_length=-1, blank=True, null=True)
    message_type = models.CharField(max_length=-1)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    message_id = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    email_layout_xmlid = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    reply_to_force_new = models.BooleanField(blank=True, null=True)
    email_add_signature = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message'


class MailMessageReaction(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey(MailGuest, models.DO_NOTHING, blank=True, null=True)
    content = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'mail_message_reaction'
        unique_together = (('message', 'content', 'guest'), ('message', 'content', 'partner'),)


class MailMessageResPartnerRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageResPartnerStarredRel(models.Model):
    mail_message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_message_res_partner_starred_rel'
        unique_together = (('mail_message', 'res_partner'),)


class MailMessageSchedule(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    notification_parameters = models.TextField(blank=True, null=True)
    scheduled_datetime = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_schedule'


class MailMessageSubtype(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    relation_field = models.CharField(max_length=-1, blank=True, null=True)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    internal = models.BooleanField(blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    hidden = models.BooleanField(blank=True, null=True)
    track_recipients = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_message_subtype'


class MailNotification(models.Model):
    author = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    notification_type = models.CharField(max_length=-1)
    notification_status = models.CharField(max_length=-1, blank=True, null=True)
    failure_type = models.CharField(max_length=-1, blank=True, null=True)
    failure_reason = models.TextField(blank=True, null=True)
    is_read = models.BooleanField(blank=True, null=True)
    read_date = models.DateTimeField(blank=True, null=True)
    sms = models.ForeignKey('SmsSms', models.DO_NOTHING, blank=True, null=True)
    sms_number = models.CharField(max_length=-1, blank=True, null=True)
    letter = models.ForeignKey('SnailmailLetter', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_notification'
        unique_together = (('mail_message', 'res_partner'),)


class MailNotificationMailResendMessageRel(models.Model):
    mail_resend_message = models.OneToOneField('MailResendMessage', models.DO_NOTHING, primary_key=True)
    mail_notification = models.ForeignKey(MailNotification, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_notification_mail_resend_message_rel'
        unique_together = (('mail_resend_message', 'mail_notification'),)


class MailResendMessage(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_message'


class MailResendPartner(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    resend_wizard = models.ForeignKey(MailResendMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    message = models.CharField(max_length=-1, blank=True, null=True)
    resend = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_resend_partner'


class MailShortcode(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    source = models.CharField(max_length=-1)
    description = models.CharField(max_length=-1, blank=True, null=True)
    substitution = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_shortcode'


class MailTemplate(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    ref_ir_act_window = models.ForeignKey(IrActWindow, models.DO_NOTHING, db_column='ref_ir_act_window', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    template_fs = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    email_to = models.CharField(max_length=-1, blank=True, null=True)
    partner_to = models.CharField(max_length=-1, blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    scheduled_date = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    description = models.JSONField(blank=True, null=True)
    subject = models.JSONField(blank=True, null=True)
    body_html = models.JSONField(blank=True, null=True)
    report_name = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_default_to = models.BooleanField(blank=True, null=True)
    auto_delete = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template'


class MailTemplateMailTemplateResetRel(models.Model):
    mail_template_reset = models.OneToOneField('MailTemplateReset', models.DO_NOTHING, primary_key=True)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_template_mail_template_reset_rel'
        unique_together = (('mail_template_reset', 'mail_template'),)


class MailTemplatePreview(models.Model):
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    resource_ref = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    error_msg = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template_preview'


class MailTemplateReset(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_template_reset'


class MailTrackingValue(models.Model):
    field = models.ForeignKey(IrModelFields, models.DO_NOTHING, db_column='field')
    old_value_integer = models.IntegerField(blank=True, null=True)
    new_value_integer = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    tracking_sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    field_desc = models.CharField(max_length=-1)
    field_type = models.CharField(max_length=-1, blank=True, null=True)
    old_value_char = models.CharField(max_length=-1, blank=True, null=True)
    new_value_char = models.CharField(max_length=-1, blank=True, null=True)
    old_value_text = models.TextField(blank=True, null=True)
    new_value_text = models.TextField(blank=True, null=True)
    old_value_datetime = models.DateTimeField(blank=True, null=True)
    new_value_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    old_value_float = models.FloatField(blank=True, null=True)
    old_value_monetary = models.FloatField(blank=True, null=True)
    new_value_float = models.FloatField(blank=True, null=True)
    new_value_monetary = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_tracking_value'


class MailWizardInvite(models.Model):
    res_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    message = models.TextField(blank=True, null=True)
    send_mail = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite'


class MailWizardInviteResPartnerRel(models.Model):
    mail_wizard_invite = models.OneToOneField(MailWizardInvite, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mail_wizard_invite_res_partner_rel'
        unique_together = (('mail_wizard_invite', 'res_partner'),)


class MailingContact(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_normalized = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    company_name = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_contact'


class MailingContactImport(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    contact_list = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_contact_import'


class MailingContactImportMailingListRel(models.Model):
    mailing_contact_import = models.OneToOneField(MailingContactImport, models.DO_NOTHING, primary_key=True)
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_import_mailing_list_rel'
        unique_together = (('mailing_contact_import', 'mailing_list'),)


class MailingContactListRel(models.Model):
    contact = models.ForeignKey(MailingContact, models.DO_NOTHING)
    list = models.ForeignKey('MailingList', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    opt_out = models.BooleanField(blank=True, null=True)
    unsubscription_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_contact_list_rel'
        unique_together = (('contact', 'list'),)


class MailingContactMailingContactToListRel(models.Model):
    mailing_contact_to_list = models.OneToOneField('MailingContactToList', models.DO_NOTHING, primary_key=True)
    mailing_contact = models.ForeignKey(MailingContact, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_mailing_contact_to_list_rel'
        unique_together = (('mailing_contact_to_list', 'mailing_contact'),)


class MailingContactResPartnerCategoryRel(models.Model):
    mailing_contact = models.OneToOneField(MailingContact, models.DO_NOTHING, primary_key=True)
    res_partner_category = models.ForeignKey('ResPartnerCategory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_contact_res_partner_category_rel'
        unique_together = (('mailing_contact', 'res_partner_category'),)


class MailingContactToList(models.Model):
    mailing_list = models.ForeignKey('MailingList', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_contact_to_list'


class MailingFilter(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    mailing_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    mailing_domain = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_filter'


class MailingList(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    is_public = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_list'


class MailingListMailingListMergeRel(models.Model):
    mailing_list_merge = models.OneToOneField('MailingListMerge', models.DO_NOTHING, primary_key=True)
    mailing_list = models.ForeignKey(MailingList, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mailing_list_mailing_list_merge_rel'
        unique_together = (('mailing_list_merge', 'mailing_list'),)


class MailingListMerge(models.Model):
    dest_list = models.ForeignKey(MailingList, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    merge_options = models.CharField(max_length=-1)
    new_list_name = models.CharField(max_length=-1, blank=True, null=True)
    archive_src_lists = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_list_merge'


class MailingMailing(models.Model):
    source = models.ForeignKey('UtmSource', models.DO_NOTHING)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    mailing_model = models.ForeignKey(IrModel, models.DO_NOTHING)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    mailing_filter = models.ForeignKey(MailingFilter, models.DO_NOTHING, blank=True, null=True)
    ab_testing_pc = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1)
    preview = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1)
    schedule_type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    mailing_type = models.CharField(max_length=-1)
    reply_to_mode = models.CharField(max_length=-1, blank=True, null=True)
    reply_to = models.CharField(max_length=-1, blank=True, null=True)
    mailing_domain = models.CharField(max_length=-1, blank=True, null=True)
    body_arch = models.TextField(blank=True, null=True)
    body_html = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    favorite = models.BooleanField(blank=True, null=True)
    keep_archives = models.BooleanField(blank=True, null=True)
    ab_testing_completed = models.BooleanField(blank=True, null=True)
    ab_testing_enabled = models.BooleanField(blank=True, null=True)
    kpi_mail_required = models.BooleanField(blank=True, null=True)
    favorite_date = models.DateTimeField(blank=True, null=True)
    sent_date = models.DateTimeField(blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    calendar_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_mailing'


class MailingMailingScheduleDate(models.Model):
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_mailing_schedule_date'


class MailingMailingTest(models.Model):
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_to = models.TextField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_mailing_test'


class MailingTrace(models.Model):
    mail_mail = models.ForeignKey(MailMail, models.DO_NOTHING, blank=True, null=True)
    mail_mail_id_int = models.IntegerField(blank=True, null=True)
    res_id = models.IntegerField(blank=True, null=True)
    mass_mailing = models.ForeignKey(MailingMailing, models.DO_NOTHING, blank=True, null=True)
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    trace_type = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1, blank=True, null=True)
    message_id = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1)
    trace_status = models.CharField(max_length=-1, blank=True, null=True)
    failure_type = models.CharField(max_length=-1, blank=True, null=True)
    sent_datetime = models.DateTimeField(blank=True, null=True)
    open_datetime = models.DateTimeField(blank=True, null=True)
    reply_datetime = models.DateTimeField(blank=True, null=True)
    links_click_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mailing_trace'


class MaintenanceEquipment(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    technician_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    owner_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey('MaintenanceEquipmentCategory', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    maintenance_count = models.IntegerField(blank=True, null=True)
    maintenance_open_count = models.IntegerField(blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    maintenance_team = models.ForeignKey('MaintenanceTeam', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_ref = models.CharField(max_length=-1, blank=True, null=True)
    location = models.CharField(max_length=-1, blank=True, null=True)
    model = models.CharField(max_length=-1, blank=True, null=True)
    serial_no = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    assign_date = models.DateField(blank=True, null=True)
    effective_date = models.DateField()
    warranty_date = models.DateField(blank=True, null=True)
    scrap_date = models.DateField(blank=True, null=True)
    next_action_date = models.DateField(blank=True, null=True)
    name = models.JSONField()
    note = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    cost = models.FloatField(blank=True, null=True)
    maintenance_duration = models.FloatField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(HrDepartment, models.DO_NOTHING, blank=True, null=True)
    equipment_assign_to = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'maintenance_equipment'


class MaintenanceEquipmentCategory(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    technician_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    note = models.JSONField(blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_equipment_category'


class MaintenanceRequest(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    owner_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(MaintenanceEquipmentCategory, models.DO_NOTHING, blank=True, null=True)
    equipment = models.ForeignKey(MaintenanceEquipment, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('MaintenanceStage', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    maintenance_team = models.ForeignKey('MaintenanceTeam', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    kanban_state = models.CharField(max_length=-1)
    maintenance_type = models.CharField(max_length=-1, blank=True, null=True)
    request_date = models.DateField(blank=True, null=True)
    close_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    archive = models.BooleanField(blank=True, null=True)
    schedule_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    employee = models.ForeignKey(HrEmployee, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_request'


class MaintenanceStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    fold = models.BooleanField(blank=True, null=True)
    done = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_stage'


class MaintenanceTeam(models.Model):
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'maintenance_team'


class MaintenanceTeamUsersRel(models.Model):
    maintenance_team = models.OneToOneField(MaintenanceTeam, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'maintenance_team_users_rel'
        unique_together = (('maintenance_team', 'res_users'),)


class MassMailingIrAttachmentsRel(models.Model):
    mass_mailing = models.OneToOneField(MailingMailing, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mass_mailing_ir_attachments_rel'
        unique_together = (('mass_mailing', 'attachment'),)


class MeetingCategoryRel(models.Model):
    event = models.OneToOneField(CalendarEvent, models.DO_NOTHING, primary_key=True)
    type = models.ForeignKey(CalendarEventType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'meeting_category_rel'
        unique_together = (('event', 'type'),)


class MessageAttachmentRel(models.Model):
    message = models.OneToOneField(MailMessage, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'message_attachment_rel'
        unique_together = (('message', 'attachment'),)


class MrpBom(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1)
    ready_to_produce = models.CharField(max_length=-1)
    consumption = models.CharField(max_length=-1)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    allow_operation_dependencies = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_bom'


class MrpBomByproduct(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey('MrpRoutingWorkcenter', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    cost_share = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_bom_byproduct'


class MrpBomByproductProductTemplateAttributeValueRel(models.Model):
    mrp_bom_byproduct = models.OneToOneField(MrpBomByproduct, models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_bom_byproduct_product_template_attribute_value_rel'
        unique_together = (('mrp_bom_byproduct', 'product_template_attribute_value'),)


class MrpBomLine(models.Model):
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING)
    operation = models.ForeignKey('MrpRoutingWorkcenter', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    manual_consumption = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_bom_line'


class MrpBomLineProductTemplateAttributeValueRel(models.Model):
    mrp_bom_line = models.OneToOneField(MrpBomLine, models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_bom_line_product_template_attribute_value_rel'
        unique_together = (('mrp_bom_line', 'product_template_attribute_value'),)


class MrpConsumptionWarning(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning'


class MrpConsumptionWarningLine(models.Model):
    mrp_consumption_warning = models.ForeignKey(MrpConsumptionWarning, models.DO_NOTHING)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_consumed_qty_uom = models.FloatField(blank=True, null=True)
    product_expected_qty_uom = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning_line'


class MrpConsumptionWarningMrpProductionRel(models.Model):
    mrp_consumption_warning = models.OneToOneField(MrpConsumptionWarning, models.DO_NOTHING, primary_key=True)
    mrp_production = models.ForeignKey('MrpProduction', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_consumption_warning_mrp_production_rel'
        unique_together = (('mrp_consumption_warning', 'mrp_production'),)


class MrpDocument(models.Model):
    ir_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_document'


class MrpImmediateProduction(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_immediate_production'


class MrpImmediateProductionLine(models.Model):
    immediate_production = models.ForeignKey(MrpImmediateProduction, models.DO_NOTHING)
    production = models.ForeignKey('MrpProduction', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to_immediate = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_immediate_production_line'


class MrpProduction(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    backorder_sequence = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    lot_producing = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    location_src = models.ForeignKey('StockLocation', models.DO_NOTHING)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    procurement_group = models.ForeignKey('ProcurementGroup', models.DO_NOTHING, blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    production_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    reservation_state = models.CharField(max_length=-1, blank=True, null=True)
    product_description_variants = models.CharField(max_length=-1, blank=True, null=True)
    consumption = models.CharField(max_length=-1)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_producing = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    is_planned = models.BooleanField(blank=True, null=True)
    allow_workorder_dependencies = models.BooleanField(blank=True, null=True)
    date_planned_start = models.DateTimeField()
    date_planned_finished = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_uom_qty = models.FloatField(blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    extra_cost = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production'
        unique_together = (('name', 'company'),)


class MrpProductionBackorder(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_backorder'


class MrpProductionBackorderLine(models.Model):
    mrp_production_backorder = models.ForeignKey(MrpProductionBackorder, models.DO_NOTHING)
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to_backorder = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_backorder_line'


class MrpProductionMrpProductionBackorderRel(models.Model):
    mrp_production_backorder = models.OneToOneField(MrpProductionBackorder, models.DO_NOTHING, primary_key=True)
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_production_mrp_production_backorder_rel'
        unique_together = (('mrp_production_backorder', 'mrp_production'),)


class MrpProductionProductionRel(models.Model):
    mrp_immediate_production = models.OneToOneField(MrpImmediateProduction, models.DO_NOTHING, primary_key=True)
    mrp_production = models.ForeignKey(MrpProduction, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_production_production_rel'
        unique_together = (('mrp_immediate_production', 'mrp_production'),)


class MrpProductionSplit(models.Model):
    production_split_multi = models.ForeignKey('MrpProductionSplitMulti', models.DO_NOTHING, blank=True, null=True)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    counter = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_split'


class MrpProductionSplitLine(models.Model):
    mrp_production_split = models.ForeignKey(MrpProductionSplit, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_split_line'


class MrpProductionSplitMulti(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_production_split_multi'


class MrpRoutingWorkcenter(models.Model):
    workcenter = models.ForeignKey('MrpWorkcenter', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING)
    time_mode_batch = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    worksheet_type = models.CharField(max_length=-1, blank=True, null=True)
    worksheet_google_slide = models.CharField(max_length=-1, blank=True, null=True)
    time_mode = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    time_cycle_manual = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter'


class MrpRoutingWorkcenterDependenciesRel(models.Model):
    operation = models.OneToOneField(MrpRoutingWorkcenter, models.DO_NOTHING, primary_key=True)
    blocked_by = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter_dependencies_rel'
        unique_together = (('operation', 'blocked_by'),)


class MrpRoutingWorkcenterProductTemplateAttributeValueRel(models.Model):
    mrp_routing_workcenter = models.OneToOneField(MrpRoutingWorkcenter, models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_routing_workcenter_product_template_attribute_value_rel'
        unique_together = (('mrp_routing_workcenter', 'product_template_attribute_value'),)


class MrpUnbuild(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True)
    mo = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    product_qty = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mrp_unbuild'


class MrpWorkcenter(models.Model):
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField()
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    code = models.CharField(max_length=-1, blank=True, null=True)
    working_state = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    time_efficiency = models.FloatField(blank=True, null=True)
    default_capacity = models.FloatField(blank=True, null=True)
    costs_hour = models.FloatField(blank=True, null=True)
    time_start = models.FloatField(blank=True, null=True)
    time_stop = models.FloatField(blank=True, null=True)
    oee_target = models.FloatField(blank=True, null=True)
    costs_hour_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter'


class MrpWorkcenterAlternativeRel(models.Model):
    workcenter = models.OneToOneField(MrpWorkcenter, models.DO_NOTHING, primary_key=True)
    alternative_workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_alternative_rel'
        unique_together = (('workcenter', 'alternative_workcenter'),)


class MrpWorkcenterCapacity(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    capacity = models.FloatField(blank=True, null=True)
    time_start = models.FloatField(blank=True, null=True)
    time_stop = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_capacity'
        unique_together = (('workcenter', 'product'),)


class MrpWorkcenterMrpWorkcenterTagRel(models.Model):
    mrp_workcenter = models.OneToOneField(MrpWorkcenter, models.DO_NOTHING, primary_key=True)
    mrp_workcenter_tag = models.ForeignKey('MrpWorkcenterTag', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_mrp_workcenter_tag_rel'
        unique_together = (('mrp_workcenter', 'mrp_workcenter_tag'),)


class MrpWorkcenterProductivity(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    workorder = models.ForeignKey('MrpWorkorder', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    loss = models.ForeignKey('MrpWorkcenterProductivityLoss', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    loss_type = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    cost_already_recorded = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity'


class MrpWorkcenterProductivityLoss(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    loss = models.ForeignKey('MrpWorkcenterProductivityLossType', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    loss_type = models.CharField(max_length=-1, blank=True, null=True)
    manual = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity_loss'


class MrpWorkcenterProductivityLossType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    loss_type = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_productivity_loss_type'


class MrpWorkcenterTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workcenter_tag'


class MrpWorkorder(models.Model):
    workcenter = models.ForeignKey(MrpWorkcenter, models.DO_NOTHING)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING)
    leave = models.ForeignKey('ResourceCalendarLeaves', models.DO_NOTHING, blank=True, null=True)
    duration_percent = models.IntegerField(blank=True, null=True)
    operation = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    production_availability = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    qty_produced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    duration_expected = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_reported_from_previous_wo = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date_planned_start = models.DateTimeField(blank=True, null=True)
    date_planned_finished = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_finished = models.DateTimeField(blank=True, null=True)
    production_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    duration_unit = models.FloatField(blank=True, null=True)
    costs_hour = models.FloatField(blank=True, null=True)
    mo_analytic_account_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING, blank=True, null=True)
    wc_analytic_account_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mrp_workorder'


class MrpWorkorderDependenciesRel(models.Model):
    workorder = models.OneToOneField(MrpWorkorder, models.DO_NOTHING, primary_key=True)
    blocked_by = models.ForeignKey(MrpWorkorder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mrp_workorder_dependencies_rel'
        unique_together = (('workorder', 'blocked_by'),)


class PaymentCountryRel(models.Model):
    payment = models.OneToOneField('PaymentProvider', models.DO_NOTHING, primary_key=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_country_rel'
        unique_together = (('payment', 'country'),)


class PaymentIcon(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_icon'


class PaymentIconPaymentProviderRel(models.Model):
    payment_provider = models.OneToOneField('PaymentProvider', models.DO_NOTHING, primary_key=True)
    payment_icon = models.ForeignKey(PaymentIcon, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payment_icon_payment_provider_rel'
        unique_together = (('payment_provider', 'payment_icon'),)


class PaymentLinkWizard(models.Model):
    res_id = models.IntegerField()
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    description = models.CharField(max_length=-1, blank=True, null=True)
    payment_provider_selection = models.CharField(max_length=-1)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    amount_max = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_link_wizard'


class PaymentProvider(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    redirect_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    inline_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    token_inline_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    express_checkout_form_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    module_state = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    display_as = models.JSONField(blank=True, null=True)
    pre_msg = models.JSONField(blank=True, null=True)
    pending_msg = models.JSONField(blank=True, null=True)
    auth_msg = models.JSONField(blank=True, null=True)
    done_msg = models.JSONField(blank=True, null=True)
    cancel_msg = models.JSONField(blank=True, null=True)
    maximum_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_published = models.BooleanField(blank=True, null=True)
    allow_tokenization = models.BooleanField(blank=True, null=True)
    capture_manually = models.BooleanField(blank=True, null=True)
    allow_express_checkout = models.BooleanField(blank=True, null=True)
    fees_active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    fees_dom_fixed = models.FloatField(blank=True, null=True)
    fees_dom_var = models.FloatField(blank=True, null=True)
    fees_int_fixed = models.FloatField(blank=True, null=True)
    fees_int_var = models.FloatField(blank=True, null=True)
    so_reference_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_provider'


class PaymentProviderOnboardingWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    payment_method = models.CharField(max_length=-1, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=-1, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=-1, blank=True, null=True)
    manual_name = models.CharField(max_length=-1, blank=True, null=True)
    journal_name = models.CharField(max_length=-1, blank=True, null=True)
    acc_number = models.CharField(max_length=-1, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_provider_onboarding_wizard'


class PaymentRefundWizard(models.Model):
    payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    amount_to_refund = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_refund_wizard'


class PaymentToken(models.Model):
    provider = models.ForeignKey(PaymentProvider, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    payment_details = models.CharField(max_length=-1, blank=True, null=True)
    provider_ref = models.CharField(max_length=-1)
    verified = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_token'


class PaymentTransaction(models.Model):
    provider = models.ForeignKey(PaymentProvider, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    token = models.ForeignKey(PaymentToken, models.DO_NOTHING, blank=True, null=True)
    source_transaction = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    callback_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    callback_res_id = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    partner_state = models.ForeignKey('ResCountryState', models.DO_NOTHING, blank=True, null=True)
    partner_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    reference = models.CharField(unique=True, max_length=-1)
    provider_reference = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1)
    operation = models.CharField(max_length=-1, blank=True, null=True)
    landing_route = models.CharField(max_length=-1, blank=True, null=True)
    callback_method = models.CharField(max_length=-1, blank=True, null=True)
    callback_hash = models.CharField(max_length=-1, blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    partner_lang = models.CharField(max_length=-1, blank=True, null=True)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_address = models.CharField(max_length=-1, blank=True, null=True)
    partner_zip = models.CharField(max_length=-1, blank=True, null=True)
    partner_city = models.CharField(max_length=-1, blank=True, null=True)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    state_message = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=65535, decimal_places=65535)
    fees = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_post_processed = models.BooleanField(blank=True, null=True)
    tokenize = models.BooleanField(blank=True, null=True)
    callback_is_done = models.BooleanField(blank=True, null=True)
    last_state_change = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    payment = models.ForeignKey(AccountPayment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_transaction'


class PhoneBlacklist(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    number = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist'


class PhoneBlacklistRemove(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    phone = models.CharField(max_length=-1)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'phone_blacklist_remove'


class PickingLabelType(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    label_type = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'picking_label_type'


class PickingLabelTypeStockPickingRel(models.Model):
    picking_label_type = models.OneToOneField(PickingLabelType, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey('StockPicking', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'picking_label_type_stock_picking_rel'
        unique_together = (('picking_label_type', 'stock_picking'),)


class PortalShare(models.Model):
    res_id = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_share'


class PortalShareResPartnerRel(models.Model):
    portal_share = models.OneToOneField(PortalShare, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_share_res_partner_rel'
        unique_together = (('portal_share', 'res_partner'),)


class PortalWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    welcome_message = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard'


class PortalWizardResPartnerRel(models.Model):
    portal_wizard = models.OneToOneField(PortalWizard, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'portal_wizard_res_partner_rel'
        unique_together = (('portal_wizard', 'res_partner'),)


class PortalWizardUser(models.Model):
    wizard = models.ForeignKey(PortalWizard, models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'portal_wizard_user'


class PrivacyLog(models.Model):
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    anonymized_name = models.CharField(max_length=-1)
    anonymized_email = models.CharField(max_length=-1)
    execution_details = models.TextField(blank=True, null=True)
    records_description = models.TextField(blank=True, null=True)
    additional_note = models.TextField(blank=True, null=True)
    date = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'privacy_log'


class PrivacyLookupWizard(models.Model):
    log = models.ForeignKey(PrivacyLog, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    email = models.CharField(max_length=-1)
    execution_details = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'privacy_lookup_wizard'


class PrivacyLookupWizardLine(models.Model):
    wizard = models.ForeignKey(PrivacyLookupWizard, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField()
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    execution_details = models.CharField(max_length=-1, blank=True, null=True)
    has_active = models.BooleanField(blank=True, null=True)
    is_active = models.BooleanField(blank=True, null=True)
    is_unlinked = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'privacy_lookup_wizard_line'


class ProcurementGroup(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    move_type = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'procurement_group'


class ProductAttrExclusionValueIdsRel(models.Model):
    product_template_attribute_exclusion = models.OneToOneField('ProductTemplateAttributeExclusion', models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attr_exclusion_value_ids_rel'
        unique_together = (('product_template_attribute_exclusion', 'product_template_attribute_value'),)


class ProductAttribute(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_variant = models.CharField(max_length=-1)
    display_type = models.CharField(max_length=-1)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute'


class ProductAttributeCustomValue(models.Model):
    custom_product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    custom_value = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_custom_value'
        unique_together = (('custom_product_template_attribute_value', 'sale_order_line'),)


class ProductAttributeProductTemplateRel(models.Model):
    product_attribute = models.OneToOneField(ProductAttribute, models.DO_NOTHING, primary_key=True)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_product_template_rel'
        unique_together = (('product_attribute', 'product_template'),)


class ProductAttributeValue(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    html_color = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    is_custom = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_attribute_value'
        unique_together = (('name', 'attribute'),)


class ProductAttributeValueProductTemplateAttributeLineRel(models.Model):
    product_attribute_value = models.OneToOneField(ProductAttributeValue, models.DO_NOTHING, primary_key=True)
    product_template_attribute_line = models.ForeignKey('ProductTemplateAttributeLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_attribute_value_product_template_attribute_line_rel'
        unique_together = (('product_attribute_value', 'product_template_attribute_line'),)


class ProductCategory(models.Model):
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    removal_strategy = models.ForeignKey('ProductRemoval', models.DO_NOTHING, blank=True, null=True)
    packaging_reserve_method = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'


class ProductLabelLayout(models.Model):
    custom_quantity = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    print_format = models.CharField(max_length=-1)
    extra_html = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    picking_quantity = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'product_label_layout'


class ProductLabelLayoutProductProductRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey('ProductProduct', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_product_rel'
        unique_together = (('product_label_layout', 'product_product'),)


class ProductLabelLayoutProductTemplateRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, models.DO_NOTHING, primary_key=True)
    product_template = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_product_template_rel'
        unique_together = (('product_label_layout', 'product_template'),)


class ProductLabelLayoutStockMoveLineRel(models.Model):
    product_label_layout = models.OneToOneField(ProductLabelLayout, models.DO_NOTHING, primary_key=True)
    stock_move_line = models.ForeignKey('StockMoveLine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_label_layout_stock_move_line_rel'
        unique_together = (('product_label_layout', 'stock_move_line'),)


class ProductOptionalRel(models.Model):
    src = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    dest = models.ForeignKey('ProductTemplate', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_optional_rel'
        unique_together = (('src', 'dest'),)


class ProductPackaging(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    barcode = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sales = models.BooleanField(blank=True, null=True)
    package_type = models.ForeignKey('StockPackageType', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_packaging'


class ProductPricelist(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    discount_policy = models.CharField(max_length=-1)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist'


class ProductPricelistItem(models.Model):
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductProduct', models.DO_NOTHING, blank=True, null=True)
    base_pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    applied_on = models.CharField(max_length=-1)
    base = models.CharField(max_length=-1)
    compute_price = models.CharField(max_length=-1)
    min_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    fixed_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_round = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_surcharge = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_min_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_max_margin = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    percent_price = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_pricelist_item'


class ProductProduct(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    combination_indices = models.CharField(max_length=-1, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    can_image_variant_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_product'
        unique_together = (('product_tmpl', 'combination_indices'),)


class ProductProductStockTrackConfirmationRel(models.Model):
    stock_track_confirmation = models.OneToOneField('StockTrackConfirmation', models.DO_NOTHING, primary_key=True)
    product_product = models.ForeignKey(ProductProduct, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_product_stock_track_confirmation_rel'
        unique_together = (('stock_track_confirmation', 'product_product'),)


class ProductRemoval(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    method = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_removal'


class ProductReplenish(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_has_variants = models.BooleanField()
    date_planned = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'product_replenish'


class ProductReplenishStockRouteRel(models.Model):
    product_replenish = models.OneToOneField(ProductReplenish, models.DO_NOTHING, primary_key=True)
    stock_route = models.ForeignKey('StockRoute', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_replenish_stock_route_rel'
        unique_together = (('product_replenish', 'stock_route'),)


class ProductSupplierTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_supplier_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductSupplierinfo(models.Model):
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey('ProductTemplate', models.DO_NOTHING, blank=True, null=True)
    delay = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_name = models.CharField(max_length=-1, blank=True, null=True)
    product_code = models.CharField(max_length=-1, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_supplierinfo'


class ProductTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_tag'


class ProductTagProductProductRel(models.Model):
    product_product = models.OneToOneField(ProductProduct, models.DO_NOTHING, primary_key=True)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_product_product_rel'
        unique_together = (('product_product', 'product_tag'),)


class ProductTagProductTemplateRel(models.Model):
    product_template = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    product_tag = models.ForeignKey(ProductTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_tag_product_template_rel'
        unique_together = (('product_template', 'product_tag'),)


class ProductTaxesRel(models.Model):
    prod = models.OneToOneField('ProductTemplate', models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_taxes_rel'
        unique_together = (('prod', 'tax'),)


class ProductTemplate(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    uom_po = models.ForeignKey('UomUom', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    detailed_type = models.CharField(max_length=-1)
    type = models.CharField(max_length=-1, blank=True, null=True)
    default_code = models.CharField(max_length=-1, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    description_purchase = models.JSONField(blank=True, null=True)
    description_sale = models.JSONField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    volume = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    sale_ok = models.BooleanField(blank=True, null=True)
    purchase_ok = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    can_image_1024_be_zoomed = models.BooleanField(blank=True, null=True)
    has_configurable_attributes = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    can_be_expensed = models.BooleanField(blank=True, null=True)
    service_type = models.CharField(max_length=-1, blank=True, null=True)
    sale_line_warn = models.CharField(max_length=-1)
    expense_policy = models.CharField(max_length=-1, blank=True, null=True)
    invoice_policy = models.CharField(max_length=-1, blank=True, null=True)
    sale_line_warn_msg = models.TextField(blank=True, null=True)
    service_tracking = models.CharField(max_length=-1, blank=True, null=True)
    tracking = models.CharField(max_length=-1)
    description_picking = models.JSONField(blank=True, null=True)
    description_pickingout = models.JSONField(blank=True, null=True)
    description_pickingin = models.JSONField(blank=True, null=True)
    sale_delay = models.FloatField(blank=True, null=True)
    produce_delay = models.FloatField(blank=True, null=True)
    days_to_prepare_mo = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template'


class ProductTemplateAttributeExclusion(models.Model):
    product_template_attribute_value = models.ForeignKey('ProductTemplateAttributeValue', models.DO_NOTHING, blank=True, null=True)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_exclusion'


class ProductTemplateAttributeLine(models.Model):
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING)
    value_count = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_line'


class ProductTemplateAttributeValue(models.Model):
    product_attribute_value = models.ForeignKey(ProductAttributeValue, models.DO_NOTHING)
    attribute_line = models.ForeignKey(ProductTemplateAttributeLine, models.DO_NOTHING)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING, blank=True, null=True)
    attribute = models.ForeignKey(ProductAttribute, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    price_extra = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    ptav_active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value'
        unique_together = (('attribute_line', 'product_attribute_value'),)


class ProductTemplateAttributeValueSaleOrderLineRel(models.Model):
    sale_order_line = models.OneToOneField('SaleOrderLine', models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_template_attribute_value_sale_order_line_rel'
        unique_together = (('sale_order_line', 'product_template_attribute_value'),)


class ProductVariantCombination(models.Model):
    product_product = models.OneToOneField(ProductProduct, models.DO_NOTHING, primary_key=True)
    product_template_attribute_value = models.ForeignKey(ProductTemplateAttributeValue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_variant_combination'
        unique_together = (('product_product', 'product_template_attribute_value'),)


class ProjectCollaborator(models.Model):
    project = models.ForeignKey('ProjectProject', models.DO_NOTHING)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_collaborator'
        unique_together = (('project', 'partner'),)


class ProjectFavoriteUserRel(models.Model):
    project = models.OneToOneField('ProjectProject', models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_favorite_user_rel'
        unique_together = (('project', 'user'),)


class ProjectMilestone(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey('ProjectProject', models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    deadline = models.DateField(blank=True, null=True)
    reached_date = models.DateField(blank=True, null=True)
    is_reached = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True)
    quantity_percentage = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_milestone'


class ProjectProject(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    alias = models.ForeignKey(MailAlias, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    stage = models.ForeignKey('ProjectProjectStage', models.DO_NOTHING, blank=True, null=True)
    last_update = models.ForeignKey('ProjectUpdate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    privacy_visibility = models.CharField(max_length=-1)
    rating_status = models.CharField(max_length=-1)
    rating_status_period = models.CharField(max_length=-1)
    last_update_status = models.CharField(max_length=-1)
    date_start = models.DateField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    name = models.JSONField()
    label_tasks = models.JSONField(blank=True, null=True)
    task_properties_definition = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    allow_subtasks = models.BooleanField(blank=True, null=True)
    allow_recurring_tasks = models.BooleanField(blank=True, null=True)
    allow_task_dependencies = models.BooleanField(blank=True, null=True)
    allow_milestones = models.BooleanField(blank=True, null=True)
    rating_active = models.BooleanField(blank=True, null=True)
    rating_request_deadline = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True)
    allow_billable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project'


class ProjectProjectProjectTagsRel(models.Model):
    project_project = models.OneToOneField(ProjectProject, models.DO_NOTHING, primary_key=True)
    project_tags = models.ForeignKey('ProjectTags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_project_project_tags_rel'
        unique_together = (('project_project', 'project_tags'),)


class ProjectProjectProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField('ProjectTaskTypeDeleteWizard', models.DO_NOTHING, primary_key=True)
    project_project = models.ForeignKey(ProjectProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_project_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_project'),)


class ProjectProjectStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_project_stage'


class ProjectShareWizard(models.Model):
    res_id = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_model = models.CharField(max_length=-1)
    access_mode = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    display_access_mode = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_share_wizard'


class ProjectShareWizardResPartnerRel(models.Model):
    project_share_wizard = models.OneToOneField(ProjectShareWizard, models.DO_NOTHING, primary_key=True)
    res_partner = models.ForeignKey('ResPartner', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_share_wizard_res_partner_rel'
        unique_together = (('project_share_wizard', 'res_partner'),)


class ProjectTags(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_tags'


class ProjectTagsProjectTaskRel(models.Model):
    project_task = models.OneToOneField('ProjectTask', models.DO_NOTHING, primary_key=True)
    project_tags = models.ForeignKey(ProjectTags, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_tags_project_task_rel'
        unique_together = (('project_task', 'project_tags'),)


class ProjectTask(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    stage = models.ForeignKey('ProjectTaskType', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING, blank=True, null=True)
    display_project = models.ForeignKey(ProjectProject, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)
    displayed_image = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    ancestor = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    milestone = models.ForeignKey(ProjectMilestone, models.DO_NOTHING, blank=True, null=True)
    recurrence = models.ForeignKey('ProjectTaskRecurrence', models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    kanban_state = models.CharField(max_length=-1)
    partner_email = models.CharField(max_length=-1, blank=True, null=True)
    partner_phone = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    date_deadline = models.DateField(blank=True, null=True)
    task_properties = models.JSONField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    working_hours_open = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    working_hours_close = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    is_closed = models.BooleanField(blank=True, null=True)
    is_blocked = models.BooleanField(blank=True, null=True)
    recurring_task = models.BooleanField(blank=True, null=True)
    is_analytic_account_id_changed = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_assign = models.DateTimeField(blank=True, null=True)
    date_last_stage_update = models.DateTimeField(blank=True, null=True)
    rating_last_value = models.FloatField(blank=True, null=True)
    planned_hours = models.FloatField(blank=True, null=True)
    working_days_open = models.FloatField(blank=True, null=True)
    working_days_close = models.FloatField(blank=True, null=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    sale_line = models.ForeignKey('SaleOrderLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task'


class ProjectTaskRecurrence(models.Model):
    recurrence_left = models.IntegerField(blank=True, null=True)
    repeat_interval = models.IntegerField(blank=True, null=True)
    repeat_number = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    repeat_unit = models.CharField(max_length=-1, blank=True, null=True)
    repeat_type = models.CharField(max_length=-1, blank=True, null=True)
    repeat_on_month = models.CharField(max_length=-1, blank=True, null=True)
    repeat_on_year = models.CharField(max_length=-1, blank=True, null=True)
    repeat_day = models.CharField(max_length=-1, blank=True, null=True)
    repeat_week = models.CharField(max_length=-1, blank=True, null=True)
    repeat_weekday = models.CharField(max_length=-1, blank=True, null=True)
    repeat_month = models.CharField(max_length=-1, blank=True, null=True)
    next_recurrence_date = models.DateField(blank=True, null=True)
    repeat_until = models.DateField(blank=True, null=True)
    mon = models.BooleanField(blank=True, null=True)
    tue = models.BooleanField(blank=True, null=True)
    wed = models.BooleanField(blank=True, null=True)
    thu = models.BooleanField(blank=True, null=True)
    fri = models.BooleanField(blank=True, null=True)
    sat = models.BooleanField(blank=True, null=True)
    sun = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_recurrence'


class ProjectTaskType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    rating_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    legend_blocked = models.JSONField()
    legend_done = models.JSONField()
    legend_normal = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    fold = models.BooleanField(blank=True, null=True)
    auto_validation_kanban_state = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sms_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type'


class ProjectTaskTypeDeleteWizard(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_type_delete_wizard'


class ProjectTaskTypeProjectTaskTypeDeleteWizardRel(models.Model):
    project_task_type_delete_wizard = models.OneToOneField(ProjectTaskTypeDeleteWizard, models.DO_NOTHING, primary_key=True)
    project_task_type = models.ForeignKey(ProjectTaskType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_project_task_type_delete_wizard_rel'
        unique_together = (('project_task_type_delete_wizard', 'project_task_type'),)


class ProjectTaskTypeRel(models.Model):
    type = models.OneToOneField(ProjectTaskType, models.DO_NOTHING, primary_key=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project_task_type_rel'
        unique_together = (('type', 'project'),)


class ProjectTaskUserRel(models.Model):
    task = models.ForeignKey(ProjectTask, models.DO_NOTHING)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    stage = models.ForeignKey(ProjectTaskType, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_task_user_rel'
        unique_together = (('task', 'user'),)


class ProjectUpdate(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email_cc = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    status = models.CharField(max_length=-1)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_update'


class RatingRating(models.Model):
    res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField()
    parent_res_model = models.ForeignKey(IrModel, models.DO_NOTHING, blank=True, null=True)
    parent_res_id = models.IntegerField(blank=True, null=True)
    rated_partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    res_name = models.CharField(max_length=-1, blank=True, null=True)
    res_model_0 = models.CharField(db_column='res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    parent_res_name = models.CharField(max_length=-1, blank=True, null=True)
    parent_res_model_0 = models.CharField(db_column='parent_res_model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    rating_text = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    is_internal = models.BooleanField(blank=True, null=True)
    consumed = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    publisher = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    publisher_comment = models.TextField(blank=True, null=True)
    publisher_datetime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rating_rating'


class RelBadgeAuthUsers(models.Model):
    gamification_badge = models.OneToOneField(GamificationBadge, models.DO_NOTHING, primary_key=True)
    res_users = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_badge_auth_users'
        unique_together = (('gamification_badge', 'res_users'),)


class RelModulesLangexport(models.Model):
    wiz = models.OneToOneField(BaseLanguageExport, models.DO_NOTHING, primary_key=True)
    module = models.ForeignKey(IrModuleModule, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_modules_langexport'
        unique_together = (('wiz', 'module'),)


class RelServerActions(models.Model):
    server = models.OneToOneField(IrActServer, models.DO_NOTHING, primary_key=True)
    action = models.ForeignKey(IrActServer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rel_server_actions'
        unique_together = (('server', 'action'),)


class RepairFee(models.Model):
    repair = models.ForeignKey('RepairOrder', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom')
    invoice_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.TextField()
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    invoiced = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_fee'


class RepairFeeLineTax(models.Model):
    repair_fee_line = models.OneToOneField(RepairFee, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'repair_fee_line_tax'
        unique_together = (('repair_fee_line', 'tax'),)


class RepairLine(models.Model):
    repair = models.ForeignKey('RepairOrder', models.DO_NOTHING)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom')
    invoice_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    location_dest = models.ForeignKey('StockLocation', models.DO_NOTHING)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1)
    name = models.TextField()
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    invoiced = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_line'


class RepairOperationLineTax(models.Model):
    repair_operation_line = models.OneToOneField(RepairLine, models.DO_NOTHING, primary_key=True)
    tax = models.ForeignKey(AccountTax, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'repair_operation_line_tax'
        unique_together = (('repair_operation_line', 'tax'),)


class RepairOrder(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom')
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    address = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey('StockLocation', models.DO_NOTHING)
    lot = models.ForeignKey('StockLot', models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING, blank=True, null=True)
    partner_invoice = models.ForeignKey('ResPartner', models.DO_NOTHING, blank=True, null=True)
    invoice = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('ResCompany', models.DO_NOTHING)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    description = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    invoice_method = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    schedule_date = models.DateField(blank=True, null=True)
    guarantee_limit = models.DateField(blank=True, null=True)
    internal_notes = models.TextField(blank=True, null=True)
    quotation_notes = models.TextField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    invoiced = models.BooleanField(blank=True, null=True)
    repaired = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount_untaxed = models.FloatField(blank=True, null=True)
    amount_tax = models.FloatField(blank=True, null=True)
    amount_total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_order'


class RepairOrderMakeInvoice(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    group = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_order_make_invoice'


class RepairOrderRepairTagsRel(models.Model):
    repair_order = models.OneToOneField(RepairOrder, models.DO_NOTHING, primary_key=True)
    repair_tags = models.ForeignKey('RepairTags', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'repair_order_repair_tags_rel'
        unique_together = (('repair_order', 'repair_tags'),)


class RepairTags(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_tags'


class ReportLayout(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    image = models.CharField(max_length=-1, blank=True, null=True)
    pdf = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_layout'


class ReportPaperformat(models.Model):
    page_height = models.IntegerField(blank=True, null=True)
    page_width = models.IntegerField(blank=True, null=True)
    header_spacing = models.IntegerField(blank=True, null=True)
    dpi = models.IntegerField()
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    format = models.CharField(max_length=-1, blank=True, null=True)
    orientation = models.CharField(max_length=-1, blank=True, null=True)
    default = models.BooleanField(blank=True, null=True)
    header_line = models.BooleanField(blank=True, null=True)
    disable_shrinking = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    margin_top = models.FloatField(blank=True, null=True)
    margin_bottom = models.FloatField(blank=True, null=True)
    margin_left = models.FloatField(blank=True, null=True)
    margin_right = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_paperformat'


class ResBank(models.Model):
    state = models.ForeignKey('ResCountryState', models.DO_NOTHING, db_column='state', blank=True, null=True)
    country = models.ForeignKey('ResCountry', models.DO_NOTHING, db_column='country', blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    bic = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_bank'


class ResCompany(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    partner = models.ForeignKey('ResPartner', models.DO_NOTHING)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    paperformat = models.ForeignKey(ReportPaperformat, models.DO_NOTHING, blank=True, null=True)
    external_report_layout = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    base_onboarding_company_state = models.CharField(max_length=-1, blank=True, null=True)
    font = models.CharField(max_length=-1, blank=True, null=True)
    primary_color = models.CharField(max_length=-1, blank=True, null=True)
    secondary_color = models.CharField(max_length=-1, blank=True, null=True)
    layout_background = models.CharField(max_length=-1)
    report_footer = models.JSONField(blank=True, null=True)
    report_header = models.TextField(blank=True, null=True)
    company_details = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    logo_web = models.BinaryField(blank=True, null=True)
    resource_calendar = models.ForeignKey('ResourceCalendar', models.DO_NOTHING, blank=True, null=True)
    hr_presence_control_email_amount = models.IntegerField(blank=True, null=True)
    hr_presence_control_ip_list = models.CharField(max_length=-1, blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    iap_enrich_auto_done = models.BooleanField(blank=True, null=True)
    snailmail_color = models.BooleanField(blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    snailmail_duplex = models.BooleanField(blank=True, null=True)
    payment_provider_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    payment_onboarding_payment_method = models.CharField(max_length=-1, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    fiscalyear_last_day = models.IntegerField()
    transfer_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_income_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    default_cash_difference_expense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_suspense_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_debit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_payment_credit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_early_pay_discount_gain_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_journal_early_pay_discount_loss_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    account_sale_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    account_purchase_tax = models.ForeignKey(AccountTax, models.DO_NOTHING, blank=True, null=True)
    currency_exchange_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    income_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expense_currency_exchange_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_input_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    property_stock_account_output_categ = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    property_stock_valuation_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, blank=True, null=True)
    account_opening_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    account_default_pos_receivable_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    expense_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    revenue_accrual_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    automatic_entry_default_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account_fiscal_country = models.ForeignKey('ResCountry', models.DO_NOTHING, blank=True, null=True)
    tax_cash_basis_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account_cash_basis_base_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    fiscalyear_last_month = models.CharField(max_length=-1)
    bank_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    cash_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    early_pay_discount_computation = models.CharField(max_length=-1, blank=True, null=True)
    transfer_account_code_prefix = models.CharField(max_length=-1, blank=True, null=True)
    tax_calculation_rounding_method = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_bank_data_state = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_fy_data_state = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_coa_state = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_taxes_state = models.CharField(max_length=-1, blank=True, null=True)
    account_onboarding_invoice_layout_state = models.CharField(max_length=-1, blank=True, null=True)
    account_onboarding_sale_tax_state = models.CharField(max_length=-1, blank=True, null=True)
    account_invoice_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    account_dashboard_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    terms_type = models.CharField(max_length=-1, blank=True, null=True)
    account_setup_bill_state = models.CharField(max_length=-1, blank=True, null=True)
    quick_edit_mode = models.CharField(max_length=-1, blank=True, null=True)
    period_lock_date = models.DateField(blank=True, null=True)
    fiscalyear_lock_date = models.DateField(blank=True, null=True)
    tax_lock_date = models.DateField(blank=True, null=True)
    account_opening_date = models.DateField()
    invoice_terms = models.JSONField(blank=True, null=True)
    invoice_terms_html = models.JSONField(blank=True, null=True)
    expects_chart_of_accounts = models.BooleanField(blank=True, null=True)
    anglo_saxon_accounting = models.BooleanField(blank=True, null=True)
    qr_code = models.BooleanField(blank=True, null=True)
    invoice_is_email = models.BooleanField(blank=True, null=True)
    invoice_is_print = models.BooleanField(blank=True, null=True)
    account_use_credit_limit = models.BooleanField(blank=True, null=True)
    account_onboarding_create_invoice_state_flag = models.BooleanField(blank=True, null=True)
    tax_exigibility = models.BooleanField(blank=True, null=True)
    account_storno = models.BooleanField(blank=True, null=True)
    expense_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    company_expense_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    invoice_is_snailmail = models.BooleanField(blank=True, null=True)
    social_twitter = models.CharField(max_length=-1, blank=True, null=True)
    social_facebook = models.CharField(max_length=-1, blank=True, null=True)
    social_github = models.CharField(max_length=-1, blank=True, null=True)
    social_linkedin = models.CharField(max_length=-1, blank=True, null=True)
    social_youtube = models.CharField(max_length=-1, blank=True, null=True)
    social_instagram = models.CharField(max_length=-1, blank=True, null=True)
    vat_check_vies = models.BooleanField(blank=True, null=True)
    quotation_validity_days = models.IntegerField(blank=True, null=True)
    sale_quotation_onboarding_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_order_confirmation_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_sample_quotation_state = models.CharField(max_length=-1, blank=True, null=True)
    sale_onboarding_payment_method = models.CharField(max_length=-1, blank=True, null=True)
    portal_confirmation_sign = models.BooleanField(blank=True, null=True)
    portal_confirmation_pay = models.BooleanField(blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True)
    nomenclature = models.ForeignKey(BarcodeNomenclature, models.DO_NOTHING, blank=True, null=True)
    internal_transit_location = models.ForeignKey('StockLocation', models.DO_NOTHING, blank=True, null=True)
    stock_mail_confirmation_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    annual_inventory_day = models.IntegerField(blank=True, null=True)
    annual_inventory_month = models.CharField(max_length=-1, blank=True, null=True)
    stock_move_email_validation = models.BooleanField(blank=True, null=True)
    stock_sms_confirmation_template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    stock_move_sms_validation = models.BooleanField(blank=True, null=True)
    has_received_warning_stock_sms = models.BooleanField(blank=True, null=True)
    security_lead = models.FloatField()
    manufacturing_lead = models.FloatField()
    overtime_company_threshold = models.IntegerField(blank=True, null=True)
    overtime_employee_threshold = models.IntegerField(blank=True, null=True)
    attendance_kiosk_delay = models.IntegerField(blank=True, null=True)
    attendance_kiosk_mode = models.CharField(max_length=-1, blank=True, null=True)
    attendance_barcode_source = models.CharField(max_length=-1, blank=True, null=True)
    overtime_start_date = models.DateField(blank=True, null=True)
    hr_attendance_overtime = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_company'


class ResCompanyUsersRel(models.Model):
    cid = models.OneToOneField(ResCompany, models.DO_NOTHING, db_column='cid', primary_key=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_company_users_rel'
        unique_together = (('cid', 'user'),)


class ResConfig(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config'


class ResConfigInstaller(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_installer'


class ResConfigSettings(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    user_default_rights = models.BooleanField(blank=True, null=True)
    external_email_server_default = models.BooleanField(blank=True, null=True)
    module_base_import = models.BooleanField(blank=True, null=True)
    module_google_calendar = models.BooleanField(blank=True, null=True)
    module_microsoft_calendar = models.BooleanField(blank=True, null=True)
    module_mail_plugin = models.BooleanField(blank=True, null=True)
    module_auth_oauth = models.BooleanField(blank=True, null=True)
    module_auth_ldap = models.BooleanField(blank=True, null=True)
    module_base_gengo = models.BooleanField(blank=True, null=True)
    module_account_inter_company_rules = models.BooleanField(blank=True, null=True)
    module_voip = models.BooleanField(blank=True, null=True)
    module_web_unsplash = models.BooleanField(blank=True, null=True)
    module_partner_autocomplete = models.BooleanField(blank=True, null=True)
    module_base_geolocalize = models.BooleanField(blank=True, null=True)
    module_google_recaptcha = models.BooleanField(blank=True, null=True)
    group_multi_currency = models.BooleanField(blank=True, null=True)
    show_effect = models.BooleanField(blank=True, null=True)
    module_product_images = models.BooleanField(blank=True, null=True)
    profiling_enabled_until = models.DateTimeField(blank=True, null=True)
    alias_domain = models.CharField(max_length=-1, blank=True, null=True)
    twilio_account_sid = models.CharField(max_length=-1, blank=True, null=True)
    twilio_account_token = models.CharField(max_length=-1, blank=True, null=True)
    module_google_gmail = models.BooleanField(blank=True, null=True)
    module_microsoft_outlook = models.BooleanField(blank=True, null=True)
    restrict_template_rendering = models.BooleanField(blank=True, null=True)
    use_twilio_rtc_servers = models.BooleanField(blank=True, null=True)
    group_analytic_accounting = models.BooleanField(blank=True, null=True)
    auth_signup_template_user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    auth_signup_uninvited = models.CharField(max_length=-1, blank=True, null=True)
    auth_signup_reset_password = models.BooleanField(blank=True, null=True)
    google_gmail_client_identifier = models.CharField(max_length=-1, blank=True, null=True)
    google_gmail_client_secret = models.CharField(max_length=-1, blank=True, null=True)
    module_hr_presence = models.BooleanField(blank=True, null=True)
    module_hr_skills = models.BooleanField(blank=True, null=True)
    module_hr_homeworking = models.BooleanField(blank=True, null=True)
    hr_presence_control_login = models.BooleanField(blank=True, null=True)
    hr_presence_control_email = models.BooleanField(blank=True, null=True)
    hr_presence_control_ip = models.BooleanField(blank=True, null=True)
    module_hr_attendance = models.BooleanField(blank=True, null=True)
    hr_employee_self_edit = models.BooleanField(blank=True, null=True)
    product_pricelist_setting = models.CharField(max_length=-1, blank=True, null=True)
    product_weight_in_lbs = models.CharField(max_length=-1, blank=True, null=True)
    product_volume_volume_in_cubic_feet = models.CharField(max_length=-1, blank=True, null=True)
    group_discount_per_so_line = models.BooleanField(blank=True, null=True)
    group_uom = models.BooleanField(blank=True, null=True)
    group_product_variant = models.BooleanField(blank=True, null=True)
    module_sale_product_matrix = models.BooleanField(blank=True, null=True)
    module_loyalty = models.BooleanField(blank=True, null=True)
    group_stock_packaging = models.BooleanField(blank=True, null=True)
    group_product_pricelist = models.BooleanField(blank=True, null=True)
    group_sale_pricelist = models.BooleanField(blank=True, null=True)
    unsplash_access_key = models.CharField(max_length=-1, blank=True, null=True)
    unsplash_app_id = models.CharField(max_length=-1, blank=True, null=True)
    digest = models.ForeignKey(DigestDigest, models.DO_NOTHING, blank=True, null=True)
    digest_emails = models.BooleanField(blank=True, null=True)
    chart_template = models.ForeignKey(AccountChartTemplate, models.DO_NOTHING, blank=True, null=True)
    show_line_subtotals_tax_selection = models.CharField(max_length=-1)
    module_account_accountant = models.BooleanField(blank=True, null=True)
    group_warning_account = models.BooleanField(blank=True, null=True)
    group_cash_rounding = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_excluded = models.BooleanField(blank=True, null=True)
    group_show_line_subtotals_tax_included = models.BooleanField(blank=True, null=True)
    group_show_sale_receipts = models.BooleanField(blank=True, null=True)
    group_show_purchase_receipts = models.BooleanField(blank=True, null=True)
    module_account_budget = models.BooleanField(blank=True, null=True)
    module_account_payment = models.BooleanField(blank=True, null=True)
    module_account_reports = models.BooleanField(blank=True, null=True)
    module_account_check_printing = models.BooleanField(blank=True, null=True)
    module_account_batch_payment = models.BooleanField(blank=True, null=True)
    module_account_sepa = models.BooleanField(blank=True, null=True)
    module_account_sepa_direct_debit = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_qif = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_ofx = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_csv = models.BooleanField(blank=True, null=True)
    module_account_bank_statement_import_camt = models.BooleanField(blank=True, null=True)
    module_currency_rate_live = models.BooleanField(blank=True, null=True)
    module_account_intrastat = models.BooleanField(blank=True, null=True)
    module_product_margin = models.BooleanField(blank=True, null=True)
    module_l10n_eu_oss = models.BooleanField(blank=True, null=True)
    module_account_taxcloud = models.BooleanField(blank=True, null=True)
    module_account_invoice_extract = models.BooleanField(blank=True, null=True)
    module_snailmail_account = models.BooleanField(blank=True, null=True)
    use_invoice_terms = models.BooleanField(blank=True, null=True)
    group_sale_delivery_address = models.BooleanField(blank=True, null=True)
    expense_alias_prefix = models.CharField(max_length=-1, blank=True, null=True)
    use_mailgateway = models.BooleanField(blank=True, null=True)
    module_hr_payroll_expense = models.BooleanField(blank=True, null=True)
    module_hr_expense_extract = models.BooleanField(blank=True, null=True)
    mass_mailing_mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    group_mass_mailing_campaign = models.BooleanField(blank=True, null=True)
    mass_mailing_outgoing_mail_server = models.BooleanField(blank=True, null=True)
    show_blacklist_buttons = models.BooleanField(blank=True, null=True)
    mass_mailing_reports = models.BooleanField(blank=True, null=True)
    module_project_forecast = models.BooleanField(blank=True, null=True)
    module_hr_timesheet = models.BooleanField(blank=True, null=True)
    group_subtask_project = models.BooleanField(blank=True, null=True)
    group_project_rating = models.BooleanField(blank=True, null=True)
    group_project_stages = models.BooleanField(blank=True, null=True)
    group_project_recurring_tasks = models.BooleanField(blank=True, null=True)
    group_project_task_dependencies = models.BooleanField(blank=True, null=True)
    group_project_milestone = models.BooleanField(blank=True, null=True)
    deposit_default_product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    invoice_mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    default_invoice_policy = models.CharField(max_length=-1, blank=True, null=True)
    group_auto_done_setting = models.BooleanField(blank=True, null=True)
    group_proforma_sales = models.BooleanField(blank=True, null=True)
    group_warning_sale = models.BooleanField(blank=True, null=True)
    automatic_invoice = models.BooleanField(blank=True, null=True)
    use_quotation_validity_days = models.BooleanField(blank=True, null=True)
    module_delivery = models.BooleanField(blank=True, null=True)
    module_delivery_bpost = models.BooleanField(blank=True, null=True)
    module_delivery_dhl = models.BooleanField(blank=True, null=True)
    module_delivery_easypost = models.BooleanField(blank=True, null=True)
    module_delivery_sendcloud = models.BooleanField(blank=True, null=True)
    module_delivery_fedex = models.BooleanField(blank=True, null=True)
    module_delivery_ups = models.BooleanField(blank=True, null=True)
    module_delivery_usps = models.BooleanField(blank=True, null=True)
    module_product_email_template = models.BooleanField(blank=True, null=True)
    module_sale_amazon = models.BooleanField(blank=True, null=True)
    module_sale_loyalty = models.BooleanField(blank=True, null=True)
    module_sale_margin = models.BooleanField(blank=True, null=True)
    group_sale_order_template = models.BooleanField(blank=True, null=True)
    module_sale_quotation_builder = models.BooleanField(blank=True, null=True)
    module_product_expiry = models.BooleanField(blank=True, null=True)
    group_stock_production_lot = models.BooleanField(blank=True, null=True)
    group_stock_lot_print_gs1 = models.BooleanField(blank=True, null=True)
    group_lot_on_delivery_slip = models.BooleanField(blank=True, null=True)
    group_stock_tracking_lot = models.BooleanField(blank=True, null=True)
    group_stock_tracking_owner = models.BooleanField(blank=True, null=True)
    group_stock_adv_location = models.BooleanField(blank=True, null=True)
    group_warning_stock = models.BooleanField(blank=True, null=True)
    group_stock_sign_delivery = models.BooleanField(blank=True, null=True)
    module_stock_picking_batch = models.BooleanField(blank=True, null=True)
    group_stock_picking_wave = models.BooleanField(blank=True, null=True)
    module_stock_barcode = models.BooleanField(blank=True, null=True)
    module_stock_sms = models.BooleanField(blank=True, null=True)
    module_quality_control = models.BooleanField(blank=True, null=True)
    module_quality_control_worksheet = models.BooleanField(blank=True, null=True)
    group_stock_multi_locations = models.BooleanField(blank=True, null=True)
    group_stock_storage_categories = models.BooleanField(blank=True, null=True)
    group_stock_reception_report = models.BooleanField(blank=True, null=True)
    module_stock_landed_costs = models.BooleanField(blank=True, null=True)
    group_lot_on_invoice = models.BooleanField(blank=True, null=True)
    default_picking_policy = models.CharField(max_length=-1)
    group_display_incoterm = models.BooleanField(blank=True, null=True)
    use_security_lead = models.BooleanField(blank=True, null=True)
    use_manufacturing_lead = models.BooleanField(blank=True, null=True)
    group_mrp_byproducts = models.BooleanField(blank=True, null=True)
    module_mrp_mps = models.BooleanField(blank=True, null=True)
    module_mrp_plm = models.BooleanField(blank=True, null=True)
    module_mrp_workorder = models.BooleanField(blank=True, null=True)
    module_mrp_subcontracting = models.BooleanField(blank=True, null=True)
    group_mrp_routings = models.BooleanField(blank=True, null=True)
    group_unlocked_by_default = models.BooleanField(blank=True, null=True)
    group_mrp_reception_report = models.BooleanField(blank=True, null=True)
    group_mrp_workorder_dependencies = models.BooleanField(blank=True, null=True)
    module_website_hr_recruitment = models.BooleanField(blank=True, null=True)
    module_hr_recruitment_survey = models.BooleanField(blank=True, null=True)
    group_applicant_cv_display = models.BooleanField(blank=True, null=True)
    module_hr_recruitment_extract = models.BooleanField(blank=True, null=True)
    delay_alert_contract = models.IntegerField(blank=True, null=True)
    overtime_company_threshold = models.IntegerField(blank=True, null=True)
    overtime_employee_threshold = models.IntegerField(blank=True, null=True)
    overtime_start_date = models.DateField(blank=True, null=True)
    group_attendance_use_pin = models.BooleanField(blank=True, null=True)
    hr_attendance_overtime = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_config_settings'


class ResCountry(models.Model):
    address_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey('ResCurrency', models.DO_NOTHING, blank=True, null=True)
    phone_code = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    code = models.CharField(unique=True, max_length=2, blank=True, null=True)
    name_position = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField(unique=True)
    vat_label = models.JSONField(blank=True, null=True)
    address_format = models.TextField(blank=True, null=True)
    state_required = models.BooleanField(blank=True, null=True)
    zip_required = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country'


class ResCountryGroup(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_group'


class ResCountryGroupPricelistRel(models.Model):
    pricelist = models.OneToOneField(ProductPricelist, models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_group_pricelist_rel'
        unique_together = (('pricelist', 'res_country_group'),)


class ResCountryResCountryGroupRel(models.Model):
    res_country = models.OneToOneField(ResCountry, models.DO_NOTHING, primary_key=True)
    res_country_group = models.ForeignKey(ResCountryGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_country_res_country_group_rel'
        unique_together = (('res_country', 'res_country_group'),)


class ResCountryState(models.Model):
    country = models.ForeignKey(ResCountry, models.DO_NOTHING)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_country_state'
        unique_together = (('country', 'code'),)


class ResCurrency(models.Model):
    name = models.CharField(unique=True, max_length=-1)
    symbol = models.CharField(max_length=-1)
    decimal_places = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    full_name = models.CharField(max_length=-1, blank=True, null=True)
    position = models.CharField(max_length=-1, blank=True, null=True)
    currency_unit_label = models.CharField(max_length=-1, blank=True, null=True)
    currency_subunit_label = models.CharField(max_length=-1, blank=True, null=True)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency'


class ResCurrencyRate(models.Model):
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.DateField()
    rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_currency_rate'
        unique_together = (('name', 'currency', 'company'),)


class ResGroups(models.Model):
    name = models.JSONField()
    category = models.ForeignKey(IrModuleCategory, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    comment = models.JSONField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_groups'
        unique_together = (('category', 'name'),)


class ResGroupsImpliedRel(models.Model):
    gid = models.OneToOneField(ResGroups, models.DO_NOTHING, db_column='gid', primary_key=True)
    hid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='hid')

    class Meta:
        managed = False
        db_table = 'res_groups_implied_rel'
        unique_together = (('gid', 'hid'),)


class ResGroupsReportRel(models.Model):
    uid = models.OneToOneField(IrActReportXml, models.DO_NOTHING, db_column='uid', primary_key=True)
    gid = models.ForeignKey(ResGroups, models.DO_NOTHING, db_column='gid')

    class Meta:
        managed = False
        db_table = 'res_groups_report_rel'
        unique_together = (('uid', 'gid'),)


class ResGroupsSpreadsheetDashboardRel(models.Model):
    spreadsheet_dashboard = models.OneToOneField('SpreadsheetDashboard', models.DO_NOTHING, primary_key=True)
    res_groups = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_groups_spreadsheet_dashboard_rel'
        unique_together = (('spreadsheet_dashboard', 'res_groups'),)


class ResGroupsUsersRel(models.Model):
    gid = models.OneToOneField(ResGroups, models.DO_NOTHING, db_column='gid', primary_key=True)
    uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='uid')

    class Meta:
        managed = False
        db_table = 'res_groups_users_rel'
        unique_together = (('gid', 'uid'),)


class ResLang(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    code = models.CharField(unique=True, max_length=-1)
    iso_code = models.CharField(max_length=-1, blank=True, null=True)
    url_code = models.CharField(unique=True, max_length=-1)
    direction = models.CharField(max_length=-1)
    date_format = models.CharField(max_length=-1)
    time_format = models.CharField(max_length=-1)
    week_start = models.CharField(max_length=-1)
    grouping = models.CharField(max_length=-1)
    decimal_point = models.CharField(max_length=-1)
    thousands_sep = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_lang'


class ResLangInstallRel(models.Model):
    language_wizard = models.OneToOneField(BaseLanguageInstall, models.DO_NOTHING, primary_key=True)
    lang = models.ForeignKey(ResLang, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_lang_install_rel'
        unique_together = (('language_wizard', 'lang'),)


class ResPartner(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    title = models.ForeignKey('ResPartnerTitle', models.DO_NOTHING, db_column='title', blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('ResUsers', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    industry = models.ForeignKey('ResPartnerIndustry', models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    commercial_partner = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    display_name = models.CharField(max_length=-1, blank=True, null=True)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    tz = models.CharField(max_length=-1, blank=True, null=True)
    vat = models.CharField(max_length=-1, blank=True, null=True)
    company_registry = models.CharField(max_length=-1, blank=True, null=True)
    website = models.CharField(max_length=-1, blank=True, null=True)
    function = models.CharField(max_length=-1, blank=True, null=True)
    type = models.CharField(max_length=-1, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    mobile = models.CharField(max_length=-1, blank=True, null=True)
    commercial_company_name = models.CharField(max_length=-1, blank=True, null=True)
    company_name = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    partner_latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    partner_longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    employee = models.BooleanField(blank=True, null=True)
    is_company = models.BooleanField(blank=True, null=True)
    partner_share = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    message_bounce = models.IntegerField(blank=True, null=True)
    email_normalized = models.CharField(max_length=-1, blank=True, null=True)
    signup_token = models.CharField(max_length=-1, blank=True, null=True)
    signup_type = models.CharField(max_length=-1, blank=True, null=True)
    signup_expiration = models.DateTimeField(blank=True, null=True)
    partner_gid = models.IntegerField(blank=True, null=True)
    additional_info = models.CharField(max_length=-1, blank=True, null=True)
    phone_sanitized = models.CharField(max_length=-1, blank=True, null=True)
    supplier_rank = models.IntegerField(blank=True, null=True)
    customer_rank = models.IntegerField(blank=True, null=True)
    invoice_warn = models.CharField(max_length=-1, blank=True, null=True)
    invoice_warn_msg = models.TextField(blank=True, null=True)
    debit_limit = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    last_time_entries_checked = models.DateTimeField(blank=True, null=True)
    l10n_id_nik = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_tax_address = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_tax_name = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_kode_transaksi = models.CharField(max_length=-1, blank=True, null=True)
    l10n_id_pkp = models.BooleanField(blank=True, null=True)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    sale_warn = models.CharField(max_length=-1, blank=True, null=True)
    sale_warn_msg = models.TextField(blank=True, null=True)
    picking_warn = models.CharField(max_length=-1, blank=True, null=True)
    picking_warn_msg = models.TextField(blank=True, null=True)
    calendar_last_notif_ack = models.DateTimeField(blank=True, null=True)
    plan_to_change_car = models.BooleanField(blank=True, null=True)
    plan_to_change_bike = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner'


class ResPartnerAutocompleteSync(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    synched = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_autocomplete_sync'


class ResPartnerBank(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    bank = models.ForeignKey(ResBank, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    acc_number = models.CharField(max_length=-1)
    sanitized_acc_number = models.CharField(max_length=-1, blank=True, null=True)
    acc_holder_name = models.CharField(max_length=-1, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    allow_out_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_bank'
        unique_together = (('sanitized_acc_number', 'partner'),)


class ResPartnerCategory(models.Model):
    color = models.IntegerField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_category'


class ResPartnerIndustry(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(blank=True, null=True)
    full_name = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_industry'


class ResPartnerResPartnerCategoryRel(models.Model):
    category = models.OneToOneField(ResPartnerCategory, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'res_partner_res_partner_category_rel'
        unique_together = (('category', 'partner'),)


class ResPartnerTitle(models.Model):
    create_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('ResUsers', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    shortcut = models.JSONField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_partner_title'


class ResUsers(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    login = models.CharField(unique=True, max_length=-1)
    password = models.CharField(max_length=-1, blank=True, null=True)
    action_id = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey('self', models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    share = models.BooleanField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    totp_secret = models.CharField(max_length=-1, blank=True, null=True)
    notification_type = models.CharField(max_length=-1)
    odoobot_state = models.CharField(max_length=-1, blank=True, null=True)
    odoobot_failed = models.BooleanField(blank=True, null=True)
    karma = models.IntegerField(blank=True, null=True)
    rank = models.ForeignKey(GamificationKarmaRank, models.DO_NOTHING, blank=True, null=True)
    next_rank = models.ForeignKey(GamificationKarmaRank, models.DO_NOTHING, blank=True, null=True)
    sale_team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users'


class ResUsersApikeys(models.Model):
    name = models.CharField(max_length=-1)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    scope = models.CharField(max_length=-1, blank=True, null=True)
    index = models.CharField(max_length=8, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys'


class ResUsersApikeysDescription(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_apikeys_description'


class ResUsersDeletion(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    user_id_int = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_deletion'


class ResUsersIdentitycheck(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    request = models.CharField(max_length=-1, blank=True, null=True)
    password = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_identitycheck'


class ResUsersLog(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_log'


class ResUsersSettings(models.Model):
    user = models.OneToOneField(ResUsers, models.DO_NOTHING)
    voice_active_duration = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    push_to_talk_key = models.CharField(max_length=-1, blank=True, null=True)
    is_discuss_sidebar_category_channel_open = models.BooleanField(blank=True, null=True)
    is_discuss_sidebar_category_chat_open = models.BooleanField(blank=True, null=True)
    use_push_to_talk = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_settings'


class ResUsersSettingsVolumes(models.Model):
    user_setting = models.ForeignKey(ResUsersSettings, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    guest = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'res_users_settings_volumes'
        unique_together = (('user_setting', 'guest'), ('user_setting', 'partner'),)


class ResetViewArchWizard(models.Model):
    view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    compare_view = models.ForeignKey(IrUiView, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    reset_mode = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset_view_arch_wizard'


class ResourceCalendar(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    tz = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    two_weeks_calendar = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    hours_per_day = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar'


class ResourceCalendarAttendance(models.Model):
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    dayofweek = models.CharField(max_length=-1)
    day_period = models.CharField(max_length=-1)
    week_type = models.CharField(max_length=-1, blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    date_from = models.DateField(blank=True, null=True)
    date_to = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    hour_from = models.FloatField()
    hour_to = models.FloatField()

    class Meta:
        managed = False
        db_table = 'resource_calendar_attendance'


class ResourceCalendarLeaves(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING, blank=True, null=True)
    resource = models.ForeignKey('ResourceResource', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    time_type = models.CharField(max_length=-1, blank=True, null=True)
    date_from = models.DateTimeField()
    date_to = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    holiday = models.ForeignKey(HrLeave, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resource_calendar_leaves'


class ResourceResource(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    calendar = models.ForeignKey(ResourceCalendar, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    resource_type = models.CharField(max_length=-1)
    tz = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    time_efficiency = models.FloatField()

    class Meta:
        managed = False
        db_table = 'resource_resource'


class RuleGroupRel(models.Model):
    rule_group = models.OneToOneField(IrRule, models.DO_NOTHING, primary_key=True)
    group = models.ForeignKey(ResGroups, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'rule_group_rel'
        unique_together = (('rule_group', 'group'),)


class SaleAdvancePaymentInv(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    deposit_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    advance_payment_method = models.CharField(max_length=-1)
    fixed_amount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    deduct_down_payments = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv'


class SaleAdvancePaymentInvSaleOrderRel(models.Model):
    sale_advance_payment_inv = models.OneToOneField(SaleAdvancePaymentInv, models.DO_NOTHING, primary_key=True)
    sale_order = models.ForeignKey('SaleOrder', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_advance_payment_inv_sale_order_rel'
        unique_together = (('sale_advance_payment_inv', 'sale_order'),)


class SaleOrder(models.Model):
    campaign = models.ForeignKey('UtmCampaign', models.DO_NOTHING, blank=True, null=True)
    source = models.ForeignKey('UtmSource', models.DO_NOTHING, blank=True, null=True)
    medium = models.ForeignKey('UtmMedium', models.DO_NOTHING, blank=True, null=True)
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    partner_invoice = models.ForeignKey(ResPartner, models.DO_NOTHING)
    partner_shipping = models.ForeignKey(ResPartner, models.DO_NOTHING)
    fiscal_position = models.ForeignKey(AccountFiscalPosition, models.DO_NOTHING, blank=True, null=True)
    payment_term = models.ForeignKey(AccountPaymentTerm, models.DO_NOTHING, blank=True, null=True)
    pricelist = models.ForeignKey(ProductPricelist, models.DO_NOTHING)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    team = models.ForeignKey(CrmTeam, models.DO_NOTHING, blank=True, null=True)
    analytic_account = models.ForeignKey(AccountAnalyticAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    access_token = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    client_order_ref = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    signed_by = models.CharField(max_length=-1, blank=True, null=True)
    invoice_status = models.CharField(max_length=-1, blank=True, null=True)
    validity_date = models.DateField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    currency_rate = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_untaxed = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_tax = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    amount_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    commitment_date = models.DateTimeField(blank=True, null=True)
    date_order = models.DateTimeField()
    signed_on = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_order_template = models.ForeignKey('SaleOrderTemplate', models.DO_NOTHING, blank=True, null=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING, blank=True, null=True)
    incoterm = models.ForeignKey(AccountIncoterms, models.DO_NOTHING, db_column='incoterm', blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)
    procurement_group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    incoterm_location = models.CharField(max_length=-1, blank=True, null=True)
    picking_policy = models.CharField(max_length=-1)
    delivery_status = models.CharField(max_length=-1, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order'


class SaleOrderCancel(models.Model):
    template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_cancel'


class SaleOrderLine(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    currency = models.ForeignKey(ResCurrency, models.DO_NOTHING, blank=True, null=True)
    order_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    salesman = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom', blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    qty_delivered_method = models.CharField(max_length=-1, blank=True, null=True)
    invoice_status = models.CharField(max_length=-1, blank=True, null=True)
    analytic_distribution = models.JSONField(blank=True, null=True)
    name = models.TextField()
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_subtotal = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_total = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxexcl = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    price_reduce_taxinc = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_delivered = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    qty_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_invoiced = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    untaxed_amount_to_invoice = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    is_downpayment = models.BooleanField(blank=True, null=True)
    is_expense = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_tax = models.FloatField(blank=True, null=True)
    product_packaging_qty = models.FloatField(blank=True, null=True)
    customer_lead = models.FloatField()
    is_service = models.BooleanField(blank=True, null=True)
    project = models.ForeignKey(ProjectProject, models.DO_NOTHING, blank=True, null=True)
    task = models.ForeignKey(ProjectTask, models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_line'


class SaleOrderLineInvoiceRel(models.Model):
    invoice_line = models.OneToOneField(AccountMoveLine, models.DO_NOTHING, primary_key=True)
    order_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_line_invoice_rel'
        unique_together = (('invoice_line', 'order_line'),)


class SaleOrderOption(models.Model):
    order = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.TextField()
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    price_unit = models.DecimalField(max_digits=65535, decimal_places=65535)
    discount = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_option'


class SaleOrderTagRel(models.Model):
    order = models.OneToOneField(SaleOrder, models.DO_NOTHING, primary_key=True)
    tag = models.ForeignKey(CrmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_tag_rel'
        unique_together = (('order', 'tag'),)


class SaleOrderTemplate(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    number_of_days = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    note = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    require_signature = models.BooleanField(blank=True, null=True)
    require_payment = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template'


class SaleOrderTemplateLine(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    display_type = models.CharField(max_length=-1, blank=True, null=True)
    name = models.JSONField()
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_line'


class SaleOrderTemplateOption(models.Model):
    sale_order_template = models.ForeignKey(SaleOrderTemplate, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_order_template_option'


class SaleOrderTransactionRel(models.Model):
    transaction = models.OneToOneField(PaymentTransaction, models.DO_NOTHING, primary_key=True)
    sale_order = models.ForeignKey(SaleOrder, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sale_order_transaction_rel'
        unique_together = (('transaction', 'sale_order'),)


class SalePaymentProviderOnboardingWizard(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    payment_method = models.CharField(max_length=-1, blank=True, null=True)
    paypal_user_type = models.CharField(max_length=-1, blank=True, null=True)
    paypal_email_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_seller_account = models.CharField(max_length=-1, blank=True, null=True)
    paypal_pdt_token = models.CharField(max_length=-1, blank=True, null=True)
    manual_name = models.CharField(max_length=-1, blank=True, null=True)
    journal_name = models.CharField(max_length=-1, blank=True, null=True)
    acc_number = models.CharField(max_length=-1, blank=True, null=True)
    manual_post_msg = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sale_payment_provider_onboarding_wizard'


class SmsComposer(models.Model):
    res_id = models.IntegerField(blank=True, null=True)
    template = models.ForeignKey('SmsTemplate', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    composition_mode = models.CharField(max_length=-1)
    res_model = models.CharField(max_length=-1, blank=True, null=True)
    res_ids = models.CharField(max_length=-1, blank=True, null=True)
    recipient_single_number_itf = models.CharField(max_length=-1, blank=True, null=True)
    number_field_name = models.CharField(max_length=-1, blank=True, null=True)
    numbers = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField()
    mass_keep_log = models.BooleanField(blank=True, null=True)
    mass_force_send = models.BooleanField(blank=True, null=True)
    mass_use_blacklist = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_composer'


class SmsResend(models.Model):
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend'


class SmsResendRecipient(models.Model):
    sms_resend = models.ForeignKey(SmsResend, models.DO_NOTHING)
    notification = models.ForeignKey(MailNotification, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    partner_name = models.CharField(max_length=-1, blank=True, null=True)
    sms_number = models.CharField(max_length=-1, blank=True, null=True)
    resend = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_resend_recipient'


class SmsSms(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    mail_message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    number = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1)
    failure_type = models.CharField(max_length=-1, blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_sms'


class SmsTemplate(models.Model):
    model = models.ForeignKey(IrModel, models.DO_NOTHING)
    sidebar_action = models.ForeignKey(IrActWindow, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    template_fs = models.CharField(max_length=-1, blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    model_0 = models.CharField(db_column='model', max_length=-1, blank=True, null=True)  # Field renamed because of name conflict.
    name = models.JSONField(blank=True, null=True)
    body = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template'


class SmsTemplatePreview(models.Model):
    sms_template = models.ForeignKey(SmsTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    resource_ref = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template_preview'


class SmsTemplateReset(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sms_template_reset'


class SmsTemplateSmsTemplateResetRel(models.Model):
    sms_template_reset = models.OneToOneField(SmsTemplateReset, models.DO_NOTHING, primary_key=True)
    sms_template = models.ForeignKey(SmsTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'sms_template_sms_template_reset_rel'
        unique_together = (('sms_template_reset', 'sms_template'),)


class SnailmailConfirmInvoice(models.Model):
    invoice_send = models.ForeignKey(AccountInvoiceSend, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    model_name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_confirm_invoice'


class SnailmailLetter(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    res_id = models.IntegerField()
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    report_template = models.ForeignKey(IrActReportXml, models.DO_NOTHING, db_column='report_template', blank=True, null=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    model = models.CharField(max_length=-1)
    state_0 = models.CharField(db_column='state', max_length=-1)  # Field renamed because of name conflict.
    error_code = models.CharField(max_length=-1, blank=True, null=True)
    info_msg = models.CharField(max_length=-1, blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    color = models.BooleanField(blank=True, null=True)
    cover = models.BooleanField(blank=True, null=True)
    duplex = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter'


class SnailmailLetterFormatError(models.Model):
    message = models.ForeignKey(MailMessage, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    snailmail_cover = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_format_error'


class SnailmailLetterMissingRequiredFields(models.Model):
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    letter = models.ForeignKey(SnailmailLetter, models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(ResCountryState, models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey(ResCountry, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    street = models.CharField(max_length=-1, blank=True, null=True)
    street2 = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snailmail_letter_missing_required_fields'


class SpreadsheetDashboard(models.Model):
    dashboard_group = models.ForeignKey('SpreadsheetDashboardGroup', models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spreadsheet_dashboard'


class SpreadsheetDashboardGroup(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spreadsheet_dashboard_group'


class StockAssignSerial(models.Model):
    move = models.ForeignKey('StockMove', models.DO_NOTHING, blank=True, null=True)
    next_serial_count = models.IntegerField()
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    next_serial_number = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    serial_numbers = models.TextField(blank=True, null=True)
    multiple_lot_components_names = models.TextField(blank=True, null=True)
    expected_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    produced_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    show_apply = models.BooleanField(blank=True, null=True)
    show_backorders = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_assign_serial'


class StockBackorderConfirmation(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    show_transfers = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation'


class StockBackorderConfirmationLine(models.Model):
    backorder_confirmation = models.ForeignKey(StockBackorderConfirmation, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to_backorder = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_backorder_confirmation_line'


class StockChangeProductQty(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    new_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_change_product_qty'


class StockConflictQuantRel(models.Model):
    stock_inventory_conflict = models.OneToOneField('StockInventoryConflict', models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_conflict_quant_rel'
        unique_together = (('stock_inventory_conflict', 'stock_quant'),)


class StockImmediateTransfer(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    show_transfers = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer'


class StockImmediateTransferLine(models.Model):
    immediate_transfer = models.ForeignKey(StockImmediateTransfer, models.DO_NOTHING)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    to_immediate = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_immediate_transfer_line'


class StockInventoryAdjustmentName(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    inventory_adjustment_name = models.CharField(max_length=-1, blank=True, null=True)
    show_info = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name'


class StockInventoryAdjustmentNameStockQuantRel(models.Model):
    stock_inventory_adjustment_name = models.OneToOneField(StockInventoryAdjustmentName, models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_adjustment_name_stock_quant_rel'
        unique_together = (('stock_inventory_adjustment_name', 'stock_quant'),)


class StockInventoryConflict(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict'


class StockInventoryConflictStockQuantRel(models.Model):
    stock_inventory_conflict = models.OneToOneField(StockInventoryConflict, models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_conflict_stock_quant_rel'
        unique_together = (('stock_inventory_conflict', 'stock_quant'),)


class StockInventoryWarning(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning'


class StockInventoryWarningStockQuantRel(models.Model):
    stock_inventory_warning = models.OneToOneField(StockInventoryWarning, models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey('StockQuant', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_inventory_warning_stock_quant_rel'
        unique_together = (('stock_inventory_warning', 'stock_quant'),)


class StockLocation(models.Model):
    location = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    posx = models.IntegerField(blank=True, null=True)
    posy = models.IntegerField(blank=True, null=True)
    posz = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    removal_strategy = models.ForeignKey(ProductRemoval, models.DO_NOTHING, blank=True, null=True)
    cyclic_inventory_frequency = models.IntegerField(blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    complete_name = models.CharField(max_length=-1, blank=True, null=True)
    usage = models.CharField(max_length=-1)
    parent_path = models.CharField(max_length=-1, blank=True, null=True)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    last_inventory_date = models.DateField(blank=True, null=True)
    next_inventory_date = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    scrap_location = models.BooleanField(blank=True, null=True)
    return_location = models.BooleanField(blank=True, null=True)
    replenish_location = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    valuation_in_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    valuation_out_account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_location'
        unique_together = (('barcode', 'company'),)


class StockLot(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    ref = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_lot'


class StockMove(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING, db_column='product_uom')
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    rule = models.ForeignKey('StockRule', models.DO_NOTHING, blank=True, null=True)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING, blank=True, null=True)
    origin_returned_move = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    restrict_partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True)
    next_serial_count = models.IntegerField(blank=True, null=True)
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    product_packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    procure_method = models.CharField(max_length=-1)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    next_serial = models.CharField(max_length=-1, blank=True, null=True)
    reservation_date = models.DateField(blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    product_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    product_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    quantity_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    scrapped = models.BooleanField(blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    is_inventory = models.BooleanField(blank=True, null=True)
    additional = models.BooleanField(blank=True, null=True)
    date = models.DateTimeField()
    date_deadline = models.DateTimeField(blank=True, null=True)
    delay_alert_date = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_unit = models.FloatField(blank=True, null=True)
    analytic_account_line = models.ForeignKey(AccountAnalyticLine, models.DO_NOTHING, blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)
    sale_line = models.ForeignKey(SaleOrderLine, models.DO_NOTHING, blank=True, null=True)
    is_done = models.BooleanField(blank=True, null=True)
    unit_factor = models.FloatField(blank=True, null=True)
    created_production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    raw_material_production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, blank=True, null=True)
    consume_unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, blank=True, null=True)
    operation = models.ForeignKey(MrpRoutingWorkcenter, models.DO_NOTHING, blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True)
    bom_line = models.ForeignKey(MrpBomLine, models.DO_NOTHING, blank=True, null=True)
    byproduct = models.ForeignKey(MrpBomByproduct, models.DO_NOTHING, blank=True, null=True)
    order_finished_lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True)
    cost_share = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    manual_consumption = models.BooleanField(blank=True, null=True)
    repair = models.ForeignKey(RepairOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move'


class StockMoveLine(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    package_level = models.ForeignKey('StockPackageLevel', models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True)
    result_package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_category_name = models.CharField(max_length=-1, blank=True, null=True)
    lot_name = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    reference = models.CharField(max_length=-1, blank=True, null=True)
    description_picking = models.TextField(blank=True, null=True)
    reserved_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reserved_uom_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_done = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    date = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_move_line'


class StockMoveLineConsumeRel(models.Model):
    consume_line = models.OneToOneField(StockMoveLine, models.DO_NOTHING, primary_key=True)
    produce_line = models.ForeignKey(StockMoveLine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_line_consume_rel'
        unique_together = (('consume_line', 'produce_line'),)


class StockMoveMoveRel(models.Model):
    move_orig = models.OneToOneField(StockMove, models.DO_NOTHING, primary_key=True)
    move_dest = models.ForeignKey(StockMove, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_move_move_rel'
        unique_together = (('move_orig', 'move_dest'),)


class StockOrderpointSnooze(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    predefined_date = models.CharField(max_length=-1, blank=True, null=True)
    snoozed_until = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze'


class StockOrderpointSnoozeStockWarehouseOrderpointRel(models.Model):
    stock_orderpoint_snooze = models.OneToOneField(StockOrderpointSnooze, models.DO_NOTHING, primary_key=True)
    stock_warehouse_orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_orderpoint_snooze_stock_warehouse_orderpoint_rel'
        unique_together = (('stock_orderpoint_snooze', 'stock_warehouse_orderpoint'),)


class StockPackageDestination(models.Model):
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_destination'


class StockPackageLevel(models.Model):
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING)
    picking = models.ForeignKey('StockPicking', models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_level'


class StockPackageType(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    width = models.IntegerField(blank=True, null=True)
    packaging_length = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    barcode = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    base_weight = models.FloatField(blank=True, null=True)
    max_weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_package_type'


class StockPackageTypeStockPutawayRuleRel(models.Model):
    stock_putaway_rule = models.OneToOneField('StockPutawayRule', models.DO_NOTHING, primary_key=True)
    stock_package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_package_type_stock_putaway_rule_rel'
        unique_together = (('stock_putaway_rule', 'stock_package_type'),)


class StockPicking(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    backorder = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    picking_type = models.ForeignKey('StockPickingType', models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    move_type = models.CharField(max_length=-1)
    state = models.CharField(max_length=-1, blank=True, null=True)
    priority = models.CharField(max_length=-1, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    has_deadline_issue = models.BooleanField(blank=True, null=True)
    printed = models.BooleanField(blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    immediate_transfer = models.BooleanField(blank=True, null=True)
    scheduled_date = models.DateTimeField(blank=True, null=True)
    date_deadline = models.DateTimeField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    date_done = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale = models.ForeignKey(SaleOrder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking'
        unique_together = (('name', 'company'),)


class StockPickingBackorderRel(models.Model):
    stock_backorder_confirmation = models.OneToOneField(StockBackorderConfirmation, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_backorder_rel'
        unique_together = (('stock_backorder_confirmation', 'stock_picking'),)


class StockPickingSmsRel(models.Model):
    confirm_stock_sms = models.OneToOneField(ConfirmStockSms, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_sms_rel'
        unique_together = (('confirm_stock_sms', 'stock_picking'),)


class StockPickingTransferRel(models.Model):
    stock_immediate_transfer = models.OneToOneField(StockImmediateTransfer, models.DO_NOTHING, primary_key=True)
    stock_picking = models.ForeignKey(StockPicking, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_picking_transfer_rel'
        unique_together = (('stock_immediate_transfer', 'stock_picking'),)


class StockPickingType(models.Model):
    color = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    sequence_0 = models.ForeignKey(IrSequence, models.DO_NOTHING, db_column='sequence_id', blank=True, null=True)  # Field renamed because of name conflict.
    default_location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    default_location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    return_picking_type = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    reservation_days_before = models.IntegerField(blank=True, null=True)
    reservation_days_before_priority = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    sequence_code = models.CharField(max_length=-1)
    code = models.CharField(max_length=-1)
    reservation_method = models.CharField(max_length=-1)
    barcode = models.CharField(max_length=-1, blank=True, null=True)
    create_backorder = models.CharField(max_length=-1)
    name = models.JSONField()
    show_entire_packs = models.BooleanField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    use_create_lots = models.BooleanField(blank=True, null=True)
    use_existing_lots = models.BooleanField(blank=True, null=True)
    print_label = models.BooleanField(blank=True, null=True)
    show_operations = models.BooleanField(blank=True, null=True)
    show_reserved = models.BooleanField(blank=True, null=True)
    auto_show_reception_report = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    use_create_components_lots = models.BooleanField(blank=True, null=True)
    use_auto_consume_components_lots = models.BooleanField(blank=True, null=True)
    is_repairable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_picking_type'


class StockPutawayRule(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    location_in = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_out = models.ForeignKey(StockLocation, models.DO_NOTHING)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_putaway_rule'


class StockQuant(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    storage_category = models.ForeignKey('StockStorageCategory', models.DO_NOTHING, blank=True, null=True)
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey('StockQuantPackage', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    inventory_date = models.DateField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    reserved_quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    inventory_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_diff_quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    inventory_quantity_set = models.BooleanField(blank=True, null=True)
    in_date = models.DateTimeField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant'


class StockQuantPackage(models.Model):
    package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    package_use = models.CharField(max_length=-1)
    pack_date = models.DateField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quant_package'


class StockQuantStockRequestCountRel(models.Model):
    stock_request_count = models.OneToOneField('StockRequestCount', models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(StockQuant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_request_count_rel'
        unique_together = (('stock_request_count', 'stock_quant'),)


class StockQuantStockTrackConfirmationRel(models.Model):
    stock_track_confirmation = models.OneToOneField('StockTrackConfirmation', models.DO_NOTHING, primary_key=True)
    stock_quant = models.ForeignKey(StockQuant, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_quant_stock_track_confirmation_rel'
        unique_together = (('stock_track_confirmation', 'stock_quant'),)


class StockQuantityHistory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    inventory_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_quantity_history'


class StockReplenishmentInfo(models.Model):
    orderpoint = models.ForeignKey('StockWarehouseOrderpoint', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_replenishment_info'


class StockReplenishmentOption(models.Model):
    route = models.ForeignKey('StockRoute', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    replenishment_info = models.ForeignKey(StockReplenishmentInfo, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_replenishment_option'


class StockRequestCount(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    set_count = models.CharField(max_length=-1, blank=True, null=True)
    inventory_date = models.DateField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    accounting_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_request_count'


class StockReturnPicking(models.Model):
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True)
    original_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    parent_location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    move_dest_exists = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking'


class StockReturnPickingLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    wizard = models.ForeignKey(StockReturnPicking, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    to_refund = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_return_picking_line'


class StockRoute(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    supplied_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    supplier_wh = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    product_selectable = models.BooleanField(blank=True, null=True)
    product_categ_selectable = models.BooleanField(blank=True, null=True)
    warehouse_selectable = models.BooleanField(blank=True, null=True)
    packaging_selectable = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    sale_selectable = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_route'


class StockRouteCateg(models.Model):
    route = models.OneToOneField(StockRoute, models.DO_NOTHING, primary_key=True)
    categ = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_categ'
        unique_together = (('route', 'categ'),)


class StockRouteMove(models.Model):
    move = models.OneToOneField(StockMove, models.DO_NOTHING, primary_key=True)
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_move'
        unique_together = (('move', 'route'),)


class StockRoutePackaging(models.Model):
    route = models.OneToOneField(StockRoute, models.DO_NOTHING, primary_key=True)
    packaging = models.ForeignKey(ProductPackaging, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_packaging'
        unique_together = (('route', 'packaging'),)


class StockRouteProduct(models.Model):
    route = models.OneToOneField(StockRoute, models.DO_NOTHING, primary_key=True)
    product = models.ForeignKey(ProductTemplate, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_product'
        unique_together = (('route', 'product'),)


class StockRouteStockRulesReportRel(models.Model):
    stock_rules_report = models.OneToOneField('StockRulesReport', models.DO_NOTHING, primary_key=True)
    stock_route = models.ForeignKey(StockRoute, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_stock_rules_report_rel'
        unique_together = (('stock_rules_report', 'stock_route'),)


class StockRouteWarehouse(models.Model):
    route = models.OneToOneField(StockRoute, models.DO_NOTHING, primary_key=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_route_warehouse'
        unique_together = (('route', 'warehouse'),)


class StockRule(models.Model):
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    location_dest = models.ForeignKey(StockLocation, models.DO_NOTHING)
    location_src = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    route = models.ForeignKey(StockRoute, models.DO_NOTHING)
    route_sequence = models.IntegerField(blank=True, null=True)
    picking_type = models.ForeignKey(StockPickingType, models.DO_NOTHING)
    delay = models.IntegerField(blank=True, null=True)
    partner_address = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    propagate_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    group_propagation_option = models.CharField(max_length=-1, blank=True, null=True)
    action = models.CharField(max_length=-1)
    procure_method = models.CharField(max_length=-1)
    auto = models.CharField(max_length=-1)
    name = models.JSONField()
    active = models.BooleanField(blank=True, null=True)
    propagate_cancel = models.BooleanField(blank=True, null=True)
    propagate_carrier = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rule'


class StockRulesReport(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_tmpl = models.ForeignKey(ProductTemplate, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_has_variants = models.BooleanField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_rules_report'


class StockRulesReportStockWarehouseRel(models.Model):
    stock_rules_report = models.OneToOneField(StockRulesReport, models.DO_NOTHING, primary_key=True)
    stock_warehouse = models.ForeignKey('StockWarehouse', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_rules_report_stock_warehouse_rel'
        unique_together = (('stock_rules_report', 'stock_warehouse'),)


class StockSchedulerCompute(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scheduler_compute'


class StockScrap(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_uom = models.ForeignKey('UomUom', models.DO_NOTHING)
    lot = models.ForeignKey(StockLot, models.DO_NOTHING, blank=True, null=True)
    package = models.ForeignKey(StockQuantPackage, models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    picking = models.ForeignKey(StockPicking, models.DO_NOTHING, blank=True, null=True)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    scrap_location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    origin = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    scrap_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    date_done = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    production = models.ForeignKey(MrpProduction, models.DO_NOTHING, blank=True, null=True)
    workorder = models.ForeignKey(MrpWorkorder, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_scrap'


class StockStorageCategory(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    allow_new_product = models.CharField(max_length=-1)
    max_weight = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_storage_category'


class StockStorageCategoryCapacity(models.Model):
    storage_category = models.ForeignKey(StockStorageCategory, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    package_type = models.ForeignKey(StockPackageType, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'stock_storage_category_capacity'
        unique_together = (('package_type', 'storage_category'), ('product', 'storage_category'),)


class StockTraceabilityReport(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_traceability_report'


class StockTrackConfirmation(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_confirmation'


class StockTrackLine(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING, blank=True, null=True)
    wizard = models.ForeignKey(StockTrackConfirmation, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_track_line'


class StockValuationLayer(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    stock_valuation_layer = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    stock_move = models.ForeignKey(StockMove, models.DO_NOTHING, blank=True, null=True)
    account_move = models.ForeignKey(AccountMove, models.DO_NOTHING, blank=True, null=True)
    account_move_line = models.ForeignKey(AccountMoveLine, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    quantity = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_qty = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    remaining_value = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    price_diff_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer'


class StockValuationLayerRevaluation(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    account_journal = models.ForeignKey(AccountJournal, models.DO_NOTHING, blank=True, null=True)
    account = models.ForeignKey(AccountAccount, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    added_value = models.DecimalField(max_digits=65535, decimal_places=65535)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_valuation_layer_revaluation'


class StockWarehouse(models.Model):
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    view_location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    lot_stock = models.ForeignKey(StockLocation, models.DO_NOTHING)
    wh_input_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_qc_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_output_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    wh_pack_stock_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    pick_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    pack_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    out_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    in_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    int_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    return_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    crossdock_route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True)
    reception_route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True)
    delivery_route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    code = models.CharField(max_length=5)
    reception_steps = models.CharField(max_length=-1)
    delivery_steps = models.CharField(max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    manufacture_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    manufacture_mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    pbm_mto_pull = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    sam_rule = models.ForeignKey(StockRule, models.DO_NOTHING, blank=True, null=True)
    manu_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    pbm_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    sam_type = models.ForeignKey(StockPickingType, models.DO_NOTHING, blank=True, null=True)
    pbm_route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True)
    pbm_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    sam_loc = models.ForeignKey(StockLocation, models.DO_NOTHING, blank=True, null=True)
    manufacture_steps = models.CharField(max_length=-1)
    manufacture_to_resupply = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse'
        unique_together = (('code', 'company'), ('name', 'company'),)


class StockWarehouseOrderpoint(models.Model):
    warehouse = models.ForeignKey(StockWarehouse, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(ProcurementGroup, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING)
    route = models.ForeignKey(StockRoute, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    trigger = models.CharField(max_length=-1)
    snoozed_until = models.DateField(blank=True, null=True)
    product_min_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    product_max_qty = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_multiple = models.DecimalField(max_digits=65535, decimal_places=65535)
    qty_to_order = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    bom = models.ForeignKey(MrpBom, models.DO_NOTHING, blank=True, null=True)
    manufacturing_visibility_days = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_warehouse_orderpoint'
        unique_together = (('product', 'location', 'company'),)


class StockWarnInsufficientQtyRepair(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    repair = models.ForeignKey(RepairOrder, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_uom_name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_repair'


class StockWarnInsufficientQtyScrap(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    scrap = models.ForeignKey(StockScrap, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_uom_name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_scrap'


class StockWarnInsufficientQtyUnbuild(models.Model):
    product = models.ForeignKey(ProductProduct, models.DO_NOTHING)
    location = models.ForeignKey(StockLocation, models.DO_NOTHING)
    unbuild = models.ForeignKey(MrpUnbuild, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    product_uom_name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    quantity = models.FloatField()

    class Meta:
        managed = False
        db_table = 'stock_warn_insufficient_qty_unbuild'


class StockWhResupplyTable(models.Model):
    supplied_wh = models.OneToOneField(StockWarehouse, models.DO_NOTHING, primary_key=True)
    supplier_wh = models.ForeignKey(StockWarehouse, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'stock_wh_resupply_table'
        unique_together = (('supplied_wh', 'supplier_wh'),)


class SummaryEmpRel(models.Model):
    sum = models.OneToOneField(HrHolidaysSummaryEmployee, models.DO_NOTHING, primary_key=True)
    emp = models.ForeignKey(HrEmployee, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'summary_emp_rel'
        unique_together = (('sum', 'emp'),)


class SurveyInvite(models.Model):
    template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    mail_server = models.ForeignKey(IrMailServer, models.DO_NOTHING, blank=True, null=True)
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    lang = models.CharField(max_length=-1, blank=True, null=True)
    subject = models.CharField(max_length=-1, blank=True, null=True)
    email_from = models.CharField(max_length=-1, blank=True, null=True)
    existing_mode = models.CharField(max_length=-1)
    body = models.TextField(blank=True, null=True)
    emails = models.TextField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_invite'


class SurveyInvitePartnerIds(models.Model):
    invite = models.OneToOneField(SurveyInvite, models.DO_NOTHING, primary_key=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_invite_partner_ids'
        unique_together = (('invite', 'partner'),)


class SurveyMailComposeMessageIrAttachmentsRel(models.Model):
    wizard = models.OneToOneField(SurveyInvite, models.DO_NOTHING, primary_key=True)
    attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_mail_compose_message_ir_attachments_rel'
        unique_together = (('wizard', 'attachment'),)


class SurveyQuestion(models.Model):
    survey = models.ForeignKey('SurveySurvey', models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    random_questions_count = models.IntegerField(blank=True, null=True)
    page = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    validation_length_min = models.IntegerField(blank=True, null=True)
    validation_length_max = models.IntegerField(blank=True, null=True)
    triggering_question = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    triggering_answer = models.ForeignKey('SurveyQuestionAnswer', models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    question_type = models.CharField(max_length=-1, blank=True, null=True)
    matrix_subtype = models.CharField(max_length=-1, blank=True, null=True)
    answer_date = models.DateField(blank=True, null=True)
    validation_min_date = models.DateField(blank=True, null=True)
    validation_max_date = models.DateField(blank=True, null=True)
    title = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    question_placeholder = models.JSONField(blank=True, null=True)
    comments_message = models.JSONField(blank=True, null=True)
    validation_error_msg = models.JSONField(blank=True, null=True)
    constr_error_msg = models.JSONField(blank=True, null=True)
    is_page = models.BooleanField(blank=True, null=True)
    is_scored_question = models.BooleanField(blank=True, null=True)
    save_as_email = models.BooleanField(blank=True, null=True)
    save_as_nickname = models.BooleanField(blank=True, null=True)
    is_time_limited = models.BooleanField(blank=True, null=True)
    comments_allowed = models.BooleanField(blank=True, null=True)
    comment_count_as_answer = models.BooleanField(blank=True, null=True)
    validation_required = models.BooleanField(blank=True, null=True)
    validation_email = models.BooleanField(blank=True, null=True)
    constr_mandatory = models.BooleanField(blank=True, null=True)
    is_conditional = models.BooleanField(blank=True, null=True)
    answer_datetime = models.DateTimeField(blank=True, null=True)
    validation_min_datetime = models.DateTimeField(blank=True, null=True)
    validation_max_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    answer_numerical_box = models.FloatField(blank=True, null=True)
    answer_score = models.FloatField(blank=True, null=True)
    validation_min_float_value = models.FloatField(blank=True, null=True)
    validation_max_float_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question'


class SurveyQuestionAnswer(models.Model):
    question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING, blank=True, null=True)
    matrix_question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    value_image_filename = models.CharField(max_length=-1, blank=True, null=True)
    value = models.JSONField()
    is_correct = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    answer_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_question_answer'


class SurveyQuestionSurveyUserInputRel(models.Model):
    survey_user_input = models.OneToOneField('SurveyUserInput', models.DO_NOTHING, primary_key=True)
    survey_question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'survey_question_survey_user_input_rel'
        unique_together = (('survey_user_input', 'survey_question'),)


class SurveySurvey(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    color = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    attempts_limit = models.IntegerField(blank=True, null=True)
    certification_mail_template = models.ForeignKey(MailTemplate, models.DO_NOTHING, blank=True, null=True)
    certification_badge = models.OneToOneField(GamificationBadge, models.DO_NOTHING, blank=True, null=True)
    session_question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    questions_layout = models.CharField(max_length=-1)
    questions_selection = models.CharField(max_length=-1)
    progression_mode = models.CharField(max_length=-1, blank=True, null=True)
    access_mode = models.CharField(max_length=-1)
    access_token = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    scoring_type = models.CharField(max_length=-1)
    certification_report_layout = models.CharField(max_length=-1, blank=True, null=True)
    session_state = models.CharField(max_length=-1, blank=True, null=True)
    session_code = models.CharField(unique=True, max_length=-1, blank=True, null=True)
    title = models.JSONField()
    description = models.JSONField(blank=True, null=True)
    description_done = models.JSONField(blank=True, null=True)
    active = models.BooleanField(blank=True, null=True)
    users_login_required = models.BooleanField(blank=True, null=True)
    users_can_go_back = models.BooleanField(blank=True, null=True)
    is_attempts_limited = models.BooleanField(blank=True, null=True)
    is_time_limited = models.BooleanField(blank=True, null=True)
    certification = models.BooleanField(blank=True, null=True)
    certification_give_badge = models.BooleanField(blank=True, null=True)
    session_speed_rating = models.BooleanField(blank=True, null=True)
    session_start_time = models.DateTimeField(blank=True, null=True)
    session_question_start_time = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    scoring_success_min = models.FloatField(blank=True, null=True)
    time_limit = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_survey'


class SurveyUserInput(models.Model):
    message_main_attachment = models.ForeignKey(IrAttachment, models.DO_NOTHING, blank=True, null=True)
    survey = models.ForeignKey(SurveySurvey, models.DO_NOTHING)
    last_displayed_page = models.ForeignKey(SurveyQuestion, models.DO_NOTHING, blank=True, null=True)
    partner = models.ForeignKey(ResPartner, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(unique=True, max_length=-1)
    invite_token = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    nickname = models.CharField(max_length=-1, blank=True, null=True)
    test_entry = models.BooleanField(blank=True, null=True)
    scoring_success = models.BooleanField(blank=True, null=True)
    is_session_answer = models.BooleanField(blank=True, null=True)
    start_datetime = models.DateTimeField(blank=True, null=True)
    end_datetime = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    scoring_percentage = models.FloatField(blank=True, null=True)
    scoring_total = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_user_input'


class SurveyUserInputLine(models.Model):
    user_input = models.ForeignKey(SurveyUserInput, models.DO_NOTHING)
    survey = models.ForeignKey(SurveySurvey, models.DO_NOTHING, blank=True, null=True)
    question = models.ForeignKey(SurveyQuestion, models.DO_NOTHING)
    question_sequence = models.IntegerField(blank=True, null=True)
    suggested_answer = models.ForeignKey(SurveyQuestionAnswer, models.DO_NOTHING, blank=True, null=True)
    matrix_row = models.ForeignKey(SurveyQuestionAnswer, models.DO_NOTHING, blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    answer_type = models.CharField(max_length=-1, blank=True, null=True)
    value_char_box = models.CharField(max_length=-1, blank=True, null=True)
    value_date = models.DateField(blank=True, null=True)
    value_text_box = models.TextField(blank=True, null=True)
    skipped = models.BooleanField(blank=True, null=True)
    answer_is_correct = models.BooleanField(blank=True, null=True)
    value_datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    value_numerical_box = models.FloatField(blank=True, null=True)
    answer_score = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'survey_user_input_line'


class TaskDependenciesRel(models.Model):
    task = models.OneToOneField(ProjectTask, models.DO_NOTHING, primary_key=True)
    depends_on = models.ForeignKey(ProjectTask, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'task_dependencies_rel'
        unique_together = (('task', 'depends_on'),)


class TeamFavoriteUserRel(models.Model):
    team = models.OneToOneField(CrmTeam, models.DO_NOTHING, primary_key=True)
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_favorite_user_rel'
        unique_together = (('team', 'user'),)


class TrxFleetDriver(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    account_id = models.CharField(max_length=50, blank=True, null=True)
    driver_id = models.CharField(max_length=50, blank=True, null=True)
    driver_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx_fleet_driver'


class TrxFleetLookup(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    lookup_header = models.CharField(max_length=50, blank=True, null=True)
    lookup_body = models.CharField(max_length=50, blank=True, null=True)
    detail_code = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.CharField(max_length=50, blank=True, null=True)
    long_description = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx_fleet_lookup'


class TrxFleetWorkingRotation(models.Model):
    id = models.IntegerField(primary_key=True)
    vehicle_driver_id = models.IntegerField(blank=True, null=True)
    load_id = models.IntegerField(blank=True, null=True)
    load_category_id = models.IntegerField(blank=True, null=True)
    notes = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx_fleet_working_rotation'


class TrxFleetWorkingTimesheet(models.Model):
    id = models.IntegerField(primary_key=True)
    working_group_id = models.IntegerField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx_fleet_working_timesheet'


class TrxFleetWorkingVehicleDriver(models.Model):
    vehicle_id = models.CharField(max_length=50, blank=True, null=True)
    drive_id = models.CharField(max_length=50, blank=True, null=True)
    parent_id = models.IntegerField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trx_fleet_working_vehicle_driver'


class UomCategory(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_category'


class UomUom(models.Model):
    category = models.ForeignKey(UomCategory, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    uom_type = models.CharField(max_length=-1)
    name = models.JSONField()
    factor = models.DecimalField(max_digits=65535, decimal_places=65535)
    rounding = models.DecimalField(max_digits=65535, decimal_places=65535)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uom_uom'


class UtmCampaign(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING)
    stage = models.ForeignKey('UtmStage', models.DO_NOTHING)
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    title = models.JSONField()
    is_auto_campaign = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    ab_testing_total_pc = models.IntegerField(blank=True, null=True)
    ab_testing_winner_selection = models.CharField(max_length=-1, blank=True, null=True)
    ab_testing_completed = models.BooleanField(blank=True, null=True)
    ab_testing_schedule_datetime = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(ResCompany, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_campaign'


class UtmMedium(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_medium'


class UtmSource(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(unique=True, max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_source'


class UtmStage(models.Model):
    sequence = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField()
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_stage'


class UtmTag(models.Model):
    color = models.IntegerField(blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.JSONField(unique=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utm_tag'


class UtmTagRel(models.Model):
    tag = models.OneToOneField(UtmCampaign, models.DO_NOTHING, primary_key=True)
    campaign = models.ForeignKey(UtmTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'utm_tag_rel'
        unique_together = (('tag', 'campaign'),)


class ValidateAccountMove(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    force_post = models.BooleanField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'validate_account_move'


class WebEditorConverterTest(models.Model):
    integer = models.IntegerField(blank=True, null=True)
    many2one = models.ForeignKey('WebEditorConverterTestSub', models.DO_NOTHING, db_column='many2one', blank=True, null=True)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    char = models.CharField(max_length=-1, blank=True, null=True)
    selection_str = models.CharField(max_length=-1, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    html = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    numeric = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    datetime = models.DateTimeField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)
    float = models.FloatField(blank=True, null=True)
    binary = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test'


class WebEditorConverterTestSub(models.Model):
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'web_editor_converter_test_sub'


class WebTourTour(models.Model):
    user = models.ForeignKey(ResUsers, models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=-1)

    class Meta:
        managed = False
        db_table = 'web_tour_tour'


class WizardIrModelMenuCreate(models.Model):
    menu = models.ForeignKey(IrUiMenu, models.DO_NOTHING)
    create_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='create_uid', blank=True, null=True)
    write_uid = models.ForeignKey(ResUsers, models.DO_NOTHING, db_column='write_uid', blank=True, null=True)
    name = models.CharField(max_length=-1)
    create_date = models.DateTimeField(blank=True, null=True)
    write_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wizard_ir_model_menu_create'
