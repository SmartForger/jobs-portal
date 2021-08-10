from django.conf.urls import url
from .views import (
    index,
    change_password,
    admin_user_list,
    new_admin_user,
    edit_user,
    view_user,
    country,
    locations,
    aws_push_to_s3,
    aws_del_from_s3,
    tech_skills,
    delete_skill,
    delete_user,
    skill_status,
    languages,
    qualification_status,
    delete_language,
    qualifications,
    delete_qualification,
    delete_functional_area,
    industries,
    delete_industry,
    industry_status,
    functional_area,
    functional_area_status,
    recruiters_list,
    view_recruiter,
    recruiter_status_change,
    recruiter_delete,
    recruiter_paid_status_change,
    post_list,
    post_detail,
    status_change,
    deactivate_job,
    enable_job,
    delete_job,
    publish_job,
    new_govt_job,
    edit_govt_job,
    preview_job,
    edit_job_title,
    post_on_all_fb_groups,
    adding_existing_candidates_to_jobposts,
    applicants,
    view_applicant,
    applicant_actions,
    emailtemplates,
    moving_duplicates,
    new_template,
    edit_template,
    view_template,
    delete_template,
    send_mail,
    sent_mails,
    view_sent_mail,
    delete_sent_mail,
    search_log,
    view_search_log,
    subscribers,
    view_subscribers,
    search_summary,
    applicants_mail,
    removing_duplicate_companies,
    reports,
    new_company,
    edit_company,
    companies,
    enable_company,
    enable_agency,
    delete_company,
    enable_paid_company,
    view_company,
    company_recruiters,
    company_jobposts,
    company_tickets,
    edit_menu,
    delete_menu,
    menu_status,
    menu_order,
    google_login,
    assessment_skills,
    new_question,
    skill_questions,
    view_question,
    save_meta_data,
    clear_cache,
)

