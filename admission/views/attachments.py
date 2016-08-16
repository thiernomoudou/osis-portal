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
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from admission import models as mdl
from admission.views import demande_validation, tabs
from admission.forms import RemoveAttachmentForm
from osis_common.forms import UploadDocumentFileForm
from osis_common.models.document_file import DocumentFile
from django.forms import formset_factory


def update(request, application_id=None):
    past_attachments = list_attachments(request.user)
    attachments_available = attachments_left_available(len(past_attachments))
    UploadDocumentFileFormSet = formset_factory(UploadDocumentFileForm, extra=0, max_num=attachments_available)

    if request.method == "POST":
        document_formset = UploadDocumentFileFormSet(request.POST, request.FILES)
        if document_formset.is_valid():
            for document in document_formset:
                save_document_from_form(document, request.user)
    elif request.method == "GET":
        document_formset = UploadDocumentFileFormSet()

    if application_id:
        application = mdl.application.find_by_id(application_id)
    else:
        application = mdl.application.init_application(request.user)

    applicant = mdl.applicant.find_by_user(request.user)
    tab_status = tabs.init(request)

    remove_attachment_form = RemoveAttachmentForm()
    return render(request, "admission_home.html", {
        "tab_active": 6,
        "application": application,
        "validated_profil": demande_validation.validate_profil(applicant),
        "validated_diploma": demande_validation.validate_diploma(application),
        "validated_curriculum": demande_validation.validate_curriculum(application),
        "validated_application": demande_validation.validate_application(application),
        "validated_accounting": demande_validation.validate_accounting(),
        "validated_sociological": demande_validation.validate_sociological(),
        "validated_attachments": demande_validation.validate_attachments(),
        "validated_submission": demande_validation.validate_submission(),
        "tab_profile": tab_status['tab_profile'],
        "tab_applications": tab_status['tab_applications'],
        "tab_diploma": tab_status['tab_diploma'],
        "tab_curriculum": tab_status['tab_curriculum'],
        "tab_accounting": tab_status['tab_accounting'],
        "tab_sociological": tab_status['tab_sociological'],
        "tab_attachments": tab_status['tab_attachments'],
        "tab_submission": tab_status['tab_submission'],
        "applications": mdl.application.find_by_user(request.user),
        "document_formset": document_formset,
        "attachments": past_attachments,
        "removeAttachmentForm": remove_attachment_form})


def remove_attachment(request):
    """
    View used to remove previous attachments.
    """
    if request.method == "POST":
        form = RemoveAttachmentForm(request.POST)
        if form.is_valid():
            attachment_pk = form.cleaned_data['attachment_id']
            # form is valid ensure that there is a document having that pk value
            attachment_to_remove = DocumentFile.objects.get(pk=attachment_pk)
            safe_document_removal(request.user, "admission_attachments", attachment_to_remove)
    return redirect(update)


def safe_document_removal(user, document_type, document):
    """
    Safely remove a document by ensuring that the user is the one
    that owns the file and the document_type is the correct one.
    :param user: a User object
    :param document_type: a string
    :return:
    """
    if document.user == user and document.document_type == document_type:
        document.delete()


def list_attachments(user):
    """
    Returns the list of all the attachments uploaded by the user.
    :param user: the current user in session.
    :return: an array of dictionnary
    """
    uploaded_attachments = DocumentFile.objects.filter(user=user,
                                                       document_type="admission_attachments")

    return list(uploaded_attachments)


def attachments_left_available(number_attachments_uploaded):
    """
    Compute the number of attachments left that the user can upload.
    :param number_attachments_uploaded: number of attachments already uploaded
    :return: slot available
    """
    max_num_attachments = 5
    num_attachments_uploaded = number_attachments_uploaded
    return max_num_attachments - num_attachments_uploaded


def save_document_from_form(document, user):
    """
    Save a document (attachment) from a form.
    :param document: an UploadDocumentForm received from a POST request.
    :param user: the current user
    :return:
    """
    file_name = document.cleaned_data['file_name']
    file = document.cleaned_data['file']
    description = document.cleaned_data['description']
    # Never trust a user. They could change the hidden input values.
    # Ex: user, document_type, storage_duration, etc.
    storage_duration = 0
    document_type = "admission_attachments"
    content_type = file.content_type
    size = file.size

    doc_file = DocumentFile(file_name=file_name, file=file,
                            description=description, storage_duration=storage_duration,
                            document_type=document_type, content_type=content_type,
                            size=size, user=user)
    doc_file.save()
