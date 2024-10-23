#DemoRe.py

import re

result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

result = re.match("[0-9]*th", "  35th")
print(result)
#print(result.group())

result = re.search("apple", "This is apple")
print(result.group())

result = re.search("\d{4}", "올해는 2024년")
print(result.group())

result = re.search("\d{5}", "우리동네는 55234")
print(result.group())

# ... 기존 코드 ...


def check_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    result = re.search(pattern, email)
    return result is not None

# 테스트 샘플
test_emails = [
    "user@example.com",
    "john.doe123@company.co.kr",
    "invalid.email@com",
    "name@subdomain.domain.com",
    "user@123.456.789.com",
    "email_with+symbol@domain.com",
    "사용자@도메인.com",
    "user@domain",
    "user@.com",
    "user@domain..com"
]

for email in test_emails:
    if check_email(email):
        print(f"{email}: 유효한 이메일 주소입니다.")
    else:
        print(f"{email}: 유효하지 않은 이메일 주소입니다.")