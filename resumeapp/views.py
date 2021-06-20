from django.shortcuts import render,redirect
from resumeapp.models import Resume

# Create your views here.



def fetch_resume_data(request,id):#id=1
    resume_list=Resume.objects.get(id=id)
    context={
        'resume_list':resume_list
    }
    return render(request,"resume.html",context)


def create_resume_form(request):
    if request.method == "POST":
        summary=request.POST.get('summary')
        name=request.POST.get('name')
        phoneno=request.POST.get('phoneno')
        email=request.POST.get('email')
        company=request.POST.get('company')
        duration=request.POST.get('duration')
        projects=request.POST.get('projects')
        skills=request.POST.get('skills')
        softwares=request.POST.get('softwares')
        certifications=request.POST.get('certifications')
        achievements=request.POST.get('achievements')
        strengths=request.POST.get('strengths')
        weakness=request.POST.get('weakness')
        schoolname=request.POST.get('schoolname')
        schoolduration=request.POST.get('schoolduration')
        schoolmarkspercentage=request.POST.get('schoolmarkspercentage')
        collegename=request.POST.get('collegename')
        collegeduration=request.POST.get('collegeduration')
        collegeuniversity=request.POST.get('collegeuniversity')
        collegemarkspercentage=request.POST.get('collegemarkspercentage')
        languages=request.POST.get('languages')

        r=Resume(summary=summary,name=name,phoneno=phoneno,emailid=email,skills=skills,
        softwares=softwares,company=company,experience=duration,projects=projects,
        certification=certifications,achievements=achievements,strengths=strengths,
        weakness=weakness,schoolname=schoolname,schoolduration=schoolduration,percentageofschoolmarks=schoolmarkspercentage,
        collegename=collegename,collegeduration=collegeduration,percentageofcollegemarks=collegemarkspercentage,
        collegeuniversity=collegeuniversity,languagesknown=languages)
        r.save()
        return redirect("/home")
        
    return render(request,"resumeform.html")  


def home_view(request):
    all_resume=Resume.objects.all()
    return render(request,"home.html",{'all_resume':all_resume})







        

      
