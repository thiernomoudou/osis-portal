##############################################################################
#
#    OSIS stands for Open Student Information System. It's an application
#    designed to manage the core business of higher education institutions,
#    such as universities, faculties, institutes and professional schools.
#    The core business involves the administration of students, teachers,
#    courses, programs and so on.
#
#    Copyright (C) 2015-2016 Université catholique de Louvain (http://www.uclouvain.be)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    A copy of this license - GNU General Public License - is available
#    at the root of the source code of this program.  If not,
#    see http://www.gnu.org/licenses/.
#
##############################################################################
from django.db import models
from django.contrib import admin
from admission.models import offer_year_calendar


class OfferYearAdmin(admin.ModelAdmin):
    list_display = ('acronym', 'title', 'academic_year', 'domain')
    fieldsets = ((None, {'fields': ('academic_year', 'acronym', 'title', 'title_international', 'domain', 'grade_type')}),)


class OfferYear(models.Model):
    external_id = models.CharField(max_length=100, blank=True, null=True)
    academic_year = models.ForeignKey('AcademicYear')
    acronym = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    title_international = models.CharField(max_length=255, blank=True, null=True)
    domain = models.ForeignKey('Domain')
    grade_type = models.ForeignKey('GradeType', blank=True, null=True, db_index=True)

    def __str__(self):
        return u"%s - %s" % (self.academic_year, self.acronym)


    @property
    def offer_year_calendar(self):
        print('find_offer_year_calendar')
        #Should only be one record
        return offer_year_calendar.OfferYearCalendar.objects.filter(offer_year=self).order_by("start_date").first()


def find_by_id(offer_year_id):
    return OfferYear.objects.get(pk=offer_year_id)


def find_all():
    return OfferYear.objects.all().order_by("acronym")


def find_by_domain_grade(domain, grade):
    return OfferYear.objects.filter(domain=domain, grade_type=grade).order_by("acronym")