app_name = "dashboard"

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^change_password/$", change_password, name="change_password"),
    url(r"^google_login/$", google_login, name="google_login"),
    # users
    url(r"^users/list/$", admin_user_list, name="admin_user_list"),
    url(r"^users/new-user/$", new_admin_user, name="new_admin_user"),
    url(r"^users/edit/(?P<user_id>[-\w]+)/$", edit_user, name="edit_user"),
    url(r"^users/view/(?P<user_id>[-\w]+)/$", view_user, name="view_user"),
    url(r"^users/delete/(?P<user_id>[-\w]+)/$", delete_user, name="delete_user"),
    # data
    url(r"^country/$", country, name="country"),
    url(r"^(?P<status>[-\w]+)/locations/$", locations, name="locations"),
    url(r"^aws-push-to-s3/$", aws_push_to_s3, name="aws_push_to_s3"),
    url(r"^aws-del-from-s3/$", aws_del_from_s3, name="aws_del_from_s3"),
    # technical skill
    url(r"^technical_skills/$", tech_skills, name="tech_skills"),
    url(r"^delete_skill/(?P<skill_id>[-\w]+)/$", delete_skill, name="delete_skill"),
    url(r"^skill/status/(?P<skill_id>[-\w]+)/$", skill_status, name="skill_status"),
    # languages
    url(r"^languages/$", languages, name="languages"),
    url(
        r"^delete_language/(?P<language_id>[-\w]+)/$",
        delete_language,
        name="delete_language",
    ),
    # qualification
    url(r"^qualifications/$", qualifications, name="qualifications"),
    url(
        r"^delete_qualification/(?P<qualification_id>[-\w]+)/$",
        delete_qualification,
        name="delete_qualification",
    ),
    url(
        r"^qualification/status/(?P<qualification_id>[-\w]+)/$",
        qualification_status,
        name="qualification_status",
    ),
    # industry
    url(r"^industries/$", industries, name="industries"),
    url(
        r"^delete_industry/(?P<industry_id>[-\w]+)/$",
        delete_industry,
        name="delete_industry",
    ),
    url(
        r"^industry/status/(?P<industry_id>[-\w]+)/$",
        industry_status,
        name="industry_status",
    ),
    # functinal area
    url(r"^functional_area/$", functional_area, name="functional_area"),
    url(
        r"^functional_area/(?P<functional_area_id>[-\w]+)/$",
        delete_functional_area,
        name="delete_functional_area",
    ),
    url(
        r"^functional_area/status/(?P<functional_area_id>[-\w]+)/$",
        functional_area_status,
        name="functional_area_status",
    ),
    # recruiter
    url(
        r"^recruiters/(?P<status>[-\w]+)/list/$",
        recruiters_list,
        name="recruiters_list",
    ),
    url(
        r"^recruiter/view/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        view_recruiter,
        name="view_recruiter",
    ),
    url(
        r"^recruiter/status/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        recruiter_status_change,
        name="recruiter_status_change",
    ),
    url(
        r"^recruiter/remove/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        recruiter_delete,
        name="recruiter_delete",
    ),
    url(
        r"^recruiter/paid-status/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        recruiter_paid_status_change,
        name="recruiter_paid_status_change",
    ),
    # jobposts
    url(r"^jobpost/(?P<job_type>[-\w]+)/list/", post_list, name="job_posts"),
    url(r"^jobpost/view/(?P<post_id>[-\w]+)/", post_detail, name="post_detail"),
    url(
        r"^jobpost/status_change/(?P<post_id>[-\w]+)/$",
        status_change,
        name="status_change",
    ),
    url(
        r"^jobpost/deactivate/(?P<job_post_id>[a-zA-Z0-9]+)/$",
        deactivate_job,
        name="deactivate_job",
    ),
    url(r"^jobpost/enable/(?P<job_post_id>[a-zA-Z0-9]+)/$", enable_job, name="enable"),
    url(r"^jobpost/delete/(?P<job_post_id>[a-zA-Z0-9]+)/$", delete_job, name="delete"),
    url(
        r"^jobpost/publish/(?P<job_post_id>[a-zA-Z0-9]+)/$", publish_job, name="publish"
    ),
    url(r"^jobpost/(?P<job_type>[-\w]+)/add/$", new_govt_job, name="new_govt_job"),
    url(r"^jobpost/edit/(?P<post_id>[-\w]+)/$", edit_govt_job, name="edit_govt_job"),
    url(r"^jobpost/preview/(?P<post_id>[-\w]+)/$", preview_job, name="preview_job"),
    url(
        r"^jobpost/title/edit/(?P<post_id>[-\w]+)/$",
        edit_job_title,
        name="edit_job_title",
    ),
    url(
        r"^jobpost/fb-groups/post/(?P<post_id>[-\w]+)/$",
        post_on_all_fb_groups,
        name="post_on_all_fb_groups",
    ),
    url(
        r"^jobpost/candidates-add/(?P<post_id>[-\w]+)/$",
        adding_existing_candidates_to_jobposts,
        name="adding_existing_candidates_to_jobposts",
    ),
    # applicants
    url(r"^applicants/list/$", applicants, name="applicants"),
    url(r"^applicants/(?P<status>[-\w]+)/list/$", applicants, name="applicants"),
    url(
        r"^applicant/view/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        view_applicant,
        name="view_applicant",
    ),
    url(
        r"^applicant/actions/(?P<user_id>[a-zA-Z0-9_-]+)/$",
        applicant_actions,
        name="applicant_actions",
    ),
    # mail templates
    url(r"^mail-template/list/", emailtemplates, name="emailtemplates"),
    url(r"^mail-template/new/", new_template, name="new_template"),
    url(
        r"^mail-template/edit/(?P<template_id>[-\w]+)/",
        edit_template,
        name="edit_mailtemplate",
    ),
    url(
        r"^mail-template/view/(?P<template_id>[-\w]+)/",
        view_template,
        name="view_mailtemplate",
    ),
    url(
        r"^mail-template/delete/(?P<template_id>[-\w]+)/",
        delete_template,
        name="delete_mailtemplate",
    ),
    url(r"^send_mail/(?P<template_id>[-\w]+)/", send_mail, name="send_mail"),
    # view sent mails
    url(r"^sent-mail/list/", sent_mails, name="sent_mails"),
    url(
        r"^sent-mail/view/(?P<sent_mail_id>[-\w]+)/",
        view_sent_mail,
        name="view_sent_mail",
    ),
    url(
        r"^sent-mail/delete/(?P<sent_mail_id>[-\w]+)/",
        delete_sent_mail,
        name="delete_sent_mail",
    ),
    # view search logs
    url(r"^search-log/list/", search_log, name="search_log"),
    url(
        r"^search-log/view/(?P<search_log_id>[-\w]+)/",
        view_search_log,
        name="view_search_log",
    ),
    # view search logs
    url(r"^subscribers/list/", subscribers, name="subscribers"),
    url(
        r"^subscribers/view/(?P<skill_id>[-\w]+)/",
        view_subscribers,
        name="view_subscribers",
    ),
    url(
        r"^search/(?P<search_type>[-\w]+)/summary/",
        search_summary,
        name="search_summary",
    ),
    url(r"^applicants-mails/", applicants_mail, name="applicants_mail"),
    url(
        r"^update-company-jobposts/",
        removing_duplicate_companies,
        name="removing_duplicate_companies",
    ),
    url(r"^reports/", reports, name="reports"),
    # companies
    url(r"^companies/new/", new_company, name="new_company"),
    url(r"^companies/edit/(?P<company_id>[-\w]+)/", edit_company, name="edit_company"),
    url(r"^companies/(?P<company_type>[-\w]+)/list/", companies, name="companies"),
    url(
        r"^company/status/(?P<company_id>[-\w]+)/",
        enable_company,
        name="enable_company",
    ),
    url(r"^company/agency/(?P<agency_id>[-\w]+)/", enable_agency, name="enable_agency"),
    url(
        r"^company/delete/(?P<company_id>[-\w]+)/",
        delete_company,
        name="delete_company",
    ),
    url(
        r"^company/paid/(?P<company_id>[-\w]+)/",
        enable_paid_company,
        name="enable_paid_company",
    ),
    url(r"^company/view/(?P<company_id>[-\w]+)/", view_company, name="view_company"),
    url(
        r"^company/(?P<company_id>[-\w]+)/recruiters/(?P<status>[-\w]+)/list/",
        company_recruiters,
        name="company_recruiters",
    ),
    url(
        r"^company/jobposts/(?P<company_id>[-\w]+)/",
        company_jobposts,
        name="company_jobposts",
    ),
    url(
        r"^company/tickets/(?P<company_id>[-\w]+)/",
        company_tickets,
        name="company_tickets",
    ),
    url(
        r"^company/(?P<company_id>[-\w]+)/menu/edit/(?P<menu_id>[a-zA-Z0-9]+)/$",
        edit_menu,
        name="edit_menu",
    ),
    url(
        r"^company/(?P<company_id>[-\w]+)/menu/delete/(?P<menu_id>[a-zA-Z0-9]+)/$",
        delete_menu,
        name="delete_menu",
    ),
    url(
        r"^company/(?P<company_id>[-\w]+)/menu/status/(?P<menu_id>[a-zA-Z0-9]+)/$",
        menu_status,
        name="menu_status",
    ),
    url(r"^company/(?P<company_id>[-\w]+)/menu/order/$", menu_order, name="menu_order"),
    # Assessment urls
    url(r"^assessment/skills/", assessment_skills, name="assessment_skills"),
    url(r"^assessment/question/new/", new_question, name="new_question"),
    url(
        r"^assement/skill/questions/(?P<skill_id>[-\w]+)/$",
        skill_questions,
        name="skill_questions",
    ),
    url(
        r"^assement/question/view/(?P<question_id>[-\w]+)/",
        view_question,
        name="view_question",
    ),
    url(r"^save/meta-data/", save_meta_data, name="save_meta_data"),
    url(
        r"^moving/duplicate/(?P<value>[-\w]+)/",
        moving_duplicates,
        name="move_duplicates",
    ),
    url(r"^clear/cache/", clear_cache, name="clear_cache"),
]
