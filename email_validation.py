from email_validator import validate_email, EmailNotValidError

# validating function
def v_email(email):
    try:
        valid = validate_email(email, check_deliverability=True)
        return True, valid.email
    except EmailNotValidError as e:
        return False, str(e)

# read txt file
def read_file(path):
    with open(path, 'r') as f:
        return [line.strip() for line in f]

# write results (replace old results)
def write_file(results, path):
    with open(path, 'w') as f:
        for email, (valid, result) in results.items():
            status = 'Valid' if valid else f'Invalid: {result}'
            f.write(f"{email}: {status}\n")

def validate_file(input_file, output_file):
    emails = read_file(input_file)
    results = {email: v_email(email) for email in emails}
    write_file(results, output_file)

in_file = 'emails.txt'
out_file = 'results.txt'


print("Validating with deliverability check...")
validate_file(in_file, out_file)
print(f"Results saved to {out_file}")
