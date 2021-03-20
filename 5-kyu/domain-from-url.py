def domain_name(url):
    import re
    pattern = "(https?)?(:\/{2})?(www\.)?([\w|-]+)(\.\w+)"
    match = re.match(pattern, url)
    return match.group(4)