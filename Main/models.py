from django.db import models


class BoardMembers(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FinancialOrganization(models.Model):
    chairman_board_directors = models.ForeignKey(
        BoardMembers,
        on_delete=models.SET_NULL,
        related_name="chair_directors",
        null=True,
        blank=True,
        verbose_name="Председатель Совета директоров"
    )
    chairman_board = models.ForeignKey(
        BoardMembers,
        on_delete=models.SET_NULL,
        related_name="chair_board",
        null=True,
        blank=True,
        verbose_name="Председатель Правления"
    )
    board_of_directors = models.ManyToManyField(
        BoardMembers,
        related_name='board_directors',
        blank=True,
        verbose_name="Совет директоров"
    )
    executive_board_members = models.ManyToManyField(
        BoardMembers,
        related_name='executive_board_organizations',
        blank=True,
        verbose_name="Члены Правления"
    )
    chief_accountant = models.CharField(max_length=255, verbose_name="Главный бухгалтер")
    bin = models.PositiveIntegerField(unique=True, verbose_name="БИН")
    address = models.CharField(max_length=255, verbose_name="Адрес(Адрес (город, улица, дом, квартира)")
    phone_number = models.CharField(max_length=20, verbose_name="Телефон организации")
    fax = models.CharField(max_length=20, verbose_name="Факс организации")
    email = models.EmailField(verbose_name="Электронная почта организации")
    website = models.URLField(verbose_name="Веб-сайт организации", null=True, blank=True)
    second_tier_bank = models.CharField(max_length=255, verbose_name="Банк второго уровня")
    custodian = models.CharField(max_length=255, verbose_name="Кастодиан")
    broker_dealers = models.CharField(max_length=255, verbose_name="Брокеры-дилеры")
    related_organizations = models.ManyToManyField('self', related_name='related_organizations', blank=True,
                                                   verbose_name="Связанные организации")


class SanctionsAndMeasures(models.Model):
    organization = models.ForeignKey(
        "FinancialOrganization",
        on_delete=models.CASCADE,
        related_name="sanctions_measures",
        verbose_name="Организация"
    )
    organization_type = models.CharField(max_length=255, verbose_name="Тип организации")
    decision_date = models.DateField(null=True, blank=True, verbose_name="Дата решения уполномоченного органа")
    decision_number = models.CharField(max_length=255, verbose_name="Номер принятия решение/дела")
    penalty_type = models.CharField(max_length=255, verbose_name="Вид взыскания")
    foreclosure_type = models.CharField(max_length=255, verbose_name="Тип взыскания")
    penalty_imposed = models.CharField(max_length=255, verbose_name="Наложенное взыскание")
    violation_reason = models.CharField(max_length=255, verbose_name="Существо нарушения")
    due_date = models.DateField(null=True, blank=True, verbose_name="Срок исполнения")
    article_paragraphs = models.CharField(max_length=255, verbose_name="Статья/пункты НПА, Статья КоАП")
    remark = models.CharField(max_length=255, verbose_name="Примечание")
    regular_act = models.CharField(max_length=255, verbose_name="Тип НПА")
    department_name = models.CharField(max_length=255, verbose_name="Наименование департамента АРРФР / УРП")
