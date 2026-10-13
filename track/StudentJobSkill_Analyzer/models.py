class StudentProfile:
    def __init__(self,name,skills):
        self.name=name
        self.skills=self.normalize_skills(skills)
    def normalize_skills(self,skills):
        return {skill.strip().lower()
        for skill in skills 
        if skill.strip()}

class JobDescription:
    def __init__(self,title,required_skills):
        self.title=title
        self.required_skills=self.normalize_skills(required_skills)
    def normalize_skills(self,required_skills):
        return {skill.strip().lower()
        for skill in required_skills 
        if skill.strip()}