from django.shortcuts import render
from django.http import Http404
from .data import (
    PERSONAL, ABOUT, EDUCATION, TIMELINE, SKILL_CATEGORIES,
    TECH_TAGS, PROJECTS, COMPETITIONS, CONTACT,
)


def home(request):
    return render(request, "home.html", {
        "personal": PERSONAL,
        "tech_tags": TECH_TAGS,
        "active": "home",
    })


def about(request):
    return render(request, "about.html", {
        "personal": PERSONAL,
        "about": ABOUT,
        "education": EDUCATION,
        "timeline": TIMELINE,
        "active": "about",
    })


def skills(request):
    return render(request, "skills.html", {
        "personal": PERSONAL,
        "categories": SKILL_CATEGORIES,
        "active": "skills",
    })


def projects(request):
    return render(request, "projects.html", {
        "personal": PERSONAL,
        "projects": PROJECTS,
        "active": "projects",
    })


def project_detail(request, project_id):
    project = next((p for p in PROJECTS if p["id"] == project_id), None)
    if not project:
        raise Http404("项目未找到")
    return render(request, "project_detail.html", {
        "personal": PERSONAL,
        "project": project,
        "active": "projects",
    })


def competitions(request):
    return render(request, "competitions.html", {
        "personal": PERSONAL,
        "competitions": COMPETITIONS,
        "active": "competitions",
    })


def resume(request):
    return render(request, "resume.html", {
        "personal": PERSONAL,
        "about": ABOUT,
        "education": EDUCATION,
        "skills": SKILL_CATEGORIES,
        "projects": PROJECTS,
        "competitions": COMPETITIONS,
        "active": "resume",
    })


def contact(request):
    return render(request, "contact.html", {
        "personal": PERSONAL,
        "contact": CONTACT,
        "active": "contact",
    })
