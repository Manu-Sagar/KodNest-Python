
from models import StudentProfile, JobDescription
from analyzers import MatchScoreAnalyzer, MissingSkillAnalyzer


class Manager:
    def __init__(self, student, job):
        self.student = student
        self.job = job

        self.score_calculator = MatchScoreAnalyzer()
        self.skill_detector = MissingSkillAnalyzer()

    def generate_report(self):
        score_result = self.score_calculator.analyze(
            self.student, self.job
        )

        missing_result = self.skill_detector.analyze(
            self.student, self.job
        )

        print("\n===== STUDENT JOB MATCHING REPORT =====")
        print(f"Student Name: {self.student.name}")
        print(f"Job Title: {self.job.title}")

        print(f"Required Skills: {sorted(self.job.required_skills)}")
        print(f"Student Skills: {sorted(self.student.skills)}")
        print(f"Matched Skills: {sorted(score_result['matched_skills'])}")
        print(f"Missing Skills: {sorted(missing_result['missing_skills'])}")

        print(
            f"Match Score: "
            f"{score_result['match_percentage']:.2f}%"
        )


if __name__ == "__main__":
    student = StudentProfile(
        "Manu",
        ["Python", "SQL", "Java"]
    )

    job = JobDescription(
        "Python Developer",
        ["Python", "SQL", "Django"]
    )

    manager = Manager(student, job)
    manager.generate_report()
