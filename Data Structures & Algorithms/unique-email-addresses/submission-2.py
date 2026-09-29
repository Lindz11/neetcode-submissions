class Solution:
    """
    Last attempted 9/28/2026 

    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            cleaned = ""
            valid = email.split('@')
            local_name = valid[0]
            domain_name = valid[1]
            valid_local = local_name.split('+')[0]
            for char in valid_local:
                if char.islower():
                    cleaned +=char
            seen.add(cleaned + domain_name)
            
        return len(seen)