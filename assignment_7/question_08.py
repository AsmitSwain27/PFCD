# Question 8
# Implement a program to check if a string is a valid URL.

import re

def is_valid_url(url):
    # Regular expression for URL validation
    url_pattern = re.compile(
        r'^(https?|ftp)://'  # Protocol
        r'([a-zA-Z0-9.-]+)'  # Domain name
        r'(\.[a-zA-Z]{2,})'  # Top-level domain
        r'(:[0-9]{1,5})?'    # Optional port
        r'(/.*)?$'           # Optional path
    )
    
    return bool(url_pattern.match(url))

# Test
test_urls = [
    "https://www.google.com",
    "http://example.com/path/to/page",
    "ftp://files.server.com",
    "www.google.com",  # Invalid - no protocol
    "https://example.com:8080/page",
    "not a url",
    "https://sub.domain.example.com/path?query=value"
]

for url in test_urls:
    result = is_valid_url(url)
    print(f"'{url}' is valid URL: {result}")
