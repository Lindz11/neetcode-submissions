class Solution:
    """
    Last attempted 9/28/2026 
    
    """
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            cleaned = ""
            local_name = email.split('@')[0]
            domain_name = email.split('@')[1]
            valid_local = local_name.split('+')[0]
            for char in valid_local:
                if char.islower():
                    cleaned +=char
            cleaned +=domain_name
            seen.add(cleaned)
            
        return len(seen)