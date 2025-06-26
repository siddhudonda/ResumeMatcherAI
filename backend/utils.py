def format_resume_data(data):
    if 'error' in data:
        return data['error']
    summary = f"Name: {data.get('name', 'N/A')}\n"
    summary += f"Email: {data.get('email', 'N/A')}\n"
    summary += f"Skills: {', '.join(data.get('skills', []))}\n"
    summary += f"Experience: {data.get('total_experience', 'N/A')} years\n"
    return summary
