from openrouter import query_openrouter

def filter_jobs(jobs):
    good_jobs = []
    for job in jobs:
        sim = simulate_job(job)
        if sim['decision'] == 'REJECT':
            print(f'❌ Rejected job: {job["title"]} | Score: {sim["score"]}')
            continue
        prompt = f"Is this job worth applying to? Job title: {job['title']}, Description: {job['description']}. Reply YES or NO."
        answer = query_openrouter(prompt)
        if 'yes' in answer.lower():
            good_jobs.append(job)
    return good_jobs

def generate_cover_letter(job):
    prompt = f"Write a professional cover letter for this job: {job['title']}, {job['description']}, using the name David Muigai."
    return query_openrouter(prompt)

def choose_and_apply_jobs(jobs):
    filtered = filter_jobs(jobs)
    for job in filtered:
        letter = generate_cover_letter(job)
        print(f"🚀 Applying to {job['title']}")
        print(f"📝 Cover Letter:\n{letter}")
