from abc import ABC, abstractmethod


class SkillAnalyzer(ABC):
    @abstractmethod
    def analyze(self, student, job):
        pass


class MatchScoreAnalyzer(SkillAnalyzer):
    def analyze(self, student, job):
        matched_skills = student.skills & job.required_skills
        if not job.required_skills:
            match_percentage = 0.0
        else:
            match_percentage = (len(matched_skills) / len(job.required_skills)) * 100

        return {
            "matched_skills": matched_skills,
            "match_percentage": match_percentage,
        }


class MissingSkillAnalyzer(SkillAnalyzer):
    def analyze(self, student, job):
        missing_skills = job.required_skills - student.skills
        return {
            "missing_skills": list(missing_skills)
        }